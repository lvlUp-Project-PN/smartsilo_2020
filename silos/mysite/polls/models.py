from django.db import models



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LoginEmail(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'login_email'


class LoginPermissions(models.Model):
    user_role = models.CharField(primary_key=True, max_length=15)
    show_site = models.IntegerField()
    show_irt_statistics = models.IntegerField(db_column='show_IRT_statistics')  # Field name made lowercase.
    show_history_statistics = models.IntegerField()
    show_silos_err = models.IntegerField(db_column='show_silos_ERR')  # Field name made lowercase.
    show_resolve_errr = models.IntegerField(db_column='show_resolve_ERRR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'login_permissions'


class LoginUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_password = models.CharField(max_length=10)
    user_role = models.ForeignKey(LoginPermissions, models.DO_NOTHING, db_column='user_role')

    class Meta:
        managed = False
        db_table = 'login_user'


class Silos(models.Model):
    site_id = models.CharField(max_length=4, blank=True, null=True)
    raspberry_id = models.CharField(max_length=4, blank=True, null=True)
    silos_id = models.CharField(max_length=4, blank=True, null=True)
    silos_code = models.CharField(primary_key=True, max_length=12)

    def __str__(self):
        return self.silos_code

    class Meta:
        managed = False
        db_table = 'silos'



class SilosAvgDay(models.Model):
    day = models.DateField(primary_key=True)
    silos_code = models.CharField(max_length=12)
    day_avg = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'silos_avg_day'


class SilosAvgMonth(models.Model):
    date = models.DateField(primary_key=True)
    silos_code = models.CharField(max_length=12)
    month_avg = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'silos_avg_month'


class SilosAvgWeek(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    silos_code = models.CharField(max_length=12)
    week_avg = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'silos_avg_week'


class SilosDataIrt(models.Model):
    silos_data_time = models.DateTimeField()
    silos_code = models.ForeignKey(Silos, models.DO_NOTHING, db_column='silos_code')
    silos_value = models.FloatField()
    error_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.silos_code



    class Meta:
        managed = False
        db_table = 'silos_data_irt'


class SilosError(models.Model):
    error_code = models.CharField(primary_key=True, max_length=3)
    error_description = models.CharField(max_length=160)

    class Meta:
        managed = False
        db_table = 'silos_error'


class SilosErrorCategory(models.Model):
    error_code = models.AutoField(primary_key=True)
    error_description = models.CharField(max_length=3)
    silos_code = models.CharField(max_length=12)
    error_data_path = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'silos_error_category'
        unique_together = (('error_code', 'error_description'),)


class SilosSpecs(models.Model):
    silos_code = models.CharField(primary_key=True, max_length=12)
    d1 = models.FloatField()
    d2 = models.FloatField()
    d3 = models.FloatField()
    d4 = models.FloatField()
    d5 = models.FloatField()
    liq_density = models.FloatField()
    flow_per_second = models.FloatField()

    class Meta:
        managed = False
        db_table = 'silos_specs'
