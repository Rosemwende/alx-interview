#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log('Error:', error);
  } else {
    const data = JSON.parse(body);

    const characters = data.characters;

    characters.forEach(characterUrl => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.log('Error:', error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
