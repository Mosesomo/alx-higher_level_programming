#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode >= 200 && response.statusCode < 300) {
    fs.writeFile(path, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
        return;
      }
      return (path);
    });
  }
});
