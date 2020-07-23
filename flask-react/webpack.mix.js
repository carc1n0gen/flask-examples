const mix = require('laravel-mix');

mix.setPublicPath('server');
mix.react('client/index.js', 'static/index.js');

mix.options({
  hmrOptions: {
    host: 'localhost',
    port: 9000
  }
});

mix.webpackConfig({
  devServer: {
    proxy: {
      '/': {
        target: 'http://localhost:6000',
        pathRewrite: function(path) {
          if (path.startsWith('/static') || path.startsWith('/api')) {
              // If the request is to /static or /api, don't rewrite the path
              // so that server side routing (in flask) happens.
              return path;
          }

          // Otherwise, rewrite the path to / where the react app takes over
          // using react-router for client side routing.
          return '/';
        },
        secure: false
      },
    }
  }
});
