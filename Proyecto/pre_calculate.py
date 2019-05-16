import operator as op
from functools import reduce
from operator import floordiv

def combinatory(n, r):
  """Function that calculates the combinatorial
    c = (n-k)!/min(k,n-k)!"""
  r = min(r, n-r) 
  numer = reduce(op.mul, range(n, n-r, -1), 1)
  demon = reduce(op.mul, range(1, r+1), 1)
  return floordiv(numer, demon)

def choose():
	ans = []
	value = 0
	stop = 10**15 
	for i in range(2, 31):
		j = i + 1
		while combinatory(j, i) <= stop:
			value = combinatory(j, i)
			j += 1
		ans.append(j)
	return ans
			
def main():
	print(choose())
main()
