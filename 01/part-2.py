id_ltn = 0
somme_ltn = 0

ltns = []

for i in range(2244):
	val = input()
	if (val == ""):
		ltns.append(somme_ltn)

		id_ltn = 0
		somme_ltn = 0
	else:
		somme_ltn += int(val)



tris = list(sorted(ltns, reverse=True))

print(tris[0] + tris[1] + tris[2])
