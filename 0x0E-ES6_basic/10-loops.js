export default function appendToEachArrayValue(array, appendString) {
  const newArray = array;
  for (const [idx, item] of newArray.entries()) {
    newArray[idx] = appendString + item;
  }

  return newArray;
}
