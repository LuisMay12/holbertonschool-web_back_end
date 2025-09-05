// 5-http.js
const http = require('http');
const fs = require('fs');

const dbPath = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Split -> trim -> drop empty lines (trailing blanks aren’t students)
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

      const parts = [];
      parts.push(`Number of students: ${total}`);
      for (const [field, list] of byField.entries()) {
        parts.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }
      resolve(parts.join('\n'));
    });
  });
}

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    res.statusCode = 200;
    const header = 'This is the list of our students';

    countStudents(dbPath)
      .then((report) => {
        res.end(`${header}\n${report}`);
      })
      .catch((err) => {
        res.end(`${header}\n${err.message}`);
      });

    return;
  }

  // Any other endpoint -> same body as root (spec says “plain text” and
  // only defines responses for "/" and "/students”; safest is 404)
  res.statusCode = 404;
  res.end('Not found');
});

app.listen(1245);

module.exports = app;
