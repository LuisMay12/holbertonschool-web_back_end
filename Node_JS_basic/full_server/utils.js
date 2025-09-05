// full_server/utils.js
import { promises as fs } from 'fs';

export default async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf-8');

    const lines = data
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l.length > 0);

    // Expect header line present
    const rows = lines.slice(1);
    const byField = {};

    for (const row of rows) {
      const cols = row.split(',');
      if (cols.length < 4) continue; // skip malformed rows
      const firstName = cols[0].trim();
      const field = cols[3].trim();
      if (!firstName || !field) continue;

      if (!byField[field]) byField[field] = [];
      byField[field].push(firstName); // order of appearance preserved
    }

    return byField;
  } catch {
    throw new Error('Cannot load the database');
  }
}
