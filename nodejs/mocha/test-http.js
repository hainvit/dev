const http = require('http');
const assert = require('assert');

const server = require('./server');

describe('HTTP Server test', function() {
    before(function() {
        server.listen(8000);
    });

    after(function() {
        server.close();
    });

    describe('/', function() {
        it('should be Hello, Mocha!', function(done) {
            http.get('http://127.0.0.1:8000', function(response) {
                // Assert the status code.
                assert.equal(response.statusCode, 200);

                let body = '';
                
                // read body of response
                response.on('data', function(d) {
                    body += d;
                });

                // equal response
                response.on('end', function() {
                    // Let's wait until we read the response, and then assert the body
                    // is 'Hello, Mocha!'.
                    assert.equal(body, 'Hello, Mocha !');
                    done();
                });
            });
        });
    });
});
