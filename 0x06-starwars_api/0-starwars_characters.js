#!/usr/bin/node
/* Retrieves character information from the StarWars API
*/

const request = require('request');

const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

function promiseRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve({ response, body });
      }
    });
  });
}

async function getCharacter (url) {
  await promiseRequest(url)
    .then(( {response, body} ) => {
      if (response.statusCode === 200) {
        const character = JSON.parse(body);
        const charName = character.name;
        console.log(url)
        console.log(charName);
      }
    })
  .catch( error => console.log(error));
}

promiseRequest(url)
.then(async ({ response, body }) => {
  if (response.statusCode === 200) {
    const results = JSON.parse(body);
    const characters = results.characters;
    for (const characterUrl of characters) {
      await getCharacter(characterUrl);
    }
  }
})
.catch(error => console.log(error));
