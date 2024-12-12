import math

home_podezd = 5
home_flat = 20
home_etaz = 4

kvartira = 24

poisk_podezda = (kvartira-1) // 20 +1
poisk_etoza = (kvartira -1) % 20 // 4+1


print(poisk_podezda)
print(poisk_etoza)