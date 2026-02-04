#Sana:24.01.2026
#06 SONLAR
#Integers butun sonlar 
# a = 20# Sonlar musbat 
# b = - 30 #Manfiy bo'lish mumkin 
# c = a+b 
# print(c)
#  Pythonda operatorlar orasidagi bo'shliqlarni inobatga olmaydi.
#Kvadrat yuzini hisoblaymiz.
# kvdrt_tomoni = 20 # Kvadrat tomoni 20 teng.
# kvdrt_yuzi = kvdrt_tomoni**2#Kvadrat yzuini hisoblaymiz.
# print(kvdrt_yuzi)
#fLOATS o'nlik sonlar 
# pi =3.14159 # O'nlik son (floats)
# radius = 10 #butun son (integer )
# diamtr = radius *2 
# print('Aylaning uzunligi',pi*diamtr,"teng")
#Butun sondan o'nlik songa .
# a = 30
# b = 10
# c= a /b
# print(c)#Natija o'nli bo'ladi / belgi orqali bo'linganda.
# a = 30 
# b = 0.5 
 #Quydagi arifmetik amal natijasi o'nlik bo'ladi.
# print(a/b)
# print(a*b)
# print(a-b)
# print(2*(a+b))
#Uzun sonlarni kiritish da  _ foydalamiz.
# mening_hisobim =str(20_000_000_000) +"💰"
# print('Meni bu yil daromadim',mening_hisobim)
# #KONSTANTA o'zgarmas qiymat.
# PI = 3.14159 
# radius = 20 
#Bir nechta o'zgaruvchiga qiymat berish.
# x, y, z = 10, -1.3, 30
# print(x, y , z)
#O'zgaruvchini turini almashtirish.
# ism = 'Behruzbek'
# yosh = 18
# xabar = ism +" "+str(yosh)+" yoshda"
# print(xabar)
#O'zgaruvchini turini tekshirish type( ) Foydalanamiz.
# print(type(yosh))
# print(type(xabar))
#INPUT va sonlar 
#Foydalanuvchidan tug'ilgan yilini so'raymiz.
# t_yil = int(input("Tug'ilgan yilingizni kiriting:"))
# #Foydalanuvchi yoshini hisoblaymiz.
# yosh = 2026 -t_yil
# #Foydalnuvhi yoshini konsolga chiqaramiz.
# print("Siz " + str(yosh) + " da ekansiz" )
#AMALYOT 
#01
#Foydaluvchidan son kiritishini so'raymiz.
# foydalanuvchi = int(input('Istalgan sonni kiriting:'))
# kvdrt = foydalanuvchi**2# sonning kvadratini hisovlaymiz.
# kubi = foydalanuvchi**3# sonning kubini hisoblaymiz.
# print(f"{foydalanuvchi} ning kvadrati {kvdrt} ga teng")
# print(f"{foydalanuvchi} ning kubi {kubi} ga teng.")
#02
#Foydalanuvchidan yoshini kiritishini so'raymiz.
# yosh = int(input('Assalm aleykum yoshingizni kiriting:'))
 #Tug'ilgan yilini hisoblaymiz.
# t_yil = 2026-yosh
# print(f"Siz {t_yil} yilda da tug'ilgansiz.😁")
#03
#Foydalanuvchidan ikkita son kiritishni so'raymiz.
a = float(input("Birinchi sonni kiriting:✋"))
b = float(input('Ikkinchi sonni kiriting:🤜'))
#ARIFMETIK amallar bajarish ustida.
print(f"{a}+{b}=" ,a+b)
print(f"{a}-{b}=" ,a-b)
print(f"{a}*{b}=" ,a*b)
print(f"{a}/{b}=" ,a/b)