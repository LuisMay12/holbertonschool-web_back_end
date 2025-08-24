// 10-car.js
export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Symbol.species lets subclasses override what constructor cloneCar should use
  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    // Create a new instance of the same constructor,
    // but with undefined properties (per project spec).
    const Ctor = this.constructor[Symbol.species];
    return new Ctor();
  }
}
