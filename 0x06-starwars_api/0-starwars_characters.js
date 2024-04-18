#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);


const resource = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;

request(resource, async function (error, response, body) {
  if (!error) {
    const json = JSON.parse(body);
    const enpoint = json.characters;
    for (const data of enpoint) {
      await new Promise(function (resolve, reject) {
        request(data, function (error, response, body) {
          if (!error) {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    }
  }
});
