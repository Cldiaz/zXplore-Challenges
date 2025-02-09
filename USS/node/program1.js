const http = require('http');

const hostname = '0.0.0.0';
const port = 0;             // system will replace with a free port

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  myname = process.env.LOGNAME
  res.setHeader('Content-Type', 'text/plain');
  res.end(`Hello World from ${myname} on z/OS`)
  server.close()
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${server.address().port}/`);
});
