const express = require('express');
const bodyParser = require('body-parser');

const server = express();
const PORT = 3030;

server.use(bodyParser.json());
server.use(bodyParser.urlencoded({ extended: true }));

server.get('/', (req, res) => {
  res.send("Sup");
});

server.post('/process', (req, res) => {
  console.log(req.body);
  res.send(`Data recieved: ${req.body.text}`);
});

server.listen(PORT, () => {
  console.log(`Server listening on http://localhost:${PORT}`);
});
