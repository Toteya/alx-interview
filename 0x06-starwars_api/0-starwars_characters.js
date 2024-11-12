#!/usr/bin/node
/* Retrieves character information from the StarWars API
*/

const request = require('request');

const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

function makePromise(func) {
  return (...args) => {
    return new Promise((resolve, reject) => {
      func(...args, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve({response, body});
        }
      })
    })
  }
}

const promiseRequest = makePromise(request);

async function getCharacter (url) {
  const {response, body} = await promiseRequest(url);
  if (response.statusCode === 200) {
    const character = JSON.parse(body);
    const charName = character.name;
    console.log(charName);
  }
}

async function getFilmCharacters (url) {
  const {response, body} = await promiseRequest(url);
  if (response.statusCode === 200) {
    const results = JSON.parse(body);
    const characters = results.characters;
    for (const characterUrl of characters) {
      await getCharacter(characterUrl);
    }
  }
}

getFilmCharacters(url);
