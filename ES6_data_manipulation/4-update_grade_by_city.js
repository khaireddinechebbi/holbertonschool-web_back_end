export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city).map((student) => {
    const GradeObject = newGrades.find((grade) => grade.studentID = student.id);
    return {
      ...student, grade: GradeObject ? GradeObject.grade : 'N/A',
    };
  });
}
