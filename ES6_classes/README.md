# ES6 Classes

## Resources
Read or watch:
- [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [Metaprogramming](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming)

## Learning Objectives
By the end of this project, you should be able to explain:
- How to define a Class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols

## Requirements
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Node 20.x.x** and **npm 9.x.x**
- Allowed editors: `vi`, `vim`, `emacs`, **Visual Studio Code**
- All files should end with a new line
- A `README.md` file at the root of the project is mandatory
- Code should use the `.js` extension
- Code will be tested using **Jest** and the command `npm run test`
- Code will be verified against lint using **ESLint**
- All tests and lint must pass (`npm run full-test`)

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
- `package.json`
- `babel.config.js`
- `.eslintrc.js`

> **Note:** Don’t forget to run `npm install` when you have the `package.json`.
