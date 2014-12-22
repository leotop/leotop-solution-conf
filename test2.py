#!/usr/bin/env python
# -- coding: utf-8 --
# https://raw.github.com/leotop/leotop-solution-conf/master/bottle.py
from bottle import run, get, post, request, template

tpl = u'''
Проверьте данные, при необходимости внесите изменения вручную или с помощью формы генератора ниже<br>
Конфигурация:<br>
<form method="post" action="/write">
<textarea rows="25" cols="155" name="conf">
<VirtualHost *>
ServerName {{domain}}
ServerAlias www.{{domain}}
ServerAdmin webmaster@{{domain}}
DocumentRoot {{djangopath}}
Alias /media/ {{djangopath}}/media/
Alias /robots.txt {{djangopath}}/robots.txt
Alias /favicon.ico {{djangopath}}/favicon.ico
ErrorLog {{djangopath}}/log/mysite-error.log
LogLevel warn
CustomLog {{djangopath}}/log/mysite-access.log combined
WSGIScriptAlias / {{djangopath}}/leotop_solution/wsgi.py
WSGIDaemonProcess {{domain}} user=leotop group=www-data home={{djangopath}} processes=2 threads=4 maximum-requests=100 display-name=leotop-{{domain}}-wsgi python-path={{djangopath}}
WSGIProcessGroup {{domain}}
</VirtualHost>
</textarea><br>
Название файла конфигурации: <input value="{{domain}}.conf" name="conf_name">
<input type="submit" value="Записать на диск">
</form>
<br><br><br>

<form method="post">Имя домена без www, например leotop.org<br><input name="my_domain" value="{{domain}}">
<br><br>
Введите полный путь к загруженной папке на диске, например /home/leotop/www/leotop<br> 
<input name="my_djangopath" value="{{djangopath}}">

<br><br><br><input type="submit" value="Подготовить конфигурацию"></form>
'''

new_domain = u'''
<h1>Добавление нового решения для домена</h1><form method="post">Имя домена без www, например leotop.org<br><input name="my_domain">
<br><br>
Введите полный путь к загруженной папке на диске, например /home/leotop/www/leotop<br> 
<input name="my_djangopath" value="/home/leotop/www/...">

<br><br><br><input type="submit" value="Подготовить конфигурацию"></form>
'''

@get('/')
def index():
    return 'Hello World'

@get('/new')
def new_website():
    return new_domain

@post('/new')
def new_website():
    domain = request.forms.get('my_domain')
    djangopath = request.forms.get('my_djangopath')
    return template(tpl, {"domain" : domain, "djangopath" : djangopath})

@post('/write')
def new_website():
    conf = request.forms.get('conf')
    conf_name = request.forms.get('conf_name')
    w = open("/etc/apache2/conf.d/" + conf_name, "w")
    w.write(conf)
    
    return 'Данные записаны на диск. Перезапустить вебсервер? <br><a href="/apache-restart">Да</a> / <a href="/">Нет, вернуться на главную</a>'

@get('/apache-restart')
def index():
    import subprocess
    apache2 = subprocess.check_output(["apachectl", "restart"])
    
    return u'Сервер apache перезапущен' + apache2

run(host='0.0.0.0', port=8080)
