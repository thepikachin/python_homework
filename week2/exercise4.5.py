username = "python"
password = "rules"
givenusername = ""
givenpassword = ""
securitycounter = 0
while (givenusername != username or givenpassword != password) and securitycounter < 5:
    givenusername = input("Anna käyttäjänimi: ")
    givenpassword = input("Anna salasana: ")
    if givenusername != username or givenpassword != password:
        securitycounter = securitycounter + 1
        print("Käyttäjänimi tai salasana väärin.")
if securitycounter == 5:
    print("Pääsy evätty.")
else:
    print("Tervetuloa.")



#    username = input("Anna käyttäjänimi: ")
#    password = input("Anna salasana: ")
#    if username != "python" or password != "rules":
#        print("Kirjautumistiedot väärin.")
#        counter = counter + 1
#    if counter >= 5:
#        print("Pääsy evätty.")
#print("Tervetuloa")