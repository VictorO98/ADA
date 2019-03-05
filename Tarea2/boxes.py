# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377

from sys import stdin

def tab_solve(pesos, resistencias, maximo):
	N = len(pesos)
	tab = [[0 for i in range(maximo+1)]for i in range(N+1)]
	n,m = 1,0
	while n != N+1:
		if m == maximo+1: n, m = n+1, 0
		else: 
			tab[n][m] = tab[n-1][m]
			if pesos[n-1] <= m:
				tab[n][m] = max(tab[n][m], 1+tab[n-1][min(m-pesos[n-1],resistencias[n-1])])
			m+=1
	return tab[N][maximo]

def main():
	inp = stdin
	n = int(inp.readline().strip())
	M = 0
	while n != 0:
		W = [0 for i in range(n)]
		L = [0 for i in range(n)]
		for i in range(0, n):
			tok = inp.readline().strip().split()
			a = int(tok[0])
			b = int(tok[1])
			suma = a + b
			W[i] = a
			L[i] = b
			if M < suma:
				M = suma
		W.reverse()
		L.reverse()
		print(tab_solve(W,L,M))
		n = int(inp.readline().strip())

main() 
