
l_ist = [2, 3, 5, 9, 3]
odds_sum = sum([x[1] for x in filter(lambda x: x[0] % 2, enumerate(l_ist))])
print (odds_sum)