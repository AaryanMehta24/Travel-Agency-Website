// var staticCacheName = 'djangopwa-v2';

// self.addEventListener('install', function(event) {
// event.waitUntil(
// 	caches.open(staticCacheName).then(function(cache) {
// 	return cache.addAll([
// 		'',
// 	]);
// 	})
// );
// });

// self.addEventListener('fetch', function(event) {
// var requestUrl = new URL(event.request.url);
// 	if (requestUrl.origin === location.origin) {
// 	if ((requestUrl.pathname === '/')) {
// 		event.respondWith(caches.match(''));
// 		return;
// 	}
// 	}
// 	event.respondWith(
// 	caches.match(event.request).then(function(response) {
// 		return response || fetch(event.request);
// 	})
// 	);
// });
if ('serviceWorker' in navigator) {

    navigator.serviceWorker.getRegistrations().then(function(registrations) {

    for(let registration of registrations) {

            registration.unregister()

    }}).catch(function(err) {

        console.log('Service Worker registration failed: ', err);

    });
}

var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        'login'
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('login'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});

