# Python Backend Server

Este proyecto es un servidor backend construido en Python utilizando Flask. Está diseñado para ser utilizado como una API que se puede conectar a una aplicación frontend desarrollada en React.

## Estructura del Proyecto

```
python-backend-server
├── src
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── controllers      # Controladores para manejar la lógica de negocio
│   ├── routes           # Rutas de la aplicación
│   └── models           # Modelos de datos
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación del proyecto
```

## Requisitos

Asegúrate de tener Python 3.x instalado en tu máquina. También necesitarás instalar las dependencias del proyecto.

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd python-backend-server
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar el servidor, utiliza el siguiente comando:

```
python src/main.py
```

El servidor se iniciará en `http://localhost:5000` por defecto.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.