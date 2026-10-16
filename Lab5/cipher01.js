var chacha20 = require('chacha20')
var crypto = require('crypto');

var keyname = 'test';
var ciphertext = 'testing';

var args = process.argv;
if (args.length > 2) ciphertext = args[2];
if (args.length > 3) keyname = args[3];

var key = crypto.createHash('sha256').update(keyname).digest();

var ciphertext = Buffer.from(ciphertext, 'hex');

var nonce = new Buffer.alloc(8);
nonce.fill(0);

/*var key = crypto.createHash('sha256').update(keyname).digest();

var nonce = new Buffer.alloc(8);
nonce.fill(0);

console.log(key);

var ciphertext = chacha20.encrypt(key, nonce, new Buffer.from(plaintext));
console.log('Ciphertext:\t', ciphertext.toString('hex'));
console.log('Decipher\t', chacha20.decrypt(key, nonce, ciphertext).toString()); */
console.log('Decipher\t', chacha20.decrypt(key, nonce, ciphertext).toString('utf-8'));