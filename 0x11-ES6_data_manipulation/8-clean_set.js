<<<<<<< HEAD
export default function cleanSet(set, startString) {
  const strings = [];
=======
/* export default function cleanSet(set, startString) { */
function cleanSet() {
  let set = new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']);
  let startString = 'bon';
>>>>>>> parent of b7dbf8a... Remove test lines
  if (startString && typeof startString === 'string') {
    for (const item of set) {
      if (item.startsWith(startString)) {
        strings.push(item.slice(startString.length));
      }
    }
    return strings.join('-');
  }
  strings.push(''.slice(0, -1));
  return strings;
}
console.log(cleanSet());