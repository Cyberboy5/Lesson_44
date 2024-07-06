"""
My_sort nomli funksiya yarating va ushbu funksiya parametri sifatida faqat butun sonlardan iborat List ma'lumotlari beriladi.
 Sizning vazifangiz bu funksiyaga qiymat qaytarish sifatida Listning har bir elementlarining raqamlar yig'indisi 
 bo'yicha o'sish tartibida saralash kerak. Foydalanuvchi List elementlariga faqat musbat sonlar kirita oladi va
   shuni shartini ham exception orqali tekshirib oling

"""



#case1
# sorting = ([14,30,103])

#case2
sorting = ([5,31,123,80,11])

dct  = {}

for i in sorting:
    i = str(i)
    total = 0 
    for j in i:
        total += int(j)
    dct[i] = total

lst = [val for val in dct.values()]
lst.sort()


sorted_lst = [int(key) for num in lst for key,val in dct.items() if val == num]

print(f"\nOrginal List:{sorting}")
print(f"Sorted List:{sorted_lst}\n")





