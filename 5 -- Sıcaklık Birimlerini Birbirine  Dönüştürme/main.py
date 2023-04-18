
#Sıcaklık Birimlerini Birbirine Dönüştürme Programı 

"""
1- Dereceyi --> fahrenheit ve kelvin'e dönüştürme.
2- Fahrenheit --> derece ve kelvine dönüştürme.
3- Kelvini --> fahrenheit ve dereceye dönüştürme. 

"""

print("-" * 30)
print("1- Celcius to fahrenheit |||  Celcius to kelvin")          
print("2- Fahrenheit to celcius |||  Fahrenheit to kelvin")
print("3- Kelvin to celcius     |||  Kelvin to fahrenheit")
print("-" * 30)


choice=int(input("Your choice : "))

if choice == 1:
    celcius=float(input("Degree to convert : "))
    fahrenheit = (celcius * 1.8) + 32
    kelvin = celcius + 273
    print("{} degree celcius is equal to {} degree fahrenheit and {} degree kelvin.".format(celcius,fahrenheit,kelvin))
elif choice == 2:
    fahrenheit=float(input("Degree to convert : "))
    celcius = (fahrenheit - 32) / 1.8
    kelvin = ((fahrenheit - 32) / 1.8) + 273
    print("{} degree fahrenheit is equal to {} degree celcius and {} degree kelvin.".format(fahrenheit,celcius,kelvin))
elif choice == 3:
    kelvin=float(input("Degree to convert : "))
    celcius = kelvin - 273
    fahrenheit = ((kelvin - 273)*1.8) + 32
    print("{} degree kelvin is equal to {} degree celcius and {} degree fahrenheit.".format(kelvin,celcius,fahrenheit))




"""
------------------------------
1- Celcius to fahrenheit |||  Celcius to kelvin
2- Fahrenheit to celcius |||  Fahrenheit to kelvin
3- Kelvin to celcius     |||  Kelvin to fahrenheit
------------------------------
Your choice : 3
Degree to convert : 15
15.0 degree kelvin is equal to -258.0 degree celcius and -432.40000000000003 degree fahrenheit.


"""