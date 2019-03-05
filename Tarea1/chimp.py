#Victor Manuel Ospina Bautista
#Analisis y Diseño de Algoritmos
#Septimo Semestre

from sys import stdin

def Menor(monas, mono):
	N = len(monas)
	low = 0
	hi = N - 1	
	ans = 0
	while low <= hi:
		mid = low + ((hi - low) >> 1)
		if monas[mid] < mono:
			ans = monas[mid]
			low = mid + 1
		else:
			hi = mid - 1
	return ans

def Mayor(monas, mono):
	N = len(monas)
	low = 0
	hi = N - 1	
	ans = 0
	while low <= hi:
		mid = low + ((hi - low) >> 1)
		if monas[mid] > mono:
			ans = monas[mid]
			hi = mid - 1
		else:
			low = mid + 1
	return ans


def solve(monas, mono):	
	# place your code here	
	alturaMayor = Mayor(monas, mono)
	alturaMenor = Menor(monas, mono)

	if alturaMayor == 0: alturaMayor = 'X'
	if alturaMenor == 0: alturaMenor = 'X'
	print("{0} {1}".format(alturaMenor, alturaMayor))

def main():
  inp = stdin
  inp.readline()
  ladies = [ int(x) for x in inp.readline().split() ]
  inp.readline()
  queries = [ int(x) for x in inp.readline().split() ]
  for x in queries:
    solve(ladies, x)

main()