end=0
def start():
    print("you are in the top left corner of a 5x4 box")
    print("you have 20 turns")
    a1()
def a1():
    global end
    end=(end+1)
    if end ==20:
        print("you finished on square a1")
        return
    print("which direction would you like to go.")
    print("1.down")
    print("2.right")
    a=int(input(">"))
    if a==1:
        b1()
    elif a==2:
        a2()
    else:
        print("invalid choice. try again.")
        a1()
def a2():
    global end
    end=(end+1)
    if end ==20:
        print("you finished on square a2")
        return
    print("which direction would you like to go.")
    print("1.down")
    print("2.right")
    print("3.left")
    a=int(input(">"))
    if a==1:
        b2()
    elif a==2:
        a3()
    elif a==3:
        a1()
    else:
        print("invalid choice. try again.")
        a2()
def a3():
    global end
    end=(end+1)
    if end ==20:
        print("you finished on square a3")
        return
    print("which direction would you like to go.")
    print("1.down")
    print("2.right")
    print("3.left")
    a=int(input(">"))
    if a==1:
        b3()
    elif a==2:
        a4()
    else:
        print("invalid choice. try again.")
        a3()
def a4():
    global end
    end=(end+1)
    if end ==20:
        print("you finished on square a4")
        return
    print("which direction would you like to go.")
    print("1.down")
    print("2.left")
    a=int(input(">"))
    if a==1:
        b4()
    elif a==2:
        a3()
    else:
        print("invalid choice. try again.")
        a4()
def b1():
    global end
    end=(end+1)
    if end ==20:
        print("you finished on square b1")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.right")
    a=int(input(">"))
    if a==1:
        a1()
    elif a==2:
        c1()
    elif a==3:
        b2()
    else:
        print("invalid choice. try again.")
        b1()
def b2():
    global end
    end=(end+1)
    if end ==20:
        print("you finished on square b2")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.right")
    print("4.left")
    a=int(input(">"))
    if a==1:
        a2()
    elif a==2:
        c2()
    elif a==3:
        b3()
    elif a==4:
        b1()
    else:
        print("invalid choice. try again.")
        b2()
def b3():
    global end
    end=(end+1)
    if end ==20:
        print("you finished on square b3")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.right")
    print("4.left")
    a=int(input(">"))
    if a==1:
        a3()
    elif a==2:
        c3()
    elif a==3:
        b4()
    elif a==4:
        b2()
    else:
        print("invalid choice. try again.")
        b3()
def b4():
    global end
    end= end+1
    if end ==20:
        print("you finished on square b4")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.left")
    a=int(input(">"))
    if a==1:
        a4()
    elif a==2:
        c4()
    elif a==3:
        b3()
    else:
        print("invalid choice. try again.")
        b4()
def c1():
    global end
    end= end+1
    if end ==20:
        print("you finished on square c1")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.right")
    a=int(input(">"))
    if a==1:
        b1()
    elif a==2:
        d1()
    elif a==3:
        c2()
    else:
        print("invalid choice. try again.")
        c1()
def c2():
    global end
    end= end+1
    if end ==20:
        print("you finished on square c2")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.right")
    print("4.left")
    a=int(input(">"))
    if a==1:
        b2()
    elif a==2:
        d2()
    elif a==3:
        c3()
    elif a==4:
        c1()
    else:
        print("invalid choice. try again.")
        c2()
def c3():
    global end
    end= end+1
    if end ==20:
        print("you finished on square c3")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.right")
    print("4.left")
    a=int(input(">"))
    if a==1:
        b3()
    elif a==2:
        d3()
    elif a==3:
        c4()
    elif a==4:
        c2()
    else:
        print("invalid choice. try again.")
        c3()
def c4():
    global end
    end= end+1
    if end ==20:
        print("you finished on square c4")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.left")
    a=int(input(">"))
    if a==1:
        b4()
    elif a==2:
        d4()
    elif a==3:
        c3()
    else:
        print("invalid choice. try again.")
        c4()
def d1():
    global end
    end= end+1
    if end ==20:
        print("you finished on square d1")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.right")
    a=int(input(">"))
    if a==1:
        c1()
    elif a==2:
        e1()
    elif a==3:
        d2()
    else:
        print("invalid choice. try again.")
        d1()
def d2():
    global end
    end= end+1
    if end ==20:
        print("you finished on square d2")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.right")
    print("4.left")
    a=int(input(">"))
    if a==1:
        c2()
    elif a==2:
        e2()
    elif a==3:
        d3()
    elif a==4:
        d1()
    else:
        print("invalid choice. try again.")
        d2()
def d3():
    global end
    end= end+1
    if end ==20:
        print("you finished on square d3")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.right")
    print("4.left")
    a=int(input(">"))
    if a==1:
        c3()
    elif a==2:
        e3()
    elif a==3:
        d4()
    elif a==4:
        d2()
    else:
        print("invalid choice. try again.")
        d3()
def d4():
    global end
    end= end+1
    if end ==20:
        print("you finished on square d4")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.down")
    print("3.left")
    a=int(input(">"))
    if a==1:
        c4()
    elif a==2:
        e4()
    elif a==3:
        d3()
    else:
        print("invalid choice. try again.")
        d4()
def e1():
    global end
    end= end+1
    if end ==20:
        print("you finished on square e1")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.right")
    a=int(input(">"))
    if a==1:
        d1()
    elif a==2:
        e2()
    else:
        print("invalid choice. try again.")
        e1()
def e2():
    global end
    end= end+1
    if end ==20:
        print("you finished on square e2")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.right")
    print("3.left")
    a=int(input(">"))
    if a==1:
        d2()
    elif a==2:
        e3()
    elif a==3:
        e1()
    else:
        print("invalid choice. try again.")
        e2()
def e3():
    global end
    end= end+1
    if end ==20:
        print("you finished on square e3")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.right")
    print("3.left")
    a=int(input(">"))
    if a==1:
        d3()
    elif a==2:
        e4()
    elif a==3:
        e2()
    else:
        print("invalid choice. try again.")
        e3()
def e4():
    global end
    end= end+1
    if end ==20:
        print("you finished on square e4")
        return
    print("which direction would you like to go.")
    print("1.up")
    print("2.left")
    a=int(input(">"))
    if a==1:
        d4()
    elif a==2:
        e3()
    else:
        print("invalid choice. try again.")
        e4()
start()
