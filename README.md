# jitterbug
A just in time transpiler for Django. Instantly check your JavaScript changes while developing instead of waiting for your development server to transpile everythig.

## How it works
First, steal plugins.json from [babel-preset-env](https://github.com/babel/babel-preset-env) so that we can use the same mappings of JS features to babel plugins. Then use that list of plugins as command line arguments for babel for the specific file we want. Then use babili to minify the file since it is ES6 aware.

The files are transpiled based on the http user agent of the request. Currently [httpagentparser](https://pypi.python.org/pypi/httpagentparser) is used to parse out the browser name and version. When a file is transpiled it is saved in the same directory as <browser>.<version>.<filename>. There is currently no cache time, so the file will live forever until it is deleted and jitterbug creates a new one to replace it.

## Installing
TODO

This project relies on the [babel](https://www.npmjs.com/package/Babel) and [babili-cli](https://www.npmjs.com/package/babel-cli) packages being installed globally. They are used to transpile and minify the files for incoming requests. You'll also need to install all of the plugins listed in [plugins.json](jitterbug/static/plugins.json). You can use `jitterbug.install_helper.run_npm_install` to install of these.
