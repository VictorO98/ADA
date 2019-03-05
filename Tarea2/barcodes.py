# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377
# Colaboradores: Antonio Yu Chen, Santiago Coca, Brayan Vera, Nicolas Alvarez
 
from sys import stdin

def solve(N,K,M):
	tab=[[0 for _ in range(K+1)]for _ in range(N+1)]
	unidades,barras=0,0
	while unidades != N + 1:
		acumulado = K + 1
		if barras == acumulado:
			unidades, barras = unidades + 1, 0
		else:
			if unidades != barras:
				for i in range(1,M+1):
					if unidades - i >= 0:
						tab[unidades][barras] += tab[unidades-i][barras-1]
			else:
				tab[unidades][barras] = 1
				
		barras += 1
	return tab[N][K]

def main():
	N = [int(p) for p in  stdin.readline().split()]
	while len(N) != 0:
		print(solve(N[0],N[1],N[2]))
		N = [int(p) for p in  stdin.readline().split()]

main()