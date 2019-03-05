# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377

from sys import stdin

def tab_solve(precios, index, cantidad):
	#if cantidad > 1800 : cantidad += 200
	N = len(index)
	tab = [[0 for i in range(cantidad+1)]for i in range(N+1)]
	for i in range(1, N+1):
		for j in range(1, cantidad+1):
			if precios[i-1] <= j:
				tab[i][j] = max(index[i-1] + tab[i-1][j-precios[i-1]],
								tab[i-1][j])
			else:
				tab[i][j] = tab[i-1][j]
	return tab[N][cantidad]
	
def main():
	inp = stdin
	n = inp.readline().strip().split()
	while len(n) != 0:
		cantidad = int(n[0])
		p = int(n[1])
		pos = 0
		precios = [0 for i in range(p)]
		index = [0 for i in range(p)]
		while p > 0:
			tok = inp.readline().strip().split()
			precios[pos] = int(tok[0])
			index[pos] = int(tok[1])
			pos+=1
			p-=1
		print(tab_solve(precios,index,cantidad))
		n = inp.readline().strip().split()
	
main()
