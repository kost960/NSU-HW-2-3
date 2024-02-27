ent_list = input().split()
sqr = (int(ent_list[0])*100)**2 + (int(ent_list[1])*100)**2
hyp = int(sqr)**0.5
hyp2 = (((int(ent_list[2])*100)**2 + (int(ent_list[2])*100)**2)**0.5)/2
res = hyp - hyp2
print(round(res))