# User panel

print ("\tUser panel")
security = 0

username= ""
while not username:
    username = input ("User: ")

password = ""
while not password :
     password = input ("Password: ")

if username == "Aleksandra" and password == "sekret" :
            print ("Hello Aleksandra")
            security = 2
    
elif username == "Gosc" and password == "gosc":
            print ("Hello")
            security = 1
else:
            print ("Unauthorized access attempt!\n")


input ("\n\nPress any key to quit the program.")
