sentence=input("enter a sentence\n>")
print(sentence.upper())
print(sentence.strip())
print(sentence.replace("bad","good"))
if sentence.endswith("."):
    print(True)
else:
    print(False)