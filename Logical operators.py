print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

st_name = name1.lower()
nd_name = name2.lower()

T_occurs = int(st_name.count("t")) + int(nd_name.count("t"))
R_occurs = int(st_name.count("r")) + int(nd_name.count("r"))
U_occurs = int(st_name.count("u")) + int(nd_name.count("u"))
E_occurs = int(st_name.count("e")) + int(nd_name.count("e"))

true_times = str(T_occurs + R_occurs + U_occurs + E_occurs)

L_occurs = int(st_name.count("l")) + int(nd_name.count("l"))
O_occurs = int(st_name.count("o")) + int(nd_name.count("o"))
V_occurs = int(st_name.count("v")) + int(nd_name.count("v"))
E_occurs_love = int(st_name.count("e")) + int(nd_name.count("e"))

love_times = str(L_occurs + O_occurs + V_occurs + E_occurs_love)

love_score = int(true_times + love_times)

if love_score < 10 and love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

