#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const charId = 18;
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  let movieCount = 0;
  const checkWedgeInMovie = (movie) => {
    return movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`);
  };
  const processMovie = (movie) => {
    if (checkWedgeInMovie(movie)) {
      movieCount++;
    }
  };
  data.results.forEach(processMovie);
  console.log(movieCount);
});
