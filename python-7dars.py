#07 LIST (RO'YXAT)
# mevalar = ['olma', 'nok','banan','anjir']#mevalar ro'yxati
# narxlar = [1200,1400,200,300]# narxlar ro'yxati
# sonlar = ['bir','ikki',3,4,5]#sonlar ro'yxati
# ismlar = []# bo'sh ro'yxat
# print(mevalar)
# print('Birinchi meva :',mevalar[0])
# print('Ikkinchi meva:',mevalar[1])
#Agar list ichidagi element string bo'lsa ularga string metodini qo'llash mumkin.
# mevalar = ['olma', 'nok','banan','anjir']#mevalar ro'yxati
# print('Birinchi meva :',mevalar[0].upper())
# print('Ikkinchi meva :',mevalar[1].title())
#LIST ustida arifmetik amallar.
# narxlar = [1200,300,400,5000]
# print(narxlar[-1]-narxlar[2])
 #PYTHONDA list oxiriga -1 indeksi orqali murojat qilish mumkin.
# car_models = ['Tesla','Kia','Audi',"Bmw","Volvo"]
# print(car_models[-1])# Listning eng oxirgi elementini chaqirish uchun -1 foydalanamiz.
   
    #ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH.
    #01 Elementni o'zgartirish .
# narxlar = [1200,300,500,6000]    
# narxlar[0] = 200# 1-qiymatini 200 ga o'zgardi.
# narxlar[2] = 1000#  3-qiymati 1000 ga o'zgardi.
# print(narxlar)
    #Yangi element qo'shish .
# mevalar = ['olma','anjir','nok','apilsin']  
# mevalar.append('mandarin')# Mevalarga mandarin qo'shdim.
# print(mevalar)  # append() metodi royxat oxiriga element qo'shadi. 
  # append() metodi bo'sh ro'yxat to'ldirishda juda qulay.
# cars = []# bo'sh ro'yxat yaratdik
# cars.append('Nexia')# ro'yxatga Nexia mashinasini qo'shdim.
# cars.append('Volvo')# ro'yxatga Volvo mashinasini qo'shdim.
# print(cars)    
      # INSERT metodi 
# cars = ['Bmv','Audi','Tesla']   
# cars.insert(0,'Volvo')  #1-o'ringa Volvo mashinasini qo'shdim.
# print(cars) 
     #ELEMENTNI O'CHIRISH .
# mevalar = ['olma','anjir','nok']
# del mevalar[1] # 2-elementni o'chirib tashlaydi.
# print(mevalar)
# mevalar = ['olma','anjir','nok']
# mevalar.remove('nok')#remove() metodi ro'yxatdagi elementni qiymati bo'yicha o'chiradi.
# hayvonlar = ['mushuk','sigir','ot,''mushuk']# hayvonlar ro'yxatini yaratdim.
# hayvonlar.remove('mushuk') # remove() metodi ro'yxatda kelgan 1-chi elementni o'chiradi.
        #ELEMENTNI SUG'IRIB OLISH.pop(indeks metoidan foyalanamiz.)
# bozorlik = ['go\'sht','kartoshka','un','piyoz']  
# mahsulot = bozorlik.pop(-1)# Ro'yxatdan piyozni sug'irib oldim.
# print('Men bozordan ' + mahsulot + " sotib oldim.")
# print('Olinmagan mahsulotlar: ', bozorlik )
       
         #AMALYOT
#01 
ismlar = ['Muslima','Behruzbek','Ozodbek']    #ismlar degan ro'yxat yaratdim.
print("Salom yaxshmisan" ,ismlar[0]) 
print("Bugun maktabga borasanmi?",ismlar[1])
print('Salom qalay',ismlar[2],'ishlar yaxshimi?')  
#02
sonlar = [5,6,-8,-9,0.5,0.2]#sonlar degan ro'yxar yarardim va ichiga butun son o'lik sonlarni kirirdim.
#03 
print(sonlar[0]+sonlar[2])
print(sonlar[-1]/sonlar[1])   
print(sonlar[2]*sonlar[3])
#04 
t_shaxslar = ['Amur Temur','Mirzo Ulug\'bek',"Jalolidin Manguberdi"] # t_shaxslar degan ro'yxat tuzdim. 
z_shaxslar = ['Ilon mask','Komiljon Hamidjonov',"Davronbek Turdivey"] # z_shaxslar degan ro'xat tuzdim.
#04
t_shaxs = t_shaxslar.pop(0) # t_shaxslar ro'yxatidan Amur Temur elementini sug'urib oldim.
z_shaxs = z_shaxslar.pop(1) # z_shaxslar ro'yxatidan Komiljon Hamidjonov ni elementini sug'urib oldim.
print('Men tarixiy shaxslardan',t_shaxs," zamonaviy shaxslardan suhbat qilishni hohlardim.")
#05 
friends = []
friends.append("Muslima")
friends.append("Behruzbek")
friends.append("Ozodbek")
friends.append("Bahtiniso")
friends.append("Bilolbek")
print(friends)
#06
#Kela olmaydigan mehmonlar ro'yxati.
friends.remove("Ozodbek")
friends.remove('Bilolbek')
print(friends)
#07
friends[1]="Muslim"
friends[-1]="Jony"
#07
mehmonlar =[]
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(-1))
print(friends)

