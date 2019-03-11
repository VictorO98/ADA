# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377
# Colaboradores: Clase Explicada con Miguel y https://bitbucket.org/snippets/hquilo/b6n5e del repositorio de Camilo Rocha

from sys import stdin
from math import *

def pit(num1, num2):
	return sqrt((num1*num1)-(num2*num2))

def solve(areas):
	areas.sort(key=lambda x:x[1])
	n,N,ans = 0,len(areas),1
	while n != N:
		best,n = n,n+1
		while n != N:
			if areas[best][1] < areas[n][0]:
				best = n
				ans += 1
			n += 1
	return ans

def main():
	N = stdin.readline().strip().split()
	end = ['0','0']
	case = 1
	while N != end:
		areas = []
		bandera = 0
		L = int(N[0])
		G = int(N[1])
		for i in range(0,L):
			tok = stdin.readline().strip().split()
			x = int(tok[0])
			y = int(tok[1])
			if y > G: bandera = 1
			if bandera == 0:
				cateto = pit(G, y)
				areas.append([x-cateto,x+cateto])
		if bandera == 0: print("Case {0}: {1}".format(case,solve(areas)))
		else: print("Case {0}: {1}".format(case,-1))
		N = stdin.readline().strip().split()
		N = stdin.readline().strip().split()
		case += 1 
main()