#  # Sana: 02.02.2026 
   ## Xatolar ustida ishlash.
# # print ("Hello world"  
   
#          # EOL VA EOF xatolik haqda.
# print("Salom"
# print("Hello World!"
#       # Joy tashlashda hatolik INDENTATION EROR .
# print("Hello World")     
# print( " 0'ngacha sanaymiz")
# for n in range(10):
#     print(n+1)  
# son = -5 
# if son>=0:
#      print("Musbat son")
# else:
#   print("Manfiy son")  
##  RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK  
# # 1 xatolik turi TypeEror 
# son = float(input("Istalgan soni kiriting:"))
# print(f"{son} ning kvadrati {son**2} ga teng.") 
# 2 NAME EROR xatoligi
# pint("Hello World")
# mevalar = ['olma','uzum','nok','anjir']
# for meva in mvelar:
#     print(meva)
      
## 3 ValueEror xatoligi
# son = float((input("Istalgan son kiriting:")))
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")
      
# 4 IdexEror xatoligi 
# mevalar = ['olma','anor','uzum']
# print(mevalar[3]) 
# mevalar = ['olma','anor','uzum'] # to'g'ri kod
# print(mevalar[2]) 
# 5 ZeroDivijonEror xatoligi
# Dastur davomida 0 ga bo'lish jarayonida yuzaga keladi.
# x,y = 50,50 
# z = 250/(x-y)
   ## MANTIQIY XATOLAR 
     
radius = 5 
pi = 4.14 # bu yerda pi = 3.14 teng edi 
# aylana_uzunligi = pi *radius**2
# print(aylana_uzunligi)  
# son = float(input("Istalgan sonni kiriting:"))
# ildiz = son**(1/2) 
# print(f"{son} ning ildizi {ildiz} ga teng.")  
 # Noo'rin bo'sh joy qoldirish .
# mevalar = ['olma','uzum','nok','anor']
# for meva in mevalar:
#     print(meva)
#     # print("Dastur tugadi") noo'rin qoldirilgan bo'sh joy
# print("Dastur tugadi")    

## AMALYOT 
#  01 
# son = float(input("Juft son kiriting:")) 
# if son%2!=0:
#     print("Bu son juft emas")
# else:
#     print("Rahmat")   
    
# # 02 
# yosh = int(input("Yoshingizni kiriting:"))    

# if yosh<=4 or yosh>=60:
#     narx = 0
# elif yosh <= 18 :
#     narx = 10000
# else:
#     narx = 20000
# print(f"Chipta {narx} so'm")    
    
#  03 
# x = float(input("Birinchi sonni kiriting:"))
# y = float(input("Ikkinchi sonni kiriting:"))
# if x == y :
#     print(f"{x}={y}")
# elif x < y :
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")   

# 04 
# mahsulotlar = ['un',"yog'",'sovun','tuxum',"kartoshka",'olma',
#                'banan','uzum','qovun']
# savat =[] 
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulot qo'shing:"))

# if savat:
#     for mahsulot in savat :
#         if mahsulot in mahsulotlar :
#             print(f"Do'konimizda {mahsulot} bor .")
         
            
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q.")
            
             
# else:
#      print("Savatingiz bo'sh")
# 05 
# mahsulotlar = ['un',"yog'",'sovun','tuxum',
#                'piyoz','olma','banan','uzum','qovun']

# savat = []
# for n in range(5) :
#     savat.append(input(f"Savatga {n+1}-mahsulot qo'shing:"))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat :
#     if mahsulot in mahsulotlar :
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
        
        
# if mavjud_emas :
#     print(f"Do'konimizda quydagi mahsulot yo'q:{mavjud_emas}")
# else:
#     print(f"Siz so'ragan barcha mahsulotlar do'konimizda bor:{bor_mahsulotlar}")        

# 06 
users = ['alisher1983','aziza','muslima','umar']

login = input("Yangi login kiriting:").lower()

if login in users :
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz")    





























