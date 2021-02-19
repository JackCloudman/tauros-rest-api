# tauros-rest-api
API REST en Django, repositorio de prueba para Tauros.io
# Features
- Creación de usuarios
- Modificación de perfiles
- Autenticación basada en tokens
- Aprobación por el admin

NOTA: El usuario solo puede modificar los datos que esten en blanco, esta pensado para que el usuario actualice su información, posterior un administrador revisa los datos y si detecta que uno de ellos esta mal, borrará la inforamción y entonces el usuario deberá modificarla de nuevo, cuando los datos esten aprobados el usuario no podrá modificar los datos.

Documentación disponible en: [swagger](https://app.swaggerhub.com/apis-docs/JackCloudman/Tauros_API_Test/1)

Prueba la API que esta alojada en Oracle Cloud: http://tauros.juanjoserv.com:8888/api

Descarga la colleción de Postman [aquí](https://raw.githubusercontent.com/JackCloudman/tauros-rest-api/main/documentacion/Tauros%20test.postman_collection.json)

# Requirements
- django >= 3.1.6
- djangorestframework >= 3.12.2
- django-environ == 0.4.5
- virtualenv
- Probado en Python 3.8.2

# Install
Descargamos el repositorio e instalamos las dependencias

	git clone https://github.com/JackCloudman/tauros-rest-api.git
	cd tauros-rest-api
	virtualenv .venv --python=python3
	source .venv/bin/activate
	cd src
	pip install -r src/requirements.txt
 
 Creamos un super usuario
 
 	python manage.py migrate
	python manage.py createsuperuser --email contacto@juanjoserv.com --username jack
 
 ¡No olvides modificar el .env de ejemplo que se encuentra en tauros-rest-api/src/taurosapi!
 
 # Execute
  	python manage.py runserver
 
 
 
