import csv

a = [[1, 2], [1, 2]]

alphabet = 'abcdefghijklmnopqrstuvwxyz'

cyphertext = (input('Cyphertext: ')).lower()
cyphertext_clean = ''

for letter in cyphertext:
    if letter != ' ':
        cyphertext_clean = cyphertext_clean + letter
    else:
        continue

cyphertext_clean = cyphertext_clean + 'XXXXXXXX'
        

while True:
    length = int(input('Length: '))
    for i in range(1, length+1):
        column_max_width = i
        rows = []
        current_row = []
        column = 0
        for letter in cyphertext_clean:
            if column < column_max_width:
                current_row.append(letter)
                column += 1
            else:
                rows.append(current_row)
                current_row = [letter]
                column = 1

    for i in rows:
        print(i[0])


    with open('out.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
