#!/usr/bin/node
/* Retrieves character information from the StarWars API
*/

const request = require('request');
const { promisify } = require('util');
const requestPromise = promisify(request);

const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

async function getCharacter (url) {
  const response = await requestPromise(url);
  if (response.statusCode == 200) {
    const character = JSON.parse(response.body);
    const charName = character.name;
    console.log(charName);
  };
}

async function getFilmCharacters (url) {
  const response = await requestPromise(url);
  if (response.statusCode == 200) {
    const results = JSON.parse(response.body);
    const characters = results.characters;
    for (const characterUrl of characters) {
      // console.log(characterUrl)
      await getCharacter(characterUrl);
    }
  }
};

getFilmCharacters(url);
