# Nombre: Victor Manuel Ospina Bautista
# Materia: Analisis y Diseño de Algoritmos
# Semestre: 7
# Codigo: 8922377

from sys import stdin

class dforest(object):
	"""Disjoint-Union implementation with disjoint forests using
	path compression and ranking"""

	def __init__(self, size = 100):
		"""Create an empty disjoint forest"""
		self.__parent = [i for i in range(size)]
		self.__rank = [0 for _ in range(size)]

	def __str__(self):
		"""Return the string representation"""
		return str(self.__parent)

	def find(self, x):
		"""Return the representative of x"""
		if(self.__parent[x] != x): self.__parent[x] = self.find(self.__parent[x])
		return self.__parent[x]

	def union(self, x, y):
		"""Performs the union of the collections where x and y belong"""
		rx, ry = self.find(x), self.find(y)
		krx, kry = self.__rank[rx], self.__rank[ry]
		if(krx >= kry):
			self.__parent[ry] = rx
			if(krx == kry): self.__rank[rx] = self.__rank[rx] + 1
		else: self.__parent[rx] = ry

def kruskal(G, lenv):
	ans = []
	G.sort(key = lambda x: x[2])
	df = dforest(lenv)
	for u, v, w in G:
		if(df.find(u) != df.find(v)):
			df.union(u, v)
		else:
			ans.append(w)
	return ans


def main():
	N = stdin.readline().strip().split()
	end = ['0','0']
	while N != end:
		grafo = list()
		nodos = int(N[0])
		aristas = int(N[1])
		for i in range(0, aristas):
			tok = stdin.readline().strip().split()
			lin = list()
			a = int(tok[0])
			b = int(tok[1])
			c = int(tok[2])
			lin.append(a)
			lin.append(b)
			lin.append(c)
			grafo.append(lin)
		#Llamar Funcion
		ans = kruskal(grafo, nodos)
		if len(ans) == 0: print("forest")
		else: 
			for i in range(0, len(ans)):
				print(ans[i],end = " ")
			print("")
		N = stdin.readline().strip().split()
			

main()