import math

filename = "english_entropy.txt"
file = open(filename, "r", encoding="utf-8")
content = file.read()

wordcounts = {}

#constructs the wordcounts:
for x in content:
    if x in wordcounts:
        wordcounts[x] += 1
    else:
        wordcounts[x] = 1

N = len(content)
H = 0
#Calculate entropy:
for count in wordcounts.values():
    P = count / N
    P = -P*math.log2(P)
    H += P

print(f"The entropy of {filename} is: {H} bits")
