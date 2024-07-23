export default function getStudentByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }
  if (students.filter((student) => student.location !== city)) {
    return [];
  }
  return students.filter((student) => student.location === city);
}
