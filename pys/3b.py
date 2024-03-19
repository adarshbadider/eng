from difflib import SequenceMatcher

s1 = "python exercise"
s2 = "python exercise"
sim = SequenceMatcher(None, s1, s2).ratio()
print("The similarity between the strings '" + s1 + "' and '" + s2 + "' is", sim)
