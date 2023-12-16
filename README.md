# Testing-Automation

# En este repositorio se cargaran los Casos de Prueba automatizados correspondiente al Trabajo integrador - Provinciano

# Instrucciones para configurar el entorno virtual y la instalación de módulos

Este archivo proporciona instrucciones paso a paso para configurar un entorno virtual utilizando virtualenv y para instalar los módulos necesarios desde un archivo requirements.txt.

## Paso 1: Instalación del entorno virtual (virtualenv)

Asegúrate de tener instalado Python 3.12 en tu sistema. Luego, abre una terminal y ejecuta el siguiente comando para instalar virtualenv:

pip install virtualenv

## Paso 2: Crear y activar un entorno virtual
En la misma terminal, crea un nuevo directorio para tu proyecto (si aún no lo has hecho) y navega a él. Luego, ejecuta los siguientes comandos para crear y activar un entorno virtual:
# Crear un entorno virtual

virtualenv venv

## Activar el entorno virtual (en Windows)
venv\Scripts\activate

## Paso 3: Instalar los módulos desde requirements.txt
Con el entorno virtual activado, usa el siguiente comando para instalar los módulos necesarios desde el archivo requirements.txt:

pip install -r requirements.txt

## Paso 4: Desactivar el entorno virtual (opcional)
Cuando hayas terminado de trabajar en tu proyecto, puedes desactivar el entorno virtual ejecutando el siguiente comando:
deactivate

# Ejecutar las pruebas
Para ejecutar las pruebas y generar un informe HTML, utiliza el siguiente comando

pytest -v --html=report.html

Este comando ejecutará todas las pruebas en el directorio actual, proporcionará información detallada con la opción -v y generará un informe en formato HTML llamado report.html.

## Visualizar el informe
Después de ejecutar las pruebas, abre el archivo report.html en un navegador web para visualizar el informe detallado de las pruebas.
