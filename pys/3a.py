s = input("Enter the sentence: ")
words = s.split()
print("Number of words:", len(words))

digits = []
u_letters = []
l_letters = []
spl_chars = []

for i in s:
    if i.isdigit():
        digits.append(i)
    elif i.isupper():
        u_letters.append(i)
    elif i.islower():
        l_letters.append(i)
    else:
        spl_chars.append(i)

print("Number of digits:", len(digits))
print("Number of upper case letters:", len(u_letters))
