export default class Car {
  constructor(brand, motor, color) {
    // Create objs
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Methods

  cloneCar() {
    return this.constructor[Symbol.species];
  }

  // Setters

  // Getters
}
