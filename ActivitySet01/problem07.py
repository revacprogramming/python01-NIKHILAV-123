# Strings

text = "X-DSPAM-Confidence:    0.8475";
find = text.find ('0.8475')
a = float(find)
print(text[find:])