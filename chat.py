#libraries
import random

#main

class Client:

    def __init__(self):
        self.token = random.randint(67583345, 78391264)

    def startup(self):
        print("Welcome to the chat.")
        print("Do you have an account? y or n")
        ans = input()
        if(ans.lower() == "y"):
            self.login()
        elif(ans.lower() == "n"):
            print("Would you like to create one? y or n")
            ans2 = input()
            if(ans2.lower() == "y"):
                self.register()
            elif(ans2.lower() == "n"):
                print("Oh, well piss off then.")
    def login(self):
        username = input("Username:")
        password = input("Password:")

client = Client()
client.startup()
