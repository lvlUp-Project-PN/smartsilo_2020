from rest_framework import serializers
from .models import *

class SilosDataIrtSerialize(serializers.ModelSerializer):
    class Meta:
        model=SilosDataIrt
        fields="__all__"

class LoginEmailSerialize(serializers.ModelSerializer):
    class Meta:
        model=LoginEmail
        fields="__all__"

class LoginPermissionsSerialize(serializers.ModelSerializer):
    class Meta:
        model=LoginPermissions
        fields="__all__"

class LoginUserSerialize(serializers.ModelSerializer):
    class Meta:
        model=LoginUser
        fields="__all__"

class SilosAvgDaySerialize(serializers.ModelSerializer):
    class Meta:
        model=SilosAvgDay
        fields="__all__"

class SilosAvgMonthSerialize(serializers.ModelSerializer):
    class Meta:
        model=SilosAvgMonth
        fields="__all__"

class SilosAvgWeekSerialize(serializers.ModelSerializer):
    class Meta:
        model=SilosAvgWeek
        fields="__all__"

class SilosSerialize(serializers.ModelSerializer):
    class Meta:
        model=Silos
        fields="__all__"

class SilosErrorSerialize(serializers.ModelSerializer):
    class Meta:
        model=SilosError
        fields="__all__"

class SilosErrorCategorySerialize(serializers.ModelSerializer):
    class Meta:
        model=SilosErrorCategory
        fields="__all__"

class SilosSpecsSerialize(serializers.ModelSerializer):
    class Meta:
        model=SilosSpecs
        fields="__all__"
