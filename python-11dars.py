# Sana : 30.01.2026
  ##11 Bir necha shartlarni tekshirish.
 # if-elif-else KETMA KETLIGI  HAQDA.
# yosh = int(input("Yoshingiz nechida:>>"))
# if yosh<4 :
#     print("Kirish bepul")
# elif yosh<=12:
#     print("Kirish 5000 so'm")
# elif yosh>12 :
# #     print("Kirish 10 000 so'm")
# yosh = int(input("Yoshingizni kiriting?"))
# if yosh<=4:
#     narx = 0
# elif yosh<=12:
#     narx =5000    
# else:
#     narx =10000 
# # print(f"Sizga kirish {narx} so'm")
# yosh = int(input("Yoshingizni kiriting?")) # yosh kiritishni so'radm foydalanuvchidan.
# if yosh<=4: # yosh bolalarga bepul
#     narx = 0
# elif yosh<=12: # 4 yoshdan 12 yoshgacha 5000 so'm    
#     narx = 5000
# elif yosh<65: # 12  dan 65 yoshgacha 10000 so'm    
#     narx = 10000
# else:
#     narx = 8000  # qariyalarga 8000 so'm
# print(f"Sizga kirish {narx} so'm ") 
    ## AND , OR  OPERATORLARI
# kun = input("Bugun kun qanday?")   
# if kun.lower()=="shanba" or kun.lower()=="yakshanba":
#     print("Bugun dam olish kuningiz.")
# else:
#     print("Bugun ish kuningiz.")    
# kun = input("Bugun kun nima?") # Foydalanuvchidan kunni so'raymiz.
# harorat = float(input("Havo harorati qanday?")) # Havo haroratini so'raymiz.
# if kun.lower()=="yakshanba" and harorat>=30:
#     print("Cho'milgani ketdik.")
# elif kun.lower()== "yakshanba" and harorat<30:
#     print("Uyda dam olamiz.")    
    ## Bir nechta shartlarni ketma-ket yozish
# kun = input("Bugun nima kun?") # foydaluvchidan kunni so'raymiz.
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat>=30:
#     print("Cho'milgani ketdik.")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Bugun uyda qolamiz.") 
        ##BOOLEAN MA'LUMOTLAR TURI
# narh = 15_000 # mijoz 15000 so'mga taom oldi.
# choy = True # mijoz choy oldi .
# salat = False # mijoz salat olmadi. 

# if choy and salat:# agar mijoz joy va salat olgam bo'lsa.
#     narh = narh + 10000 #  # narhga 10000 so'm qo'shiladi.
# elif choy or salat :#  choy yoki salat olgan bo'lsa.
#     narh = narh + 5000 # narhga 5000 so'm qo'shamiz.
# print(f"Jami {narh} so'm to'lov qiling mijoz.") # Yakuniy narhni chiqaramiz.
       

      ## Shartlar ketm_ketligini tekshirish
  
# narh = 15000  #  mijoz 15000 so'mga taom oldi.
# choy = True
# salat =False
# non = True 
# kompot = True
# assorti = False 
# #Quydagu har biri alohida tekshiriladi.
# if choy:#agar choy olsa
#    print("Mijoz choy oldi.")
#    narh = narh+3000
# if salat:# agar salat olsa.
#     print("Mijoz salat oldi.")
#     narh = narh+5000
# if non:# agar non olgan olsa.
#     print("Mijoz non oldi.")
#     narh = narh+2000
# if kompot :# kompot olsa.
#     print("Mijoz kompot oldi.")
#     narh =narh +5000
# if assorti:# assorti oldi.
#     print("Mijoz assorti oldi.")
#     narh = narh+15000
# print(f"Jami {narh} so'm to'lov qiling.")    
 
## RO'YXAT TARKIBINI TEKSHIRISH .
 # in OPERATORI YORDAMIDA biz ro'yxatning ma'lum bir elementini tekshirishimiz mumkin.
# mashinalar = ['Audi','Bmw','Volvo','Ferari','Rols-Royce','Bugatti','Hyundai']  
# 'Audi' in mashinalar # mashinalar da audi bormi  
# kitoblar = ['Alkimyogar','Atom odatlar','Martin idien'] # kitoblar ro'yxatini tuzdim.

# menu =['Osh ',"Somsa",'shashlik','tandirgo\'sht','pitsa'] # menu ro'yxatini tuzdim.
# ovqat = input("Qanday taom buyurtma qilasiz?>>>")
# if ovqat.lower() in menu:
#     print("Buyturtma qabul qilindi.")
# else:
#     print("Afsuski bizda bunday taom yo'q.")    

   ## not in OPERATORI HAQDA bu operator yordamid ro'yxatda element yo'qligini tekshiramiz.
# menu =['Osh ',"Somsa",'shashlik','tandirgo\'sht','pitsa'] # menu ro'yxatini tuzdim.

# mashinalar = ['bmw ','ferari','hyundai','tesla'] # mashinlar ro'yxatini yaratdim.
# sotuv = input("Qanday mashina sotib olasiz?>>>")
# if sotuv.lower() not in mashinalar :
#     print("Afsuski bu mashinalar band qilingan buyurtma.")
# else:
#     print("Buyurtma qabul qilindi.")
   
     ## IKKI RO'YXATNI SOLISHTIRISH.
