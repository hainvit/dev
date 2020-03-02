# typescript
* Flowing by tuts: https://www.tutorialspoint.com/typescript/index.htm

## helloworld
* Create `helloworld`
```
$ mkdir helloworld
$ npm i typescript --save
```
* Edit file `package.json`
```
Add script to file package.json
"tsc": "tsc"
```
* Create file `tsconfig.json`
```
$ npm run tsc -- --init
```
* Config build folders
```
"ourDir":"./build"
```
* Create file `helloworld.ts` with contents
```
console.log('hello world typescript');
```
* Build file `.ts` to `.js`
```
$ npm run tsc
```
* Run exampels
```
$ node ./build/hello-world.js
```