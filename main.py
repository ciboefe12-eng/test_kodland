soru = input("sifre ne ")
if soru == "43434343":
    print("dogru")
else:
    print("yanlis")
soru2 = input("tekrar denemek ister misin ")
if soru2 == "evet":
    print("tamam")
    soru = input("sifre ne ")
    if soru == "aba":
        print("dogru")
    else:
        print ("gene yanlis yaptin ")
        