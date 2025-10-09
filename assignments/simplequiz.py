a1=input("what is 5+5")
a2=input("what is 10x10")
a3=input("what is 2+2")
a4=input("what is 5x5")
a5=input("what is 4x4")
score=0
q1="10"
q2="100"
q3="4"
q4="25"
q5="16"

def tally_score(a, b):
    if a==b:
        score=(score+1)
    else:
        score=(score-1)
tally_score(a1,q1)
tally_score(a2,q2)
tally_score(a3,q3)
tally_score(a4,q4)
tally_score(a5,q5)
print(score)