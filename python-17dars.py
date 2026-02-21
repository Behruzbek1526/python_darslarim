                   # Sana:20.02.2026 
# _______While tsikli_______ 

# Foydalanuvchi kiritgan qiymatni biror o'zgaruvchiga yuklash 
  # va dastur davomida foydalanish.
 
# ism = input("Ismingiz nima:")
# print(f"Salom {ism.title()}")   

# # INPUT funksiyasi ichida mant promt(savol) deyiladi.

# savol = f"Salom ,{ism.title()}.Yoshingiz nechida:"
# yosh = input(savol)

# Sonlar va input() 
 # input funksiyasi har qanday ma'lumotni string ko'rinishida saqlaydi.
 
# ism = input("Ismingiz nima:")
# savol = f"Salom {ism.title()}.Yoshingiz nechida:"
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa aylantirdik.
# heigt = input("Bo'yingiz necha metr:")
# heigt = float(heigt) # bo'yni o'nlik songa aylantirdik.


# While tsikli haqda...
  # While takrorlash operatori bo'lib for dan farqli ravishdda toki 
     # ma'lum shart true bo'lsa kodni takrorlaveradi.
     
# son = 1 # son 1 qiymatini berdik.
# while son <= 5   : # toki son 5 dan kichik yoki teng  ekan...
#         print(son, end=" ")
#         son = son + 1 # songa 1 qo'shamiz.
        

#   While va input() 
  # While tsikli yordamida dasturni to'xtatish imkonini 
   # foydalanuvchiga beramiz.
   
# print("Kiritilgan sonni kvadratini qaytaruvchi dastur!")
# savol = "Istalgan son ni kiriting:"   
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing):"
  
# qiymat = " "
# while qiymat != 'exit' :
#     qiymat = input(savol)
#     if qiymat != 'exit' :
#         print(float(qiymat)**2)


# Ishora(flag)


print("Kiritilagan sonnig kvadratini qaytaruvchi dastur!")
savol = "Istalgan sonni kiriting:"
savol+="(dastur to'xtatish uchun 'exit' deb yozing:"

ishora = True 
while ishora :
    qiymat = input(savol)
    if qiymat == "exit" :
        ishora = False 
    else:
        print(float(qiymat)**2)





























