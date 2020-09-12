export default function appendToEachArrayValue(array, appendString) {
  const array2 = array;
  for (const [idx, item] of array2.entries()) {
    array2[idx] = appendString + item;
  }

  return array2;
}
