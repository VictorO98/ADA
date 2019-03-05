#Victor Manuel Ospina Bautista
#Analisis y Diseño de Algoritmos
#Septimo Semestre

from sys import stdin

marble,lenm = None,None

def solve(x):
  # place your code here
  low = 0
  hi = len(marble) - 1
  ans = 0
  esta = False
  if hi >= 1:
    while low <= hi:
      mid = low + ((hi - low) >> 1)
      if marble[mid] == x:
        esta = True
        ans = mid
        hi = mid - 1
      elif marble[mid] > x:
        hi = mid - 1
      else:
        low = mid + 1
  
  if esta:
    return ans
  else:
    return -1

def main():
  global marble,lenm
  case = 1
  lenm,lenq = [ int(x) for x in stdin.readline().split() ]
  while lenm+lenq!=0:
    marble = [ int(stdin.readline()) for i in range(lenm) ]
    marble.sort()
    print('CASE# {0}:'.format(case))
    for q in range(lenq):
      x = int(stdin.readline())
      ans = solve(x)
      if ans==-1 or marble[ans]!=x:
        print('{0} not found'.format(x))
      else:
        print('{0} found at {1}'.format(x,ans+1))
    lenm,lenq = [ int(x) for x in stdin.readline().split() ]
    case += 1

main()
