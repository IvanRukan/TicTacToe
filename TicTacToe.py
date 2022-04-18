user_input = '_________'
a = user_input[0]
b = user_input[1]
c = user_input[2]
d = user_input[3]
e = user_input[4]
f = user_input[5]
g = user_input[6]
z = user_input[7]
h = user_input[8]
banned = ['4','5','6','7','8','9','0']
result = user_input
print('---------')
print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
print('---------')
win1 = 'XXX'
win2 = 'OOO'
lol = ''
while ((a + b + c != win1) or (a + b + c != win2) or (d + e + f != win1) or (d + e + f != win2) or (g + z + h != win1) or (g + z + h != win2) or (a + d + g != win1) or (a + d + g != win2) or (b + e + z != win1) or (b + e + z != win2) or (c + f + h != win1) or (c + f + h != win2) or (a + e + h != win1) or (a + e + h != win2) or (c + e + g != win1) or (c + e + g != win2)) and '_' in user_input :
    while result.count('X') <= user_input.count('X') and '_' in user_input:
        user_coordinates = input('Enter coordinates: ').split()
        co1 = user_coordinates[0]
        co2= user_coordinates[1]
        if (co1 == '1' and co2 == '1') or (co1 == '1' and co2 == '2') or (co1 == '1' and co2 == '3') or (co1 == '2' and co2 == '1') or (co1 == '2' and co2 == '2') or (co1 == '2' and co2 == '3') or (co1 == '3' and co2 == '1') or (co1 == '3' and co2 == '2') or (co1 == '3' and co2 == '3'):
            if (co1 == '1' and co2 == '1') and a != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '1' and co2 == '1') and a == '_':
                a = 'X'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '1' and co2 == '2') and b != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '1' and co2 == '2') and b == '_':
                b = 'X'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '1' and co2 == '3') and c != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '1' and co2 == '3') and c == '_':
                c = 'X'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '2' and co2 == '1') and d != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '2' and co2 == '1') and d == '_':
                d = 'X'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '2' and co2 == '2') and e != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '2' and co2 == '2') and e == '_':
                e = 'X'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '2' and co2 == '3') and f != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '2' and co2 == '3') and f == '_':
                f = 'X'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '3' and co2 == '1') and g != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '3' and co2 == '1') and g == '_':
                g = 'X'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '3' and co2 == '2') and z != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '3' and co2 == '2') and z == '_':
                z = 'X'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '3' and co2 == '3') and h != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '3' and co2 == '3') and h == '_':
                h = 'X'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
        elif co1 in banned or co2 in banned:
            print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')
    user_input = result
    if (a + b + c == win1) or (d + e + f == win1) or (g + z + h == win1) or (a + d + g == win1) or (b + e + z == win1) or (c + f + h == win1) or (a + e + h == win1) or (c + e + g == win1):
        print('X wins')
        lol = 1
        break
    while result.count('O') <= user_input.count('O') and '_' in user_input:
        user_coordinates = input('Enter coordinates: ').split()
        co1 = user_coordinates[0]
        co2= user_coordinates[1]
        if (co1 == '1' and co2 == '1') or (co1 == '1' and co2 == '2') or (co1 == '1' and co2 == '3') or (co1 == '2' and co2 == '1') or (co1 == '2' and co2 == '2') or (co1 == '2' and co2 == '3') or (co1 == '3' and co2 == '1') or (co1 == '3' and co2 == '2') or (co1 == '3' and co2 == '3'):
            if (co1 == '1' and co2 == '1') and a != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '1' and co2 == '1') and a == '_':
                a = 'O'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '1' and co2 == '2') and b != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '1' and co2 == '2') and b == '_':
                b = 'O'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '1' and co2 == '3') and c != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '1' and co2 == '3') and c == '_':
                c = 'O'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '2' and co2 == '1') and d != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '2' and co2 == '1') and d == '_':
                d = 'O'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '2' and co2 == '2') and e != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '2' and co2 == '2') and e == '_':
                e = 'O'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '2' and co2 == '3') and f != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '2' and co2 == '3') and f == '_':
                f = 'O'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '3' and co2 == '1') and g != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '3' and co2 == '1') and g == '_':
                g = 'O'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '3' and co2 == '2') and z != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '3' and co2 == '2') and z == '_':
                z = 'O'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
            if (co1 == '3' and co2 == '3') and h != '_':
                print('This cell is occupied! Choose another one!')
            elif (co1 == '3' and co2 == '3') and h == '_':
                h = 'O'
                result = a + b + c + d + e + f + g + z + h
                print('---------')
                print('|' + ' ' + a + ' ' + b + ' ' + c + ' ' +'|')
                print('|' + ' ' + d + ' ' + e + ' ' + f + ' ' +'|')
                print('|' + ' ' + g + ' ' + z + ' ' + h + ' ' +'|')
                print('---------')
        elif co1 in banned or co2 in banned:
            print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')
    user_input = result
    if (a + b + c == win2) or (d + e + f == win2) or (g + z + h == win2) or (a + d + g == win2) or (b + e + z == win2) or (c + f + h == win2) or (a + e + h == win2) or (c + e + g == win2):
        print('O wins')
        lol = 1
        break
if result.count('_') == 0 and lol != 1:
    print('Draw')

