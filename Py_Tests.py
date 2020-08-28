# a = int(input("Natural eded daxil edin : "))
# b = a//10000
# c = (a//1000)%10
# d = (a//100)%10
# e = (a//10)%10
# f = (a//1)%10
# if (b==f) and (c==e) and (d==d):
#     print("Yes")
# else:
#     print("No")
# print(b,c,d,e,f)

# a = int(input("A ededini daxil edin : "))
# b = int(input("B ededini daxil edin : "))
# c = int(input("C ededini daxil edin : "))
# d = int(input("D ededini daxil edin : "))
# if a >= b >= c >= d:
#     b = a
#     c = a
#     d = a
#     print(a,b,c,d)
# elif a < b < c < d:
#     print(a,b,c,d)
# else:
#     print(a**2,b**2,c**2,d**2)


# x=0
# ar = [1,2,3,4,5,6,7,8,9,10]
# for i in ar:
#         x +=i
# print(x)

# a = [1,2,2,3,2,2,4,6,3,5,9,3,2,7,9,8]
# print(set(a))



# ad = input("adinizi daxil edin : ")
# soyad = input("soyadinizi daxil edin : ")
# if len(ad)>=10 or len(soyad)>=10:
#     print("yeniden daxil edin : ")
# else:
#     print(f"Hello {ad} {soyad} ! You just delved into python.")



# n1 = int(input("N1 ededini daxil edin : "))
# n2 = int(input("N2 ededini daxil edin : "))
# x=[]
# for i in range(n1,n2+1):
#     for a in str(i):
#         if str(i).count(a)>1:
#             break
#         else:
#             x.append(i)

# print(len(set(x)))


# Mesele1:
#  Verilmish array var, N ededine bolune bilen butun tek ededleri artan sira ile cap edin

# meselen, arr=[2,21,6,18,4,10,14,15,3]  N=3
# output>>> [6, 15, 18, 21]


# arr = [2,21,6,18,4,10,14,15,3]
# n = int(input("Eded daxil edin : "))
# a = []
# for i in arr:
#     if i % 2 == 1 and i % n == 0:
#        a.append(i)
# a.sort()
# print(a)


# a = input("Sozu daxil edin : ")
# n = int(input("ededi daxil edin : "))
# for i in range(0,len(a),n):
#         print(a[i:i+n])


# son edilen mesele...


# a= int(input("3 reqemli eded daxil edin : "))
# b = a//100
# c = (a//10)%10
# d = (a//1)%10
# if b > c > d:
#     i = d*100 + c*10 + b
#     print(i)
# elif b > d > c:
#     i = c*100 + d*10 + b
#     print(i)
# elif c > d > b:
#     i = b*100 + d*10 + c
#     print(i)
# elif c > b > d:
#     i = d*100 + b*10 + c
#     print(i)
# elif d > b > c:
#     i = c*100 + b*10 + d
#     print(i)
# elif d > c > b:
#     i = b*100 + c*10 + d
#     print(i)
# elif d == c == d:
#     print(a)


# eded = input("Natural eded daxil edin : ")
# uzunluq = len(eded)
# if uzunluq == 6:
#     a = int(eded) // 100000
#     b = int(eded) // 10000 %10
#     c = int(eded)//1000 %10
#     d = int(eded)//100 %10
#     e = int(eded)//10 %10
#     f = int(eded)//1 %10
#     print(f*10**5+b*10**4+c*10**3+d*10**2+e*10+a)
# elif uzunluq == 5:
#     a = int(eded) // 10000
#     b = int(eded)//1000 %10
#     c = int(eded)//100 %10
#     d = int(eded)//10 %10
#     e = int(eded)//1 %10
#     print(e*10**4+b*10**3+c*10**2+d*10+a)
# elif uzunluq==4:
#     a = int(eded)//1000 %10
#     b = int(eded)//100 %10
#     c = int(eded)//10 %10
#     d = int(eded)//1 %10
#     print(d*10**3+b*10**2+c*10+a)
# elif uzunluq==3:
#     a = int(eded)//100 %10
#     b = int(eded)//10 %10
#     c = int(eded)//1 %10
#     print(c*10**2+b*10+a)
# elif uzunluq==2:
#     a = int(eded)//10 %10
#     b = int(eded)//1 %10
#     print(b*10+a)


