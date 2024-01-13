inventory={"gold":500,"punch":['flint','twice','gemstone'],"backpack":['xylophone','dragger','bedroom','bread loaf']}
inventory.update({'packet':['seashells','storage break','lint']})
print(inventory)
inventory["backpack"].sort()
print(inventory)
inventory["backpack"].remove('dragger')
print(inventory)
inventory['gold']=inventory['gold']+50
print(inventory)


