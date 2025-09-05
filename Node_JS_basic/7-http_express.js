// 7-http_express.js
const express = require('express');
const fs = require('fs');

const app = express();
const dbPath = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    if (!path) {
      reject(new Error('Cannot load the database'));
      return;
    }

    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .map((l) => l.trim())
        .filter((l) => l.length > 0);

      if (lines.length <= 1) {
        resolve('Number of students: 0');
        return;
      }

      const rows = lines.slice(1);
      const byField = new Map();
      let total = 0;

      for (const row of rows) {
        const cols = row.split(',');
        if (cols.length < 4) continue;

        const firstName = cols[0].trim();
        const field = cols[3].trim();
        if (!firstName || !field) continue;

        if (!byField.has(field)) byField.set(field, []);
        byField.get(field).push(firstName);
        total += 1;
      }

      const parts = [`Number of students: ${total}`];
      for (const [field, list] of byField.entries()) {
        parts.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }
      resolve(parts.join('\n'));
    });
  });
}

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  const header = 'This is the list of our students';

  countStudents(dbPath)
    .then((report) => res.send(`${header}\n${report}`))
    .catch((err) => res.send(`${header}\n${err.message}`));
});

app.listen(1245);

module.exports = app;
