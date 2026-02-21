#  Sana : 05.02.2026 
#15  Lug'at elementlari bilan ishlash.Lug'atdagi barcha 
# kalit-qiymatni chiqaradi.  
   #  items()    Metodi . 
# mashina = {              #Mashina uning moddellari.
#            'Bmw':'Bl400',
#            'Volvo':'K400',
#            'Tesla':'I400',
#            'Audi':'500',
#            'Ferrari':'T600'}
# print(mashina.items())
# for  k,q in mashina.items() :
#     print("Kalit:",k)
#     print('Qiymat:',q)  
  
   # .keys() Metodi .Lug'atdagi barcha kalit so'zni chiqaradi.

# mahsulotlar = {         #Do'kondagi mahsulotlar. 
#         'Nok':'5000',
#         'Uzum':'6000',
#         'Shaftoli':'30000',
#         'Apelsin':'2000',
#         'Banan':'40000',
#         }   
# print(mahsulotlar.keys())  
#    # for operatori yordamida kalitni chiroyli ko'rinishga keltiraman.
# print("Do'kondagi mahsulotlar:")   
# for k in mahsulotlar.keys():
#     print(k)
    
# # Yuqorida keys() metodini ham ishlatamask ham shu najani beradi.
        
   # for tsikli va if sharti yordamida lug'atdagi birot qiymatni 
#          # alohida chiqarish.
# mahsulotlar= {         #Do'kondagi mahsulotlar. 
#     'nok':'5000',
#     'uzum':'6000',
#     'shaftoli':'30000',
#     'apelsin':'2000',
#     'banan':'40000',
#     }   
# bozorlik = ['olma','banan','nok','apelsin']   # bozorlik ro'yxat yaratdim.
       
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")


# for tovar in mahsulotlar:
#     if tovar not in bozorlik:
#         print(f"Iltimos do'koningizga {tovar} olib keling.")


    # Lug'at elementlarini tartib bilan chiqarish .
    
# mashinalar = {     # Mashina va narx lug'atini yaratdim .
#      'Kobalt':'12000',
#      'Nexia 3':'11000',
#      'Damas':'10000',
#      'Malibu':'30000',
#      }
# print("Avtomobillar:")
# # Alifbo tartibi bo'yicha chiqarish uchun sorted() funksiyasidan foydalandim.
# for mashina in sorted(mashinalar): # 
#     print(mashina.title()) 

    # .values() Metodi.Lug'atdagi qiymatlarni chiqaradi.
    
    
# mashinalar = {     # Mashina va narx lug'atini yaratdim .
#      'Kobalt':'12000',
#      'Nexia 3':'11000',
#      'Damas':'10000',
#      'Malibu':'30000',
#      }

# print("Bizning mashinalarimiz narxi:") 
# for mashina in mashinalar.values():
#     print(f"{mashina} $" ) 
    # Agar birot qiymat ko'p marta qaytarilsa konsolga chiqib keladi.
# telefonlar = {    # Telefon va model lug'atini tuzdim.
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'Honer 9b',
#     'behruzbek':'iphone 19 pro',
#     'bahtiniso':'redmi 9',
#     'muslima':'iphone 19 pro',
#     'hamida':'nokia 300'
#     }    
# # print("Foydalanuvchilar telefonlari:")
# # for telefon in telefonlar.values():
# #     print(f"{telefon}") 
#    # Lug'atdagi bir xil qiymatlar qayta konsolga chiqmasligi uchun set() 
#                       # metodi dan foydalandim.    
# print("Foydalanuvchi telefonlari:")
# for telefon in set(telefonlar.values()):
#     print(telefon)  
 

#-------------AMALYOT-----------
# 01 
# python_izohlar = {   # python izohlar ro'yxatini yaratdim.
#        'for':"biror amalni qayta-qayta bajarish tsikli",
#         'in':'ichida',
#         'int':'butun son',
#         'float':'o\'nlik son',
#         'string':'matn',
#         'list':'ro\'yxat',
#         'typle':'o\'zgarmas ro\'yxat',
#          'boolean':'mantiqiy qiymat',
#          'del':'indeks bo\'yicha o\'irish',
#          'if':'shartlarni tekshirish operatori',
#          }
# print("Python izohli lug'ati:")
# # Alifbo ketma-ketligi bo'yicha sorted() funksiyasi yordamida chiqardim.
# for k,q in sorted(python_izohlar.items()) :
#     print(f"{k} - {q}")

#02 
# davlat_poytaxt = {   # davalt va poytaxt nomli lug'at yaratdim.
#      'aqsh':'washington',
#      'italya':'rim',
#      'rossiya':'moskva',
#      'singapur':'kuala-lumpur',
#      'janubiy korea':'seul',
#      'hindiston':'dehli',
#      }
# print("Dunyo davlatlari:")
# for davlat in sorted(davlat_poytaxt):
#     print(davlat.title())
# print("Dunyoning poytaxtlari:")
# for poytaxt in sorted(davlat_poytaxt.values()):
#     print(poytaxt.title())

# #03 
# davlat_poytaxt = {   # davalt va poytaxt nomli lug'at yaratdim.
#      'aqsh':'washington',
#      'italya':'rim',
#      'rossiya':'moskva',
#      'singapur':'kuala-lumpur',
#      'janubiy korea':'seul',
#      'hindiston':'dehli',
#      }
# # Foydalanuvchidan istalgan davlatni kiritishin so'radim.
# davlat = input("Qaysi davlatni poytaxtini bilishni istaysiz?:").lower()
# poytaxt = davlat_poytaxt.get(davlat)
# if poytaxt == None : # agar foydalanuvchi kiritgan kalit so'z yo'q bo'lsa
#     print("Kechirasiz bunday ma'lumot yo'q.")
# else:        # agar  kalit so'z bor bo'lsa
#     print(f"{davlat.upper()} ning poytaxti {poytaxt.upper()} shahri.")
  
# #04
   
# taom_menyusi = {      # Restoran menyusin tuzdim.
#         'osh':'20000',
#         'non':'5000',
#         'somsa':'8000',
#         'shashlik':'14000',
#         'norin':'40000',
#         'mastava':'20000',
#         'baliq':'40000',
#         'burda':'20000',
#         'kabob':'17000',
#         'la\'gmon':'20000',
#         }
# print("3 ta taom buyurtma qiling:")
# buyurtmalar =[] # bo'sh ro'yxat yaratib oldim.
# for n in range(3): # range() yordamida 3 gacha sonli ro'yxat shaklantirdim.
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())
    
# for buyurtma in buyurtmalar: #Foydalanuvchi kiritgan taomni 
#    if buyurtma in taom_menyusi:  # taom_menyusi bilan solishtirish.
#        print(f"{buyurtma.title()} {taom_menyusi[buyurtma]} so'm ")
#    else: 
#        print(f"Kechirasiz bizda {buyurtma} yo'q")



















