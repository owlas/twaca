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
RUN pip install requests --upgrade

# Add source files to the containiner
ADD * twacademia/


