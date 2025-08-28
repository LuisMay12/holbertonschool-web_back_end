export default function getListStudentIds(list) {
  // Check if input is actually an array
  if (!Array.isArray(list)) {
    return [];
  }
  // Use map to extract only the ids
  return list.map((student) => student.id);
}
