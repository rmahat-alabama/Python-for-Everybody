#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the
#greatest number of mail messages. The program looks for 'From ' lines and takes the second
#word of those lines as the person who sent the mail. The program creates a Python dictionary that maps
#the sender's mail address to a count of the number of times they appear in the file. After the
#dictionary is produced, the program reads through the dictionary using a maximum loop to find the
#most prolific committer.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst = list()
for line in handle:
    if not line.startswith("From:"): continue
    words = line.split()
    lst.append(words[1])


counts = dict()
for k in lst:
    counts[k] = counts.get(k,0) + 1

max_count = None
max_id = None
for k, v in counts.items():
    if max_count is None or v > max_count:
        max_count = v
        max_id = k

print (max_id, max_count)

    
