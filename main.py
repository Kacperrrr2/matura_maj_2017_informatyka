wiersze=open('przyklad.txt','r')
tablica=[]
for wiersz in wiersze:
    wiersz=wiersz.strip().split()
    for cos in wiersz:
        tablica.append(cos)
#6.1
# max=0
# min=100000000
# for tab in tablica:
#     if int(tab)>max:
#         max=int(tab)
#     if int(tab)<min:
#         min=int(tab)
# print(max)
# print(min)
#6.2
