const calculateNumber = require("./0-calcul.js");
const mocha = require('mocha');
const assert = require("assert");

describe('calculateNumber', () => {
    it('returns rounded sum', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
    });
});