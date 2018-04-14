from python_mnemonic import mnemonic
import sys
import math
import random
import pprint

english = open('python_mnemonic/wordlist/english.txt').read().split('\n')

def get_input(n):
	while True:
		try:
			roll = input('roll: ')
			roll = int(roll)
		except ValueError:
			print('invalid roll value')
			continue
		else:
			if roll < 1 or roll > n:
				print('invalid roll value')
				continue
			else:
				break
	return roll

# mimics m-sided die using an n-sided die
# https://math.stackexchange.com/a/2249950
def uniform_generator(m, n): 
    """
    Expected number of rolls
    E = r * n^r / m
    where r = int(ceil(log(m, n)))
    """
    r = int(math.ceil(math.log(m, n)))
    while True:
    	candidate = sum(n**power * (int(get_input(n))-1) for power in range(r)) + 1
    	if candidate <= m:
    		return candidate

seed_length = input('seed length? (12,15,18,21,24): ')
sides = input('dice # of sides: ')

try:
	seed_length = int(seed_length)
	sides = int(sides)
except ValueError:
	print('Error, input must be numbers')
	sys.exit(1);

if seed_length not in [12,15,18,21,24]:
	print('seed length invalid.')
	sys.exit(1)

if sides < 2:
	print('dice must have 2+ sides.')
	sys.exit(1)

m = 2048 # BIP39 word list length

seed = []

for x in range(seed_length-1):
	while True:
		word_index = uniform_generator(m, sides) - 1
		if word_index in seed:
			# already found this word, skip it try again
			print('skipping word: ', english[word_index])
			continue
		else:
			print('found word: ', english[word_index])
			seed.append(word_index)
			break

phrase_array = []

for word_index in seed:
	phrase_array.append(english[word_index])

phrase = ' '.join(phrase_array)

checksum = []

m = mnemonic.Mnemonic('english')
for word in english:
    tested = phrase + ' ' + word
    if m.check(tested):
        checksum.append(word)

checksum_length = len(checksum)

if checksum_length == 0:
	print('there was an error, no checksum word found.')
	sys.exit(1)

# now we roll for checksum value
checksum_index = uniform_generator(checksum_length, sides) - 1

phrase = phrase + ' ' + checksum[checksum_index]

print('seed phrase:')
print(phrase)
