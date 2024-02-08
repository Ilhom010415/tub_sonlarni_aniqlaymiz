# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 05:47:31 2024

TUB SONLARNI ANIQLOVCHI DASTUR

@author: Rahmonov Ilhom
"""

# TUB SONLARNI ANIQLAYDI

son = int(input("Eng kichik qiymatni kiriting:\n >>> "))
max_qiymat = int(input("Eng katta qiymatni kiriting: >>> "))
sonlar = []
print(f"{son} dan {max_qiymat} gacha bo`lgan tub sonlar.\n({son} va {max_qiymat} kirmaydi)!")
if son < 2 and max_qiymat > 2:
    print(2)
if son < 3 and max_qiymat > 3:
    print(3)
if son < 5 and max_qiymat > 5:
    print(5)
if son < 7 and max_qiymat > 7:
    print(7)
while son<max_qiymat:
    son += 1
    if son % son != 0:
        continue
    if son % 2 == 0:   # 2dan yuqori barcha juft sonlar albatta 2 ga bo`linadi
        continue
    if son % 3 == 0:
        continue
    if son % 5 == 0:
        continue
    if son % 7 == 0:
        continue
    if son == 1:  # 1 tub son emas
        continue

    else:
        print(son)
        sonlar.append(son)
print(f"{len(sonlar)} ta tub son bor ekan!")
print("Dastur tugadi!")