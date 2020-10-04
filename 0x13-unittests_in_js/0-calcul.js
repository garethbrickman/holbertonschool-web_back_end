module.exports = function calculateNumber(a, b) {
  const numA = Number(a);
  const numB = Number(b);

  return (Math.round(numA) + Math.round(numB));
}
