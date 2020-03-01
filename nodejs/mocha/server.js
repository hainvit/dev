const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200);
    res.end('Hello, Mocha !');
});

// listen starts the server on the given port
exports.listen = port => {
    console.log('Listening on: ' + port);
    server.listen(port);
};

// close destroys the server
exports.close = () => {
    server.close();
};
