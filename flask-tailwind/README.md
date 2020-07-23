Flask Tailwind
======================

This is a sample project that uses tailwind css in a flask app.  It also uses
laravel mix in order to make configuring webpack easier.

Quickstart
----------

1. **Install dependencies**

    `npm install && pipenv sync --dev`

2. **Build the css**

    `npm run dev` or `npm run prod`

    Or `npm run watch` so that the css is built whenever changes are made

3. **Run the app**

    `pipenv run flask run`


So what the heck is happening?
------------------------------

First things first.  Laravel mix is a wrapper around Webpack that covers 95%
of use cases out of the box.  It provides convenient functions that make it easy
to bundle preprocessed or vanilla JavaScript and CSS in to one or many bundles.

For example to do a react app you simply write:

```js
mix.react('path/to/app/entry/point.js', 'app/static/bundle.js');
```

But in this sample project we only care about tailwind, which is powered by
PostCSS.  PostCSS is a tool that is used to transform CSS using JavaScript.
Laravel mix has a helper for it:

```js
mix.postCss('path/to/main.css', 'app/static/bundle.css');
```

But without any plugins, PostCSS does nothing to the css.  So we need to
include the tailwind plugin:

```js
mix.postCss('app/css/main.css', 'app/static/bundle.css', [
  require('tailwindcss'),
]);
```

When running `npm run prod` it will also pass the compiled css through PurgeCSS.  
Your templates will be scanned for what clases you use, and the rest will be 
thrown away from the final built css, which is placed in app/static/bundle.css
for the flask app to easily find.
