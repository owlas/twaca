# twacademia
Quick hack of a twitter platform to track academic conference buzz

# Example
See the following link for an example of the current output: 
http://twacademia.me/html/

# Requirements
python 2.7,
virtualenv,
TwitterAPI,
mysql-python,
MySQL

# Container provision
apt-get update

apt-get install git

apt-get install python-pip

apt-get install mysql-server

pip install virtualenv

git clone https://github.com/owlas/twacademia.git

cd twacademia

virtualenv twaca-env

pip install TwitterAPI

pip install requests --upgrade

apt-get install libmysqlclient-dev

pip install MySQL-python
