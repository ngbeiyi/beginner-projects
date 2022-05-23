# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
if size == "L":
    lbill = 25
    if add_pepperoni == "Y":
        lbill +=3
    else:
        lbill +=0
    if extra_cheese == "Y":
        lbill += 1
    else: 
        lbill += 0
    bill = lbill
elif size == "M":
    mbill = 20
    if add_pepperoni == "Y":
        mbill +=3
    else:
        mbill +=0
    if extra_cheese == "Y":
        mbill += 1
    else: 
        mbill += 0
    bill = mbill
else :
    sbill = 15
    if add_pepperoni == "Y":
        sbill +=2
    else: 
        sbill +=0
    if extra_cheese == "Y":
        sbill += 1
    else: 
        sbill += 0
    bill = sbill
print (f"Your final bill is: $ {bill}" )
