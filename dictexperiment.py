import string
print(list(string.ascii_letters))
print(list(string.ascii_uppercase))
print(list(string.ascii_lowercase))
sentence = input("What is your sentence?")
sentence.lower()
vowels = {'a':0,
          'e':0,
          'i':0,
          'o':0,
          'u':0}
for s in sentence:
    if s in vowels:
        vowels[s] += 1
print(vowels)
vdata = {}
for s in sentence:
    if s.isalpha():
        if s in vdata:
            vdata[s] +=1
        else:
            vdata[s] = 1
print(vdata)
numcount = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9':0
    
}
for s in sentence:
    if s in numcount:
        numcount[s] += 1
panagram = True
for s in numcount.values():
    if s == 0:
        panagram = False
if panagram:
    print("It's a panagram!")
else:
    print("It's not a panagram :(")
print(numcount)

alpha = {
    letter:False 
    for letter in string.ascii_lowercase
    
}
print(alpha)
al = {}    




for i in string.ascii_lowercase:
    al[i] = 0
print(al)

for s in sentence.lower():
    if s in alpha:
        alpha[s] = True
panagram = True
for s in alpha.values():
    if not s:
        panagram = False
if panagram:
    print("It's a panagram!")
else:
    print("It's not a panagram :(")
print(alpha)