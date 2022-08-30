/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - placementmanagementsystem
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`placementmanagementsystem` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `placementmanagementsystem`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `Complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `Comp_date` varchar(50) DEFAULT NULL,
  `S_id` int(11) DEFAULT NULL,
  `Complaint` varchar(100) DEFAULT NULL,
  `Reply` varchar(100) DEFAULT NULL,
  `Status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Complaint_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `Course_id` int(11) NOT NULL AUTO_INCREMENT,
  `Course_name` varchar(50) DEFAULT NULL,
  `Dept_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`Course_id`,`Course_name`,`Dept_id`) values 
(1,'MbA',1),
(2,'MCA',2);

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `Dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `Dept_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`Dept_id`,`Dept_name`) values 
(1,'A'),
(2,'Computer Application');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Login_id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `Type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Login_id`,`Username`,`Password`,`Type`) values 
(1,'Devika','6666','Student');

/*Table structure for table `question` */

DROP TABLE IF EXISTS `question`;

CREATE TABLE `question` (
  `Q_id` int(11) NOT NULL AUTO_INCREMENT,
  `Question` varchar(200) DEFAULT NULL,
  `Answer` varchar(200) DEFAULT NULL,
  `Difficulty_level` varchar(50) DEFAULT NULL,
  `Option1` varchar(50) DEFAULT NULL,
  `Option2` varchar(50) DEFAULT NULL,
  `Option3` varchar(50) DEFAULT NULL,
  `Option4` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Q_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `question` */

insert  into `question`(`Q_id`,`Question`,`Answer`,`Difficulty_level`,`Option1`,`Option2`,`Option3`,`Option4`,`type`) values 
(1,'Analyze safe and dangerous aspects of these features.',NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(2,'About what proportion of the population of the US is living on farms?','122','Knowledge','122','rt','xc','tty',NULL),
(3,'About what proportion of the population of the US is living on farms?','d','Knowledge','sa','s','sd','d',NULL),
(4,'Analyze safe and dangerous aspects of these features.','xc','Analysis','as','asx','cc','xc',NULL),
(5,'Analyze safe and dangerous aspects of these features.','sxs','Analysis','az','sx','s','xs',NULL);

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `S_id` int(11) NOT NULL AUTO_INCREMENT,
  `S_name` varchar(50) DEFAULT NULL,
  `Course_id` int(11) DEFAULT NULL,
  `Semester` varchar(50) DEFAULT NULL,
  `Adm_no` varchar(50) DEFAULT NULL,
  `S_email` varchar(50) DEFAULT NULL,
  `S_phone` varchar(50) DEFAULT NULL,
  `S_dob` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`S_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
