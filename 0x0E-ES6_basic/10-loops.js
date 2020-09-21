export default function appendToEachArrayValue(array, appendString) {
  const array2 = [];
  for (const [idx, item] of array.entries()) {
    array2[idx] = appendString + item;
  }

  return array2;
}
