export default function taskBlock(trueOrFalse) {
  let task = false; // Using let for block-scoping
  let task2 = true; // Using let for block-scoping

  if (trueOrFalse) {
    task = true; // Directly assign to the existing task variable
    task2 = false; // Directly assign to the existing task2 variable
  }

  return [task, task2];
}
