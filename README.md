# Tetris PWA

## Descripción

Una implementación del juego clásico Tetris con una interfaz futurista como Progressive Web App (PWA) utilizando tecnologías modernas.

## Requisitos

* Node.js (última versión)
* Python (última versión)
* FastAPI
* Uvicorn
* Workbox

## Comandos

### Desarrollo

* `npm run dev` para iniciar el servidor de desarrollo de frontend
* `uvicorn main:app --host 0.0.0.0 --port 8000` para iniciar el servidor de desarrollo de backend

### Construcción

* `npm run build` para construir el frontend
* `docker build -t tetris-pwa .` para construir la imagen de Docker

### Despliegue

* `npm run deploy` para desplegar la PWA en producción

## Checklist PWA

* [ ] HTTPS
* [ ] Manifest.json
* [ ] Iconos
* [ ] Offline flows
* [ ] Lighthouse
* [ ] Service Worker

## Contribuir

Si deseas contribuir, por favor crea un fork de este repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está bajo la licencia MIT. Ver archivo LICENSE para más detalles.