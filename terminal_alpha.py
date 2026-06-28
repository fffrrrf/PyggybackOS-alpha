#import the stuff

import psutil
import sys

print("boot")
usrtrue = 0
while not usrtrue:
    usr = input("Enter your username")
    if len(usr) <= 10:
        usrtrue = 1
    else: print("Username must be 10 or less characters.")
#loop for it
running = 1
while running:
   print('')
   cmd =  input(f"{usr}@pyggy:~$ ")
   if cmd == "ver":
       print("alpha_0.11")
   elif cmd == "raminf":
      mem = psutil.virtual_memory()
      print(mem.percent, "in use of", mem.total)
      
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
   elif cmd == "whoami":
       print(usr)
   elif cmd == "liveram":
       ramactike = 1
       bean = 1
       while ramactike:
           #this crap really annoyed me
           mem = psutil.virtual_memory()
           print(f"\rram: {mem.percent}%",
            end="")
           bean -= 0.00002
           if bean <= 0:
               ramactike = 0
   else:
        print(f"Unkown command: {cmd}")