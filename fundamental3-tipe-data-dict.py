"""
Tipe data dictionary sekedar menghubungkan KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {
    'anak': 'son',
    'istri': 'wife',
    'ayah': 'father',
    'ibu': 'mother'
}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\n------------------')
print('Data ini dikrimkan oleh server Gojek, untuk memberikan info dreiver disekitar pemakai aolikasi')
data_dari_server_gojek = {
    'tanggal' : '2020-07-12',
    'driver_list' : [
        {'nama': 'gumi', 'jarak': 10},
        {'nama': 'gia', 'jarak': 30},
        {'nama': 'umar', 'jarak': 100},
        {'nama': 'usman', 'jarak': 1000}
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"\nDriver ke-1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver ke-3 {data_dari_server_gojek['driver_list'][2]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
print(f"Driver dengan jarak terdekat bernama {data_dari_server_gojek['driver_list'][0]['nama']}")
print(f"Driver dengan jarak terjauh bernama {data_dari_server_gojek['driver_list'][3]['nama']}")