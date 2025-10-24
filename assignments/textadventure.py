def story_start():
    print("you are")
    print("what form of motorsports do you like")
    print("1. formula 1")
    print("2. motoGP")
    print("3. endurance racing")
    choice1=input(">")
    if choice1=="1":
        formula_1()
    elif choice1=="2":
        moto_gp()
    elif choice1=="3":
        WEC()
    else:
        print("invaled choice. try again.")
        story_start()
def formula_1():
    print("you are a formula one fan")
    print("what is your favorite team")
    print("1. ")
    print("2. ")
    choice2=input(">")
    if choice2=="1":
        ()
    elif choice2=="2":
        ()
    else:
        print("invaled choice. try again.")
        formula_1()
def moto_gp():
    print("you are a motogp fan")
    print("what is you favorite team")
    print("1. ")
    print("2. ")
    choice2=input(">")
    if choice2=="1":
        ()
    elif choice2=="2":
        ()
    else:
        print("invaled choice. try again.")
        moto_gp()
def WEC():
    print("you are a world endurance championship fan")
    print("what is you favorite team")
    print("1. ")
    print("2. ")
    choice2=input(">")
    if choice2=="1":
        ()
    elif choice2=="2":
        ()
    else:
        print("invaled choice. try again.")
        WEC()











story_start()