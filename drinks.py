#this is to recommend drinks to people based on their age
age = int(input("How old are you?: "))

if age <= 13:
    print("We would recommend juices and smoothies, for example chivita.")
elif age > 13 and age <= 18:
    print("We would recommend juices, smoothies and soft drinks like fanta and coca cola.")
elif age > 18:
    print("We would recommend juices, smoothies, soft drinks and alcoholic drinks like red wine and whisky")