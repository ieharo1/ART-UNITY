# Gateway de Aplicaciones WebGL con Nginx y Microservicio API

Arquitectura tipo edge gateway para experiencias WebGL, separando frontend y backend bajo un único punto de entrada.

## Descripción

Este servidor actúa como fachada de aplicación: entrega el frontend WebGL y enruta peticiones de API a un microservicio interno.

## ¿Qué hace este proyecto?

- Publica cliente WebGL estático detrás de Nginx.
- Expone una API desacoplada (Flask) para datos auxiliares.
- Centraliza tráfico HTTP con reverse proxy en `/api`.
- Permite escalar frontend y backend de forma independiente.

## Características Principales

| Característica | Descripción |
|---|---|
| Reverse proxy | Enrutamiento de `/api` hacia backend |
| Frontend desacoplado | Entrega estática de WebGL |
| Backend liviano | Microservicio Flask para endpoints de soporte |
| Puerta única | Menor complejidad para cliente final |

## Stack Tecnológico

- Nginx
- Python Flask
- Docker / Docker Compose

## Instalación y Uso

### Levantar entorno

```bash
docker compose up -d --build
```

### Probar

- Frontend: `http://localhost:8082`
- Health API: `http://localhost:8082/api/health`

## Variables de Entorno

- `NGINX_PORT`: puerto externo del gateway.

## Estructura del Proyecto

```text
.
├── Dockerfile
├── docker-compose.yml
├── .env
├── api/
│   ├── app.py
│   └── requirements.txt
├── webgl/
│   └── index.html
└── nginx/
    └── default.conf
```

## Casos de Uso

- Demos técnicas de videojuegos en web.
- Portales de visualización 3D con backend de catálogo.
- Publicación de clientes pesados con API ligera.

---

## ‍ Desarrollado por Isaac Esteban Haro Torres

**Ingeniero en Sistemas · Full Stack · Automatización · Data**

-  Email: zackharo1@gmail.com
-  WhatsApp: 098805517
-  GitHub: https://github.com/ieharo1
-  Portafolio: https://ieharo1.github.io/portafolio-isaac.haro/

---

##  Licencia

© 2026 Isaac Esteban Haro Torres - Todos los derechos reservados.
