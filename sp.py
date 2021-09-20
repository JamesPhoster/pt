#wget https://raw.githubusercontent.com/JamesPhoster/pt/master/sp.py && python3 sp.py

#!/usr/bin/env python
# Author: Alamot
import argparse
import re
import subprocess
import sys
import os

def run_command(command):
    print("\nRunning command: "+' '.join(command))
    sp = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ""
    while True:
        out = sp.stdout.read(1).decode('utf-8', 'ignore')
        if out == '' and sp.poll() != None:
            break
        if out != '':
            output += out
            sys.stdout.write(out)
            sys.stdout.flush()
    return output

def main():
    parser = argparse.ArgumentParser(description="Port/Service enumaration tool.")
    args = parser.parse_args()

    cmd = ["sudo", "apt", "install", "masscan"]
    output = run_command(cmd) 
    
    cmd = ["wget", "https://raw.githubusercontent.com/Alamot/code-snippets/master/enum/htbscan.py"]
    output = run_command(cmd) 

    filein = os.getcwd() + "/htbscan.py"
    f = open(filein,'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace("tun0","eth0")

    fileout = os.getcwd() + "/scan.py"
    f = open(fileout,'w')
    f.write(newdata)
    f.close()

    cmd = ["rm", "-rf", "htbscan.py"]
    output = run_command(cmd)    
if __name__ == "__main__":
    main()
