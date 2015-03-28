#!/bin/bash

# Bash script to set up SQL table format
service mysql restart
mysql -e "create database tweet"
mysql tweet -e "create table tweet (id_str varchar(100) NOT NULL, primary key(id_str)) engine=InnoDB"
mysql tweet -e "alter table tweet add column name varchar(100);"
mysql tweet -e "alter table tweet add column screen_name varchar(100);"
mysql tweet -e "alter table tweet add column text varchar(150);"
mysql tweet -e "alter table tweet add column created_at varchar(150);"
mysql tweet -e "alter table tweet add column hashtags varchar(150);"
mysql tweet -e "alter table tweet add column urls varchar(150);"
mysql tweet -e "alter table tweet add column followers_count int;"
mysql tweet -e "CREATE USER pythonapp@localhost IDENTIFIED BY 'pypass'"
mysql tweet -e "GRANT ALL PRIVILEGES ON tweet.tweet to pythonapp@localhost"
