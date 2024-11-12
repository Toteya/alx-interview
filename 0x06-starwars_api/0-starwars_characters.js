#!/usr/bin/node

const request = require('request');

film_id = process.argv[2];
url = 'https://swapi-api.alx-tools.com/api/films/' + film_id;

process.on('unhandledRejection', (error) => {
  console.error('Unhandled promise rejection: ', error);
  // Or some other error logging process
});

request(url, (error, response, body) => {
  if (response.statusCode == 200) {
    results = JSON.parse(body);
    characters = results.characters;
    characters.forEach(get_character);
  } else if (error) {
    console.log(error);
  }
});

function get_character(url) {
  request(url, (error, response, body) => {
    if (response.statusCode == 200) {
      character = JSON.parse(body)
      ch_name = character.name;
      console.log(ch_name);
    } else if (error) {
      console.log(error);
    }
  });
}
