#Victor Manuel Ospina Bautista
#Analisis y Diseño de Algoritmos
#Septimo Semestre

from sys import stdin

def Llenar(mid, jarras, numCont):
	N = len(jarras) 
	n = N -1
	cantidadCont = 1
	capacidadMax = mid
	j = 0
	while  cantidadCont <= numCont:
		if jarras[j] > mid:
		 	return False
		if jarras[j] <= capacidadMax:
			capacidadMax -= jarras[j]
			if j == n:
				return True
		else:
			cantidadCont += 1
			capacidadMax = mid
			j -= 1
		j += 1
	return False

def solve(jarras, numCont):
  # place your code here
  low = 1
  hi = 1000000
  ans = 0
  if hi >= 1:
  	while low <= hi:
  		mid = low + ((hi - low) >> 1)
  		if Llenar(mid, jarras, numCont):
  			ans = mid
  			hi = mid - 1
  		else:
  			low = mid + 1
  return ans

def main():
  line = stdin.readline()
  while len(line)!=0:
    n,M = [ int(x) for x in line.split() ]
    A = [ int(x) for x in stdin.readline().split() ]
    print(solve(A, M))
    line = stdin.readline()

main()
