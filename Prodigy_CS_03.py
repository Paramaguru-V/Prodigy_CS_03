import string

def check_pwd(pwd):
    
    with open("common_password.txt","r") as f:
        common=f.read().splitlines()
        if pwd in common:
            print("The password is a common one. Score: 0/10\nThe Password Should not be a common password")
            return
        

    length=len(pwd)
    lenscore = 0
    if length < 8:
        print("The password must at least 8 letters\nIt is recomended to increase the length of the Password by adding more characters ")
        return
    if length >=8:
        lenscore+=1
    if length >=10:
        lenscore+=1
    if length >=12:
        lenscore+=1
    if length >=16:
        lenscore+=1
    print(f"Password length added {str(lenscore)} points to password")  #To acknowge the user about length of pass

    uppercase=any([1 if char in string.ascii_uppercase else 0 for char in pwd])
    lowercase=any([1 if char in string.ascii_lowercase else 0 for char in pwd])
    specialchar=any([1 if char in string.punctuation else 0 for char in pwd])
    number=any([1 if char in string.digits else 0 for char in pwd])
    
    char=[uppercase,lowercase,specialchar,number]
    charscore=sum(char)
    print(f"There are {str(charscore)} different characters which adds {str(charscore)} to Score")  #To acknowge the user about characters of pass
    

    score=charscore+lenscore
    if score<4:
        print(f"The Score is {str(score)}/8 and so the password is week")
        if lenscore < 2:
            print("It is recomended to increase the length of the Password by adding more characters ")
        if charscore < 3:
            print("It is recomended to add differnt types of characters")
            
    elif score==4 | score<=6:
        print(f"The Score is {str(score)}/8 and so the password is good")
        if lenscore < 2:
            print("It is recomended to increase the length of the Password by adding more characters ")
        if charscore < 3:
            print("It is recomended to add differnt types of characters")
    else:
        print(f"The Score is {str(score)}/8 and so the password is Great")
        if charscore < 3:
            print("It is recomended to add differnt types of characters")

def main():
    pwd=input("Enter the password: ")
    check_pwd(pwd)
    
    yeschoice=["yes","y"]
    nochoice=["no","n"]
    while(True):
        loop=input("Do you want to check again[y/n]: ").lower()
        if loop in yeschoice:
            pwd=input("Enter the password: ")
            check_pwd(pwd)
        elif loop in nochoice:
            break
        else:
            print("Enter correct input")

main()