# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377

from sys import stdin

def solve(L, G, areas):
	areas.sort()
	ans,low,n,N, ok = list(),0,0,len(areas),True 
	while ok and low < L and n != G:
		ok = areas[n][0] <= low
		best,n = n,n+1
		while ok and n != N and areas[n][0] <= low:
			if areas[n][1] > areas[best][1]:
				best = n
			n += 1
		ans.append(best)
		low = areas[best][1]
	ok = ok and low >= L
	if not ok:
		ans = list()
	return len(ans)


def main():
	N = stdin.readline().strip().split()
	end = ['0','0']
	while N != end:
		areas = []
		L = int(N[0])
		G = int(N[1])
		for i in range(0, G):
			tok = stdin.readline().strip().split()
			x = int(tok[0])
			r = int(tok[1])
			areas.append([x-r,x+r])
		ans = solve(L,G,areas)
		if ans == 0:   
			print(-1)
		else: 
			print(G-ans)
		N = stdin.readline().strip().split()

main()
