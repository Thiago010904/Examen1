Integrantes:
SANTIAGO QUINTERO GRISALES
HELEN YURAHAY YANES BARON
CARLOS MARIO ATEHORTUA PINEDA

Para descargar las dependencias poner el comando "pip install -r requirements.txt"

-----------------------------------------------------------------------------------------------
En git bash dentro del proyecto 
python -m venv venv 

luego activarlo 
source venv/Scripts/activate 

Cuando está activo se debe visualizar 
(venv)

Ejecuta el microservicio con Uvicorn utilizando el comando "uvicorn main:app --reload"

En la url " http://127.0.0.1:8000" aparece el proyecto

se agrega el "/docs" al final de la url para acceder al swagger y ya se puede crear una nueva reserva en el metodo POST y se vera en el metodo GET