# a = 0
# eded = int(input("Natural ededi daxil edin : "))
# for i in range(1,eded+1):
#     for x in str(i):
#         a += int(x)
# print(a)



# a = int(input("A ededini daxil edin : "))
# b = int(input("B ededini daxil edin : "))
# c = []
# for x in range(a+1,b):
#     c.append(x)
# print(*c)

        
# a = int(input("A daxil edin : "))
# b = int(input("B daxil edin : "))
# c = int(input("C daxil edin : "))
# d = int(input("D daxil edin : "))
# if (b+c==a+d):
#     print("Yes")
# else:
#     print("No")


# faktorial=1

# while True:
#     eded = int(input("Menfi olmayan eded daxil edin : "))
#     if (eded<=0):
#         print("Musbet eded daxil edin....")
#     else:
#         for i in range(1,eded+1):
#             faktorial *= i
#         print(faktorial)
#         break

# print("Orxan Mustafayev")

# tam =100
# kesir = 5.58
# ad = "Orxan"
# prosses = True
# prosses2 = False
# print(tam,kesir,ad,prosses,prosses2)

# adlandirmada deyiskenin evveline reqem vere bilmerik..deyiskenden sonra yazilmalidir reqem

# price = 100 + 20
# print(price)
# price = 100 - 20
# print(price)
# price = 100 * 20
# print(price)
# price = 100 / 20
# print(price)
# price = 100 % 30
# print(price)
# price = 100 // 30
# print(price)
# price = 10 ** 2
# print(price)

# a = 10
# a += 5
# print(a)
# a -= 10
# print(a)
# a *= 5
# print(a)
# a /= 5
# print(a)
# a = 100
# a //= 30
# print(a)
# a = 100
# a %= 30
# print(a)

# a = 15
# b = 5.25
# c = a * b
# print(c)
# c *= 1.18
# print(c)


# yazi = "Orxan Mustafayev"
# print(yazi[-2])
# print(yazi[:10:4])

# string1 = "Orxan"
# string2 = "Mustafayev"
# string3 = "Tahir"
# print(string1,string2,string3, sep='   ') sep funksiyasi yazi aralarina elaveler ucundur
# a=5
# b=6
# c=3
# print(a,b,c)

# string = """Burada istenilen yazini yazmaq mumkundur.  Meselen Eli`nin kecen defeki meselesi.
# gerek o defe ciddi ustune duserdi

# ama basini bos buraxdi
#  """
# print(string)

# ad = input("Istifadeci adinizi qeyd edin : ")
# reng = input("Beyendiyiniz rengi qeyd edin : ")
# print(ad,reng,"rengi xoslayir")

# yazi = "Orxan Mustafayev"
# yazi += " Tahir oglu"
# yazi += " 1993cu ilde"
# yazi += " Bakida anadan olub"
# print(yazi)

# birthday = int(input("Doguldugun ili daxil et : "))
# yas = 2020 - (birthday)
# print("Sizin yasiniz",yas)


# ev = int(input("Evinizin uzaqligini metre olaraq girin : "))
# isYeri = int(input("isyerinizin uzaqligini metre olaraq girin : "))
# ev /= 1000
# isYeri /= 1000
# print(ev,"km",isYeri,"km")

# firstName = "Orxan"
# lastName = "Mustafayev"

# message = f"{firstName} ({lastName}) adini dasiyir"

# message = f"{firstName:.3} {lastName:.1}" burada :.3 ve :.1 girilen stringi evvelden kesib saxlayir 
# print(message)
# message = f"{firstName:10} {lastName:10}" burada yazilan :10 ara vermek ucundur lakin ara vererken girilen stringin de xarakter sayini da hesaba qatir
# print(message)

# a = "Baki haqqinda"
# b = "Tarixi haqqinda"
# c = "Problemleri haqqinda"
# informa = f"{a} {b} {c}"
# print(informa)

