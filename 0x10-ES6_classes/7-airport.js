export default class Airport {
  constructor(name, code) {
    // Create objs
    this._code = code;
    this._name = name;
  }

  // Methods

  toString() {
    return `[object ${this._code}]`;
  }

  // Setters
  set name(newName) {
    this._name = newName;
  }

  set code(newCode) {
    this._name = newCode;
  }

  // Getters
  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }
}
