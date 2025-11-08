import sys

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
RGB = (R, G, B)

with open(colorfile) as fp:
	min_dist = 255 * 3
	colorname = None
	for line in fp:
		name, hexcode, rgb = line.split()
		r, g, b = rgb.split(',')
		r = int(r)
		g = int(g)
		b = int(b)
		rgb = (r, g, b)
		d = dtc(RGB, rgb)
		if d < min_dist:
			min_dist = d
			colorname = name

print(colorname)
