#!/usr/bin/python

import string, sys, getopt
import mpat

def main(argv):
	#count = 0
	wordStr = ""
	wordList = []
	patternList = []
	#cipherList = ['wnxdtcytcgiqg', 'uodncgxdntgj']

	corpusFile = ''
	outputFile = ''

	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
	except getopt.GetoptError:
		print('usage: dictreader.py -i <inputfile> -o <outputfile>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('usage: dictreader.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			corpusFile = arg
		elif opt in ("-o", "--ofile"):
			outputFile = arg

	corpusRaw = open(corpusFile, 'rb').read()

	# load dictionary into wordlist
	print('loading dictionary: be patient')

	corpus = corpusRaw.decode('cp1252', 'replace')
	for line in corpus:
		char = line.strip()
		if char == '' and wordStr != '':
			wordList.append(wordStr)
			wordStr = ""
		else:
			if char == 'ä' or char == 'Ä':
				wordStr += 'ae'
			elif char == 'ö' or char == 'Ö':
				wordStr += 'oe'
			elif char == 'ü' or char == 'Ü':
				wordStr += 'ue'
			else:
				wordStr += char.lower()

	# writing paterns
	print('finding and writing patterns to pattern list')
	for i in range(0, len(wordList)):
		patternList.append(mpat.makePattern(wordList[i]))

	output = open(outputFile, 'w')

	print('writing to output file')
	for i in range(0, len(wordList)):
		output.write(wordList[i] + '\n')
		output.write(patternList[i] + '\n')

	'''
	print('finding matching patterns')
	zerothPattern = makePattern(cipherlist[0])
	for i in range(0, len(wordList)):
		if zerothPattern == patternList[i]:
			print(patternList[i] + ': ' + wordList[i])
	'''

	#print(wrdlist)
	
	#print(list(wrdlist[5]))
	#print(list(patternlist[5]))

'''
def makePattern(word):
	az = string.ascii_lowercase
	pattern = ''
	
	for i in range(0, len(word)):
		for j in range(0, i):
			if word[j] == word[i]:
				pattern += pattern[j]
				break

		if len(pattern) < i + 1:
			pattern += az[0]
			az = az[1:]

	return pattern
'''		

if __name__ == '__main__':
	main(sys.argv[1:])
