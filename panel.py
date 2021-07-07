# panel uzytkownika

print ("\tPanel uzytkownika")
security = 0

username= ""
while not username:
    username = input ("Uzytkownik: ")

password = ""
while not password :
     password = input ("Haslo: ")

if username == "Aleksandra" and password == "sekret" :
            print ("Hello Aleksandra")
            security = 2
    
elif username == "Gosc" and password == "gosc":
            print ("Hello")
            security = 1
else:
            print ("Nieautoryzowana proba dostepu!\n")


input ("\n\nAby zakonczyc dzialanie programu nacisnij dowolny klawisz.")
