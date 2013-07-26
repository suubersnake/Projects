# Have the user enter a number and find all Prime Factors (if there are any) and display them.
import sys
from math import sqrt
from NextPrimeNumber import genNPrimes
#simple unoptimized is prime function. Can only find one prime number
def isPrime(number):
	if number == 2 :
		return True
	if number % 2 == 0 :
		return False
	#from number to square root, inclusive.
	for num in range(3, int(sqrt(number)+1)) : # + 1 fixes offset issue.
		if( number % num == 0 ):
			return False
	return True
			

#returns a list of the prime factors for number
def getPrimeFactors(number):
	primes = genNPrimes()
	pnumber = primes.__next__()
	factors = []
	while True :
		print(str(number) + ", " + str(pnumber))
		#sys.stdin.readline()
		while(number % pnumber == 0):
			number = number // pnumber
			factors.append(pnumber)
		pnumber = primes.__next__()
		if isPrime(number):
			if number > 1 :
				factors.append(number)
			break
	return factors
	
	
if __name__ == '__main__':
	print(getPrimeFactors(10))
	print(getPrimeFactors(20))
	print(getPrimeFactors(50))
	print(getPrimeFactors(100))
	print(getPrimeFactors(125))
	print(getPrimeFactors(500))