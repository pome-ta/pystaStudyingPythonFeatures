ii = '\u3042'
ss = ii.encode('UTF-8')

a = 'あ'
#ab = a.encode('utf-8')
ab = a.encode('utf_16_be')
intab = int.from_bytes(ab, byteorder='big')


HEX_LETTERS = '0123456789abcdef'
s_num = '3042'
#s_num = '1F914'

u = 0
s = ''
for s in s_num:
  i = HEX_LETTERS.find(s)
  u = u * 16 | i
  print(chr(u))
if u < 0x80:
  s += chr(u)
elif u < 0x800:
  s += chr(0xc0 | (u >> 6))
  s += chr(0x80 + (u & 0x3f))
elif u < 0x10000:
  s += chr(0xe0 | (u >> 12))
  s += chr(0x80 | ((u >> 6) & 0x3f))
  s += chr(0x80 | (u & 0x3f))
elif u < 0x200000:
  s += chr(0xf0 | (u >> 18))
  s += chr(0x80 | ((u >> 12) & 0x3f))
  s += chr(0x80 | ((u >> 6) & 0x3f))
  s += chr(0x80 | (u & 0x3f))
elif u < 0x4000000:
  s += chr(0xf8 | (u >> 24))
  s += chr(0x80 | ((u >> 18) & 0x3f))
  s += chr(0x80 | ((u >> 12) & 0x3f))
  s += chr(0x80 | ((u >> 6) & 0x3f))
  s += chr(0x80 | (u & 0x3f))
else:
  s += chr(0xfc | (u >> 30))
  s += chr(0x80 | ((u >> 24) & 0x3f))
  s += chr(0x80 | ((u >> 18) & 0x3f))
  s += chr(0x80 | ((u >> 12) & 0x3f))
  s += chr(0x80 | ((u >> 6) & 0x3f))
  s += chr(0x80 | (u & 0x3f))




emoji = '🤔'
bemoji = emoji.encode('utf-8')
