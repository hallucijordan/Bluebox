#Logbook数据库的搭建
drop database if exists Logbook;
create database Logbook;
use Logbook;
drop table if exists Users;
drop table if exists Games;
drop table if exists Levels;
drop table if exists Articles;
drop table if exists Comments;




create table Users(
    user_id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户ID',
    user_name varchar(20) NOT NULL COMMENT '用户名',
    avatar varchar(50) DEFAULT NULL COMMENT '头像',
    passwd varchar(255) NOT NULL COMMENT '密码',
    
    PRIMARY KEY (user_id),
    KEY (user_name)
);

create table Games(
    game_id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '游戏ID',
    game_name varchar(20) NOT NULL COMMENT '游戏名(简洁起见，只放原名)',
    screen_1 varchar(50) DEFAULT NULL COMMENT '游戏截图1',
    screen_2 varchar(50) DEFAULT NULL COMMENT '游戏截图2',
    screen_3 varchar(50) DEFAULT NULL COMMENT '游戏截图3',
    screen_4 varchar(50) DEFAULT NULL COMMENT '游戏截图4',
    screen_5 varchar(50) DEFAULT NULL COMMENT '游戏截图5',
    
    min_demand varchar(20) NOT NULL DEFAULT '' COMMENT '最低配置',
    min_operator varchar(20) NOT NULL DEFAULT '' COMMENT '最低操作系统',
    min_cpu varchar(20) NOT NULL DEFAULT '' COMMENT '最低处理器',
    min_istorage varchar(20) NOT NULL DEFAULT '' COMMENT '最低内存',
    min_gpu varchar(20) NOT NULL DEFAULT '' COMMENT '最低显卡',
    min_directX varchar(20) NOT NULL DEFAULT '' COMMENT '最低directX',
    
    rec_demand varchar(20) NOT NULL DEFAULT '' COMMENT '最低配置',    
    rec_operator varchar(20) NOT NULL DEFAULT '' COMMENT '推荐操作系统',
    rec_cpu varchar(20) NOT NULL DEFAULT '' COMMENT '推荐处理器',
    rec_istorage varchar(20) NOT NULL DEFAULT '' COMMENT '推荐内存',
    rec_gpu varchar(20) NOT NULL DEFAULT '' COMMENT '推荐显卡',
    rec_directX varchar(20) NOT NULL DEFAULT '' COMMENT '推荐directX',

    min_storage varchar(20) NOT NULL DEFAULT '' COMMENT '需求存储空间',
    
    score numeric(3,2) unsigned DEFAULT NULL COMMENT '游戏评分',
    abstract varchar(255) DEFAULT NULL COMMENT '游戏简介',
    publish_time int (10) unsigned NOT NULL DEFAULT '0' COMMENT '游戏发行时间', 
    producer varchar(20) DEFAULT NULL COMMENT '发行厂商',
    PRIMARY KEY (game_id),
    KEY (game_name)
);

create table Levels(
    level_id int(3) unsigned NOT NULL COMMENT '关卡id 为零时为游戏本身', 
    game_id int(11) unsigned NOT NULL COMMENT '游戏ID',
    level_name varchar(20) NOT NULL COMMENT '关卡名',
    screen_1 varchar(50) DEFAULT NULL COMMENT '游戏截图1',
    screen_2 varchar(50) DEFAULT NULL COMMENT '游戏截图2',
    screen_3 varchar(50) DEFAULT NULL COMMENT '游戏截图3',
    screen_4 varchar(50) DEFAULT NULL COMMENT '游戏截图4',
    screen_5 varchar(50) DEFAULT NULL COMMENT '游戏截图5',
    
    PRIMARY KEY (game_id,level_id),
    KEY (level_name),
    foreign key (game_id) references Games(game_id) 
    on delete cascade
);

create table Articles(
    article_id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '文章ID',
    title varchar(80) NOT NULL DEFAULT 'Unknown Record' COMMENT '标题',   
    content text COMMENT '原文',
    stars int(1) check(stars>=0 AND stars<=10) NOT NULL COMMENT '玩家给出的星级',
    game_id int(11) unsigned NOT NULL COMMENT '游戏ID',
    level_id int(3) unsigned NOT NULL COMMENT '关卡id 为零时为游戏本身', 
    
    user_id int(11) unsigned NOT NULL COMMENT '用户ID',
    create_time int (10) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
    update_time int (10) unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
    
    PRIMARY KEY (article_id),
    KEY (title),
    foreign key (game_id,level_id) references Levels(game_id,level_id) 
    on delete cascade,
    foreign key (user_id) references Users(user_id)
);

create table Comments(
    comment_id int(11) unsigned NOT NULL COMMENT '评论ID',
    article_id int(11) unsigned NOT NULL COMMENT '文章ID',
    user_id int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户ID',
    create_time int (10) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
    update_time int (10) unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
    PRIMARY KEY (comment_id),
    foreign key (user_id) references Users(user_id),
    foreign key (article_id) references Articles(article_id)
    on delete cascade
);
