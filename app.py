# # tuple, list, while, match-case, enumerate(), filter(), lambda, map(), any() va all()
# print("Guruh qatnashchilari ro'yxati")
# talabalar=[]

# while True:
#     print("\n--- Talabalar Ilg'or Tahlil Tizimi ---")
#     print("1. Talaba va uning balini qo'shish")
#     print("2. Barcha talabalarni ko'rish")
#     print("3. Imtihondan o'tganlarni chiqarish")
#     print("4. Barcha ballarni +5 ga oshirish")
#     print("5. A'lochilar va yiqilganlarni chiqarish")
#     print("6. Talaba ismini update qilish")
#     print("7. Talaba balini update qilish")
#     print("8. Talaba ismi va balini update qilish")
#     print("9. Talabani delete qilish")
#     print("10. Dasturdan chiqish")

#     tanlov = input("1 dan 10 gacha sonlardan birini tanlang: ")
#     match tanlov:

#         case "1":
#             ism = input("Talaba ismini kiriting: ")
#             bal = int(input("Ballni kiriting: "))
#             talaba = (ism, bal)
#             talabalar.append(talaba)
#             print(f"{ism} - {bal} ro'yxatga qo'shildi!")

#         case "2":
#             if len(talabalar) == 0:
#                 print("Ro'yxat mavjud emas")
#             else:
#                 print("\nBarcha talabalar ro'yxati:")
#                 for son, (ism, bal) in enumerate(talabalar, start=1):
#                     print(f"{son}. {ism} - {bal}")

#         case "3":
#             if talabalar:
#                 print("\nImtihondan o'tgan talabalar:")
#                 natija = list(filter(lambda i: i[1] >= 60, talabalar))
#                 for son, (ism, bal) in enumerate(natija, start=1):
#                     print(f"{son}. {ism} - {bal}")
#             else:
#                 print("Hali talabalar qo'shilmagan!")

#         case "4":
#             if talabalar:
#                 talabalar = list( map(lambda i: (i[0], i[1]+5 ), talabalar) )
#                 print("\nBallar 5 ga oshirildi:")
#                 for son, (ism, bal) in enumerate(talabalar, start=1):
#                     print(f"{son}. {ism} - {bal}")
#             else:
#                 print("Hali talabalar qo'shilmagan!")

#         case "5":
#             if talabalar:
#                 print("\nBarcha talabalar 50 balldan yuqori olganmi?")
#                 print(all(bal >= 50 for ism, bal in talabalar))

#                 print("\nA'lochi bormi (90 va undan yuqori)?")
#                 print(any(bal >= 90 for ism, bal in talabalar))
#                 # print("bor" if alochi else "")
  
#                 print("\nA'lochilar:")
#                 alo = list(filter(lambda i: i[1] >= 90, talabalar))

#                 for ism, bal in alo:
#                     print(f"{ism} - {bal}")

#                 print("\nYiqilgan talabalar:")
#                 yiqilgan = list(filter(lambda i: i[1] < 60, talabalar))

#                 if yiqilgan:
#                     for ism, bal in yiqilgan:
#                         print(f"{ism} - {bal}")
#                 else:
#                     print("Yiqilgan talabalar yo'q!")
#             else:
#                 print("Hali talabalar qo'shilmagan!")

#         case "6":
#             eski_ism = input("O'zgartiriladigan talaba ismi: ")

#             for son, (ism, bal) in enumerate(talabalar):
#                 if ism.lower() == eski_ism.lower():
#                     yangi_ism = input("Yangi ismni kiriting: ")
#                     talabalar[son] = (yangi_ism, bal)
#                     print("Talaba ismi yangilandi!")
#                     break
#             else:
#                 print("Talaba topilmadi!")

#         case "7":
#             ism = input("Ballini o'zgartirmoqchi bo'lgan talaba: ")

