# input mac + 1 from the sticker 
# much thanks to Selenium on hashkiller forums for implementing the commander binary into an emulator
# without it would not have been possible to debug this and extract the keygen

import hashlib
import argparse

def lte3301_q222(mac):

	filler = 'TWAMIT';
	charset = '0123456789ABCDEF'

	mac_bytes = []
	for i in range(0, 12, 2):
		mac_bytes.append(mac[i:i+2].upper())

	input_string = ''
	for i in range(0, 6):
		input_string += filler[i]
		input_string += mac_bytes[i]

	password = ''
	digest = hashlib.md5()
	digest.update(input_string.encode())
	digest = digest.digest()

	for i in range(0, 13):
		new_digest = hashlib.md5()
		new_digest.update(digest)
		new_digest = new_digest.digest()
		long_int = 0
		long_int = long_int + new_digest[0]
		long_int = long_int + new_digest[1] * 2 ** 8
		long_int = long_int + new_digest[2] * 2 **16
		long_int = long_int + new_digest[3] * 2 ** 24
		char_pos = 1 + long_int % 16
		letter = charset[char_pos-1]
		password += letter
		digest = new_digest

	print(password)


parser = argparse.ArgumentParser(description='lte3301_q222 Keygen')
parser.add_argument('mac', help='Mac address + 1 from sticker.')
args = parser.parse_args()

lte3301_q222(args.mac)
