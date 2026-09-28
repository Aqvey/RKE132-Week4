# Kirjuta Pythoni programm, mis kontrollib kliendi staatust tema kulutuste põhjal.
# Tingimused:
# Kui klient on kulutanud vähemalt 5000 €, siis tema staatus on Platinum.
# Kui klient on kulutanud vähemalt 1000 €, siis staatus on Gold.
# Kui klient on kulutanud vähemalt 500 €, siis staatus on Silver.
# Kui klient on kulutanud vähemalt 100 €, siis staatus on Bronze.
# Kui vähem kui 100 €, siis on ta Tavaline klient.

kulutatud_summa = int(input("Kui palju raha sa oled meie juures kulutanud? "))

""" if kulutatud_summa >= 5000:
    print("Platinum")
elif kulutatud_summa >= 1000:
    print("Gold.")
elif kulutatud_summa >= 500:
    print("Silver.")
elif kulutatud_summa >= 100:
    print("Bronze.")
else:
    print("Tavaline klient.")
 """


if kulutatud_summa < 100:
    print("Tavaline klient.")
elif kulutatud_summa >= 100 and kulutatud_summa < 500:
    print("Bronze.")
elif kulutatud_summa >= 500 and kulutatud_summa < 1000:
    print("Silver.")
elif kulutatud_summa >= 1000 and kulutatud_summa < 5000:
    print("Gold.")
else:
    print("Platinum.")