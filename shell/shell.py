import subprocess
from subprocess import PIPE

# Simple command execution
proc = subprocess.run('date', shell=True, stdout=PIPE, stderr=PIPE, text=True)
date = proc.stdout
print('STDOUT: {0}'.format(date))

# Passing variables to sub processes
array = ['1','2','3','4','5']
input_text = '\n'.join(array)
proc = subprocess.run('cat -n', shell=True, input=input_text, stdout=PIPE, stderr=PIPE, text=True)
print(proc.stdout)

# File input / output
with open('./data/input.txt') as input_file:
    with open('./data/output.txt','w') as output_file:
        proc = subprocess.run('cat -n', shell=True, stdin=input_file, stdout=output_file, text=True)