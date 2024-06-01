# Görev:
#
# Python'da fonksiyonlar ve döngüler kavramlarını kullanarak, aşağıdaki işlemleri gerçekleştiren bir program yazmanız gerekmektedir:
#
# Noktaların Tanımlanması:
#
# ‘points’ adında bir liste oluşturun. Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir.
#
# Öklid Mesafesi İçin Bir Fonksiyon Yazma:
#
# ‘euclideanDistance’ adında bir fonksiyon tanımlayın. Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir.
#
# Mesafelerin Hesaplanması:
#
# Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. Bu mesafeleri ‘distances’ adında başka bir listede saklayın.
#
# Minimum Mesafenin Bulunması:
#
# ‘distances’ listesinden minimum mesafeyi bulun ve yazdırın.


points= (((1,2),(9,-5)),((6,19),(-10,-15)))

def euclideanDistance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

distances=[]
for i in points:
    distances.append(euclideanDistance(i[0],i[1]))


# min değeri bulma
min_distance = min(distances)
print(min_distance)

