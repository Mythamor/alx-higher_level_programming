#!/usr/bin/node

const url = process.argv[2];
const filename = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  fs.writeFile(filename, body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
