day=['понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
for i in range(len(day)):
    q=i+1
    if i==5 or i==6:
        print(day[i],' ',q,' ','выходной')
    else:
        print(day[i],' ',q)

