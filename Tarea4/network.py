# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377
# Colaboradores: Antonio Yu Chen, Brayan vera, Lina Valencia

from sys import stdin
from collections import deque

INF = float('inf')

def bfs(G, s, t):
	"""G is the graph, s is the starting node, t is the final node
	The representation of the graph is through an adjacency list"""
	colores = [1 for _ in range(len(G))] #1: Blanco, 2: Gris, 3:Negro
	distancia = [INF for _ in range(len(G))]
	padre = [None for _ in range(len(G))]
	queue = deque()
	colores[s] = 2 #No ha sido procesado el nodo pero ya visitado
	distancia[s] = 0
	padre[s] = None
	queue.append(s)
	while(queue):
		u = queue.popleft()
		for v in G[u]:
			if colores[v] == 1: #Validar que no esta visitado
				distancia[v] = distancia[u] + 1
				colores[v] = 2
				padre[v] = u
				queue.append(v)
		colores[u] = 3 # ya se proceso todo el nodo
	return distancia[t] - 1


def main():
	
	casosPrueba= stdin.readline()
	while len(casosPrueba) != 0:
		x = stdin.readline()
		for i in range(int(casosPrueba)): 
			N = stdin.readline().strip('\n')
			grafo = ['' for i in range(int(N))]
			for j in range(int(N)):
				lin = stdin.readline().split()
				lin = [int(x) for x in lin]
				index = lin.pop(0)
				nc = lin.pop(0)
				grafo[index] = lin
			s, t = stdin.readline().split()
			ans = bfs(grafo, int(s),int(t))
			print(str(s) + " " + str(t) + " " +str(ans))
			print("",end="\n")
			x = stdin.readline()
		casosPrueba=stdin.readline()
main()