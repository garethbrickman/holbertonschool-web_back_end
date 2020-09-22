import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    // Create objs
    this._amount = amount;
    this._currency = currency;
  }

  // Methods

  displayFullPrice() {
    return (`${this.amount} ${this.currency.name} (${this.currency.code})`);
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }

  // Setters
  set amount(newAmount) {
    this._amount = newAmount;
  }

  set currency(newCurrency) {
    this._currency = newCurrency;
  }

  // Getters
  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }
}
