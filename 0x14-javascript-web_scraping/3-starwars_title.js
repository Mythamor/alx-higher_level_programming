#!/usr/bin/node

const mid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + mid;

const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('Error Code:' + response.statusCode);
  }
});
