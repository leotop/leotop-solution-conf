#!/bin/sh
# Базовая настройка сервера для django (apache2 + uwsgi) Виртуальный сервер reg.ru ubuntu 12.04-x86
# https://raw.github.com/leotop/leotop-solution-conf/master/base-config.sh
apt-get update
apt-get upgrade -y
# Освобождаем память удаляем samba
apt-get purge samba* -y
# Установка консольного текстового редактора
apt-get install nano -y
# Апач на сервере установлен по умолчанию, добавляем библиотеки
apt-get install libapache2-mod-wsgi
apachectl restart
# Библиотека обработки изображений для python
apt-get install python-imaging
# Python PIP для установки свежих версий ПО
apt-get install python-pip
# Установка приложений и дополнений
pip install -r https://raw.github.com/leotop/leotop-solution-conf/master/requirements.txt
# Создаем пользователя
useradd -m -G www-data leotop
# Задаем пароль пользователю
echo "enter a password"
passwd leotop
# Создаем папку www для пользователя, для размещения приложений
mkdir /home/leotop/www/
chown leotop:leotop /home/leotop/www/
