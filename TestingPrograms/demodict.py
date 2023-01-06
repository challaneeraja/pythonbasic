data = {'name' : 'steve', 'num' : 78998, 'place' : 'chennai'}
print(data['name'])
print(data.get('num'))
print(data.get('contact'))
print(data.setdefault('contact',6797790804))
print(data)
print(data.setdefault('num',89798))
for i in data:
    print(i)
for i in data.values():
    print(i)
for k,v in data.items():
    print(k,v,sep='->')
data.update({'contact':6576443439})
print(data)
data.pop('name')
print(data)
