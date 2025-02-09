const http = require('http');
const {datasets} = require("zoau") // import the datasets class from the zoau module

const hostname = '0.0.0.0';
const port = process.env.PORT|| 0;             // system will replace with a free port
let myname = process.env.LOGNAME;

function sendResponse(res,content, code,type){
  res.statusCode = code;
  res.setHeader('Content-Type', type || 'text/plain');
  res.end(content)
}


const server = http.createServer((req, res) => {
  const basic = /^\/$/; // between the beginning (^) and end ($) look for "/"
  const hello = /^\/hello\//;
  const data = /^\/data\/.*/ // "/data/<member>"


  console.log(req.url)
  if (hello.test(req.url)){
    const name = req.url.replace(/^\/[^\/]*\/([A-Z0-9a-z]+).*$/,'$1')
    sendResponse(res,`Hello ${name}!`,200,'text/plain')
  }

  if (data.test(req.url)){
    const name = req.url.replace(/^\/[^\/]*\/([A-Z0-9a-z]+).*$/,'$1')
    let datasetName = `ZXP.PUBLIC.SOURCE(${name})`
    const dsopen = datasets.read(datasetName).then(function(contents){
      sendResponse(res,contents,200,'text/plain')
        
    }).catch(function(error){
        sendResponse(res,`${datasetName} not found`,404,"text/plain")
         })
  }
    
  if(basic.test(req.url)){
  sendResponse(res,`Hello World from ${myname} on z/OS`,200,'text/plain')
  }

  //sendResponse(res,`Hello World from ${myname} on z/OS`,200,'text/plain')
  server.close()
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${server.address().port}/`);
});
