# EmailTest

## Descripción
Este proyecto es una aplicación desarrollada en Python que permite enviar correos electrónicos utilizando el protocolo SMTP.  
El programa se ejecuta desde la consola y solicita al usuario los datos necesarios para enviar el correo.

El cuerpo del correo incluye los nombres de los integrantes del equipo, cumpliendo con los requisitos funcionales del ejercicio académico.

## Requisitos Funcionales
- Enviar correos electrónicos.
- El cuerpo del correo debe contener el nombre de cada integrante del equipo.

## Requisitos Técnicos
- Proyecto construido aplicando conceptos básicos de ingeniería de software.
- Uso de variables de entorno para proteger credenciales.
- Envío del enlace (URL) del repositorio de GitHub dentro del correo electrónico.

## Tecnologías Utilizadas
- Python 3
- Librerías estándar:
  - smtplib
  - ssl
  - os
- Librería externa:
  - python-dotenv

## Estructura del Proyecto

EmailTest
│
├── main.py
├── email_sender.py
├── message_builder.py
├── .env
├── README.md
 

## Configuración
Antes de ejecutar el programa, se debe crear un archivo `.env` con la siguiente información:

EMAIL_SENDER=correo@gmail.com
EMAIL_PASSWORD=contraseña_de_aplicación


> Para Gmail se recomienda usar una contraseña de aplicación.

## Ejecución del Programa
Desde la terminal, ejecutar:


El programa solicitará:
- Correo del destinatario
- Asunto
- Cuerpo del mensaje (finaliza escribiendo `END`)

## Observaciones
En caso de presentarse inconvenientes técnicos durante el desarrollo del proyecto, estos deben ser documentados en un archivo con el formato:


y copiados en la carpeta indicada por el docente.

## Repositorio
El enlace del repositorio GitHub debe ser enviado dentro del correo electrónico, tal como lo solicita el enunciado del proyecto.
