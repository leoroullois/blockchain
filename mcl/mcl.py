import sys
sys.path.insert(1, "/lib/mcl-python/")

from mcl import GT
from mcl import G2
from mcl import G1
from mcl import Fr

import time

G1_STR = b"1 3685416753713387016781088315183077757961620795782546409894578378688607592378376318836054947676345821548104185464507 1339506544944476473020471379941921221584933875938349620426543736416511423956333506472724655353366534992391756441569"
G2_STR = b"1 352701069587466618187139116011060144890029952792775240219908644239793785735715026873347600343865175952761926303160 3059144344244213709971259814753781636986470325476647558659373206291635324768958432433509563104347017837885763365758 1985150602287291935568054521177171638300868978215655730859378665066344726373823718423869104263333984641494340347905 927553665492332455747201965776037880757740193453592970025027978793976877002675564980949289727957565575433344219582"

a = Fr()
b = Fr()
c = Fr()
d = Fr()
e = Fr()
f = Fr()
n = Fr()
v = Fr()

a.setByCSPRNG()
b.setByCSPRNG()
c.setByCSPRNG()

a.setInt(2)
b.setInt(3)
c.setInt(5)
d.setInt(6)




g1 = G1()
g1.setStr(G1_STR)

h1 = G1()
h1 = G1.hashAndMapTo(b"abcd")
h2 = G2()
h2 = G2.hashAndMapTo(b"efgh")


g2 = G2()
g2.setStr(G2_STR)

print(e.getStr())

t = time.time()
f = Fr.setHashOf(b"abcd")

h1 = g1 * a * b
h1 = g1 * f

k2 = G2()
k1 = G1()

e6 = GT.pairing(h1 * e, g2 *f)

e1 = GT.pairing(g1 * a, g2 *b)

h1 = g1 * d

k1 = h1 - g1

print("subtraction")
print(g1 * c == k1)

e7 = GT.pairing(h1 * e * f, g2 * f)
e1 = GT.pairing(g1 * a, g2 * b)

print (time.time()-t)
t = time.time()

e2 = GT.pairing(g1, g2)

e17 = GT.pairing(k1, g2)

e3 = e2 * e2 * e2 * e2 * e2



print (time.time()-t)


print(e7.getStr())

print(e3.getStr() == e7.getStr())
print(e3 == e7)

t = time.time()

a.setByCSPRNG()
b.setByCSPRNG()
c.setByCSPRNG()

g1 = G1.hashAndMapTo(b"abcd")
g2 = G2.hashAndMapTo(b"abcd")

h1 = g1 * a * b

k2 = g2 * c

e1 = GT.pairing(h1, k2)
e2 = GT.pairing(g1, k2 * a * b)

print("uwaga")
print(e1 == e2)

a.setInt(2)
b.setInt(3)
c.setInt(6)
v.setInt(5)

d.setByCSPRNG()

h1 = g1 * b
h1 = g1 * d
k1 = h1 - g1
z2 = g2 * d - g2

e7 = GT.pairing(k1, g2)
e8 = GT.pairing(g1, z2)
print(e8 == e7)



h1 = g1 * d
k1 = h1 - g1
z2 = g2 * c - g2

e2 = GT.pairing(g1, g2)
e8 = GT.pairing(g1, z2)
e5 = e2 * e2 * e2 * e2 * e2
ee1 = e2 ** v

print("exp check")
print(ee1 == e5)

print (time.time()-t)

e3 = e2 * e2 * e2 * e2 * e2

n.setByCSPRNG()

Fr.setInt(n, 5)

e9 = e2 ** n
print(e9 == e3)

p = G1.hashAndMapTo(b"abcd")
q = G2.hashAndMapTo(b"abcd")

p1 = p * b
q1 = q * b

e2 = GT.pairing(p, q)
e3 = GT.pairing(p1, q1)
e4 = GT.pairing(p1, q1)

f.setInt(9)
e5 = e2 ** f

print(e4 == e3)

# Fr.setInt(d, 8) # tez dziala

d.setInt(6)




e6 = e2 * e2 * e2 * e2 * e2 * e2
e7 = e2 ** d

print(e6 == e7)
