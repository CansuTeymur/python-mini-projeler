
#Vücut Kitle Endeksi Hesaplama Programı


boy=float(input("Boy (m) : "))
kilo=int(input("Kilo (kg) : "))


endeks = kilo/(boy*boy)


if endeks <=18:
    print(f"\n zayıf VKİ : {endeks}")
elif endeks >18 and endeks <=25:
    print(f"\n kilolu VKİ : {endeks}")
elif endeks >25 and endeks <=30:
    print(f"\n obez VKİ : {endeks}")
elif endeks >30:
    print(f"\n ciddi obez VKİ : {endeks}")



"""
Boy (m) : 1.65
Kilo (kg) : 50

 kilolu VKİ : 18.36547291092746

"""