# num1 = 5
# num2 = 7
# print(f"{num1} ustegel {num2} beraberdir {num1 + num2} bu reqeme beraber deyil {2 * (num1 + num2)}.")
# num1 = 3.14965887
# print(f"Bu reqemin qisa halidir {num1:.4} ve bu da hemin reqemin yari hissesidir {num1/2:.6}")

# newNo = 255
# print(f"{newNo:b}")

# number = 123456789123456789
# print(f"{number:,}")

# number = 123456789
# print(f"{number:<30}")
# print(f"{number:>30}")
# print(f"{number:^30}")
# print(f"{number:*^30}")

# ad = input("Adinizi daxil edin : ")
# mesaj1 = (f"{ad:.10} xos gelmisiz")
# mesaj2 = (f"{ad:.10} ozunuzu rahat hesab ede bilersiz")
# mesaj3 = "Bize qosuldugunuz ucun tesekkur"
# print(f"{mesaj1:^50}")
# print(f"{mesaj2:^50}")
# print(f"{mesaj3:^50}")

# radius = int(input("Dairenin yari hissesini girin : "))
# print(f"Dairenin tam olaraq sahesi {radius}: {radius * 2 *3.14}")

# sampleString = "Python is a high level language"
# # print(len(sampleString))
# print(sampleString)
# print(sampleString.upper())
# print(sampleString.lower())
# print(sampleString.title())
# print(sampleString.find("o"))
# print(sampleString.rfind("g"))
# print(sampleString.replace("high","low"))
# print("is" in sampleString)
# print(sampleString.count("a"))


# a = input("Her hansi bir string girin : ")
# a = a[:3] + a[-3:]
# print(a.upper())

# a = int(input("bir eded daxil edin : "))
# b = int(input("bir eded daxil edin : "))
# c = int(input("bir eded daxil edin : "))
# if (a + b)>c:
#     print("YES")
# else:
#     print("NO")

# a = input("Tam eded daxil edin : ")
# b = int(a.count("1"))
# c = int(a.count("3"))
# d = int(a.count("5"))
# e = int(a.count("7"))
# f = int(a.count("9"))
# print(b + c + d + e + f)

# a = input("Natural eded daxil edin : ")
# b = a[0]
# c = a[-1]

# a = input("Natural eded daxil edin : ")
# b = a[::]
# print(b)

# a = input("Natural eded daxil edin : ")
# b = int("1" in a)
# c = int("2" in a)
# d = int("3" in a)
# e = int("4" in a)
# f = int("5" in a)
# g = int("6" in a)
# h = int("7" in a)
# r = int("8" in a)
# i= int("9" in a)
# x = int("0" in a)


# a = int(input("Natural eded daxil edin : "))
# a = a**(1/2)
# print(a)


# import math
# math.pi = 3.14 pi sayi deyerine.
# math.tau math.pi 2 qatidir.
# math.pow quvvet operatorudu..normal **-den ferqi odur ki deyeri Float tipinde verir.
# print(math.ceil(-2.9))
# print(math.floor(-2.9))
# print(math.factorial(5))
# radius = 5
# print(f"dairenin radiusu {radius}: {radius * 2 * math.pi}")

# h = int(input("Silindirin hundurluyunu girin : "))
# y = int(input("Silindirin yari capini girin : "))
# print(f"Sualin Cavabi Budur : {math.floor(math.pi * h * math.pow(y,2))}")
# hecm = h * y ** 2 * math.pi
# print(f"Sualin Cavabi : {hecm} dir ")


