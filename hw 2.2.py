file = open('train.csv','r')
lines=list(file.readlines())
file.close()

all_count=0
female_count=0
male_count=0
f=[]
for i in range(1,len(lines)):
    f=lines[i].split(',')
    if f[1] == '1' and f[5] == 'male':
        male_count += 1
    if f[1] == '1' and f[5] == 'female':
        female_count += 1
all_count = male_count +female_count
print('Всего выжило: ', all_count )
print('Выжило женщин: ', female_count )
print('Выжило мужчин: ', male_count )