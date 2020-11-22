'''Python script that searches a keyword in all text files in current directory and all subdirectories and tells the number of occurrences of that keyword.'''

import sys,glob
a=glob.glob('**/*.txt', recursive=True)
count=0
for file in a:
    with open(file, 'r') as f:
        content=f.readlines()
    for line in content:
        if sys.argv[1] in line:
            count+=1
print(sys.argv[1]+' occurs '+str(count)+' times.')