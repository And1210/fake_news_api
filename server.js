const express = require('express');
const bodyParser = require('body-parser');
const {PythonShell} = require('python-shell');

const server = express();
const PORT = 3030;

server.use(bodyParser.json());
server.use(bodyParser.urlencoded({ extended: true }));

server.get('/', (req, res) => {
  res.send("Sup");
});

server.post('/process', (req, res) => {
  console.log(req.body);
  //res.send(`Data recieved: ${req.body.text}`);

  let pyshell = new PythonShell('predict.py');
  pyshell.send(req.body.text);
  pyshell.on('message', (msg) => {
    console.log(`Output: ${msg}`);
    res.send(msg);
  });
  pyshell.end((err, code, signal) => {
    if (err)
      throw err;
    console.log('Finished python execution');
  });
});

server.listen(PORT, () => {
  console.log(`Server listening on http://localhost:${PORT}`);
});
