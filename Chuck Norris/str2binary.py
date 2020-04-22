message = input()
message_bin = ''.join(format(ord(i), 'b').zfill(7) for i in message)
code = ('00 ', '0 ')
char_b = 2
for i, char in enumerate(message_bin):
    if char != char_b:
        if i != 0:
            print(' ', end='')
        print(code[int(char)], end='')
    print('0', end='')
    char_b = char
