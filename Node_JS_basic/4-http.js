const http = require('http');

const app = http.createServer((requeste, responce) => {
  responce.statusCode = 200;
  responce.setHeader('Content-Type', 'text/plain');
  responce.end('Hello Holberton School!');
});

const port = 1245;
app.listen(port, () => {
  console.log(`Server is lisening on port ${port}`);
});

module.exports = app;
