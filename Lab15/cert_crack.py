from cryptography.hazmat.primitives.serialization import (
    pkcs12,
    Encoding,
    PrivateFormat,
    NoEncryption
)
from cryptography import x509

filenames = ["country01.pfx", "country02.pfx", "country03.pfx", "country04.pfx", "country05.pfx", "country06.pfx"]

passwords = [
    "ankle",
    "battery",
    "password",
    "bill",
    "apple",
    "apples",
    "orange"
]

for filename in filenames:
    with open(filename, "rb") as f:
        pfx_data = f.read()

    for password in passwords:
        try:
            # Load the PKCS#12 file
            private_key, certificate, additional_certs = (
                pkcs12.load_key_and_certificates(
                    pfx_data,
                    password.encode("utf-8")
                )
            )

            if certificate is None:
                print(f"No certificate found for password: {password}")
                continue

            print(f"Found: {password}")
            print("FILE:", filename)
            # Export private key as PEM
            if private_key:
                privkey = private_key.private_bytes(
                    encoding=Encoding.PEM,
                    format=PrivateFormat.PKCS8,
                    encryption_algorithm=NoEncryption()
                )
            #    print(privkey.decode("utf-8"))

            # Certificate details
            print("Issuer:", certificate.issuer)
            print("Subject:", certificate.subject)
            print("Serial number:", certificate.serial_number)

            # print(
            #    "Hash:",
            #    certificate.signature_hash_algorithm.name
            # )

            # Export certificate as PEM
            cert_pem = certificate.public_bytes(Encoding.PEM)
            print(cert_pem.decode("utf-8"))

        except Exception:
            continue