#             for son, (nom, bal) in enumerate(talabalar):
#                 if nom.lower() == ism.lower():
#                     yangi_bal = int(input("Yangi ballni kiriting: "))
#                     talabalar[son] = (nom, yangi_bal)
#                     print("Talaba bali yangilandi!")
#                     break
#             else:
#                 print("Talaba topilmadi!")

#         case "8":
#             ism = input("O'zgartiriladigan talaba ismi: ")

#             for son, (nom, bal) in enumerate(talabalar):
#                if nom.lower() == ism.lower():
#                     yangi_ism = input("Yangi ismni kiriting: ")
#                     yangi_bal = int(input("Yangi ballni kiriting: "))

#                     talabalar[son] = (yangi_ism, yangi_bal)

#                     print("Talaba ismi va bali yangilandi!")
#                     break
#                else:
#                     print("Talaba topilmadi!")

#         case "9":
#             ism = input("O'chiriladigan talaba ismi: ")

#             for son, (nom, bal) in enumerate(talabalar):
#                 if nom.lower() == ism.lower():
#                     talabalar.pop(son)
#                     print(f"{nom} ro'yxatdan o'chirildi!")
#                     break
#             else:
#                 print("Talaba topilmadi!")

#         case "10":
#             print("Dasturdan chiqdingiz!")
#             break

#         case _:
#             print("Noto'g'ri tanlov! 1 dan 10 gacha son kiriting!")



# ---------------------------------------------------------------------------------------------------------


# list, append(), pop(), enumerate() va len()

# qatnashuvchi=[]
# print("Guruh qatnashhilari r'yxati")
# while True:
#     print("\nAsosiy menu: ")
#     print("1.Yangi qatnashchi qo'shish")
#     print("2.Ro'yxatni ko'rish ")
#     print("3.Delete qilish")
#     print("4.Dasturdan chiqish")
    
#     tanlov = input("1,2,3,4 sonlaridan birini tanlang:  ")

#     if tanlov == "1":
#         ism = input("Qatnashchi ismini kiriting: ")
#         qatnashuvchi.append(ism)
#         print(ism, "ro'yxatga qo'shildi!")
#     elif tanlov == "2":
#         if len(qatnashuvchi) == 0:
#             print("Ro'yxat mavjud emas")
#         else:
#             print("\nGuruh qatnashchilari:")
#             for son, ism in enumerate(qatnashuvchi, start=1):
#                 print(f"{son}. {ism}")
#     elif tanlov == "3":
#         if qatnashuvchi:
#             print("\nGuruh qatnashchilari:")
#             for son, ism in enumerate(qatnashuvchi, start=1):
#                 print(f"{son}. {ism}")

#             ochirish = int(input("O'chirmoqchi bo'lgan qatnashchi raqamini kiriting: "))

#             if 1 <= ochirish <= len(qatnashuvchi):
#                 ism = qatnashuvchi.pop(ochirish - 1)
#                 print(ism, "ro'yxatdan o'chirildi!")
#             else:
#                 print("Bunday raqam mavjud emas!")
#         else:
#             print("Guruh mavjud emas!")

#     elif tanlov == "4":
#         print("Dasturdan chiqdingiz!")
#         break
#     else:
#         print(" 1, 2 yoki 3 ni kiriting.")




# -------------------------------------------------------------------------------------------------

# talabalar = [
#     ("Ali", 85),
#     ("Husan", 45),
#     ("Zuhra", 92),
#     ("Fotima", 64)
# ]

# def talabalarni_korish(students):
#     if students:
#         for i, (ism, bal) in enumerate(students, start=1):
#             print(f"{i}. {ism} - {bal}")
#     else:
#         print("Talaba mavjud emas!")


