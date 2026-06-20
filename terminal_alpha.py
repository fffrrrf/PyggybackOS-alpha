#import

import psutil
import sys

print("boot")

running = 1
while running:
   print('')
   cmd =  input()
   if cmd == "ver":
       print("alpha0.1")
   elif cmd == "raminf":
      mem = psutil.virtual_memory()
      print(mem.percent, "in use")
   elif cmd == "esc":
       sys.exit() 
   elif cmd == "cpuinf":
       print(psutil.cpu_count(), "cores")
   elif cmd == "help":
       print("ver")
       print("raminf")
       print("esc")
       print("cpuinf")
       print("help")
   elif cmd == "liveram":
       ramactike = 1
       while ramactike:
           mem = psutil.virtual_memory()
           print(f"\rram: {mem.percent}%", end="")