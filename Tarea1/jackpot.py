#Victor Manuel Ospina Bautista
#Analisis y Diseño de Algoritmos
#Septimo Semestre

from sys import stdin

def solve(A):
  # place your code here
  s = A[0]
  tmp = s
  N = len(A)
  for i in range(1, N, 1):
  	if tmp <= 0: tmp = 0
  	tmp += A[i]
  	s = max(tmp,s) 	
  return s

def main():
  inp = stdin
  n = int(inp.readline().strip())
  while n!=0:
    tok = inp.readline().strip().split()
    for i in range(n): tok[i] = int(tok[i])
    ans = solve(tok)
    if ans<=0: print('Losing streak.')
    else: print('The maximum winning streak is {0}.'.format(ans))
    n = int(inp.readline().strip())

main()