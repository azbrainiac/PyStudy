import random

def generateString(num):
	alfabetical = "abcdefghijklmnopqrstuvyxyz "
	result = ""
	for i in range(num):
		result = result + alfabetical[random.randrange(len(alfabetical))]
	return result

def compareStr(str1, str2):
	numChars = 0
	for i in range(len(str1)):
		if str1[i] == str2[i]:
			numChars = numChars + 1
	return (numChars/(len(str1)) * 100)

def runExperiment(phrase):
	monkeyStr = generateString(len(phrase))	
	percentCompare = compareStr(monkeyStr, phrase)
	bestStr = monkeyStr
	bestPercent = percentCompare
	i = 1
	while monkeyStr != phrase:
		monkeyStr = generateString(len(phrase))
		i = i + 1
		percentCompare = compareStr(monkeyStr, phrase)
		if percentCompare > bestPercent:
			bestPercent = percentCompare
			bestStr = monkeyStr
		if i % 100000 == 0:
			print(i, monkeyStr)
			print("The best is %s has %f percents" % (bestStr, bestPercent))

	print("100%% is on %d iteration" % (i))
	return

#sss1 = generateString(10)
#sss2 = generateString(10)
#print("%s in %s is %f" % (sss1, sss2, compareStr(sss1, sss2)))
runExperiment("methinks it is like a weasel")