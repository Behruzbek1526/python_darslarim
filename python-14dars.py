##  Sana:04.02.2026
# 14 LUG'AT BILAN TANISHUV

# Lug'at bilan ishlash.
# car_0 = {'model':'ferari','rang':'sariq'}
# print(car_0['rang']) # lug'atdagi qiymatni ko'rish uchun 
                     # kalit so'z orqali murojat qilinadi.
                     
#  Lug'atdagi qiymatlar (son,int,float, va matn,stirng) va 
# (list,tuple) va hatto boshqa  lug'at ham bo'lishi mumkin.
   
# talaba_0 = {'ism':'behruzbek akmedov','yosh':'19','t_yil':'2007'}
# print(f"{talaba_0['ism'].title()},\
#   {talaba_0['t_yil']}-yilda tu\'gilgan ,\
#   {talaba_0['yosh']} yoshda ")

# YANGI JUFTLIK QO'SHISH .
    
# talaba_0 = {'ism':'behruzbek akmedov','yosh':'19','t_yil':'2007'}
# talaba_0['kurs'] = 1 # yangi , 'kurs' nomli kalit so'zga 
#                      # 1 qiymatini yukladim.
# talaba_0['fakultet'] = "matematika" # 'fakultet' ga matematika 
#                     # qiymatini yukladim.
# print(talaba_0)                    


      #  Bo'sh lug'at.
      
# talaba_1 = { }  
# talaba_1['ism'] = "beruzbek akmedov"
# talaba_1['kurs'] = 5 # talaba_1 lug'atiga 'kurs' ga 5 qiymat berdim.
# talaba_1['yosh'] = 20 # 'yosh' ga 20 qiymat yukladim.
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

     # KALIT SO'ZLAR JUFLIGINI O'CHIRISH.
 
# talaba_0 = {'ism':'behruzbek akmedov','yosh':'20','t_yil':'2000'}  
# print(talaba_0) 
# del talaba_0['ism'] # ism degan kalitni so'zni qiymatini o'chirdim,
# print(talaba_0)    # del operatoriga kalit so'z nomini bergan holda.
                     

     # LUG'ATNI QATORLARGA BO'LIB YOZISH.
# mashinalar = { 
#     'model':'bmw',
#     'ot kuchi':'250',
#     'rangi':'qora',
#     'ch_yili':'2026'
#     }       
# # qatorlarga bo'lib yozish uchun katta qavslardan foydalamiz 
# # yangi qatordan joy tashlab 1-chi kalit so'zni kiritamiz va oxirida vergul qo'yamiz.
# print(mashinalar)
       
 
    # Qiymatni o'zgartirish .
    
# talaba_0 = {'ism':'behruzbek akmedov','yosh':'19','t_yil':'2007'}
# talaba_0["ism"] ="dexruzbek akmedov" # ismni dexruzbek akmedov ga o'zgartirdim.
# print(f"Talaba {talaba_0['ism'].title()} {talaba_0['yosh']} da")
    
    # ger() Metodi haqda 
# Biz hozirda lug'atdagi qiymatlarga kalit so'z to'gridan-tog'ri kalit
#so'z orqali murojat qildik buni kamchiligi lug'atda biz so'ragan 
# kalit so'z topilmasa KerEROR xatolik berib to'xtaydi.


    
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     } 
 
# # phone = telefonlar['ali']
# # print(f"Alining telefoni {phone}")   

 
# phone = telefonlar.get("murod","Bunday ism mavjud emas.")
# print(phone) 
     
# phone = telefonlar.get("hasan")
# print(phone)


#=========AMALIYOT========

 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    