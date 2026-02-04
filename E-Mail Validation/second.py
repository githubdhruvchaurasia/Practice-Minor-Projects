email = input(f"Enter your email : ") #d@g.in

k = 0
j = 0
d = 0
 
if len(email)>=6:
    if email[0].isalpha():
       if ("@" in email) and (email.count("@")==1):
           if (email[-4]==".") ^ (email[-3]=="."):
            for i in email:
                if i == i.isspace():
                    k=1
                elif i.isalpha():
                   if i == i.upper():
                        j=1
                elif i.isdigit():
                   continue
                elif i == "_" or i == "." or i == "@":
                   continue
                else:
                   d=1
            if k == 1 or j == 1 or d == 1:
                print("Wrong Email. You have entered a space or a uppercase character!")
            else:
                print(f"You have entered a right Email. \n Email : {email}")
           else:
                print("Wrong Email. You are not using '.com' or '.in' Domain Extension!") #w
       else: 
            print("Wrong Email. You are using @ more than 1 times!")
    else:
        print("Wrong Email. You are using digit at the starting of the email.")
else:
    print("Wrong Email. You are using less than 7 characters.") #w