
text = "ZJ7{aolnylhaqbspbzjhlzhy}"

def shift(text, num):
    new_text = ""
    for c in text:
        new_text += chr(ord('a') + (ord(c) + num) % 26)
    
    return new_text

def c():
    for i in range(0, 26):
        print(i)
        print(shift(text.lower(), i))

c()
print(shift(text.lower(), -11))