import random
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
maxLen = 7
minLen = 4
maxConsecutiveConsonants = 2
maxConsecutiveVowels = 2
numOfNames = 100
composite = 2

def pick(sir):

    pos = random.randrange(0,len(sir)+1)
    let = sir[pos:pos+1]
    return let

for p in range(numOfNames):
    name = ""
    for j in range(composite):
        currName = ""
        currV = 0
        currC = 0
        length = random.randrange(minLen,maxLen+1)
        for i in range(length):
            toGen = random.randrange(0,2)
            if toGen == 0 and currV < maxConsecutiveVowels:
                currName = currName + pick(vowels)
                currV = currV + 1
                currC = 0
            elif currC < maxConsecutiveConsonants:
                currName = currName + pick(consonants)
                currC = currC + 1
                currV = 0
            else:
                currName = currName + pick(vowels)
                currV = 1
                currC = 0
        currName = currName.capitalize()
        name = name + " " + currName
    print(name)