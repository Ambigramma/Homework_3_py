word = list(input().upper())

count = 0

score_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']

score_2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']

score_3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']

score_4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']

score_5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']

score_8 = ['J', 'X', 'Ш', 'Э', 'Ю']

score_10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

for i in word:
    if i in score_1:
        count+=1
    elif i in score_2:
        count+=2
    elif i in score_3:
        count+=3
    elif i in score_4:
        count+=4
    elif i in score_5:
        count+=5
    elif i in score_8:
        count+=8
    elif i in score_10:
        count+=10
print(count)