#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  const characterPromises = characters.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (charErr, charRes, charBody) => {
        if (charErr) {
          reject(charErr);
        } else {
          const characterData = JSON.parse(charBody);
          resolve(characterData.name);
        }
      });
    });
  });
  Promise.all(characterPromises)
    .then((names) => {
      names.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.error(error);
    });
});
