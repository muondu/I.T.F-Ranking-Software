import sqlite3
import time
def login():
    for i in range(3):
        username = input("Enter your username: ")
        if username == " " :
            print("You didn't put anything in username. PLS try again")
            login()
        else:
            password = input("Please enter your password: ")
            with sqlite3.connect('Auth.db') as db:
                cursour = db.cursor()
            find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
            cursour.execute(find_user,[(username),(password)])
            result = cursour.fetchall()

            if result:
                for i in result:
                    print("Welcome " + i[2])
                # return("exit")
                    break
                exit()
            elif username == " " :
                print("You didn't put anything in username. PLS try again")
                continue
            elif password == " " :
                print("You didn't put anything in password. PLS try again")
                continue
            elif password == " " and username == " ":
                print("You didn't put anything. PLS try again")
                continue
            else:
                print("Username and password not recognised")
                again = input("Do you want to try again?(Y/N): ")
                if again.lower() == "n" or again == "N":
                    print("Good Bye")
                    time.sleep(2)
                    # return("Exit")
                    exit() 
              
login()
