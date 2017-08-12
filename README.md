# jitterbug
A just in time transpiler for Django.

h1. How it works
First, steal plugins.json from https://github.com/babel/babel-preset-env so that we can use the same mappings of
JS features to babel plugins. Then use that list of plugins as command line arguments for babel for the specific file
we want. Then use babili to minify the file since it is ES6 aware.

The files are transpiled based on the http user agent of the request. Currently httpagentparser is used to parse out
the browser name and version. When a file is transpiled it is saved in the same directory as <browser>.<version>.<filename>.
There is currently no cache time, so the file will live forever until it is deleted and jitterbug creates a new one to
replace it.
