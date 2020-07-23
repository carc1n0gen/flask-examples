const mix = require('laravel-mix');

mix.postCss('app/css/main.css', 'app/static/bundle.css', [
  require('tailwindcss'),
]);
