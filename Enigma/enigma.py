a="abcdefghijklmnopqrstuvwxyz"
d = {}
for i in range(len(a)):
    d[a[i]] = i


class Rotor:
	def __init__(self, offset, cycles):
		self.offset = offset
		self.fa = {}
		self.ra = {}
		for i in range(26):
			self.fa[i] = i
			self.ra[i] = i

		for cycle in cycles.split():
			c = cycle[1:-1]

			for i in range(len(c)):
				self.fa[d[c[i]]] = d[c[(i+1)%len(c)]]
				self.ra[d[c[i]]] = d[c[(i-1)%len(c)]]

	def fout(self, x):
		return (self.fa[(x+self.offset)%26]-self.offset)%26

	def rout(self, x):
		return (self.ra[(x+self.offset)%26]-self.offset)%26

r1 = Rotor(3,'(wordle) (is) (fun)')
r2 = Rotor(2, '(tears) (boing) (lucky)')
r3 = Rotor(13, '(quack) (froze) (twins) (glyph)')
r4 = Rotor(0, '(az) (by) (cx) (dw) (ev) (fu) (gt) (hs) (ir) (jq) (kp) (lo) (mn)')

def encode(c):
	x = d[c]

	o1 = r1.fout(x)
	o2 = r2.fout(o1)
	o3 = r3.fout(o2)
	o4 = r4.fout(o3)
	o5 = r3.rout(o4)
	o6 = r2.rout(o5)
	o7 = r1.rout(o6)

	return a[o7]

print(encode('j'))
