# Tuples

filename = "dataset/mbox-short.txt"
name = input("Enter file name:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
counts = dict()

for line in fh:
    if line.startswith('From ') :
        words = line.split()
        time = words[5]
        hours = time[:2]
        counts[hours] = counts.get(hours,0) + 1

for key, val in sorted(counts.items()):
    print (key, val)



'''~/python01-NIKHILAV-123$ cd ActivitySet01
~/python01-NIKHILAV-123/ActivitySet01$ ls
files1.py     problem05.py  problem12.py  problem19.py
files3.py     problem06.py  problem13.py  problem20.py
files.py      problem07.py  problem14.py  problem21.py
files.txt     problem08.py  problem15.py  problem22.py
problem02.py  problem09.py  problem16.py  problem23.py
problem03.py  problem10.py  problem17.py
problem04.py  problem11.py  problem18.py
~/python01-NIKHILAV-123/ActivitySet01$ python problem11.py
Enter file name:files.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
~/python01-NIKHILAV-123/ActivitySet01$ '''
