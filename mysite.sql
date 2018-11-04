/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50547
Source Host           : 127.0.0.1:3306
Source Database       : mysite

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2018-11-04 18:49:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for dbmethod
-- ----------------------------
DROP TABLE IF EXISTS `dbmethod`;
CREATE TABLE `dbmethod` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL COMMENT 'db 操作名称',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of dbmethod
-- ----------------------------
INSERT INTO `dbmethod` VALUES ('1', '1');

-- ----------------------------
-- Table structure for environment
-- ----------------------------
DROP TABLE IF EXISTS `environment`;
CREATE TABLE `environment` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL COMMENT '环境名称',
  `dbHost` varchar(50) DEFAULT NULL COMMENT '数据库host',
  `dbName` varchar(50) DEFAULT NULL COMMENT '数据库名称',
  `dbUsername` varchar(50) DEFAULT NULL COMMENT '用户名',
  `dbPassword` varchar(50) DEFAULT NULL COMMENT '密码',
  `dbProt` smallint(3) unsigned DEFAULT '3306' COMMENT '端口',
  `createTime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of environment
-- ----------------------------
INSERT INTO `environment` VALUES ('1', 'ckk', '127.0.0.1', 'ckk', 'root', 'root', '3306', '0000-00-00 00:00:00');
INSERT INTO `environment` VALUES ('2', '2', '127.0.0.2', 'mysity2', 'root', 'root', '3306', '0000-00-00 00:00:00');

-- ----------------------------
-- Table structure for fields
-- ----------------------------
DROP TABLE IF EXISTS `fields`;
CREATE TABLE `fields` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `tableId` int(11) NOT NULL COMMENT '外键 表id',
  `name` varchar(50) DEFAULT NULL COMMENT '字段名',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of fields
-- ----------------------------
INSERT INTO `fields` VALUES ('1', '1', '127.0.0.1');

-- ----------------------------
-- Table structure for managesql
-- ----------------------------
DROP TABLE IF EXISTS `managesql`;
CREATE TABLE `managesql` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `sql` varchar(255) DEFAULT NULL,
  `tableName` varchar(255) DEFAULT NULL,
  `createTime` datetime NOT NULL,
  KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of managesql
-- ----------------------------
INSERT INTO `managesql` VALUES ('1', '查用户', 'select * from setting', 'User', '0000-00-00 00:00:00');
INSERT INTO `managesql` VALUES ('2', '查别的', 'select * from shoprecommendcontent', 'shoprecommendcontent', '0000-00-00 00:00:00');

-- ----------------------------
-- Table structure for tables
-- ----------------------------
DROP TABLE IF EXISTS `tables`;
CREATE TABLE `tables` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL COMMENT 'table名称',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tables
-- ----------------------------
INSERT INTO `tables` VALUES ('1', '1');
