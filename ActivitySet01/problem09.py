# Lists

filename = "dataset/romeo.txt"
fname = input('Enter file name: ')
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
print(sorted(lst))

fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        line = line[1]
        print(line)
    count += 1
print("There were",count,"lines in the file with From as the first word")


