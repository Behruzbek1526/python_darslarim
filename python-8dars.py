   #27.01.2026 
#08  Ro'yxatlar bilan ishlash.
# Ro'yxatni tartiblash .
# cars = ['nexia','Bmw','volvo','gm','tesla','audi']
# cars.sort()
# print(cars)
#Ro'yxatni teskari saqlash .
# cars = ['audi','bmw','volvo','gm','tesla']
# cars.sort(reverse=True)# Ro'yxatni teskari tartiblash uchun reverse=True argumentini qo'ladim.
# print(cars)
  # Ro'yxatdagi elemtni tartibini buzmagan holda ro'yxatni tartiblash.
# mehmonlar = ['behruzbek','bilolbek','ozodbek','asilbek']
# print("sorted() qaytargan ro'yxat:",sorted(mehmonlar))
# print('Asl ro\'yxat:',mehmonlar)  
# print(sorted(mehmonlar,reverse=True))
ages = [12,30,60,45,20,17]
ages.sort()
# print(ages)
# print(sorted(ages,reverse=True))
   ## Ro'yxatni aylantirish boshidan oxiriga oxiridan boshiga .
# fruits = ['olma','banan','nok','olcha','qulupnay']
# fruits.reverse() # reverse() metodi ro'yxatni aylantiradi.
# print(fruits)   
   ## Ro'yxatni uzunligini o'lchash.
fruits = ['olma','banan','nok','olcha','qulupnay']
# print('Elementlar uzunligi:',len(fruits))# len( ) funksiyasi ro'yxat uzunligini o'lchaydi.
  ### range() FUNKSIYASI ma'lum bir oraliqdagi sonlar ketma ketligini yaratadi.
# sonlar = list(range(0,10)) # list() funksiyasi ro'yxatga shaklida saqlaydi. 
# print(sonlar) 
  ## range() funksiyasi yordamida qadamni berish.
juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha raqamlarni 2 qadam bilan shaklantiradi.
toq_sonlar = list(range(1,20,2)) # 1 dan 20 gacha raqamlarni 2 qadam bilan shaklantiradi.
# print('Juft sonlar:',juft_sonlar)
# print('Toq sonlar:',toq_sonlar) 
  #Sonli ro'yxat ustida amallar.
narxlar = [1200,3000,400,5000,900,5000]
arzon = min(narxlar) #eng kichik qiymatni min() funksiyasi yordamida topdim.
qimmat = max(narxlar) #eng katta qiymatni max() funksiyasi yordamida topdim.
jami = sum(narxlar)
# print("Arzon narxlar.",arzon,"Qimmat narxlar.",qimmat,"Jami narx.",jami)
   ##Ro'yxatni kesish.
# mashinalar = ['Nexia','Cobalt','Tesla','Audi','BMW']
# mening_mashinalrim = mashinalar[0:2]  # 0-indeksdan boshlab 2 ta  elemntni ajratib olaman.
# print("Men yangi mashinam:",mening_mashinalrim)
  #Bu usul yordamida istalgan joyni kesib olishimiz mumkin.
fruits = ['olma','banan','nok','olcha','qulupnay']
# print("Yangi mashina:",mashinam)  
  #Agar boshlang'ich indeksni bermasak ,Python avtomat ravisha 0 indeksdan boshlab kesadi.Agar indeks kiritilmasa.
# mashinalar = ['Nexia','Cobalt','Tesla','Audi','BMW']  
# print(mashinalar[:3])#Ro'yxat boshidan 3-gacha kesadi.  
# print(mashinalar[0:]) # 0-indeksdan boshigacha kesadi.
 
  # #  Ro'yxatdan nusxa olish.
# sonlar = [0,5,5,5,6,6,9,7] #sonlar degan ro'yxat yaratdik.
# sonlar2 = sonlar #sonlar2 degan ro'yxatga sonlarni tenglaymiz.
# sonlar2.insert(0,120)# 0 indeks o'rniga 120 qo'shdim.
# sonlar2.append(80) #sonlarga 80 qo'shdim .
# print("Bu sonlar ro'yxati:",sonlar)
# print("Bu sonlar2 ro'yxati:",sonlar2)    #natija biz kutgandek chiqmadi.
# ikki ro'yxatda ham o'zgarish bo'ldi.
  ###Buning kesish usulidan foydalamiz.
