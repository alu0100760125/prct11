import timeit

if __name__ == '__main__':
  t1 = timeit.Timer('(a*b)**3', setup='import random; a = random.uniform(0,100); b = random.uniform(0,100)')
  tiempo1 = t1.timeit(10000000)

  t2 = timeit.Timer('(a**3)*(b**3)', setup='import random; a = random.uniform(0,100); b = random.uniform(0,100)')
  tiempo2 = t2.timeit(10000000)
  
  if tiempo1 > tiempo2:
    p = (tiempo2/tiempo1)*100
    print p
    
  else:
    p = (tiempo1/tiempo2)*100
    print p
    
