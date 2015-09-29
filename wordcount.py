
word_count = {}

text = open("test.txt")

for line in text:
    line = line.strip().replace(",", "").replace("?", "").split()
    for word in line:
        word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print "{} {}".format (word, count)

text.close()