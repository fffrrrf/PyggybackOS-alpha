#import the stuff
#quote of the update: "sorry ladies, im busy coding"

import termios
import select
import psutil
import sys
import calculator_microapp
import randomnumber_microapp
import tty

#i will leanr what this means later...
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr

print("boot")
while True:
    usr = input("Enter your username: ")
    if len(usr) <= 10:
        break
    else: print("Username must be 10 or less characters.")
#loop for it
while True:
    print('')
    cmd =  input(f"{usr}@pyggy:~$ ")
    if cmd == "ver":
        print("alpha_0.13")
    elif cmd == "raminf":
        mem = psutil.virtual_memory()
        print(mem.percent, "in use of", mem.total)
      
    elif cmd == "esc":
        sys.exit()
    elif cmd == "ls microapp":
        print("Calculator")
        print("Random Number Generator (name is rng)")
    elif cmd == "cpuinf":
        print(psutil.cpu_count(), "cores")
    elif cmd == "help":
        print("ver")
        print("raminf")
        print("esc")
        print("cpuinf")
        print("help")
        print("liveram")
        print("whoami")
        print("ls microapp")
        print("run microapp")
    elif cmd == "whoami":
        print(usr)
    elif cmd == "run microapp":
        print("Which microapp do you want to run or type esc to exit")
        while True:
            MATR = input("<run microapp>:~$ ")
            if MATR.lower() == "calculator":
                break
                calculator_microapp.calculation(usr)
            elif MATR.lower() == "esc":
                break
            elif MATR.lower() == "rng":
                break
                randomnumber_microapp.getrandnum(usr)
            else:
                print(f"Unkown microapp: {MATR}")
    elif cmd == "liveram":
        while True:
            tty.setcbreak(fd)
            #this crap really damn annoyed me: its finally fixed
            mem = psutil.virtual_memory()
            print(f"\rram: {mem.percent}%", end="")
            if select.select([sys.stdin], [], [], 0)[0]:
               sys.stdin.read(1)  # consume the key
               break
               termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            
    else:
        print(f"Unkown command: {cmd}")