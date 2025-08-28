# ES6 Data Manipulation

## Resources

Read or watch:

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)
- [Set Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

## Learning Objectives

By the end of this project, you should be able to explain:

- How to use `map`, `filter`, and `reduce` on arrays
- Typed arrays
- The Set, Map, and WeakMap data structures

## Requirements

- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Node 20.x.x** and **npm 9.x.x**
- Allowed editors: `vi`, `vim`, `emacs`, **Visual Studio Code**
- All files should end with a new line
- A `README.md` file at the root of the project is mandatory
- Your code should use the `.js` extension
- Your code will be tested using **Jest** and the command `npm run test`
- Your code will be verified against lint using **ESLint**
- Your code needs to pass all the tests and lint. You can verify the entire project running `npm run full-test`
- All of your functions must be exported

## Setup

### Install NodeJS 20.x.x

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v
# v20.15.1
npm -v
# 10.7.0
```

### Install Jest, Babel, and ESLint

In your project directory:

```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

## Configuration Files

Make sure to include and configure the necessary files for Babel, Jest, and ESLint in your project.