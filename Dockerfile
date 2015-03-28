FROM ubuntu:14.04
MAINTAINER Oliver W. Laslett <O.Laslett@soton.ac.uk>

# Install depenencies
RUN apt-get update
RUN apt-get install python-dev -y
RUN apt-get install python-pip -y
RUN apt-get install mysql-server -y
RUN apt-get install libmysqlclient-dev -y

RUN pip install TwitterAPI
RUN pip install MySQL-python

# Add source files to the containiner
ADD * twacademia/

# Set up mysql database format
RUN mysql -e "create database tweet"
RUN mysql -e "create table tweet (id_str varchar(100) NOT NULL, primary key(id_str)) engine=InnoDB"
RUN mysql -e "alter table tweet add column `name` varchar(100)"
RUN mysql -e "alter table tweet add column `screen_name` varchar(100)"
RUN mysql -e "alter table tweet add column `text` varchar(150)"
RUN mysql -e "alter table tweet add column `created_at` varchar(150)"
RUN mysql -e "alter table tweet add column `hashtags` varchar(150)"
RUN mysql -e "alter table tweet add column `urls` varchar(150)"
RUN mysql -e "alter table tweet add column `followers_count` int"
RUN mysql -e "CREATE USER `pythonapp`@`localhost` IDENTIFIED BY 'pypass'

