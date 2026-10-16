from Crypto.PublicKey import RSA

# Privacy-Enhanced Mail?
with open("privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem", "r") as f:
    key = RSA.importKey(f.read())

print(key.d)

# CERTainly not
with open("2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der", "rb") as f:
    key = RSA.importKey(f.read())

print("")
print("Modulus (N):", key.n)
print("Public Exponent (e):", key.e)

# SSH Keys
with open("bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub", "rb") as f:
    key = RSA.importKey(f.read())

print("")
print("Modulus (N):", key.n)
print("Public Exponent (e):", key.e)

# Transparency
# openssl rsa -in transparency_afff0345c6f99bf80eab5895458d8eab.pem -pubin -text -noout
# curl https://thetransparencyflagishere.cryptohack.org/