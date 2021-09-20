#!/usr/bin/env python
# Author: Alamot
import argparse
import re
import subprocess
import sys

def run_command(command):
    print("\nRunning command: "+' '.join(command))
    sp = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ""
    while True:
        out = sp.stdout.read(1).decode('utf-8')
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

    cmd = ["sudo", "apt", "install", "massscan", "&&", "wget", "https://raw.githubusercontent.com/Alamot/code-snippets/master/enum/htbscan.py"]
    output = run_command(cmd)
    if outfile:
        for line in output.splitlines():
            if "rate:" not in line: # Don't write 'rate:' lines
                outfile.write(line + "\n")
        outfile.flush()    
        
    
if __name__ == "__main__":
    main()
