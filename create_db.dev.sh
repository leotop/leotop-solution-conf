#!/bin/bash
mysql -u root -p123Pass << EOF
CREATE DATABASE newtbase;
CREATE USER 'newtuser'@'localhost' IDENTIFIED BY 'newtpass';
GRANT USAGE ON *.* TO 'newtuser'@'localhost' IDENTIFIED BY 'newtpass' WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0 ;
GRANT ALL PRIVILEGES ON newtbase.* TO 'newtuser'@'localhost';
EOF
