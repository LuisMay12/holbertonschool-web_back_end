// 3-read_file_async.js
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Split lines, trim, and drop empties
      const lines = data
        .split('\n')
        .map((l) => l.trim())
        .filter((l) => l.length > 0);

      if (lines.length <= 1) {
        console.log('Number of students: 0');
        resolve();
        return;
      }

      // Remove header
      const [, ...rows] = lines;

      // Group by field while preserving insertion order
      const byField = new Map();
      let total = 0;

      for (const row of rows) {
        // Expect CSV with at least 4 columns
        const parts = row.split(',');
        if (parts.length < 4) continue;

        const firstName = parts[0].trim();
        const field = parts[3].trim();

        if (!firstName || !field) continue;

        if (!byField.has(field)) byField.set(field, []);
        byField.get(field).push(firstName);
        total += 1;
      }

      console.log(`Number of students: ${total}`);
      for (const [field, list] of byField.entries()) {
        console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }

      resolve();
    });
  });
}

module.exports = countStudents;
