word1=input("what is your first word?\n>")
word2=input("what is your second word?\n>")
word3=input("what is your third word?\n>")
print(word1+word2+word3)

a=input("what is your first number")
b=input("what is your second number")
c=input("what is your third number")
def add_three(a,b,c):
    print(int(a)+int(b)+int(c))

add_three(a,b,c)

def data_three():
    word=input("what is your word")
    integer=input("what is your integer")
    float1=input("what is your float")
    d=(int(integer) + float(float1))
    print(str(d)+word)

data_three()
