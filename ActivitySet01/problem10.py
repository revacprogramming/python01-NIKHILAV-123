# Dictionaries

#filename = "dataset/mbox-short.txt"
name = input("dataset/mbox-short.txt")
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