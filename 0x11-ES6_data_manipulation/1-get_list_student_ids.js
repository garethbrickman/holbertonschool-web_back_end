export default function getListStudentIds(students) {
  // check arg is an array before using map
  if (Object.getPrototypeOf(students) === Array.prototype) {
    return students.map((items) => items.id);
  } return [];
}
