# FLASK-M09

## Aplicació amb VENV i Flask
1- Creem el entorn VIRTUAL amb Python3

    python3 -m venv .venv

2- Iniciem el entorn Virtual

    source .venv/bin/activate

3 - Instalem el Flask

    pip install flask

4- Creem la app.py

    from flask import Flask, render_template
    from flask import request

    app = Flask(__name__)

    @app.route("/ep0")
    def ep0():
        return "<html><body><h1>Aquest és el meu primer endpoint</h1></body></html>"
    @app.route("/ep1")

    def ep1():
        return render_template("index.html")

5- Creem la carpeta de templates i dins de la meteixa creem el ficher index.html

6- Inicialitzem el flask amb la seguent comanda

    flask run --debug

7- Finalment comprovem amb l'IP que ens dona el Flask els dos endpoints creats
    http://127.0.0.1:5000/ep0
    http://127.0.0.1:5000/ep1

## Aplicació amb VENV,Flask inegrat en un server APACHE

1- Instalem Python i Pip
    
    sudo apt update sudo apt install python3 python3-pip

2- Instalem el server Apache2

    sudo apt install apache2

3- Inicialitzem el servei de apache

    sudo systemctl start apache2

4- Creem la arrel myflaskapp dins de /var/www

    cd /var/www
    sudo mkdir myflaskapp

5- Dins de la nova carpeta creem l'entorn virtual i l'activem

    sudo python3 -m venv venv
    
    source venv/bin/activate

6- Instalem el flas amb el PIP dins de l'entorn virtual

    pip install Flask

7- Creem el app.py

    from flask import Flask, render_template
    from flask import request

    app = Flask(__name__, template_folder='/var/www/myflaskapp/venv/templates')

    @app.route("/ep0")
    def ep0():
        return "<html><body><h1>Aquest és el meu primer endpoint</h1></body></html>"
    @app.route("/ep1")

    def ep1():
        return render_template("index.html")
    
8- Creem la carpeta templates dins del entorn virtual i afegim el index.html

    mkdir /venv/templates
    nano /venv/templates/index.html


9- Instalem el mod_wsgi

    sudo apt install libapache2-mod-wsgi-py3

10- Creem el archiu de configuració de apache per la pàgina

    sudo nano /etc/apache2/sites-available/myflaskapp.conf

11- Afegim el següent

    <VirtualHost *:80>
        ServerName 192.168.110.225

        WSGIDaemonProcess myflaskapp python-path=/var/www/myflaskapp:/var/www/myflaskapp/venv/lib/python3.12/site-packages
        WSGIScriptAlias / /var/www/myflaskapp/myflaskapp.wsgi

        <Directory /var/www/myflaskapp>
            WSGIProcessGroup myflaskapp
            WSGIApplicationGroup %{GLOBAL}
            Require all granted
        </Directory>

        Alias /static /var/www/myflaskapp/static
        <Directory /var/www/myflaskapp/static/>
            Require all granted
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/myflaskapp_error.log
        CustomLog ${APACHE_LOG_DIR}/myflaskapp_access.log combined
    </VirtualHost>

12- Creem el fitxer wsgi

    sudo nano /var/www/myflaskapp/myflaskapp.wsgi

13- Afegim el següent contingut

    #!/usr/bin/python3

    import sys
    import logging

    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0, '/var/www/myflaskapp')

    from app import app as application
    application.secret_key = 'supersecretkey'

14- Inicialitzem la pagina

    sudo a2ensite myflaskapp

15- Fem un reload del server

    sudo systemctl restart apache2

16- I per finalitzar entrem a la següent pagina per internet per comprobar els dos endpoints

    http://192.168.110.225/ep0
    http://192.168.110.225/ep1


