apt-get update
apt-get dist-upgrade
locale-gen ru_RU.UTF-8
apt-get install dialog -y
apt-get install apache2 mc nano libapache2-mod-wsgi-py3 python3-pip python3-pil -y
pip3 install django
pip3 install django-mptt
pip3 install django-taggit

#mysql python3
apt-get install python3-dev libmysqlclient-dev
pip3 install mysqlclient
pip3 install PyMySQL
