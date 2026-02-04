#Sana: 27.01.2026
# # FOR TAKRORLASH OPERATORI .
# mehmonlar = ['Vali','Ali','Husan','Behruzbek']
# for mehmon in mehmonlar :
    # print(mehmon)
# mehmonlar = ['Vali','Ali','Husan','Behruzbek']
# for mehmon in mehmonlar:
    # print(f"Salom  do'stim nima yangiliklar, {mehmon}")
# For yordamida o'nlik sonlar bilan ishlash.
# sonlar = list(range(1,11))# range() yordamida 1,10 gacha  ro'yxat tuzdim.
# for son in sonlar:
    # print(f"{son} ning kvadradi {son**2} ga teng")
    ## For yordamida yangi ro'yxat shaklantirish.
# sonlar = list(range(11))    
# sonlar_kvadrati =[]    
# for son in sonlar:
    # sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)  


   ## AMALYOT 
#01    
# ismlar = ['Behruzbek',"Bilolbek",'Ozodbek','Dildora',"Muslima"]
# for ism in  ismlar :
#     print(f"Salom sizlarni yaxshi ko'raman {ism}")
#02 
# for ism in ismlar :
#     print('Salom',ism)
# print('Kod 5 marta takrorlandi.')    
#03 
# toq_sonlar = list(range(10,100,3))    
# for son in toq_sonlar:
#     print(son**3)
     ##  Amalyot 
#01 
# ismlar = ['Behruzbek','Bilolbek','Ozodbek','Muslima',"Bahtiniso"]  #  ismlar ro'yxatini tuzdim.
# for ism in ismlar:
    # print("Salom yaxshimisan",ism)
#02 
# ismlar = ['Behruzbek','Bilolbek','Ozodbek','Muslima',"Bahtiniso"]  #  ismlar ro'yxatini tuzdim.
# for ism in ismlar:
    # print("Salom yaxshimisiz.",ism)
# print("Kod 5 marta takrorlandi.")     
#03
# toq_sonlar = list(range(10,100,3)) # toq sonlar ro'yxatini tuzdim.
# for son in toq_sonlar:
    # print("Bu soning kubi:",son**3)
#04 
# ism = [] #bo'sh ro'yxat yaratdim.
# print("Sizning eng yaxshi ko'rgan 5 ta doramangiz?")
# for n in range(0,5):
    # ism.append(input(f"{n+1}-dorama nomi:"))
    # print(ism)
# 05 
ismlar = []
n_people = int(input("Bugun techta odam bilan suhbatlashdingiz?:>>"))
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi?"))
    print(ismlar)  
    
