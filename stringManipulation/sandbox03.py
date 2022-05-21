ii = '\u3042'
ss = ii.encode('UTF-8')

a = 'あ'
#ab = a.encode('utf-8')
ab = a.encode('utf_16_be')
intab = int.from_bytes(ab, byteorder='big')


HEX_LETTERS = '0123456789abcdef'
s_num = '3042'

u = 0
for s in s_num:
  i = HEX_LETTERS.find(s)
  u = u * 16 | i

print(chr(u))


emoji = '🤔'
bemoji = emoji.encode('utf-8')
