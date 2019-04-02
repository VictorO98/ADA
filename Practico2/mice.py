# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377

from sys import stdin
from heapq import heappop,heappush

INF = float('inf')

def dijkstra(G, s):
	distancia = [INF for _ in range(len(G))]
	visitados = [0 for _ in range(len(G))]
	distancia[s] = 0
	heap = [(0,s)]
	while(heap):
		d,u = heappop(heap)
		if visitados[u] == 0:
			visitados[u] = 1
			for v,w in G[u]:
				if distancia[v] > d + w:
					distancia[v] = d + w
					heappush(heap, (distancia[v],v))
	return distancia

def main():
	N = int(stdin.readline())
	while N != 0:
		x = stdin.readline()
		numCells = int(stdin.readline())
		numExitCell = int(stdin.readline())
		startingValue = int(stdin.readline())
		connections = int(stdin.readline())
		cells = [[] for _ in range(numCells)]
		mice = 0
		for j in range(0,connections):
			tok = stdin.readline().strip().split()
			a = int(tok[0])
			b = int(tok[1])
			t = int(tok[2])
			cells[b-1].append([a-1,t])
		ans = dijkstra(cells, numExitCell-1)
		for k in range(numCells):
			if ans[k] <= startingValue: mice += 1
		print(mice,end="\n\n")
		N -= 1
main()