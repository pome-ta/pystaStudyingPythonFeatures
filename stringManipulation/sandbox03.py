ii = '\u3042'
ss = ii.encode('UTF-8')

a = 'あ'
#ab = a.encode('utf-8')
#ab = a.encode('utf_16_be')
#intab = int.from_bytes(ab, byteorder='big')

HEX_LETTERS = '0123456789abcdef'
s_num = '3042'
s_num = '1F914'

u = 0
st = ''
for s in s_num:
  i = HEX_LETTERS.find(s.lower())
  print(f'pre: {u}, {i}')
  u = u * 16 | i
  print(f'mdn: {u}')
print(chr(u))

if u < 0x80:
  st += chr(u)
elif u < 0x800:
  st += chr(0xc0 | (u >> 6))
  st += chr(0x80 + (u & 0x3f))
elif u < 0x10000:
  st += chr(0xe0 | (u >> 12))
  st += chr(0x80 | ((u >> 6) & 0x3f))
  st += chr(0x80 | (u & 0x3f))
elif u < 0x200000:
  st += chr(0xf0 | (u >> 18))
  st += chr(0x80 | ((u >> 12) & 0x3f))
  st += chr(0x80 | ((u >> 6) & 0x3f))
  st += chr(0x80 | (u & 0x3f))
elif u < 0x4000000:
  st += chr(0xf8 | (u >> 24))
  st += chr(0x80 | ((u >> 18) & 0x3f))
  st += chr(0x80 | ((u >> 12) & 0x3f))
  st += chr(0x80 | ((u >> 6) & 0x3f))
  st += chr(0x80 | (u & 0x3f))
else:
  st += chr(0xfc | (u >> 30))
  st += chr(0x80 | ((u >> 24) & 0x3f))
  st += chr(0x80 | ((u >> 18) & 0x3f))
  st += chr(0x80 | ((u >> 12) & 0x3f))
  st += chr(0x80 | ((u >> 6) & 0x3f))
  st += chr(0x80 | (u & 0x3f))

emoji = '🤔'
bemoji = emoji.encode('utf-8')

#print(chr(4036994196))

code = 0x1F600
#while code <= 0x1F64F:
while code <= 0x1F915:
  ch = chr(code)
  #print(ch,f':{code}', end='')
  code += 1
  if code % 0x10 == 0:
    pass
    #print()
