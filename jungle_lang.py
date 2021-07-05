n=input().split()
m=n.lower()
result =[]
vowels={"a":"1","e":"2","i":"3","o":"4","u":"5"}
for c in m:
    if c in vowels.keys():
        result.append(vowels[c])
    if c not in vowels.keys():
        result.append(c+"a")
print("".join(result))

