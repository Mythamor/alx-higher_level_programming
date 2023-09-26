#!/usr/bin/node

const filepath = process.argv[2];
const data = process.argv[3];

const fs = require('fs');

fs.writeFile(filepath, data, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
