print('\n------------------------------')
print('tipe data skalar => tipe data sederhana')
anak1 = 'gumi'
anak2 = 'gia'
anak3 = 'umar'
anak4 = 'usman'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\n------------------------------')
print('tipe data list/daftar/array')
anak = ['gumi', 'gia', 'umar', 'usman']
print(anak)
anak.append('uwais')
print('\ntambahkan anak ke-5}')
print(anak)

print('\n------------------------------')
print('sapa anak ke-2')
print(f'halo {anak[1]}!')

print('\n------------------------------')
print('sapa semua anak')
for a in (anak):
    print(f'Halo {a}!')

print('\n------------------------------')
print('sapa semua anak: cara ribet')
for a in range(0, len(anak)):
    print(f'{a + 1}. halo {anak[a]}')
