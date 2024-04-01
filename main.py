import sys
from montred import MontgomeryReducer
import time

a=995674
b=653999
p=357957

if (len(sys.argv)>1):
	a=int(sys.argv[1])
if (len(sys.argv)>2):
	b=int(sys.argv[2])
if (len(sys.argv)>3):
	p=int(sys.argv[3])  

print (f"x={a}, y={b}, p={p}")

time1 = time.time()
mr = MontgomeryReducer(p)
aval=mr.convert_in(a)
bval=mr.convert_in(b)
res=mr.convert_out(mr.multiply(aval,bval))
time2 = time.time()

print(time2-time1)
print (f"({a}x{b}) (mod {p})={res}")

time1 = time.time()
res1 = (a*b)%p
time2 = time.time()
print(time2-time1)
print(f"({a}x{b}) (mod {p})={res1}")
