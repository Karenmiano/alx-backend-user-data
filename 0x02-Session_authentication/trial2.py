i = {}
j = []
def set():
    i['foo'] = 'bar'
    j.append('qux')
set()
print(i) # prints {'foo': 'bar'}
print(j) # prints ['qux']