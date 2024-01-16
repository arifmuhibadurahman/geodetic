import math as m

def dms_to_decimal(degrees, minutes, seconds):
    decimal_degrees = degrees + minutes / 60 + seconds / 3600
    return decimal_degrees

# Contoh penggunaan
degrees = 37
minutes = 45
seconds = 0
decimal_degrees = dms_to_decimal(degrees, minutes, seconds)
print(f"Sudut dalam bentuk desimal: {decimal_degrees} derajat")
#######################################################################
print("SOAL NO 1")
l = dms_to_decimal(7, 32, 28.3)
b = dms_to_decimal(110, 26, 45.7)
h = 2900
a = 6378137
b = 6356752.314245
print()
e = (a**2-b**2)/(a**2)
print("e",e)
print(e**2)
print(e**3)
print(e**4)
print(e**5)
print()
N = a/((m.sqrt((1-e**2*m.sin(l)**2)))**(1/2))
print("N = ", N)
#KONVERSI KOORDINAT GEODETIK KE KARTESI
Xq = (N+h)*m.cos(l)*m.cos(b)
Yq = (N+h)*m.cos(l)*m.sin(b)
Zq = (N*(1-e**2)+h)*m.sin(b)
print("X = ",Xq)
print("Y = ", Yq)
print("Z = ", Zq)
print()
print("SOAL NO 2 DENGAN KONSTANTA")
l1 = dms_to_decimal(30, 0, 0)
l2 = dms_to_decimal(30, 10, 0)
A = 1+(3/4)*(e**2)+(45/64)*(e**4)+(175/256)*(e**6)+(11025/16384)*(e**8)+(43659/65536)*(e**10)
B = (3/4)*(e**2)+(15/16)*(e**4)+(525/512)*(e**6)+(2205/2048)*(e**8)+(72765/65536)*(e**10)
C = (15/16)*(e**4)+(105/256)*(e**6)+(2205/2048)*(e**8)+(10395/16384)*(e**10)
D = (35/512)*(e**6)+(315/2048)*(e**8)+(31185/131072)*(e**10)
E = (315/16384)*(e**8)+(3465/65536)*(e**10)
F = (693/131072)*(e**10)
print("A = ", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)
print("E = ", E)
print("F = ", F)

#SM = a*(1-e**2)(A*(l2-l1)-(B/2*(m.sin(2*l2)))-(m.sin(2*l1))+C/4*(m.sin(4*l2))-(m.sin(4*l1))-D/6*(m.sin(6*l2))-(m.sin(6*l1))+E/8*(m.sin(8*l2))-(m.sin(8*l1))-F/10*(m.sin(10*l2))-(m.sin(10*l1)))
SM = a * (1 - e**2) * ((A * (l2)-l1) - (B / 2) * (m.sin(2 * l2)) - (m.sin(2 * l1)) + (C / 4) * (m.sin(4 * l2)) - (m.sin(4 * l1)) - (D / 6) * (m.sin(6 * l2)) - (m.sin(6 * l1)) + (E / 8) * (m.sin(8 * l2)) - (m.sin(8 * l1)) - (F / 10) * (m.sin(10 * l2)) - (m.sin(10 * l1)))
print("SM = ", SM)
print()
print("SOAL NO 2 TANPA KONSTANTA")
l1 = dms_to_decimal(89, 0, 0)
l2 = dms_to_decimal(90, 0, 0)
#beda lintang 
p = 180*60*60/3.14
dl = (l2-l1)/p
print("dl = ",dl)
#lintang rerata
lm = (l2+l1)/2
print("lm = ", lm)
#jari jari kelengkungam meridian rerata
M = a*((1-(e**2))/(1-(e**2)*m.sin(lm)**2)**(3/2))
print("M = ",M)
#rumus S
S = M*dl*(1+(1/8)*e**2*dl**2*m.cos(2*lm))
print("S =", S)







