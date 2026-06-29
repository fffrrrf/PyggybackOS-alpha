#import the stuff
#todo: fix raminf

#import keyboard
import psutil
import sys
import calculator_microapp
import randomnumber_microapp

print("boot")
usrtrue = 0
while not usrtrue:
    usr = input("Enter your username: ")
    if len(usr) <= 10:
        usrtrue = 1
    else: print("Username must be 10 or less characters.")
#loop for it
running = 1
while running:
    print('')
    cmd =  input(f"{usr}@pyggy:~$ ")
    if cmd == "ver":
        print("alpha_0.12")
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
        mait = 0
        while not mait:
            MATR = input("<run microapp>:~$ ")
            if MATR.lower() == "calculator":
                mait = 1
                calculator_microapp.calculation(usr)
            elif MATR.lower() == "esc":
                mait = 1
            elif MATR.lower() == "rng":
                mait = 1
                randomnumber_microapp.getrandnum(usr)
            else:
                print(f"Unkown microapp: {MATR}")
    elif cmd == "liveram":
        ramactike = 1
        bean = 1.0
        while ramactike:
            #this crap really annoyed me: its only temporarily fixed
            mem = psutil.virtual_memory()
            print(f"\rram: {mem.percent}%",
            end="")
            bean -= 0.00006
            if bean <= 0:
                ramactike = 0
    else:
        print(f"Unkown command: {cmd}")