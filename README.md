# API REST USUARIOS V1.0.0

## Comenzando 🚀   
_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

_Requerimientos mínimos del sistema._

1. Gestor de Base de datos PostgreSQL.
2. Python3.x.
3. virtualenv.

### Instalación 🔧

_Sigue los siguientes pasos despues de tener instalado todos los requisitos mensionados enteriormente._

Descarga el proyecto desde el repositorio, desde la consola ejecuta el siguiente comando dentro de un directorio de tu elección.
```
$ git clone https://github.com/JoseMMenchaca/api-usuarios.git
```
Desde la consola de comando ingresa hasta el directorio del proyecto descargado ejecutando el siguiente comando.
```
$ cd /api-usuarios

```

Dentro del directorio del proyecto ejecuta los siguientes comandos para crear un entorno virtual y activarlo.

```
$ python -m venv .venv
$ .\.venv\Scripts\activate
```
Despues de activar el entorno virtual, ejecuta el siguiente comando para instalar las librerias requeridas para el funcionamiento del sistema.

```
(env)$ pip install -r requirements.txt
```

Crear una copia del archivo .env-example a .env, configurar y cambiar con sus credenciales lo siguiente:

````
SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:contraseña@localhost:5432/base_de_datos'
````
Ejecutar las siguientes lineas en la consola para generar las migraciones y tablas de la base de datos
````
(env)$ flask db init
(env)$ flask db migrate -m "base de datos inicial"
(env)$ flask db upgrade
````

Finalmente tienes listo el Api Rest para su funcionamiento y consumo, para poner en marcha el servidor de desarrollo ejecuta el siguiente comando.
````
(env)$ python run.py
````
## Ejecutando las pruebas ⚙️

Para observar el despliegue del sistema, ingresa el siguiente enlace http://localhost:5000/api/v1/usuario en tu navegador, deberias obtener la lista de los registro de la tabla usuarios en formato JSON.
````
{
    "data": []
}
````
## ENDPOINTS ⚙️
http://localhost:5000/api/v1/usuario                METHOD GET  Mostrar usuarios
http://localhost:5000/api/v1/usuario                METHOD POST Crear nuevo Usuario
http://localhost:5000/api/v1/usuario/id_usuario     METHOD GET  Mostrar usuario específico
http://localhost:5000/api/v1/usuario/id_usuario     METHOD PUT  Actualizar un usuario 
http://localhost:5000/api/v1/usuario/id_usuario     METHOD DELETE  Eliminar un usuario 
http://localhost:5000/api/v1/usuario/promedio-edad  METHOD GET  Mostrar el promedio de edades
http://localhost:5000/api/v1/usuario/estado         METHOD GET  Información de la API

Para consumir los servicios del api rest te recomiendo que tengas instalado [Postman](https://www.postman.com/downloads/).


## Autor ✒️

* [JOSÉ MANUEL MENCHACA ENCINAS] *
