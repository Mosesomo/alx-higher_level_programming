#!/usr/bin/node
const fs = require('fs');
const arg = process.argv;
const path = arg[2];
fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
