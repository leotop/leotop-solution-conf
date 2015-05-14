apt-get update
apt-get dist-upgrade

locale-gen ru_RU.UTF-8
apt-get install dialog apache2 mysql-server mysql-client php5 php5-gd php5-curl curl php-gettext php5-mcrypt php5-mysql mc nano phpmyadmin -y
a2enmod rewrite
php5enmod gd mcrypt mysql json curl
service apache2 restart
