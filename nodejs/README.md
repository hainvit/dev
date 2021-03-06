# NodeJS
* List of category
    * express nodejs
    * yarn/npm
    * testing with mocha
    * coding convention with eslint

## Express
* Flowing by tuts: https://www.tutorialspoint.com/expressjs/index.htm

## Yarn
* Flowing by tuts: https://classic.yarnpkg.com/en/docs/creating-a-project/
* Basic workflow:
    * 1. Create a new project
    * 2. Adding/updating/removing dependencies
    * 3. Installing/reinstalling your dependencies
    * 4. Working with version control
    * 5. Continuous Integration

### 1. Crating a new project
* Flowing command
```
$ yarn init

name (your-project):
version (1.0.0):
description:
entry point (index.js):
git repository:
author:
license (MIT):
```

### 2. Manaing dependencies
* Adding a denpendency
```
$ yarn add [package]
```
* yarn update history instal package
* Add other types of dependencies using flags:
    * `yarn add --dev` to add to `devDependencies`
    * `yarn add --peer` to add to `peerDependencies`
    * `yarn add --optional` to add to `optionalDependencies`
* Install with versions
```
$ yarn add [package]@[version]
$ yarn add [package]@[tag]
```
* Upgrading a denpendency
```
$ yarn upgrade [package]
$ yarn upgrade [package]@[version]
$ yarn upgrade [package]@[tag]
```
* Removing a denpendency
```
$ yarn remove [package]
```

## NPM
* Initial project
```
$ npm init
```
* Install local libs
```
$ npm i [pagekage]@[version] --save
```
* Install global libs
```
$ npm i [package]@[version]
```
* `npm uninstall [name]` removes the module from node_modules, but not `package.json`
* `npm uninstall [name] --save` also removes it from `dependencies` in `package.json`
* `npm uninstall [name] --save-dev` also removes it from `devDependencies` in `package.json`
* `npm -g uninstall <name> --save` also removes it globally

## Mocha
* Flowing by tuts:
    * https://gist.github.com/soheilhy/867f76feea7cab4f8a84
    * https://semaphoreci.com/community/tutorials/getting-started-with-node-js-and-mocha
    * https://mochajs.org/#-grep-regexp-g-regexp
* Run test
```
$ cd ROOT_FOLDE/node_modules/mocha/bin
$ ./mocha /home/rombk/hainv.work.it/dev/nodejs/mocha/test-calc.js
```

## Coding Conventions
*  Flowing by tuts:
    * https://github.com/airbnb/javascript
    * https://www.w3schools.com/js/js_conventions.asp
* Use eslint
    * https://eslint.org/docs/rules/
    * https://github.com/standard/eslint-config-standard
* Rule basics
    * IDE: VSCode
    * Use indent 4 (4 spaces)
    * Use blacktick with string
    * Use camelCase for indentifier name
    * Promise use resolve, reject
    * Limit in line 80 chars
    * File name conventions `file-name.js`

### Install ENV
* IDE:VSCode
* Extension: Prettier
* Config with VSCode
```
"editor.formatOnSave": false,
  "[javascript]": {
  "editor.formatOnSave": true
  }
```
* Setup file `package.json`
```
 "devDependencies": {
        "eslint": "^6.3.0",
        "eslint-config-standard": "^14.1.0",
        "eslint-plugin-import": "^2.18.2",
        "eslint-plugin-node": "^10.0.0",
        "eslint-plugin-promise": "^4.2.1",
        "eslint-plugin-standard": "^4.0.1"
    }
```
* Setup eslint commands in package.json
```
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "lint": "eslint ."
  },
```
* Run commands and fix bug