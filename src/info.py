import os, sys
import platform

def CPUinfo():
  infofile = '/proc/cpuinfo'
  cpuinfo = {}
  if os.path.isfile(infofile):
    f = open(infofile, 'r')
    for line in f:
      try:
        name, value = [w.strip() for w in line.split(':')]
      except:
        continue
      if name == 'model name':
        cpuinfo['CPU type'] = value
      elif name == 'cache size':
        cpuinfo['cache size'] = value
      elif name == 'cpu MHz':
        cpuinfo['CPU speed'] = value + ' Hz'
      elif name == 'vendor_id':
        cpuinfo['vendor ID'] = value
    f.close()
  return cpuinfo
    
  
if __name__ == '__main__':
  fichero = (sys.argv[1])
  
  f = open('info', 'w')
  A = CPUinfo()
  for i in A:
    f.write('%s\n'%i)
   
  f.write('\n')
  
  B = platform.uname()
  for i in B:
    f.write('%s\n'%i)
    
  C = platform.platform()
  for i in C:
    f.write('%s'%i)
    
  f.write('\n')
    
  f.write('Pyhton: %s\n'%platform.python_version())
  
  D = platform.python_build()
  for i in D:
    f.write('%s\n'%i)
    
  f.close()