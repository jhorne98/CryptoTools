import string

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
