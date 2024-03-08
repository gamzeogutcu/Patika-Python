def reverse(l):
    for i in range(len(l)):
        l.reverse()
        for sublist in l:
            sublist.reverse()
    return l
    
print(reverse([[1, 2], [3, 4], [5, 6, 7]]))