# import math
# print("ax^2+bx+c=0 kvadrat tenliyine deyerler girin..")
# a = int(input("A ededini daxil edin : "))
# b = int(input("B ededini daxil edin : "))
# c = int(input("C ededini daxil edin : "))
# delta = math.pow(b,2)-4*a*c
# if delta<0:
#     print("Kvadrat tenliyin helli yoxdur")
# elif delta==0:
#     print("Kvadrat tenlikde 2 eded beraber kok var")
#     print(f"Birinci kok beraberdir : {(-b-(math.pow(delta,1/2)))/(2*a)}")
#     print(f"Ikinci kok beraberdir : {(-b+(math.pow(delta,1/2)))/(2*a)}")
# elif delta>0:
#     print("Tenliyin iki muxtelif koku var")
#     print(f"Birinci kok beraberdir : {(-b-(math.pow(delta,1/2)))/(2*a)}")
#     print(f"Ikinci kok beraberdir : {(-b+(math.pow(delta,1/2)))/(2*a)}")

# import random
# number = random.randint(1, 10)
# guessCount = 0
# guessChans = 5
# while guessCount < guessChans:
#     guess = int(input("Ededi daxil edin : "))
#     guessCount += 1
#     if number == guess:
#         print("Tebrikler !")
#         break
# else:
#     print("Tessuf uduzdunuz !")


# ad = input("Adinizi daxil edin : ")
# soyad = input("Soyadinizi daxil edin : ")
# a = int(len(ad))
# b = int(len(soyad))
# if a < 3 or a > 15:
#     print("Girdiyiniz ad xeta verir..")
# elif b < 3 or b > 15:
#     print("Girdiyiniz soyad xeta verir..")
# else:
#     print(f"Salam {ad} {soyad}")

# index = 5
# while index <= 10:
#     print(index)
#     index += 1
# print("Done !")

# index = 1
# while index <= 9:
#     print(f'{"*" * index:^9}')
#     index += 2
# print("Done !")

# a = int(input("Natural eded daxil edin : "))
# index = 0
# yekun = 0
# while index < a:
#     print(index)
#     index += 1
# print("Done !")



# a = int(input("Natural eded daxil edin : "))
# i=1
# while i<=a:
#     print(f'{"*" * i:^100}')
#     i += 2
# print("Done !")





# import random
# number = random.randint(1, 6)
# guessCount = 0
# sans = 5
# while guessCount < sans:
#     guess = int(input("bir reqem girin : "))
#     guessCount += 1
#     if guess == number:
#         print("Qazandiniz tebrikler.!")
#         break
# else:
#     print("Reqemi tapa bilmediniz !")

# while True:
#     ad = input("adinizi daxil edin : ")
#     if ad.lower() == "quit":
#         print("exit")
#         break
#     elif len(ad) < 3 or len(ad) > 15:
#         print("Yeniden cehd edin")
#     else:
#         print(f"hi, {ad}")
#         break

# index = 1
# while index <= 5:
#     print("*" * index)
#     index += 1
# print("done !")


# for index in range(1, 9, 2):
#     print(f'{"*" * index:^9}')
# print("Done")


# x = float(input("X ededi daxil edin : "))
# y = float(input("Y ededi daxil edin : "))
# if x < 0 and y < 0:
#     print(abs(x), abs(y))
# elif x < 0 or y < 0:
#     print(x + 0.5 , y + 0.5)
# elif (x > 0 and y > 0) and (x < 0.5) and (y < 0.5) and (y > 2) and (x > 2):
#     print(x/10 , y/10)
# else:
#     print(x,y)


# a = int(input("A ededini daxil edin : "))
# b = int(input("B ededini daxil edin : "))
# c = int(input("C ededini daxil edin : "))
# d = int(input("D ededini daxil edin : "))
# if (a >= b , a >= c , a >= d) and (b <= a , b >= c , b >= d) and (c <= a , c <= b , c >= d) and (d <= a , d <= b , d <= c):

# for index in [5,2,5,2,2]:
#     print(f"{index * 'X'}")



# import math
# number = int(input("Natural eded daxil edin : "))
# if math.pow(number,1/2)%1==0:
#     print("Yes")
# else:
#     print("No")


# number = int(input("Natural eded daxil edin : "))
# index = 1
# while index <= number:
#     print(number//index)
#     index += 1
#     if (number//index)%1 == 0:


# n = int(input("daxil edin : "))
# arr=[]
# n = len(arr)
# x=0
# for i in arr:
#     x += i
# print(x)









    
























