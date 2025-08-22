# ES6 Basic

## Resources

Read or watch:

- [ECMAScript 6 - ECMAScript 2015](https://www.w3schools.com/js/js_es6.asp)
- [Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Declarations)
- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [Rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [Javascript ES6 — Iterables and Iterators](https://medium.com/@thejasonfile/javascript-es6-iterables-and-iterators-869d906442a0)

## Learning Objectives

By the end of this project, you should be able to explain:

- What ES6 is
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and default function parameters
- Rest and spread function parameters
- String templating in ES6
- Object creation and properties in ES6
- Iterators and for-of loops

## Requirements

- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **node 20.x.x** and **npm 9.x.x**
- Allowed editors: `vi`, `vim`, `emacs`, **Visual Studio Code**
- All files should end with a new line
- A `README.md` file at the root of the project is mandatory
- Use the `.js` extension for code files
- Code will be tested using the **Jest Testing Framework**
- Code will be analyzed using **ESLint** with provided rules
- All functions must be exported

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

Create the following files in your project directory:

- `package.json`
- `babel.config.js`
- `.eslintrc.js`

(See project instructions for file contents.)

## Final Steps

- Run `npm install` in your project folder to install all dependencies.
- **Do not push the `node_modules` folder** to your repository.
