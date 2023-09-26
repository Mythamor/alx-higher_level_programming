#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, (response, body) => {
  console.log('code: ' + response.statusCode);
});
