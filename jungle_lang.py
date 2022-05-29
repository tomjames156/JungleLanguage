users_text = input("Type in text here: ").split()

inputed_words = ""
for index in range(len(users_text)):
    if index < len(users_text) - 1:
        inputed_words += users_text[index].lower() + " "
    elif index == len(users_text) -1:
        inputed_words += users_text[index].lower()

vowels = {
    "a":"1",
    "e":"2",
    "i":"3",
    "o":"4",
    "u":"5"
    }

result = []
for char in inputed_words:
    if char in vowels.keys():
        result.append(vowels[char])
    elif char not in vowels.keys() and char != " ":
        result.append(char +"a")
    elif char == " ":
        result.append(" ")

print("".join(result))