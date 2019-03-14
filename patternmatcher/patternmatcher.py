#!/usr/bin/python

import string, sys, getopt
import mpat

def main(argv):
	dictFile = ''
	cipher = 'nwtutxnynts'

	try:
		opts, args = getopt.getopt(argv, "hd:", ["--dfile"])
	except getopt.GetoptError:
		print('usage: patternmatcher.py -d <patterndictionary>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('usage: patternmatcher.py -d <patterndictionary>')
			sys.exit()
		elif opt in ("-d", "--ifile"):
			dictFile = arg

	dictionary = open(dictFile, 'rb')

	while True:
		word = dictionary.readline().decode('cp1252', 'replace').strip('\n')
		pattern = dictionary.readline().decode('cp1252', 'replace').strip('\n')

		if not word:
			break
		
		if pattern == mpat.makePattern(cipher):
			print("{}: {}".format(pattern, word))
		#else:
			#print("", flush=True, end='\r')
			#print("{}: {}".format(pattern, word), end='\r')


if __name__ == '__main__':
	main(sys.argv[1:])
