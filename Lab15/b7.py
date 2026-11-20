from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import dsa, rsa
from cryptography.x509.oid import NameOID

csr = b"""-----BEGIN NEW CERTIFICATE REQUEST-----
MIICyTCCAbECAQAwajELMAkGA1UEBhMCVUsxDTALBgNVBAgTBE5vbmUxEjAQBgNV
BAcTCUVkaW5idXJnaDEXMBUGA1UEChMOTXkgTGl0dGxlIENvcnAxDDAKBgNVBAsT
A01MQzERMA8GA1UEAxMITUxDLm5vbmUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
ggEKAoIBAQCuQE68qgssJ210wGxfKjCX3PG/RgSb5VpAp2rzavx71M9Bhg9kUORE
OP7BQC3E6DGu+xba3NdnhrHAFNa+hH9dnTZrlxb98aM5q9+TUm76V1toIseOMDdU
UE9IpxXoFvD6b0inbFZnbrjFj3XUUzIIqvvizw4rIOxzgbWqZ5+F7YpP8d59eWW0
6iXzJKoeE/+Gw7Slsdr1+QQAUaX05MHTweMYbZEHir2M8f1RA4o81zEd2tWCK85F
6VS/EkCzUG1cqDBQQ7D2S9MWN8Zk2P7CS8/yZx7uRTmT1t3UWKLUyIN0TU3IjCeY
t53P6C+9DT6UD0fDFZRBCmPOH+qb6/YBAgMBAAGgGjAYBgkqhkiG9w0BCQcxCxMJ
UXdlcnR5MTIzMA0GCSqGSIb3DQEBBQUAA4IBAQCqpXjmaQf2/o/xbNZG5ggAV8yV
d6rSabnov5zIkcit9NQXsPJEi84u7CbcriYqY5h7XlMWjv476mAGbgAVZB2ZhIlp
qLal+lx9xwhFbuLHNRxZcUMM0g9KQZaZTkAQdlDVU/vPzRjq+EHGoPfG7R9QKGD0
k1b4DqOvInWLOs+yuWT7YYtWdr2TNKPpcBqbzCYzrWL6UaUN7LYFpNn4BbqXRgVw
iMAnUh9fvLMe7oreYfTaevXT/506Sj9WvQFXTcLtRhs+M30q22/wUK0ZZ8APjpwf
rQMegvzXXEIO3xEGrBi5/wXJxsawRLcM3ZSGPu/Ws950oM5Ahn8K8HBdKubQ
-----END NEW CERTIFICATE REQUEST-----"""

req = x509.load_pem_x509_csr(csr)
key = req.public_key()

if isinstance(key, rsa.RSAPublicKey):
  key_type = "RSA"
elif isinstance(key, dsa.DSAPublicKey):
  key_type = "DSA"
else:
  key_type = "Other"

subject = req.subject

# Helper function to safely grab a subject attribute by its OID
get_attr = lambda oid: subject.get_attributes_for_oid(oid)[0].value

print("Key algorithm:", key_type)
print("Key size:", key.key_size)
print("Common name:", get_attr(NameOID.COMMON_NAME))
print("Organisation:", get_attr(NameOID.ORGANIZATION_NAME))
print("Organisational unit:", get_attr(NameOID.ORGANIZATIONAL_UNIT_NAME))
print("City/locality:", get_attr(NameOID.LOCALITY_NAME))
print("State/province:", get_attr(NameOID.STATE_OR_PROVINCE_NAME))
print("Country:", get_attr(NameOID.COUNTRY_NAME))

