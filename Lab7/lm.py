import passlib.hash

words = ['Napier', 'Foxtrot']
for x in words:
	print("LM Hash: " + passlib.hash.lmhash.encrypt(x))
	print("NT Hash: " + passlib.hash.nthash.encrypt(x))
