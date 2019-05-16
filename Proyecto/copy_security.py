# Desarrollador: Victor Manuel Ospina Bautista
# Codigo : 8922377
# Frase Compromiso : 
#           Como Miembro de la comunidad academica de la Pontifica Universidad
#           Javeriana Cali me comprometo a seguir los màs altos estandares de 
#           de integridad academica

import operator as op
from functools import reduce
from sys import stdin
from operator import floordiv

#Values to pre calculate
PASCAL = {} 

#Values ​​of the highs for each line of the triangle
HIGHS = [44721361, 181714, 12449, 2608, 950, 
		 473, 286, 197, 148, 119, 100, 87, 78, 
		 72, 67, 63, 61, 59, 57, 56, 55, 54, 
		 54, 54, 54, 54, 54, 54, 54]

def choose2(n):
    """Function to column 2 in pascal"""
    return ((n * (n - 1)) >> 1)

def choose3(n):
	"""Function to column 3 in pascal"""
	return ((n * (n - 1) * (n - 2)) // 6)

def combinatory(n, r):
	"""Function that calculates the combinatorial
		c = (n-k)!/min(k,n-k)!"""
	r = min(r, n-r)
	numer = reduce(op.mul, range(n, n-r, -1), 1)
	demon = reduce(op.mul, range(1, r+1), 1)
	return floordiv(numer, demon)

def add_dictionary(key, a, b):
	"""Function to add values ​​to the dictionary, 
	first validate if it exists but keep it"""
	if key not in PASCAL:
		PASCAL[key] = [(a, b)]
	else:
		if (a,b) not in PASCAL[key]:
			PASCAL[key].append((a, b)) 

def binary_search(k, c):
	"""Function to perform the binary search in pascal"""
	low = 0
	hi = HIGHS[k-2]
	while hi - low > 1: 
		mid = low + ((hi - low) >> 1) 
		if k == 2: aux = choose2(mid)
		if k == 3: aux = choose3(mid)
		if aux <= c:  
			low = mid
			if aux == c:
				return mid 
		else: 
			hi = mid
	return False

def solve(value):
	"""Function"""
	for k in range(2, 4):
		found = binary_search(k, value)
		if found != False:
			add_dictionary(value, found, k)
			if k < found - k: #Property Reverse Binomial
				add_dictionary(value, found, found - k)
	

def pre_calculate():
	"""Function to have values ​​precalculated 
	from column 5 in the triangle of pascal"""
	for i in range(4, 31):
		for j in range(i+2, HIGHS[i-2]):
			val = combinatory(j, i)
			add_dictionary(val, j, i)
			if i < j - i: #Property Reverse Binomial
				add_dictionary(val, j, j - i)
			
def main():
	"""Principal Function of the program"""
	N = int(stdin.readline())
	pre_calculate() #Start the pre calculate
	for i in range(N):
		#Cases
		value = int(stdin.readline()) 

		#Its called the solve to save the coefficients of the numbers
		solve(value)

		#Add reflexive value 
		if value == 2: #Base case
			add_dictionary(value, value, 1)
		else:
			add_dictionary(value, value, 1)
			add_dictionary(value, value, value-1)

		#Fill the list with the answers values
		values = PASCAL[value]
	
		#We organize the tuples to be able to print them in the 
		#Correct order and not have problems with the output of the program
		values.sort()

		#Show values in the window
		print(len(values))
		ans = " ".join(str(tup).replace(" ", '') for tup in values)
		print(ans)
main()