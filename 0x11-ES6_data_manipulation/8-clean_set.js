export default function cleanSet(set, startString) {
  if (startString && typeof startString === 'string') {
    const strings = [];
    for (const item of set) {
      if (item.startsWith(startString)) {
        strings.push(item);
      }
    }
    return strings.join('-');
  }
  return '';
}