# def filter_students():
#     if talabalar:
#         otganlar=list(filter(lambda x:x[1]>=60,talabalar))
#         if otganlar:
#             talabalarni_korish(otganlar)
#         else:
#             print("o'tgan talaba yoq")
#     else: 
#         print("talabalar mavjud emas ")
        
        
# def balarni_oshirish():
#     if talabalar:
#         new_talabalar = list(map(lambda x: (x[0], x[1] + 5), talabalar))
#         talabalarni_korish(new_talabalar)
#     else:
#         print("talaba mavjud emas")
           
 
# def alochi_talabalar():
#     alochi = any(bal >= 90 for ism, bal in talabalar)
#     print("alochi bor" if alochi else "alochi yo'q")


# def xammasi_utgan():    
#     all_passed = all(bal > 50 for ism, bal in talabalar)
#     print("barchasi o'tgan" if all_passed else "barchasi o'tolmagan")
  
# def update_student(index,yangi_nom,yangi_bal):
    
#     yangi_talabalar = []
#     for i, (ism, bal) in enumerate(talabalar):
#         talaba = []
#         if i == index-1:
#            talaba.append(yangi_nom or ism)
#            talaba.append(yangi_bal or bal)
#         else:
#             talaba.append(ism)
#             talaba.append(bal)
#         yangi_talabalar.append(tuple(talaba))
    
#     talabalarni_korish(yangi_talabalar)
    
          
            
# while True:
#     print("<----------------------------------------------------->")
#     print("1. Talaba va uning balini qo'shish")
#     print("2. Barcha talabalarni ko'rish (enumerate va unpacking)")
#     print("3. Imtihondan o'tganlarni filtrlash (filter va lambda) bal>=60")
#     print("4. Ballarni  +5 ga oshirish (map va lambda) yordamida")
#     print("5. Shartlarni tekshirish (any va all yordamida) alochi,yiqilgan talabalarni chiqarish")
#     print("6.Talabani update qilish")
#     print("7.Talaba balini update qilish")
#     print("8.Talaba va balini bir vaqtda update qilish")
#     print("9.talabani delete qilish")
#     print("10. Dasturdan chiqish")
#     print("<----------------------------------------------------->")
#     tanlov = int(input("buyruqni tanla: "))

#     match tanlov:
#         case 1:
#             ism = input("ism kiriting: ")
#             ball = int(input("ball kiriting: "))
#             talaba = (ism, ball)
#             talabalar.append(talaba)
#             print(f"{ism} - {ball} balli talaba qo'shildi")
#         case 2:
#             talabalarni_korish(talabalar)
#         case 3:
#             filter_students()
#         case 4:
#             balarni_oshirish()
#         case 5:
#             alochi_talabalar()
#             xammasi_utgan()
#         case 6:
#             print("ozgartirmoqchi bolgan talabani tanla")
#             talabalarni_korish(talabalar)
#             index = int(input("talabani tanla: "))
#             yangi_nom = input("talaba nomini kirit: ")
#             update_student(index,yangi_nom,None)
#         case 7:
#             print("ozgartirmoqchi bolgan talabani tanla")
#             talabalarni_korish(talabalar)
#             index = int(input("talabani tanla: "))
#             yangi_bal = int(input("talaba nomini kirit: "))
#             update_student(index,None,yangi_bal)
#         case 8:
#             print("ozgartirmoqchi bolgan talabani tanla")
#             talabalarni_korish(talabalar)
#             index = int(input("talabani tanla: "))
#             yangi_nom = input("talaba nomini kirit: ")
#             yangi_bal = int(input("talaba balini kirit: "))
#             update_student(index,yangi_nom,yangi_bal)
#         case 9:
#             print("O'chirmoqchi bo'lgan talabani tanla!")
#             talabalarni_korish(talabalar)
#             index = int(input("Talabani tanla: "))
#             del talabalar[index-1]
#             talabalarni_korish(talabalar)
#         case 10:
#             print("Dasturdan chiqildi!")
#             break
#         case _:
#             print("Xato buyruq kiritildi!")



# ---------------------------------------------------------------------------------------------------


