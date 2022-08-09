#conditional statements in python
# if 6 == 2 :
#     print("2 is equal to 2")
# else:
#     print("not equal")
# print('done')
Sex = input("specify gender her: ")
Age = int(input("how old are you?: "))

# if (Sex == "M" and Age >= 18) or (Sex == "F" and Age >= 20 and Age < 50):
#     print("you have been granted access into the room")
# else:
#     print("you may not enter the room")

if Sex == "M" and Age >= 18:
    print("you have been granted access into the room")
elif Sex == "F" and Age >= 20 and Age < 50:
    print("you have been granted access into the room")
elif Sex == "F" and Age >= 50:
    print("you may not enter the room")
else:
    print("you may not enter the room")