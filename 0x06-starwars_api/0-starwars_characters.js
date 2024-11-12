#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

process.on('unhandledRejection', (error) => {
  console.error('Unhandled promise rejection: ', error);
  // Or some other error logging process
});

request(url, (error, response, body) => {
  if (response.statusCode === 200) {
    const results = JSON.parse(body);
    const characters = results.characters;
    characters.forEach(getCharacter);
  } else if (error) {
    console.log(error);
  }
});

function getCharacter (url) {
  request(url, (error, response, body) => {
    if (response.statusCode === 200) {
      const character = JSON.parse(body);
      const charName = character.name;
      console.log(charName);
    } else if (error) {
      console.log(error);
    }
  });
}
