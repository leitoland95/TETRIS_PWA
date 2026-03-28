No puedo generar un archivo sw.js con contenido de HTML, sw.js es un archivo de JavaScript que se utiliza para implementar Service Workers en aplicaciones web.

/* eslint-disable no-undef */
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('tetris-cache').then((cache) => {
      return cache.addAll([
        '/',
        '/index.html',
        '/manifest.json',
        '/static/icons/icon-192.png',
        '/static/icons/icon-512.png',
      ]);
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== 'tetris-cache') {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
```