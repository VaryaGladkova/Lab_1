import csv
import random

count = 0
with open('books.csv') as csvfile:
    books = csv.reader(csvfile, delimiter = ';')
    title = csvfile.readline()
    for row in books:
        count += 1

print(f'Количество записей: {count}')

count_30 = 0
with open ('books.csv') as csvfile:
    books = csv.reader(csvfile, delimiter = ';')
    title = csvfile.readline()
    for row in books:
        if len(row[1]) > 30:
            count_30 += 1

print(f'Количество записей, c НАЗВАНИЕ строка длиннее 30 символов: {count_30}')

flag = 0
search = input('Search for: ')
with open ('books.csv') as csvfile:
    books = csv.reader(csvfile, delimiter = ';')
    title = csvfile.readline()
    for row in books:

        lower_znach = row[3].lower()
        index = row[3].find(search)
        if index != -1 and (str(row[6])[6:10] == "2014" or "2016" or "2017"):
            flag = 1
            print(row)
    if flag == 0:
        print('Nothing found')


books_new = []
with open ('books.csv') as csvfile:
    books = csv.reader(csvfile, delimiter = ';')
    title = csvfile.readline()
    f = open('generator.txt', 'w')
    for row in books:
        books_new.append(row[3] + '. ' + row[1] + ' - ' + row[6])

for i in range (1, 21):
    f.write(str(i) + ' ' + random.choice(books_new) + '\n')