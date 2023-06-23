#adp = adminpassword
#users = users they've access to website
import webbrowser
import time
adp = "admin1234"
users = ['1234', '2244', '1994']
def admin():
    print(users)
    newu = input("do you want to add new user ?(y/n)")
    if newu == "y":
        nuse = input()
        users.append(nuse)
    else:
        pass
def aou():
    print("login as Admin or User")
    aou = input("A or U : ")

aou()
if aou == "A":
    ap = input("password : ")
    if ap == adp:
        admin()
        e = input("exit or stay?")
        if e == "exit":
            aou()
else:
    if aou == "U":
        un = input("usercode : ")
        webbrowser.open('url')