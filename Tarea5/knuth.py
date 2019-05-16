# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377
# Colaboradores:: Diego Felipe Galarza

from sys import stdin

def solve(arreglo, indice, caracter):
	if indice == len(arreglo):
		print(''.join(caracter))
		return
	else:
		caracter = arreglo[indice]
		tmp = []
		for i in range(len(caracter)+1):
			tmp = list(caracter)
			tmp.insert(i,caracter)
			solve(arreglo, indice+1,tmp)
	return

def main():
	N = stdin.readline()
	while N:
		arreglo = line[:len(line)-1]
		arreglo = list(arreglo)
		solve(1,list(arreglo[0]),arreglo)
		print("",end="\n")
		N = stdin.readline()
main()
