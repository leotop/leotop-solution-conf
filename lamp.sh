apt-get update
apt-get dist-upgrade

locale-gen ru_RU.UTF-8
apt-get install apache2 mysql-server mysql-client php5 php5-gd php-gettext php5-mcrypt php5-mysql mc nano -y
a2enmod rewrite
php5enmod gd mcrypt mysql json
service apache2 restart
