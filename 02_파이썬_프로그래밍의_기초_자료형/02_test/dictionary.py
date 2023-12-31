a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.keys()
# dict_keys(['name', 'phone', 'birth'])

for k in a.keys():
    print(k)


a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.get('name')
# 'pey'

a.get('ph2one')
print(a.get('hihih'))
# print(a['hih'])
# '010-9999-1234'
    

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
c = 'name' in a
# True
print(c)

'email' in a
# False