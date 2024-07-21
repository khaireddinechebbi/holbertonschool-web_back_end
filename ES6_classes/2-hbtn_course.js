export default class HolbertonCourse {
  constructor(name, lenght, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;

    if (typeof lenght !== 'number') {
      throw new TypeError('Lenght must be a number');
    }
    this._lenght = lenght;

    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(newname) {
    if (typeof newname !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newname;
  }

  get lenght() {
    return this._lenght;
  }

  set lenght(newlenght) {
    if (typeof newlenght !== 'number') {
      throw new TypeError('Lenght must be a nember');
    }
    this._lenght = newlenght;
  }

  get students() {
    return this._students;
  }

  set students(newstudents) {
    if (!Array.isArray(newstudents) || !newstudents.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of srtings');
    }
    this._students = newstudents;
  }
}
