# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL :Eksekusi berurutan
print('hello world!')
print('by GUMI')
print('Tanggal 9 Juli 2020')

print('\n')
print('---' * 20)

# PERCABANGAN: Eksekusi terpilih
ingin_cepat = True
if ingin_cepat:
    print('jalur lurus aja ya!')
    print('nanti pasti cepat sampai')
else:
    print('jalan lain')
    print('nanti sampai, tapi mungkin lama karena jalan tidak lurus')

# PERULANGAN
print("\n")
print('-----' * 10)
jumlah_anak = 4

for urutan_anak in range(1, jumlah_anak+1): #jumlah perulangan = 5 -1 = 4
    print(f'kamu adalah anak ke-{urutan_anak} dari {jumlah_anak} anak')
