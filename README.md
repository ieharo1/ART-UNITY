# ART-UNITY - Nginx Gateway + API

Este repo queda como ejemplo de gateway para Unity WebGL con backend desacoplado.

## Arquitectura

- `unity-nginx`: entrega frontend WebGL y enruta `/api`.
- `unity-api`: microservicio Flask para catalogo/health.
- `.env`: controla puerto de publicacion.

## Levantar

```bash
docker compose up -d --build
```

Abrir: `http://localhost:8082`

## Variables

- `NGINX_PORT`: puerto del gateway.

## Valor para perfil

- Patron real de reverse proxy para juegos/web apps.
- Separacion frontend Unity y API de soporte.

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
