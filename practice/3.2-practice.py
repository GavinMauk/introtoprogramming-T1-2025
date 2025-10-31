def password():
    submitted_password= input("enter your password\n>")
    real_password="1234"
    password()
    if submitted_password == real_password:
        print("access granted")

    else:
        print("access denied")
        password()

password()