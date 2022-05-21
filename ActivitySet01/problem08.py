# Files

filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        t=(line.find("0"))
        num=float(line[t:])
        count=count+1
        total=total+num
average=total/count
print("Average spam confidence:",average)
        