#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body);
    const dict = {};
    list.forEach(e => {
      if (e.userId in dict && e.completed) {
        dict[e.userId] += 1;
      } else if (e.completed) {
        dict[e.userId] = 1;
      }
    });
    console.log(dict);
  }
});
