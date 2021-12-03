#nimed=["Anna","Inna"]
#for i in range(3):
#	nimi=input("Sisesta nimi - ")
#	nimed.append(nimi)
#print(nimed)
#nimed.sort(reverse=True)
#print(nimed)
#nimed.insert(1,input("Sisesta veel nimi - "))
#print(nimed)
#nimed.remove("Anna")
#print(nimed)
#nimed.pop(2)
#print(nimed)
#print(len(nimed))
#nimed.count(nimed[0])
#print(nimed)


#1 задание
#Maakonnad=["Tallinn", "Narva", "Kohtla-Järve","Narva-Jõesuu", "Ida-Virumaa", "Lääne-Virumaa", "Jõgevamaa", "Tartu linn Tartumaa", "Põlvamaa", "Võrumaa", "Valgamaa" "Viljandimaa","Järvamaa", "Harjumaa", "Raplamaa", "Pärnumaa", "Läänemaa", "Hiiumaa", "Saaremaa"]
#while 1:
#	try:
#		index=int(input("Введите индекс: "))
#		if 10000<=index<=999999:
#			break
#	except ValueError:
#		print("Неверный индекс!")
#index_1=index//10000
#print(Maakonnad[index_1-1])
#if index_1 in[1,2,3]:
#	print("Оставайтесь дома!")
#else:
#	print("Носите маски!")
#2 задание
#from random import *
#spisok=[]
#N=randint(2,20)
#for i in range(N):
#	spisok.append(randint(-50,50))
#print(spisok)
#while 1:
#	try:
#		k=int(input("С какой позиции начаинать - "))
#		if k<=N//2:
#			break
#	except ValueError:
#		print("Значение должно быть меньше, чем N//2")
#k-=1
#for i in range(k,-1,-1):
#	print(spisok[i-1],end=" <-> ")
#	print(spisok[N-i-1]) #print(spisok[-1*i])
#	a=spisok.pop(i)
#	spisok.insert(N-i-1-1,a)
#	a=spisok.pop(N-i-1)
#	spisok.insert(i,a)
#print(spisok)
#3 задание
#from random import *
#spisok=[]
#N=randint(2,20)
#for i in range(N):
#	spisok.append(randint(-50,50))
#print(spisok)
#while 1:
#	try:
#		k=int(input("С какой позиции начаинать - "))
#		if k<=N//2:
#			break
#	except ValueError:
#		print("Значение должно быть меньше, чем N//2")
#k-=1
#for i in range(k,-1,-1):
#	print(spisok[i-1],end=" <-> ")
#	print(spisok[N-i-1]) #print(spisok[-1*i])
#	a=spisok.pop(i)
#	spisok.insert(N-i-1-1,a)
#	a=spisok.pop(N-i-1)
#	spisok.insert(i,a)
#print(spisok)
#max=-50
#for element in spisok:
#	if element>max: max=element
#new_max=max/N #/len(spisok)
#ind=spisok.index(max)
#spisok.remove(max)
#spisok.insert(ind,new_max)
#print(spisok)

#4 задание
#from random import *
#spisok=[]
#N=randint(2,20)
#for i in range(N):
#	spisok.append(randint(-50,50))
#print(spisok)
#while 1:
#	try:
#		k=int(input("С какой позиции начаинать - "))
#		if k<=N//2:
#			break
#	except ValueError:
#		print("Значение должно быть меньше, чем N//2")
#k-=1
#for i in range(k,-1,-1):
#	print(spisok[i-1],end=" <-> ")
#	print(spisok[N-i-1]) #print(spisok[-1*i])
#	a=spisok.pop(i)
#	spisok.insert(N-i-1-1,a)
#	a=spisok.pop(N-i-1)
#	spisok.insert(i,a)
#print(spisok)
#max=-50
#for element in spisok:
#	if element>max: max=element
#new_max=max/N #/len(spisok)
#ind=spisok.index(max)
#spisok.remove(max)
#spisok.insert(ind,new_max)
#print(spisok)
#spisok2=[]
#for e in spisok:
#	spisok2.append(abs(e))
#print(spisok2.sort())
#print(spisok2.sort(reverse=True))


# 5 задание
#l=['крот', 'белка', 'выхухоль']
#nl=[]
#max=0
#for e in l:
#	x=len(e)
#	if x>max:
#		max=x
#for e in l:
#	nl.append(e.ljust(max,"_"))
#print(nl)

#from random import*
#s1=['крот', 'белка', 'выхухоль']
#s2=['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
#s3=['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
#ss=[s1,s2,s3]
#N=0
#while N<len(ss):
#	print(ss[N])
#	max=0
#	sN_=[]
#	for s in ss[N]:
#		pikkus=len(s)
#		if pikkus>max: max=pikkus
#	for s in ss[N]:
#		sN_.append(s.ljust(max,"_"))
#	print(sN_)
#	N+=1

# 6 задание
while 1:
	try:
		nimi=input("Ввеите своё имя - ")
		break
	except ValueError:
		print("Имена состоят только из букв!")
print("Добро пожаловать,",nimi.title())




#uksikud=[x for x in abc if abc.count(x)>=1]
#uksikud=list(set(uksikud))
#print(uksikud)