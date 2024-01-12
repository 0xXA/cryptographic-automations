#!/usr/bin/env python

alphabet = {chr(0x41 + x): x for x in range(26)}
rev_alphabet_1 = {x: chr(0x61 + x) for x in range(26)}
rev_alphabet_2 = {x: chr(0x41 + x) for x in range(26)}

def brute(ciphertext):
	for key in range(1,26):
		L = [rev_alphabet_1[(alphabet[ciphertext[i]] - key) % 26] for i in range(len(ciphertext))]
		print('key=%d %s' % (key,''.join(L)))

def frequencify(ciphertext, frequency_table):
	for i in range(len(ciphertext)):
		frequency_table[ciphertext[i]] += 1

def pr_frq(ciphertext):
	frequency_table = {chr(0x41 + x): 0 for x in range(26)}
	frequencify(ciphertext, frequency_table)
	for key in frequency_table:
		print(key,'=> ',frequency_table[key])

def encrypt(plaintext, key):
	L = [rev_alphabet_2[(alphabet[plaintext[i]] + key) % 26] for i in range(len(plaintext))]
	print(''.join(L))

brute('OTWEWNGWCBPQABIZVQAPMLZGZWTTQVOBQUMAPMIDGZCABEQVBMZLZIXMLAXZQVOQVLMMXAVWEIVLLIZSNZWABJQZLWNLMTQOPBVIUMLGWCBPAEQNBTGTMNBBPMVMABITIAKWCTLVBBSUMQBEPQTMQBEIAQVUGBZCAB')
#pr_frq('ONHOVEJHWOBEVGWOCBWHNUGBLHGBGR')