# counting of words 

word = ("A student of Zuri 2022 cohort learning programming to becocome a fullstack developer")
count = 0
for line in word:
    words = line.split(" ")
    count += len(words)

print("Number of words: ", count)