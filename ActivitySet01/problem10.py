# Dictionaries

#filename = "dataset/mbox-short.txt"
name = input("Enter file name:")
handle = open(name)
mails = dict()
for line in handle:
    if line.startswith("From: "):
        line = line.split()
        mails[line[1]] = mails.get(line[1], 0) + 1
maxi_key = None
maxi_value = 0
for key,value in  mails.items():
    if maxi_value is None or maxi_value < value:
        maxi_value = value
        maxi_key = key
print(maxi_key, maxi_value)






'''~/python01-NIKHILAV-123/ActivitySet01$ cd ActivitySet01
bash: cd: ActivitySet01: No such file or directory
~/python01-NIKHILAV-123/ActivitySet01$ ls
files1.py     problem05.py  problem12.py  problem19.py
files3.py     problem06.py  problem13.py  problem20.py
files.py      problem07.py  problem14.py  problem21.py
files.txt     problem08.py  problem15.py  problem22.py
problem02.py  problem09.py  problem16.py  problem23.py
problem03.py  problem10.py  problem17.py
problem04.py  problem11.py  problem18.py
~/python01-NIKHILAV-123/ActivitySet01$ python problem10.py
Enter file name:files.txt
cwen@iupui.edu 5
~/python01-NIKHILAV-123/ActivitySet01$ '''

