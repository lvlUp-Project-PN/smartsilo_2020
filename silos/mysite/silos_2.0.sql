-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: silosupdated
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add login email',1,'add_loginemail'),(2,'Can change login email',1,'change_loginemail'),(3,'Can delete login email',1,'delete_loginemail'),(4,'Can view login email',1,'view_loginemail'),(5,'Can add login permissions',2,'add_loginpermissions'),(6,'Can change login permissions',2,'change_loginpermissions'),(7,'Can delete login permissions',2,'delete_loginpermissions'),(8,'Can view login permissions',2,'view_loginpermissions'),(9,'Can add login user',3,'add_loginuser'),(10,'Can change login user',3,'change_loginuser'),(11,'Can delete login user',3,'delete_loginuser'),(12,'Can view login user',3,'view_loginuser'),(13,'Can add silos avg day',4,'add_silosavgday'),(14,'Can change silos avg day',4,'change_silosavgday'),(15,'Can delete silos avg day',4,'delete_silosavgday'),(16,'Can view silos avg day',4,'view_silosavgday'),(17,'Can add silos avg month',5,'add_silosavgmonth'),(18,'Can change silos avg month',5,'change_silosavgmonth'),(19,'Can delete silos avg month',5,'delete_silosavgmonth'),(20,'Can view silos avg month',5,'view_silosavgmonth'),(21,'Can add silos avg week',6,'add_silosavgweek'),(22,'Can change silos avg week',6,'change_silosavgweek'),(23,'Can delete silos avg week',6,'delete_silosavgweek'),(24,'Can view silos avg week',6,'view_silosavgweek'),(25,'Can add silos data',7,'add_silosdata'),(26,'Can change silos data',7,'change_silosdata'),(27,'Can delete silos data',7,'delete_silosdata'),(28,'Can view silos data',7,'view_silosdata'),(29,'Can add silos data irt',8,'add_silosdatairt'),(30,'Can change silos data irt',8,'change_silosdatairt'),(31,'Can delete silos data irt',8,'delete_silosdatairt'),(32,'Can view silos data irt',8,'view_silosdatairt'),(33,'Can add silos error',9,'add_siloserror'),(34,'Can change silos error',9,'change_siloserror'),(35,'Can delete silos error',9,'delete_siloserror'),(36,'Can view silos error',9,'view_siloserror'),(37,'Can add silos error category',10,'add_siloserrorcategory'),(38,'Can change silos error category',10,'change_siloserrorcategory'),(39,'Can delete silos error category',10,'delete_siloserrorcategory'),(40,'Can view silos error category',10,'view_siloserrorcategory'),(41,'Can add log entry',11,'add_logentry'),(42,'Can change log entry',11,'change_logentry'),(43,'Can delete log entry',11,'delete_logentry'),(44,'Can view log entry',11,'view_logentry'),(45,'Can add permission',12,'add_permission'),(46,'Can change permission',12,'change_permission'),(47,'Can delete permission',12,'delete_permission'),(48,'Can view permission',12,'view_permission'),(49,'Can add group',13,'add_group'),(50,'Can change group',13,'change_group'),(51,'Can delete group',13,'delete_group'),(52,'Can view group',13,'view_group'),(53,'Can add user',14,'add_user'),(54,'Can change user',14,'change_user'),(55,'Can delete user',14,'delete_user'),(56,'Can view user',14,'view_user'),(57,'Can add content type',15,'add_contenttype'),(58,'Can change content type',15,'change_contenttype'),(59,'Can delete content type',15,'delete_contenttype'),(60,'Can view content type',15,'view_contenttype'),(61,'Can add session',16,'add_session'),(62,'Can change session',16,'change_session'),(63,'Can delete session',16,'delete_session'),(64,'Can view session',16,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (11,'admin','logentry'),(13,'auth','group'),(12,'auth','permission'),(14,'auth','user'),(15,'contenttypes','contenttype'),(1,'polls','loginemail'),(2,'polls','loginpermissions'),(3,'polls','loginuser'),(4,'polls','silosavgday'),(5,'polls','silosavgmonth'),(6,'polls','silosavgweek'),(7,'polls','silosdata'),(8,'polls','silosdatairt'),(9,'polls','siloserror'),(10,'polls','siloserrorcategory'),(16,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-06-23 18:46:44.602693'),(2,'auth','0001_initial','2020-06-23 18:46:44.855615'),(3,'admin','0001_initial','2020-06-23 18:46:46.192070'),(4,'admin','0002_logentry_remove_auto_add','2020-06-23 18:46:46.455805'),(5,'admin','0003_logentry_add_action_flag_choices','2020-06-23 18:46:46.469692'),(6,'contenttypes','0002_remove_content_type_name','2020-06-23 18:46:46.653528'),(7,'auth','0002_alter_permission_name_max_length','2020-06-23 18:46:46.774758'),(8,'auth','0003_alter_user_email_max_length','2020-06-23 18:46:46.823252'),(9,'auth','0004_alter_user_username_opts','2020-06-23 18:46:46.839801'),(10,'auth','0005_alter_user_last_login_null','2020-06-23 18:46:46.961240'),(11,'auth','0006_require_contenttypes_0002','2020-06-23 18:46:46.967200'),(12,'auth','0007_alter_validators_add_error_messages','2020-06-23 18:46:46.984092'),(13,'auth','0008_alter_user_username_max_length','2020-06-23 18:46:47.255799'),(14,'auth','0009_alter_user_last_name_max_length','2020-06-23 18:46:47.416284'),(15,'auth','0010_alter_group_name_max_length','2020-06-23 18:46:47.445857'),(16,'auth','0011_update_proxy_permissions','2020-06-23 18:46:47.462721'),(17,'polls','0001_initial','2020-06-23 18:46:47.476610'),(18,'sessions','0001_initial','2020-06-23 18:46:47.515309');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_email`
--

DROP TABLE IF EXISTS `login_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `login_email` (
  `user_id` varchar(20) NOT NULL,
  `user_email` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_email`
--

LOCK TABLES `login_email` WRITE;
/*!40000 ALTER TABLE `login_email` DISABLE KEYS */;
INSERT INTO `login_email` VALUES ('565','pippo@paperino.net'),('569','pluto@minni.net');
/*!40000 ALTER TABLE `login_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_permissions`
--

DROP TABLE IF EXISTS `login_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `login_permissions` (
  `user_role` varchar(15) NOT NULL,
  `show_site` tinyint(1) NOT NULL,
  `show_IRT_statistics` tinyint(1) NOT NULL,
  `show_history_statistics` tinyint(1) NOT NULL,
  `show_silos_ERR` tinyint(1) NOT NULL,
  `show_resolve_ERRR` tinyint(1) NOT NULL,
  PRIMARY KEY (`user_role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_permissions`
--

LOCK TABLES `login_permissions` WRITE;
/*!40000 ALTER TABLE `login_permissions` DISABLE KEYS */;
INSERT INTO `login_permissions` VALUES ('prova',0,1,0,1,0),('prova2',0,1,0,1,0),('prova3',1,1,0,1,1);
/*!40000 ALTER TABLE `login_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_user`
--

DROP TABLE IF EXISTS `login_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `login_user` (
  `user_id` varchar(20) NOT NULL,
  `user_password` varchar(10) NOT NULL,
  `user_role` varchar(15) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `user_role` (`user_role`),
  CONSTRAINT `login_user_ibfk_1` FOREIGN KEY (`user_role`) REFERENCES `login_permissions` (`user_role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_user`
--

LOCK TABLES `login_user` WRITE;
/*!40000 ALTER TABLE `login_user` DISABLE KEYS */;
INSERT INTO `login_user` VALUES ('078','mandorla','prova2'),('0898','3prova','prova3'),('09778','sebbi','prova');
/*!40000 ALTER TABLE `login_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `silos`
--

DROP TABLE IF EXISTS `silos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `silos` (
  `site_id` varchar(4) DEFAULT NULL,
  `raspberry_id` varchar(4) DEFAULT NULL,
  `silos_id` varchar(4) DEFAULT NULL,
  `silos_code` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `silos`
--

LOCK TABLES `silos` WRITE;
/*!40000 ALTER TABLE `silos` DISABLE KEYS */;
/*!40000 ALTER TABLE `silos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `silos_avg_day`
--

DROP TABLE IF EXISTS `silos_avg_day`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `silos_avg_day` (
  `silos_code` varchar(12) NOT NULL,
  `day` float DEFAULT NULL,
  PRIMARY KEY (`silos_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `silos_avg_day`
--

LOCK TABLES `silos_avg_day` WRITE;
/*!40000 ALTER TABLE `silos_avg_day` DISABLE KEYS */;
INSERT INTO `silos_avg_day` VALUES ('silos123',154118),('silos456',154200),('silos789',154206);
/*!40000 ALTER TABLE `silos_avg_day` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `silos_avg_month`
--

DROP TABLE IF EXISTS `silos_avg_month`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `silos_avg_month` (
  `silos_code` varchar(12) NOT NULL,
  `year` date NOT NULL,
  `month` float DEFAULT NULL,
  PRIMARY KEY (`silos_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `silos_avg_month`
--

LOCK TABLES `silos_avg_month` WRITE;
/*!40000 ALTER TABLE `silos_avg_month` DISABLE KEYS */;
INSERT INTO `silos_avg_month` VALUES ('silos123','2020-06-19',6.45454),('silos456','2020-06-19',6.45454),('silos789','2020-06-19',6.45454);
/*!40000 ALTER TABLE `silos_avg_month` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `silos_avg_week`
--

DROP TABLE IF EXISTS `silos_avg_week`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `silos_avg_week` (
  `silos_code` varchar(12) NOT NULL,
  `week` float DEFAULT NULL,
  PRIMARY KEY (`silos_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `silos_avg_week`
--

LOCK TABLES `silos_avg_week` WRITE;
/*!40000 ALTER TABLE `silos_avg_week` DISABLE KEYS */;
INSERT INTO `silos_avg_week` VALUES ('silos123',160133),('silos456',160123),('silos789',160138);
/*!40000 ALTER TABLE `silos_avg_week` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `silos_data_irt`
--

DROP TABLE IF EXISTS `silos_data_irt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `silos_data_irt` (
  `silos_code` varchar(12) NOT NULL,
  `silos_data_time` date NOT NULL,
  `silos_value` float NOT NULL,
  `error_code` json NOT NULL,
  PRIMARY KEY (`silos_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `silos_data_irt`
--

LOCK TABLES `silos_data_irt` WRITE;
/*!40000 ALTER TABLE `silos_data_irt` DISABLE KEYS */;
INSERT INTO `silos_data_irt` VALUES ('silos123','2020-06-19',456.36,'[\"abs\"]'),('silos456','2020-06-19',456.36,'[\"cee\"]'),('silos789','2020-06-19',456.36,'[\"ceca\"]');
/*!40000 ALTER TABLE `silos_data_irt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `silos_error`
--

DROP TABLE IF EXISTS `silos_error`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `silos_error` (
  `error_code` varchar(3) NOT NULL,
  `error_description` varchar(160) NOT NULL,
  PRIMARY KEY (`error_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `silos_error`
--

LOCK TABLES `silos_error` WRITE;
/*!40000 ALTER TABLE `silos_error` DISABLE KEYS */;
INSERT INTO `silos_error` VALUES ('444','sensore compromesso'),('787','contenuto superiore al limite massimo'),('999','contenuto in esaurimento');
/*!40000 ALTER TABLE `silos_error` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `silos_error_category`
--

DROP TABLE IF EXISTS `silos_error_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `silos_error_category` (
  `error_code` int(11) NOT NULL AUTO_INCREMENT,
  `error_description` varchar(3) NOT NULL,
  `silos_code` varchar(12) NOT NULL,
  `error_data_path` varchar(100) NOT NULL,
  PRIMARY KEY (`error_code`,`error_description`)
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `silos_error_category`
--

LOCK TABLES `silos_error_category` WRITE;
/*!40000 ALTER TABLE `silos_error_category` DISABLE KEYS */;
INSERT INTO `silos_error_category` VALUES (444,'uri','silos456','riconducibile alla tara'),(787,'men','silos789','riconducibile al terreno'),(999,'esa','silos123','riconducibile al peso');
/*!40000 ALTER TABLE `silos_error_category` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-23 20:57:14
