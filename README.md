# twaca
Quick hack to archive keyword related tweets to an SQL database.

# Docker usage
If you use Docker, you can use the build file to easily get going. If you want
the sql database to persist, you must first mount a volume from the host and
set up the database from there:

1. Build the twaca image `$ docker build -t twaca .`

2. Run the set up script to initialise a tweet SQL database on your host
system `$ docker run -v /path/to/host/dir:/var/lib/mysql twaca
"twacademia/set_up_sqltable.sh"`

3. Now choose a keyword (such as *football*) and start streaming football
related tweets to your database `$ docker run -d -v
/path/to/host/dir:/var/lib/mysql twaca /bin/sh -c "service mysql start &&
python twacademia/stream_tags.py football"

The daemonized container will run until you stop it. The data will be saved in
the mounted volume /path/to/host/dir which can then be accessed through
another container or from your host mysql system.

## Get data with docker image (example)
Start an interactive session with the mounted data

`$ docker run -it -v /path/to/host/dir:/var/lib/mysql twaca`

Now start the sql server and look into the database

`$ service mysql start`
`$ mysql`
`$ > use tweet`
`$ > SELECT * FROM tweet;`

# Requirements
python 2.7,
virtualenv,
TwitterAPI,
mysql-python,
MySQL

# Contributors
Oliver Laslett
Alison Packer
Mikhail Kabeshov
