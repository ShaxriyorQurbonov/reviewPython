#1
# a = int(input("Son kiriting: "))
#
# if a % 2 != 0:
#     print(a + 1)
# else:
#     print(a)

# 2
# a = int(input("Son kiriting: "))
#
# if a % 2 != 0:
#     print(a + 1)
# else:
#     print(a - 2)

# 3
# a = int(input("Son kiriting: "))
#
# if a > 0:
#     print(a + 1)
# elif a < 0:
#     print(a - 2)
# else:
#     print(0)

# 4
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = int(input("Enter another number: "))
#
# musbat_sonlar = 0
#
# if a > 0:
#     musbat_sonlar += 1
# if b > 0:
#     musbat_sonlar += 1
# if c > 0:
#     musbat_sonlar += 1
#
# print("Musbat sonlar soni: ", musbat_sonlar)

# 5
# a = [1,5,-2,56,-5,45,12]
#
# musbat_sonlar = 0
# manfiy_sonlar = 0
#
# for i in a:
#     if i>0:
#         musbat_sonlar+=1
#     elif i<0:
#         manfiy_sonlar+=1
#     else:
#         print(0)
# print(f"musbat_sonlar soni: {musbat_sonlar} va manfiy_sonlar soni: {manfiy_sonlar}")

# 6
#
# a = list(map(int, input().split()))
#
# mus_son = 0
# man_son = 0
# nol = 0
#
# eng_kichik = a[0]
# eng_katta = a[0]
#
# for i in a:
#     if i > 0:
#         mus_son += 1
#     elif i < 0:
#         man_son += 1
#     else:
#         nol += 1
#     # a = a[1:]
#     # eng_katta = a[0]
#     # eng_kichik = a[0]
#
# print(f"Musbatlar: {mus_son},\n Manfiylar: {man_son},\n Nollar: {nol},\n ")

# data = input("Kiriting: ")
# while data != "chiqish":
#     print(data)
#     data = input("Kiriting: ")

while (data := input("Kiriting: ")) != "chiqish":
    print(data)


