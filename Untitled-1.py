def reverse(e):
    a= e.split()
    i=len(a)-1
    chaine=""
    while i>= 0:
        if i== len(a)-1 :
            chaine += a[i]
        else:
            chaine +=" "+ a[i]
        i-=1
    return chaine




print(reverse('j\'ai peur du froid'))