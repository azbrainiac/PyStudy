for item in [1, 3, 7, 4, "qwerty", [1, 2, 4, 6]]:
	print(item)

for item in range(5):
	print(item ** 2)

wordlist = ["hello", "ass", "new", "year"]
letterlist = []
for aword in wordlist:
	for aletter in aword:
		if aletter not in letterlist:
			letterlist.append(aletter)
print(letterlist)

sqlist = []
for x in range(4, 20):
	sqlist.append(x**2)
print(sqlist)

sqlist = [x**2 for x in range(1, 9)]
print(sqlist)

sqlist = [x**2 for x in range(1, 10) if x % 3 == 0]
print(sqlist)

letterlist = [ch.upper() for ch in "asshole" if ch not in "eloh"]
print(letterlist)
print(list(set([ch for ch in "".join(wordlist)])))
print(list(set(s[i] for s in wordlist for i in range(len(s)))))

#input("Press Enter")