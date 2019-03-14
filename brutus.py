from collections import deque
import string

def main():
	alpha = deque(string.ascii_lowercase)
	shift = deque(string.ascii_uppercase)
	plain = deque([])
	#cipher = "ZNA UNF ABG RIBYIRQ NA VAPU SEBZ GUR FYVZR GUNG FCNJARQ UVZ"
	cipher = "MHILY LZA ZBHL XBPZXBL MVYABUHL HWWPBZ JSHBKPBZ JHLJBZ KPJABT HYJHUBT LZA ULBAYVU"

	shift.rotate(-1)

	shiftAmt = 1

	for i in range(1, 26):
		for n in range(0, len(cipher)):
			if cipher[n] != ' ':
				plain.append(alpha[shift.index(cipher[n])])
			else:
				plain.append(' ')
		
		print(shiftAmt)
		print(''.join(plain))
		shiftAmt += 1
		shift.rotate(-1)
		plain = deque([])

main()
