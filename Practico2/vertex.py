# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377

from sys import stdin
from collections import deque

INF = float('inf')

def bfs(G, s):
	"""Busqueda ammplitud en el grafo"""
	distancia = [INF for _ in range(len(G))]
	visitados = [0 for _ in range(len(G))]
	queue = deque()
	distancia[s] = 0
	queue.append(s)
	while(queue):
		u = queue.popleft()
		for v in G[u]:
			if visitados[v] == 0:
				distancia[v] = distancia[u] + 1
				visitados[v] = 1
				queue.append(v)
	return visitados

def no_visitados(v):
	"""Cuenta los nodos que no fueron visitados y escribe en el archivo de salida"""
	ans = 0
	nodos = []
	for i in range(len(v)):
		if v[i]==0: 
			ans+=1
			nodos.append(i+1)
	print(ans,end=" ")
	for j in nodos:
		print(j,end=" ")
	print("")

def main():
	N = int(stdin.readline())
	while N != 0:
		grafo = [[] for _ in range(N)]
		aristas = stdin.readline().strip().split()
		while aristas != ['0']: #Validacion del cero despuès de leer todo el grafo
			i = 1
			pos = int(aristas[0]) - 1
			while int(aristas[i]) != 0: #Validacion 0 del final de la fila de las aristas
				grafo[pos].append(int(aristas[i]) - 1)
				i += 1 	 
			aristas = stdin.readline().strip().split()
		k = 1
		salida = stdin.readline().strip().split()
		m = int(salida[0])
		for i in range(0,m):
			lista = bfs(grafo, int(salida[k])-1)
			no_visitados(lista)
			k += 1
		N = int(stdin.readline())
main()