# Servicio de Usuarios con FastAPI

Aplicación de FastAPI para la gestión de usuarios.

## Características

- Endpoint de verificación del funcionamiento de la API
- Endpoints para crear usuarios, obtener la información por ID de un usuario y borrar un usuario.
- Diseño de API RESTful
- Documentación de API autogenerada (Swagger UI)

## Requisitos Previos

- Python 3.10+
- pip

## Configuración

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecutar el Servidor

Inicia el servidor de desarrollo con auto-recarga:
```bash
uvicorn api_server:app --reload
```

El servidor iniciará en `http://localhost:8000`

### Ejecutar el Frontend

Para servir la interfaz frontend HTML:
```bash
python -m http.server 8080
```

El frontend estará disponible en `http://localhost:8080`

### Opciones Adicionales para el Backend

Ejecutar en un puerto diferente:
```bash
uvicorn api_server:app --reload --port 8080
```

Ejecutar en un host diferente:
```bash
uvicorn api_server:app --reload --host 0.0.0.0
```

## Documentación de la API

Una vez que el servidor esté en ejecución, puedes acceder a:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## Desarrollo

La aplicación utiliza la validación automática de solicitudes y generación de documentación de FastAPI.

### Estructura del Proyecto
```
API_server/
├── api_server.py      # Aplicación principal de FastAPI
├── requirements.txt   # Dependencias de Python
└── README.md         # Este archivo
```
