# curso-pip-entornos-virtuales

Este es un repositorio de practica, creado para el curso de pip y entornos virtuales

La idea es iniciar con un juego creado en python

## Game proyect

Para seguir este juego debes seguir las siguientes instruccuionees en la terminal

```sh
cd game
python main.py
```

## Creación de un paquete

Primero se instaló matplotlib

```sh
pip install matplotlib
```

Luego, se creo una nueva carpeta charts con dos scripts de python charts.py y main.py
Para ejecutarlos se hace lo siguiente

```sh
cd charts
python main.py
```

## Creación y activación de entornos virtuales

Primero te ubicas dentro d ela carpeta dond evas a crear el ambiente virtual (virtual enviroment)

```sh
cd [Nombre_directorio]
#creación del ambiente virtual
python -m venv my-env #pones el nombre que quieras a tu ambiente virtual
#activacion delo ambiente virual
\.my-env\Scripts\Activate
```

# App proyect
Para contribuir a este proyecto, debes realizar los siguientes pasos

```sh
git clone
cd app
python -m venv my-env
\.my-env\Scripts\Activate
pip install -r requirements.txt
python main.py
```