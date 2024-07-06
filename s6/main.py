"""
Foydalanuvchi tomonidan faqat butun sonlardan iborat ro'yxat kiritilgan. 
Sizning vazifangiz ushbu ro'yxatda qo'shni bir xil ishorali elementlarni chiqarish. 
Agar qo'shni elementlarning ishoralari bir-biridan farqli bo'lsa, sonlar chiqarilmasin.
Har bir masala shartiga mos qo'shni elementlarni alohida qatorlarda chiqarilsin.

Eslatma:
Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo'yiladi.

Misollar:

Kiritish: [-1, 2, 3, -1, -2]
Chiqish:

diff
Copy code
2 3
-1 -2
Kiritish: [-1, 2, 3, -1, 4, 5, 6, 7]
Chiqish:

Copy code
2 3
4 5
5 6
6 7
"""

#code

def find_pairs(lst : list):

    lst2 = []
    
    for i in lst:
        for j in lst:
            if i > 0:
                if i+1 == j:
                    lst2.append([i,j])
            elif i < 0:
                if i-1 == j:
                    lst2.append([i,j])
    return lst2

#ishlatib ko`rishga osonroq bo`lishi uchun foydalanuvchidan olmadim
lst = [-1,2,3,-1,4,5,6,7]
lst = find_pairs(set(lst))

print("\n%20s\n"%('Neighbors'))

for i in lst:
    print(i)
print()