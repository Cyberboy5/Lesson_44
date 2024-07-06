"""
Tasavvur qiling-a, sizda berilgan naqshga muvofiq turli xil ranglar bilan to'ldirilishingiz kerak bo'lgan kvadratchalar qatori bor.
 Kvadratchalarni ketma-ket bo'yash kerak, ya'ni keyingi kvadrat boshqa rangda bo'lsa, qalamni o'zgartirishingiz kerak bo'ladi.

Eslatma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo'yiladi.

Ranglar ro'yxatini oladigan va butun naqshni to'ldirish uchun zarur bo'lgan vaqtning qiymatini 
(soniyalarda) qaytaradigan funksiyani yozing.
"""
# Note:Tekshirish Osonroq bolish uchun foydalanuvchidan olmadim

#code

#case2
# colors = ["Red","Blue","Red","Blue","Red"]
# colors = ["Red"]
# colors = ["Red","Yellow","Green","Blue"]
colors = ["Blue","Blue","Blue","Red","Red","Red"]

sekund = 0
color  = colors[0]

for i in colors:
    sekund += 2
    if color != i:
        sekund += 1 
    color = i

print(f"\nSecond:{sekund}\n")