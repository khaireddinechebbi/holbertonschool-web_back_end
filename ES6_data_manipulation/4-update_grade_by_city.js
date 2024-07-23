export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const GradeObject = newGrades.find((grade) => grade.studentID === student.id);
      const grade = GradeObject ? GradeObject.grade : 'N/A';
      return { ...student, grade };
    });
}
