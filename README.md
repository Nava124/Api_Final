# 💳 Sistema de Pagos - API REST

Este proyecto implementa una API REST para la gestión de usuarios y transacciones de pago. Forma parte de una prueba técnica de desarrollo con una duración estimada de 48 horas.

## 🚀 Funcionalidades

- Registro de nuevos usuarios
- Inicio de transacciones de pago
- Consulta de historial de transacciones por usuario
- Validación de transacciones autorizadas

## 🛠️ Tecnologías

- **Python 3.10+**
- **FastAPI** (framework backend)
- **SQLAlchemy** (ORM)
- **SQLite** (base de datos para pruebas)
- **Pytest** (pruebas unitarias)
- **GitHub Actions** (CI/CD)

## 📦 Instalación

```bash
git clone https://github.com/tuusuario/sistema-pagos-api.git
cd sistema-pagos-api
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ Uso

```bash
uvicorn app.main:app --reload
```

Visita la documentación interactiva en: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🧪 Ejecutar pruebas

```bash
set PYTHONPATH=.
pytest -s
```

## 📁 Estructura del Proyecto

```
.
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── routers/
│       ├── users.py
│       ├── payments.py
│       ├── transactions.py
│       └── schemas.py
├── tests/
│   ├── conftest.py
│   ├── test_users.py
│   ├── test_payments.py
│   └── test_transactions.py
├── requirements.txt
└── .github/workflows/python-ci.yml
```

## 🔒 Validación de Transacciones

Una transacción puede validarse mediante:

```http
GET /transactions/{transaction_id}/validate
```

Devuelve el estado y detalles de la transacción si es válida.

## ✅ CI/CD

Este proyecto cuenta con integración continua usando **GitHub Actions**. Cada push o PR ejecuta:

- Linter `flake8`
- Pruebas `pytest`

El archivo de configuración se encuentra en `.github/workflows/python-ci.yml`.

## 👨‍💻 Autor

**Nahum** – Prueba técnica para proceso de selección.

---

¡Gracias por revisar este proyecto!