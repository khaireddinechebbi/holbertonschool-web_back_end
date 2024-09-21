const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf-8');
        const lines = data.split('\n');
        const validLines = lines.filter(line => line.trim() !== '');
        if (validLines.length <= 1) {
            throw new Error('Cannot load the database');
        }
        const students = validLines.slice(1);
        console.log(`Number of students: ${students.length}`);
        const fields = {};
        students.forEach((line) => {
            const [firstname, lastname, age, field] = line.split(',');
            if (firstname && field) {
                if (!fields[field]) {
                    fields[field] = [];
                }
                fields[field].push(firstname);
            }
        });
        for (const [field, names] of Object.entries(fields)) {
            console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }
    } catch(err) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;