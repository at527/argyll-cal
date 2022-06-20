#!/usr/bin/env python3

import subprocess
from datetime import datetime

def stringDateTime():
    dt = datetime.now()
    dstr = dt.strftime("%m-%d_%H:%M")
    return dstr

# run dispwin to get availble monitors
# returns list of tuples(display number, description)
def getMonitor():
    monitors = []
    runner = subprocess.run(["dispwin", "-?"], 
            capture_output=True)

    err = runner.stderr
    decodeError = err.decode()
    split = decodeError.splitlines()
    for i in range(len(split)):
        split[i] = split[i].strip()

    finishedMonitors =  False
    i = 8
    while not finishedMonitors:
        monitors.append(split[i])
        i+=1
        if "-dweb[:port]" in split[i]:
            finishedMonitors = True

    # # convert to list of tuples
    # for i in range(len(monitors)):
    #     split = monitors[i].split("=")
    #     for s in range(len(split)):
    #         split[s] = split[s].strip()
    #     monitors[i] = (split[0], split[1])

    return monitors

# select monitor

# assign alias to monitor

def printAvailMonitors():
    print("Available Monitors: ")
    monitors = getMonitor()
    for i in monitors:
        print(i)

# ask user for monitor selection
# return list[monitor number, alias]
def selectMonitor():
    confirmed = False
    while not confirmed: 
        monitor = input("Select Monitor Number: ")
        try: 
            subprocess.run(["dispwin", "-d", monitor], 
                            stderr=subprocess.DEVNULL, 
                            timeout=1)
        except:
            pass

        confirm = input("Confirm selection (y/n): ")
        if confirm == "y":
            confirmed = True
        
    alias = input("Alias for Monitor: ")
    return [monitor, alias]

def genID(dispAlias):
    id = stringDateTime() + "-" + dispAlias
    return id

def genCommand(dispNum, dispAlias):
    call = ["dispcal", "-v", "-w", "0.3127,0.3290", "-Ibw", "-H", "-P", "0.5,0.5,2.0", 
            "-d", dispNum, "-o", genID(dispAlias)]
    return call

def confirmCall(call):
    print("Generated call: ")
    print(call)
    confirm = input("Confirm call (y/n): ")
    if confirm == "y":
        return True
    else:
        return False

def main():
    printAvailMonitors()
    monitorInfo = selectMonitor()
    call = genCommand(monitorInfo[0], monitorInfo[1])
    if confirmCall(call) == True:
        subprocess.run(call)


if __name__ == "__main__":
    main()