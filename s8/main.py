"""
Faylda bir necha qatorlardan iborat IT kompaniya hodimlari to'g'risidagi ma'lumot yozilgan. 
Har bir qatorda IT kompaniya hodimining ismi, lavozimi, oyligi, oyligiga bonus summa va qaysi bo'limda ishlashi.
Ushbu ma'lumotlar ichidan bonuslari orasida musbat va manfiy qiymatlar mavjud. Kompaniyada yaxshi ishlaganlar bonusi musbat,
yomon ishlaganlar uchun manfiy qiymatlar bilan to'ldirilgan.
Sizning vazifangiz yaxshi ishlagan hodimlar ko'proq qaysi bo'limda ishlashini aniqlang. 
Agar shunday bo'limlar ko'p bo'lsa, hammasini chiqaring.

Eslatma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritsmsiz ishlangan misolga past ball qo'yiladi.
"""

#code

from collections import Counter

jarima = []
bonus = []

with open("hodimlar.txt") as f:

    while True:

        data = f.readline()
        if not data:
            print(f"\n{most_common_strings}\n")
            break

        data = data.split(" ")
        data[3] = int(data[3])

        if data[3] > 0:
            bonus.append((data[4]).replace("\n", ""))

        counted_strings = Counter(bonus)
        max_count = max(counted_strings.values())

        most_common_strings = [string for string, count in counted_strings.items() if count == max_count]



        