sonlar = [0,5,5,5,6,6,9,7] #sonlar degan ro'yxat yaratdik.
sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi.  
sonlar2.append(4) # sonlar2 ga 4 qo'shdim. 
sonlar2.append(8) # sonlar2 ga 8 qo'shdim. 
# print("Bu sonlar ro'yxato:",sonlar)
# print("Bu sonlar2 ro'yxat:",sonlar2)  
   #Tuples - o'zgarmas ro'yxat   
tomonlar = (20,30,50)  # ( ) ichida olingan elementlar o'zgarmas ro'yxatdir.
print(tomonlar)
  # Tuple ro'yxatini o'zgartirish yagona yo'li.
# list() funksiyasi yordamida oddiy ro'yxat shakliga keltirib olish.
mashinalar = ('Kia','Audi',"Tesla",'Hyundai')
mashinalar =list(mashinalar) # o'zgarmas ro'yxatni oddiy ro'yxat ko'rinishiga o'tkazdik.
mashinalar.append("Nexia")# ro'yxatg Nexia mashianasini qo'shdik.
           # # AMALYOT
#O1
davlat = ['Korea','Aqsh','Rossiya','Singapur'] # davlat degan ro'yxat tuzdim.
print(davlat)# 
#02 Ro'yxat uzunligini konsoga chiqarish.         
print('Ro\'yxat uzunligi:',len(davlat)) 
#03
print(sorted(davlat)) 
#04
print(sorted(davlat,reverse=True))  
#05
print(davlat)
#06
davlat.reverse()# reverse metodi yordamida ro'yxatni aylantirdim.
print(davlat)
#07
davlat.sort() # sort() metodi alifbo bo'yicha tartiblab chiqadi ro'yxatni.
print(davlat)
davlat.sort(reverse=True)# alifboga teskari chiqaridi reverse=True argumentini qo'shdim.
print(davlat)
#08
sonlar =list(range(120,1200,2)) # 120 dan 1200 gacha sonlar 2 qadam bilan sonlar.
print(sonlar)
#09
jami = sum(sonlar) #sum yig'indini hisoblaydi.
print('Sonlar yig\'indisi',jami)
#10
katta_son = max(sonlar) # max funksiyasi yordamida eng katta qiymatni topamiz.
kichik_son = min(sonlar) # min funksiyasi eng kichik qiymatni chiqaradi.
print("Sonlar ayirmasi",katta_son-kichik_son)
#11
print("Ro'yxatdagi element soni:",len(sonlar))
#12
print("Ro'yxat boshida 20 ta son:",sonlar[0:21]) # ro'yxat boshidan 20 t qiymatni kesib oldim [:] yordamida.
print("'Ro'yxat o'rtasidan 20 ta son",sonlar[261:281])  #ro'xat o'rtasidan 20 ta raqamni kesib oldim.
print("Ro'yxat oxiridan 20 ta son:",sonlar[520:541]) #ro'yxat oxiridan 20 ta raqamni kesib oldim.
#13
taomlar =["Osh","Mastava","Shashlik",'qaymoq','saryoq']# taomlar ro'yxatini yaratdim.
nonushta = taomlar[:] # [:] yordamida nusxa oldik nonushta ro'yxatiga.
nonushta.remove("Osh")  ##  remove() funksiyasi elementni 
nonushta.remove("Mastava")## qiymati bo'yicha o'chiradi.
nonushta.remove("Shashlik")
print('Nonushta :',nonushta)
print('Taomlar:',taomlar)
#14
nonushta = tuple(nonushta) # tuple() funksiyasi o'zgarmas ro'yxat yaratadi.
nonushta.append("qaymoq")  # tuple o'zgarmas ro'yxat !!!!