#email validation


#conditions for email
#a) min length: 6
#b) 1st word must be alphabet
#c) must have only one @
#d) must have '.' either in -4 or -3 index
#e) nospace, lowercase, digit allowed and available special symbols like '.', '_', '@'   

email=input("Enter your email address: ")
a,b,c=0,0,0

if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if(email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        a=1
                    elif i.isalpha():
                        if i==i.upper():
                            b=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        c=1
                if a==1 or b==1 or  c==1:
                     print("Wrong email i.e email must be in lowecase along with special chacters like '@','.','_' without any space....")
                else:
                    print("Right Email")
            else:
                print("Wrong Email i.e '.' must be either in -4 or -3 index....")    
        else:
            print("Wrong Email i.e one @ is mandatory....")
    else:
        print("Wrong Email i.e 1st index must be alphabet....")
else:
    print("Wrong Email i.e must have minimum 6 characters....")

