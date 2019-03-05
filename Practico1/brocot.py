# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377

from sys import stdin

def solve(A, B):
	a, b, = 0,1 
	c, d  = 1,0
	izq = 1 
	der = 1
	encontrado = False
	while not encontrado:
		if izq == A and der == B:
			encontrado=True
			break
		if der * A > izq * B:
			print("R",end="")
			a,c = izq, der
		else:
			print("L",end="")
			b,d = izq,der
		der = c + d
		izq = a + b 
	print("",end="\n")

def main():
	C = stdin.readline().strip().split()
	end = ['1','1']
	while C != end:
		solve(int(C[0]),int(C[1]))
		C = stdin.readline().strip().split()

main()