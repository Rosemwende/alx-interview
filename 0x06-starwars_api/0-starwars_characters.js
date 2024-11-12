#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https:

request(url, function (error, response, body) {
  if (error) {
    console.log('Error:', error);
  } else{
    const data = JSON.parse(body);

    const characters = data.characters;
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (error) {
          console.log('Error:', error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    }
  }
});
