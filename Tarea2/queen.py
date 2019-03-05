# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377
# Colaboradores: Antonio Yu Chen

from sys import stdin

def sumaColumna(tab,N,i):
	suma = 0
	for j in range(1,N+1):
		suma += tab[i][j]
	return suma

def solve(cadena):
	N = len(cadena)
	tab = [[0 for i in range(N+1)]for i in range(N+1)]
	
	if cadena[0] == '?':
		for i in range(1,N+1):
			tab[1][i] = 1
	else:
		tab[1][int(cadena[0],16)] = 1

	for i in range(2,N+1):
		if cadena[i-1] == '?':	
			for j in range(1,N+1):
				aux = sumaColumna(tab,N,i-1)
				if j == N:
					tab[i][j] = aux - (tab[i-1][j-1] 
								+ tab[i-1][j])
				else:
					tab[i][j] = aux - (tab[i-1][j] 
						+ tab[i-1][j-1] + tab[i-1][j+1])
		else:
			parada = int(cadena[i-1],16)
			for j in range(1,parada+1):
				aux = sumaColumna(tab,N,i-1)
				if j == N:
					tab[i][parada] = aux - (tab[i-1][j-1] 
								+ tab[i-1][j])
				else:
					tab[i][parada] = aux - (tab[i-1][j] 
						+ tab[i-1][j-1] + tab[i-1][j+1])
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																							
	return sumaColumna(tab,N,N)

def main():
	N = stdin.readline().strip()
	while len(N) != 0:
		print(solve(N))
		N = stdin.readline().strip()
main()