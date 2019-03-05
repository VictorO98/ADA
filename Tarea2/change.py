# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377
# Colaboradores: Antonio Yu Chen

from sys import stdin

INF = 9999

def solve(arreglo, x):
	monedas = [5,10,20,50,100,200]
	contMax = x
	formas = []
	formasTend = []
	while contMax <= 200+x: 
		i, j = 5,5
		numMon, numMonTend = 0, 0
		copiaArr = arreglo.copy()
		acumulado = contMax
		devuelta = acumulado - x
		while i >= 0:
			if copiaArr[i] > 0 and acumulado-monedas[i] >= 0:
				acumulado -= monedas[i]
				copiaArr[i] -= 1
				numMon += 1
			else:
				i-=1
		if acumulado > 0:
			numMon = INF
		while j >= 0:
			if devuelta >= monedas[j]:
				devuelta -= monedas[j]
				numMonTend += 1
			else:
				j-=1
		formas.append(numMon)
		formasTend.append(numMonTend)
		contMax += 5
	ans = formas[0] + formasTend[0]
	p = 0
	while p < len(formas):
		suma = formas[p] + formasTend[p]
		ans = min(ans, suma)
		suma = 0
		p += 1
	return ans
		
def main():
	C = [float(x) for x in stdin.readline().split()]
	end = [0,0,0,0,0,0]
	while C != end:
		x = round(C[-1]*100)
		C = [int(C[x]) for x in range(len(C)-1)]
		print(solve(C,x))
		C = [float(x) for x in stdin.readline().split()]
main()
