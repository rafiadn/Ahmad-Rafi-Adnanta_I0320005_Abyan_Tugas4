a = 4
b = 11
print('a = 4')
print('b = 11')

print('biner dari', a, 'adalah =', format(a, '08b'))
print('biner dari', b, 'adalah =', format(b, '08b'))

# 4 | 11
print('a) 4 | 11')
c = a | b
print('biner dari', c, 'adalah =', format(c, '08b'))

# 4 >> 11
print('b) 4 >> 11')
d = a >> b
print('biner dari', d, 'adalah =', format(d, '08b'))

# 4 ^ 11
print('c) 4 ^ 11')
e = a ^ b
print('biner dari', e, 'adalah =', format(e, '08b'))

# ~4
print('d) ~4')
f = ~a
print('biner dari ', f, 'adalah =', format(f, '08b'))

# 11 & 4
print('e) 11 & 4')
g = b & a
print('biner dari', g, 'adalah =', format(g, '08b'))