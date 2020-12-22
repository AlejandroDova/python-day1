demo_list = [1,"Hello world", 1.34, True, [1,2,3]]
colors = ['red','green','blue']

numbers_list = list((1,2,3))
print(type(numbers_list))

r = list(range(1,10))
print(r)
print(len(demo_list))
print(colors[-2])

#print(dir(colors))

#colors.append('violet')
#colors.extend(['violet','yellow'])
#colors.extend('pink','black')

#colors.insert(-1,'violet')

colors.insert(len(colors),'violet')

#print(colors)

#colors.pop()
#colors.remove('green')
#colors.clear()
print(colors)
colors.sort(reverse=True)
print(colors)

print(colors.index('violet'))

