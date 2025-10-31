a1=input("what is 5+5\n>")
a2=input("what is 10x10\n>")
a3=input("what is 2+2\n>")
a4=input("what is 5x5\n>")
a5=input("what is 4x4\n>")

q1="10"
q2="100"
q3="4"
q4="25"
q5="16"

def tally_score():
    score=0
    if a1==q1:
        score=(score+1)
    if a2==q2:
        score=(score+1)
    if a3==q3:
        score=(score+1)
    if a4==q4:
        score=(score+1)
    if a5==q5:
        score=(score+1)
    print(str(score)+"/5")
tally_score()