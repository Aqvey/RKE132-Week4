# Ülesanne on luua lihtne vorm kasutaja andmete kontrollimiseks - nimelt kasutajanime ja parooli kontroll.

username = input("Sisesta oma kasutajanimi: ")
password = input("Sisesta oma parool: ")


""" if username == "user":
    if password == "1234":
        print ("Tere tulemast!")
    else: 
        ("Vale kasutajanimi või parool.")
else: 
    ("Vale kasutajanimi või parool.") """


## saab lühendada seda neljale reale kasutades AND operaatorit

""" if username == "user" and password == "1234":
    print("Tere tulemast!")
else:
    print("Ligipääš keelatud. ")
 """


## OR operaator

if username != "user" or password != "1234":
    print("Ligipääs keelatud")
else:
    print("Tere tulemast! ")