# menu = ['osh','manti','somsa']
# buyurtmalar = ['osh','somsa','shashlik']

# for taom in buyurtmalar  :   
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#          print(f"Kechirasiz ,menuda {taom} yo'q")
    

## Ro'yxatni bo'sh emasligini tekshirish.

  
# menu = ['osh','manti','somsa']
# buyurtmalar = []
# if buyurtmalar : # ro'yxatda biror element yo'q bo'lsa ifoda True qaytaradi .               
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz , menuda {taom} yo'q")
# else:#  agar ro'yxat bo'sh bo'lsa 
#     print("Savatchangiz bo'sh.")      
 
    ##Amalyot  
 #01
# son = int(input("Juft son kiriting:")) #Juft son kiritishini so'radim foydalanuvchidan .
# if son % 2 != 0 :
#     print("|Bu toq son.|") # agar qoldiq 0 teng bo'lmasa toq son
# elif son==0: # agar 0 son kiritilsa quyfagi kod ishga tushadi.
#     print(" 0 |Juft ham toq ham son emas|")    
# else: # agar qoldiq 0 ga teng bo'lsa juft son
#     print("|Bu juft son|")
 # 02
# yosh =float(input("Assalom aleykum yoshingizni kiriting:")) # foydalanuvchidan yoshini so'radim.
# if yosh ==0:  #  agar yosh 0 teng bo'lsa .
#      narx = "Onangiz qorinidan chiqib oling bolakay.😆"
# elif yosh<=4:#  4 yoshdan kichik bo'lsa bepul
#     narx = "Bepul kirish sizga bolakay.😎"    
# elif yosh<=18: # 4 yoshdan katta va 18 teng bo'lsa 10000 so'm  
#     narx = "10000 so'm kirish ancha ulg'ayibsiz.🧐"
# elif yosh>=60: # agar yosh  60 dan katta bo'lsa bepul
#        narx = "Bepul kirish sizga buva. 🙂"    
# elif yosh>18: # 18 dan katta bo'lsa 20000 so'm  
#     narx = "20000 so'm kirish sizga yosh janob.😟"
# print(f"Sizga {narx}")
#  #03 
# x = float(input("Birinchi sonni kiritting:")) #  1-son kiritshini so'radim float ko'rinishida.
# y = float(input("Ikkinchi sonni kiriting:")) # 2-son kiritishini so'radim.
# if x<y : #  agar son x<y dan kichik bo'lsa
#     son = f"{x}<{y}" 
# elif x>y: # agar x>y dan katta bo'lsa.
#     son = f"{x}>{y}"
# elif x==y:
#     son = f"{x}={y}" # agar sonlar teng bo'lsa
# print(son)    
 #  04 
# mahsulotlar = ['banan','olma','apelsin','nok','mandarin','kivi'] # mevalar ro'yxatinii yaratdim.
# savat = [] # savat nomli bo'sh ro'yxat yaratdim.
# print("Salom savatga 5 t mahsulot qo'shing.") #  savatga 5 ta mahsulot qo'shishini mijozdan so'radim.
# for n in range(5):# sonlar ketma ketligini shallantiradi.
#     savat.append(input(f"Savatga {n+1 }-mahsulot qo'shing:"))
    
# bor_mahsulotlar = [] # bo'sh ro'yxat yaratdim.
# mavjud_emas = []  # mavjud_emas nomlo bo'sh ro'yxat yaratildi.
# for mahsulot in savat : 
#     if mahsulot in mahsulotlar: 
#        bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas :
#     for bosh in mavjud_emas :# mavjud_emas ichidagi elementni yukladi, [...] shaklada ro'yxat chiqmashligi uchun.
#         print(f"Do'konda quydagi mahsulotlar yo'q:{bosh}")
# else:
#     for bor_mahsulot in bor_mahsulotlar: # ro'yxat [...] shaklda chiqmasligi uchun bor_mahsulot degan yangi o'zgaruvchiga yukladim.
#         print(f"Siz so'ragan  mahsulotlar:{bor_mahsulot}")   
#   ## 05 
# foydalanuvchilar = ["behruzbek",'Bilolbek','Muslima','ozodbek''javlon'] # foydalanuvchilar ro'yxatini tuzdim.
# login = input('Yangi login kiriting:') # foydalanuvchidan login kiritishini so'radim.
# if login in foydalanuvchilar: # foydalanuvchi ro'yxatida login ichidagi element bo'lsa.
#     print("Login band , yangi login tanlang!")           
# else: 
#     print(f" Xush kelibsiz   {login.title()}!") # agar login band bo'lmasa quydagu habarni chiqar.
     ## 06 
# son = int(input("Butun son kiriting:")) # foydalanuvchidan butun son kiritishini so'radim.
# for n in range(2,11) :  # 2 , 10 gacha sonlarni shaklintiradi.    
#      if (son%n)==0: # agar son qoldig'i 0 teng bo'lsa qo'ldiqsiz bo'linadi.
#          print(f"{son} soni {n} ga qoldiqsiz bo'linadi!")
        

        
     