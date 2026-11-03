import hashlib
 
target_hash = "06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2" # Tomtom's hash

with open("salts.txt") as f:
    salt_candidates = [line.strip() for line in f if line.strip()]

for salt in salt_candidates:
    for i in range(10000, 100000):  # digits-only, up to 5 chars first
        pw = str(i).zfill(5)
        guess = hashlib.sha1((salt + pw).encode()).hexdigest()  # swap algo as needed
        if guess == target_hash:
            print(f"FOUND salt={salt} pw={pw}")
