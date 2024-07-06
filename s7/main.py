"""
Foydalanuvchi tomonidan Dictionaryga keyga ismlar va valuega esa Boolean type(1 yoki 0) kiritadi.
 Sizning vazifangiz eng ko'p ovoz berganlarning ismlarini chiqarish. Agar durang bo'lsa, ikkalisini ham chiqarish kerak. 
 Chiqishda birinchi qatorda qaysi qiymat ko'p ovoz berilganini va keying qatorda esa ismlarni chiqarish kerak.
   Ma'lumonada keltirilgandek bo'lishi kerak.

Esaltma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo'yiladi.

Misol:
Input:

python
Copy code
{'Anvar': 1, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}
Output:

Copy code
1
Anvar Lobar Vali Baxtiyor
Input:

python
Copy code
{'Anvar': 0, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}
Output:

Copy code
0
Surayyo Asror
1
Lobar Vali Baxtiyor
"""

#code

def find_zeros_and_ones(n):

    students = {} 

    i = 0
    while i < n:
        key = input("\nName:")
        value = int(input("0 or 1 >> "))
     
        if value != 1 and value != 0:
            print("Noto`g`ri tanlov!")
        else:
            students[key] = value
            i += 1
     

    zero_winners = []
    one_winners = []
    
    count_zero = 0
    count_ones = 0

#finding winners
    for key ,val in students.items():

        if val == 0:
            count_zero += 1 
            zero_winners.append(key)
        elif val == 1:
            count_ones += 1 
            one_winners.append(key)
            
  
    print("\n\nG`oliblar:")
    if count_zero > count_ones:
        print('\n0\n',zero_winners) 
        print()
      
    elif count_ones > count_zero:
        print('\n1\n',one_winners) 

    else: 
        print('\n0\n',zero_winners) 
        print('\n1\n',one_winners) 
    

#MAIN
n = int(input("Qatnashchilar soni:"))
find_zeros_and_ones(n)
