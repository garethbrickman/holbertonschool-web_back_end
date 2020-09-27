/* export default function cleanSet(set, startString) { */
function cleanSet() {
  let set = new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']);
  let startString = 'bon';
  if (startString && typeof startString === 'string') {
    const strings = [];
    for (const item of set) {
      if (item.startsWith(startString)) {
        strings.push(item.slice(startString.length));
      }
    }
    return strings.join('-');
  }
  return '';
}
console.log(cleanSet());