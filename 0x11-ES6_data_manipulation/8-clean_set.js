export default function cleanSet(set, startString) {
  const strings = [];
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
