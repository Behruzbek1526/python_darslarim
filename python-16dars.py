# Sana:10.02.2026 
# 16 NESTING 
# LUG'ATLAR RO'YXATI 

# car0 = {
#         'model':'lasetti',
#         'rang':'qora',
#         'yil':2024,
#         'narx':11000,
#         'korobka':'avtomat'}

# car1 = {
#         'model':'cobalt',
#         'rang':'oq',
#         'yil':2024,
#         'narx':10000,
#         'korobka':'mexanik',
#         }

# car2 = {
#         'model':'damas',
#         'rang':'oq',
#         'yil':2025,
#         'narx':10000,
#         'korobka':'mexanik'
#         }   

# car = car0
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narx']}$")

# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narx']}$")

# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narx']}$")  



#  AMALYOT 

#02 4 ta mashhur shahslaring ma'lumotlar lug'atini tuzing.

# mashhur1 = {'ism':'Tom Kruz',
#             'tyil':1962,
#             'yosh':63,
#             'film':['Top Gan','Uddalab bo\'lmas topshiriq',
#                     'Yomg\'gir odami'],
#                 }
# mashhur2 = {'ism':'Lianardo Di Kaprio',
#             'tyil':1974,
#             'yosh':51,
#             'film':['Titanik','Omon qolgan','Muqaddima'],
#             }
# mashhur3 = {'ism':'Dueyn Jonson',
#             'tyil':1972,
#             'yosh':53,
#             'film':['Moana','Jumanji','Forsaj 5']}
# mashhur4 = {'ism':'Robert Dauni',
#             'tyil':1965,
#             'yosh':60,
#             'film':['Temir odam','Qasoskorlar','Oppengeymer']}

# # Lug'atni ro'yxatga joylab olaman ular ustida ishlash oson bo'ladi.
# mashhurlar = [mashhur1,mashhur2,mashhur3,mashhur4]

# for mashhur in mashhurlar :
#     print(f"\n{mashhur['ism']} "
#           f"{mashhur['tyil']}-yilda tug'ilgan."
#           f"{mashhur['yosh']} yoshda...")


# # Yuqoridagi lug'atlarga yangi ma'lumot qo'shing.

# for mashhur in mashhurlar :
#     ism = mashhur['ism'] # Lug'atdagi barcha ism larni ism o'zgaruvchiga yukladim.
#     filmlar = mashhur['film'] # Barchar filmlarni filmlar o'zgaruvchisiga yukladim.
#     print(f"\n{ism} suratga tushgan mashhur filmlar:")
#     for film in filmlar:
#         print(film)
                  
# 03 
#Oila a'zolaringiz dan 3 ta sevimli filmini so'rang .


# filmlar = {'ali':['Terminator','Qasos','Alanga'],
#            'bilol':['Qasos','Alanga','Do\'stlik'],
#            'behruz':['Jasur','Bugun','Maktab'],
#            'ozodbek':['Maktab','Tanafus','Qayta boshlash'],
#            }

# for ism,film in filmlar.items() :
#     print(f"\n{ism.title()}ning sevimli filmlari:")
#     for film in film :
#         print(film)

# 04 
# Davlatlar lug'atini yarating va lug'at ichida lug'at yaratib qo'shimcha ma'lumot qo'shing.

# davlatlar = {
#     'o\'zbekiston':{'poytaxt':'toshkent',
#                     'hudud':448978,
#                     'aholisi':33000000,
#                     'pul':'so\'m',
#                     },
#     'rossiya':{'poytaxt':'moskva',
#                'hudud':1709846,
#                'aholisi':144000000,
#                'pul':'rubl',
#                },
#     'aqsh':{'poytaxt':'vashington',
#             'hudud':9631418,
#             'aholisi':327000000,
#             'pul':'dollor',
#             },
#     'janubiy korea':{'poytaxt':'seul',
#                      'hudud':100.363,
#                      'aholisi':52000000,
#                      'pul':'von',
#                      },
#     }
# for davlat,info in davlatlar.items() :
    
#     if davlat.lower() == 'aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt']}"
#           f"\nHududi:{info['hudud']} kv.km",
#           f"\nAholisi:{info['aholisi']}",
#           f"\nPul birligi:{info['pul']} pul birligi " )
    
    
# #Yuqoridagi dasturga faqat foydalanuvchi so'ragan davlatni chiqarish .

# davlat = input("Davlat nomini kiriting:").lower()
# if davlat in davlatlar :
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi:{info['hudud']} kv.km"
#           f"\nAholisi:{info['aholisi']}"
#           f"\nPul birligi:{info['pul']} pul birligi " )
# else:    
#      print("Bizda bu davlat haqida ma'lumot yo'q")









