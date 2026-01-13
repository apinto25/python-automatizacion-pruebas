# Python: Automatización de Pruebas

Este es el repositorio del curso Python: Automatización de pruebas, cubre desde pruebas unitarias hasta pruebas de interfaz web.

## 📋 Descripción

Este repositorio contiene el material práctico del curso "Python: Automatización de Pruebas", diseñado para enseñar las mejores prácticas y técnicas de testing automatizado en aplicaciones Python.

## 🎯 Objetivos

- Dominar los fundamentos de las pruebas automatizadas en Python
- Implementar pruebas unitarias efectivas con pytest
- Realizar pruebas de integración con bases de datos
- Automatizar pruebas de APIs REST
- Crear pruebas de interfaz de usuario web con Selenium

## 📚 Contenido del Curso

### API_server
Servidor FastAPI utilizado como aplicación de ejemplo para las pruebas. Proporciona endpoints RESTful para gestión de usuarios. Este servicio se usa para las pruebas E2E de los capítulos 4 y 5.

**Tecnologías:** FastAPI, Uvicorn

### Capítulo 2: Pruebas Unitarias (`c2_pruebas_unitarias/`)
Introducción a las pruebas unitarias con pytest. Aprende a:
- Estructurar casos de prueba
- Usar fixtures y conftest
- Implementar pruebas parametrizadas
- Validar funciones individuales
- Manejar casos edge y errores

**Tecnologías:** pytest

### Capítulo 3: Pruebas de Integración (`c3_pruebas_integracion/`)
Pruebas de integración con bases de datos. Incluye:
- Conexión y configuración de bases de datos de prueba
- Pruebas de operaciones CRUD
- Gestión de transacciones en pruebas
- Fixtures para datos de prueba
- Rollback y limpieza de datos

**Tecnologías:** pytest, SQLite/bases de datos

### Capítulo 4: Pruebas de API REST (`c4_pruebas_api_rest/`)
Automatización de pruebas para APIs RESTful. Cubre:
- Pruebas de endpoints HTTP (GET, POST, PUT, DELETE)
- Validación de códigos de estado
- Verificación de respuestas JSON
- Pruebas de health checks
- Generación de reportes con Allure

**Tecnologías:** pytest, requests, Allure

### Capítulo 5: Pruebas Web UI (`c5_pruebas_web_ui/`)
Automatización de pruebas de interfaz de usuario. Aprende a:
- Configurar Selenium WebDriver
- Localizar elementos en la página
- Interactuar con formularios
- Implementar Page Object Model
- Ejecutar pruebas en diferentes navegadores

**Tecnologías:** pytest, Selenium WebDriver

## 🚀 Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- pyenv (recomendado para gestión de versiones)
- Navegador web (Chrome/Firefox para pruebas UI)

## ⚙️ Configuración del Entorno

1. **Clonar el repositorio:**
```bash
git clone https://github.com/apinto25/python-automatizacion-pruebas.git
cd python-automatizacion-pruebas
```

2. **Configurar el entorno de Python:**
```bash
pyenv shell test_automation
```

3. **Instalar dependencias del servidor API:**
```bash
cd API_server
pip install -r requirements.txt
```

4. **Instalar pytest y herramientas de testing:**
```bash
pip install pytest pytest-cov allure-pytest selenium
```

## 🏃 Ejecución

### Iniciar el Servidor API
```bash
cd API_server
uvicorn api_server:app --reload
```

### Ejecutar Pruebas Unitarias
```bash
cd c2_pruebas_unitarias
pytest tests/ -v
```

### Ejecutar Pruebas de Integración
```bash
cd c3_pruebas_integracion
pytest tests/ -v
```

### Ejecutar Pruebas de API
```bash
cd c4_pruebas_api_rest
pytest -v
```

### Ejecutar Pruebas Web UI
```bash
cd c5_pruebas_web_ui
pytest -v
```

## 📊 Reportes

### Generar Reporte de Cobertura
```bash
pytest --cov=. --cov-report=html
```

### Generar Reporte Allure
```bash
pytest --alluredir=./results
allure serve ./results
```

## 📁 Estructura del Proyecto

```
python_automatizacion_pruebas/
├── API_server/              # Servidor FastAPI de ejemplo
│   ├── api_server.py
│   ├── index.html
│   ├── requirements.txt
│   ├── models/
│   └── data/
├── c2_pruebas_unitarias/    # Capítulo 2: Pruebas unitarias
│   ├── main.py
│   └── tests/
├── c3_pruebas_integracion/  # Capítulo 3: Pruebas de integración
│   ├── main.py
│   └── tests/
├── c4_pruebas_api_rest/     # Capítulo 4: Pruebas de API REST
│   ├── test_api_health.py
│   ├── test_create_user.py
│   └── test_get_user.py
├── c5_pruebas_web_ui/       # Capítulo 5: Pruebas Web UI
│   └── test_create_user_form.py
└── README.md                # Este archivo
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.10+** - Lenguaje de programación
- **pytest** - Framework de testing
- **FastAPI** - Framework web para APIs
- **Selenium** - Automatización de navegadores web
- **Allure** - Framework de reportes
- **SQLite** - Base de datos para pruebas de integración

## 📖 Recursos Adicionales

- [Documentación de pytest](https://docs.pytest.org/)
- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de Selenium](https://www.selenium.dev/documentation/)
- [Allure Framework](https://docs.qameta.io/allure/)

## 👤 Autor

**apinto25**
- GitHub: [@apinto25](https://github.com/apinto25)

## 📝 Licencia

Este proyecto es material educativo del curso "Python: Automatización de Pruebas".

---

⭐ Si este curso te resulta útil, no olvides darle una estrella al repositorio.
