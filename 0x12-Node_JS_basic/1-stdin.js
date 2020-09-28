console.log('Welcome to Holberton School, what is your name?');
process.stdin.resume();
process.stdin.on('readable', () => {
  // check if input is coming from the terminal
  if (process.stdin.isTTY) {
    const name = process.stdin.read();
    process.stdout.write(`Your name is: ${name}`);
    process.exit();
  // not coming from the terminal
  } else {
    const name = process.stdin.read();
    process.stdout.write(`Your name is: ${name}`);
    process.stdout.write('This important software is now closing\n');
    process.exit();
  }
});
