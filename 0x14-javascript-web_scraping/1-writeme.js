#!/usr/bin/node
const fs = require('fs');
const arg = process.argv;
const path = arg[2];
const content = arg[3];
fs.writeFile(path, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
