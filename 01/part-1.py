id_ltn = 0
somme_ltn = 0
somme_max=0


for i in range(2244):
	val = input()
	if(val==""):
		if(somme_ltn > somme_max):
			somme_max = somme_ltn
		
		id_ltn = 0;
		somme_ltn = 0;
	else:
		somme_ltn += int(val)


print(somme_max)