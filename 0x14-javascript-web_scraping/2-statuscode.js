#!/usr/bin/node
const request = require('request');
const arg = process.argv;
const url = arg[2];
request.get(url, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
