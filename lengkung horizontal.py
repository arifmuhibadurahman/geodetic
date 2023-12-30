import math

phi = 3.14
PI = 241
print("PI", PI)
HZ = 100
print("HZ", HZ)
DEFLEKSI = 180 - HZ
print("DEFLEKSI", DEFLEKSI)
R = 25
print()
T = R*math.tan(math.radians(DEFLEKSI/2))
print("T",T)
'''
F = math.tan(math.radians(90))
print("F",F)
print(F)
print(round(F,2))
g = round(2.7909, 2)
print(g)
'''
BC = PI - T
print("BC",BC)
L = 2*phi*R*DEFLEKSI/360
print("L",L)
EC = BC + L
print("EC",EC)
print()
BC_ATAS = 125
panjangbusurBC = BC_ATAS - BC
DEFLEKSI2 = (DEFLEKSI/2)/L*panjangbusurBC
print("DEFLEKSI2",DEFLEKSI2)
TALI_BUSUR = 2*R*math.sin(DEFLEKSI2)
print("TALI_BUSUR2", TALI_BUSUR)
print()
EC_BAWAH = 125
panjangbusurEC = EC_BAWAH - EC
DEFLEKSI3 = (DEFLEKSI/2)/L*panjangbusurEC
print("DEFLEKSI3",DEFLEKSI3)
TALI_BUSUR = 2*R*math.sin(DEFLEKSI3)
print("TALI_BUSUR3", TALI_BUSUR)
'''
POSISI_BC_ASLI = BC
POSISI_BC_ATAS = 140
panjang_busur = POSISI_BC_ATAS - POSISI_BC_ASLI
DEFLEKSI2 = (DEFLEKSI/2)/L*panjang_busur
print("DEFLEKSI2",DEFLEKSI2)
TALI_BUSUR = 2*R*math.sin(DEFLEKSI2)
print("TALI_BUSUR", TALI_BUSUR)
'''