# while True:
#     print("== == = UNIVERSITET TIZIMI == == =")
#     print("1. Talabalarni ko'rish")
#     print("2. Yangi talaba qo'shish")
#     print("3. O'rtacha bahoni hisoblash")
#     print("4. Davomatni tekshirish (10 dan katta bo'lsa 'Pass', aks holda 'Fail')")
#     print("5. Eng yaxshi talabani aniqlash (eng yuqori bahoga ega bo'lgan talabani topish)")
#     print("0. Dasturni tugatish")

#     choice = input("Tanlovingizni kiriting: ")

#     match choice:
#         case "1":
#             # Talabalarni ko'rish
#             pass
#         case "2":
#             # Yangi talaba qo'shish
#             pass
#         case "3":
#             # O'rtacha bahoni hisoblash
#             pass
#         case "4":
#             # Davomatni tekshirish
#             pass
#         case "5":
#             # Eng yaxshi talabani aniqlash
#             pass
#         case "0":
#             print("Dastur tugatildi.")
#             break
#         case _:
#             print("Noto'g'ri tanlov, iltimos qayta urinib ko'ring.")

from datetime import datetime
  
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
def now_text():
       return datetime.now().strftime(DATE_FORMAT)


def parse_time(value):
        if isinstance(value, datetime):
            return value
        if not value:
            return None
        try:
            return datetime.strptime(str(value), DATE_FORMAT)
        except ValueError:
            return None



class Custumer:
    def __init__(self, id, name, phone, service_type, arrival_type=None, status=None, start_type=None, end_type=None ):
        self.id=id
        self.name=name
        self.phone=phone
        self.service_type=service_type
        self.arrival_type=arrival_type 
        self.status=status
        self.start_type=start_type
        self.end_type=end_type
        




class Navbat:
    def __init__(self):
        self.customers=[]

    # def generate_id(self):
    #   return f"A{len(self.customers)+1:03d}"

    def generate_id(self):
        numbers = []
        for customer in self.customers:
            try:
                numbers.append(customer.id) 

            except(ValueError, IndentationError):
               pass
            return f"A{len(numbers)+1:03d}"

    def add_customers(self):
        name = input("Ism kiriting: ").strip()
        phone = input("telefon raqamingizni kiriting: ").strip()
        service = input("Xizmat turini kiriting: ").strip()

        
        yangi=(self.generate_id(), name,phone,service)
        self.customers.append(yangi)
        print(f"{yangi[0]}. {name}-{phone}-{service} muvaffaqqiyatli qo'shildi")

     
   


   

    def call_next(self):
        serving = next(c for c in self.customers if c.status == "serving")
        if serving:
            print(f"Avval {serving.id} li mijoz bilan suhbatni tugating")
            return
        
        waiting = sorted(c for c in self.customers if c.status == "waiting"),
        key=lambda c:(parse_time(c.arrival_time))

        if not waiting:
            print("Navbatdagi mijoz yoq")

        custumer = waiting[0]
        custumer.status = "servising"
        custumer.status_time = now_text()
        print(f"Keyingi mijoz: {custumer.id}")  | {custumer.name} | {custumer.service_type}
        
navbat=Navbat()       

        

while True:
    print("\n===== SMART QUEUE MANAGEMENT SYSTEM =====")
    print("1. Yangi mijoz qo'shish")
    print("2. Keyingi mijozni chaqirish")
    print("3. Navbatdagi mijozlarni ko'rish")
    print("4. Mijozni navbatdan bekor qilish")
    print("5. Mijozni qidirish")
    print("6. Xizmat ko'rsatish tarixini ko'rish")
    print("7. Statistikani ko'rish")
    print("8. Excel faylga eksport qilish")
    print("0. Chiqish")

    tanlov = int(input("Tanlovingiz: "))

    if tanlov==1:
       navbat.add_customers()

    elif tanlov == 2:
        navbat.call_next()
    else:
        print("xato")
      