import random
mods=[]
model = open('/deku/oppo.txt','r').readlines()

for models in model:
       mods.append(models)
model2 = random.choice(mods)
print(model2)