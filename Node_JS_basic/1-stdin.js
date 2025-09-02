// 1-stdin.js
process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (chunk) => {
  const name = chunk.toString().trim();
  process.stdout.write(`Your name is: ${name}\n`);
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});

// When user presses Ctrl+C (SIGINT), print closing line and exit cleanly
process.on('SIGINT', () => {
  process.stdout.write('This important software is now closing\n');
  process.exit(0);
});
