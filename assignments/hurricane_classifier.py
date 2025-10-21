wind_speed=input("what is the wind speed>")
if int(wind_speed) < 74:
    print("the hurricane is a tropical storm")
elif int(wind_speed) < 96:
    print("the hurricane is a catagory 1")
elif int(wind_speed) < 111:
    print("the hurricane is a catagory 2")
elif int(wind_speed) < 130:
    print("the hurricane is a catagory 3")
elif int(wind_speed) < 157:
    print("the hurricane is a catagory 4")
else:
    print("the hurricane is a catagory 5")