#!/usr/bin/env python

import re

alphabet = {chr(0x41 + x): x for x in range(26)}
rev_alphabet_1 = {x: chr(0x61 + x) for x in range(26)}
rev_alphabet_2 = {x: chr(0x41 + x) for x in range(26)}
latin_alphabet_probabilities = (0.082,0.015,0.028,0.043,0.127,0.022,0.020,0.061,0.070,0.002,0.008,0.040,0.024,0.067,0.075,0.019,0.001,0.060,0.063,0.091,0.028,0.010,0.023,0.001,0.020,0.001)

def frequencify(ciphertext, frequency_table):
	for i in range(len(ciphertext)):
		frequency_table[ciphertext[i]] += 1

def pr_frq(ciphertext):
	frequency_table = {chr(0x41 + x): 0 for x in range(26)}
	frequencify(ciphertext, frequency_table)
	for key in frequency_table:
		print(key,'=> ',frequency_table[key])

def calcic(ciphertext):
	frequency_table = {chr(0x41 + x): 0 for x in range(26)}
	frequencify(ciphertext,frequency_table)
	ic = 0
	for i in range(26):
		ic += frequency_table[rev_alphabet_2[i]] * (frequency_table[rev_alphabet_2[i]] - 1)
	ic /= (len(ciphertext) * (len(ciphertext) - 1))
	return ic

def findrep(ciphertext):
	sdec={}
	for i in range(len(ciphertext)):
		if i <= len(ciphertext)-3:
			# print(ciphertext[i:i+3]) # for debugging purposes
			sdec[ciphertext[i:i+3]] = [m.start() for m in re.finditer(ciphertext[i:i+3], ciphertext)]
	# print(sdec)	# for debugging purposes
	for key in sdec.keys():
		if len(sdec[key]) > 1:	# print only those 3 length string which have more than one occurence
			print('string:',key, ', occurence indices = ', sdec[key])

def brute_key_len(ciphertext):
	kdec = {}
	for key in range(2,10):
		kdec[key] = []
		for i in range(0,key):
			substring = ''.join([ciphertext[j] for j in range(i,len(ciphertext),key)])
			kdec[key].append((substring,'%.6f' % calcic(substring)))
	#print(kdec) # for debugging purposes
	for key in kdec.keys():
		print('when key length is',key)
		for a in kdec[key]:
			print('substring:',a[0],', IC:',a[1])

def mg(ciphertext):
	frequency_table = {chr(0x41 + x): 0 for x in range(26)}
	frequencify(ciphertext, frequency_table)
	ciphertext_letter_probabilities = [(frequency_table[key]/len(ciphertext)) for key in frequency_table]
	gtable = []
	for g in range(26):
		sm = 0
		for i in range(26):
			sm += (latin_alphabet_probabilities[i]*ciphertext_letter_probabilities[(i+g)%26])
		gtable.append(sm)
	return gtable


############ FEW CIPHERTEXT SAMPLES #############
# LIOMWGFEGGDVWGHHCQUCRHRWAGWIOWQLKGZETKKMEVLWPCZVGTHVTSGXQOVGCSVETQLTJSUMVWVEUVLXEWSLGFZMVVWLGYHCUSWXQHKVGSHEEVFLCFDGVSUMPHKIRZDMPHHBVWVWJWIXGFWLTSHGJOUEEHHVUCFVGOWICQLTJSUXGLW
# MPYIGOBSRMIDBSYRDIKATXAILFDFKXTPPSNTTJIGTHDELTTXAIREIHSVOBSMLUCFIOEPZIWACRFXICUVXVTOPXDLWPENDHPTSIDDBXWWTZPHNSOCLOUMSNRCCVUUXZHHNWSVXAUHIKLXTIMOICHTYPBHMHXGXHOLWPEWWWWDALOCTSQZELT
# CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE
#################################################

#findrep('CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE')
#brute_key_len('CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE')

strs = ['CVABWEBQBUAWWQRWWXANTBDPXXRDWBFAXCWMNJJFAIACNRNCATBWKDMCDCQQXWK', 'HOEITESEWOOEGMFTIFUDSTNSNVTNDPASNHESBGSEGEMRDRSHEAIEORTHNHOANOE', 'RARANOBQRASAJNVRAPTCXUGRJRUQTHLVGRLJHNGYNQRRGINRYQPVEEBRVRHIRIE', 'EHAXXPQEVKXHMKGZKSEMMIMEEVLWYXJBLZEIWMLPRJVELMRQEEEKWMHTRCPIMI', 'EMTXBHMRXXXBMGXXLKMGXAGLLPHTGTHFLBKKRGXHBTLMXGWHVBEAAXHKZLWWGF']
cipher_key = []
for s in strs:
	gtable = mg(s)
	cipher_key.append(rev_alphabet_2[gtable.index(max(gtable))])

print('key is',''.join(cipher_key))