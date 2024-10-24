li=['gowtham','nithish','narasi']
print(li)
for i in li:
    if i=='narasi':
        li.remove(i)
        li.append('hi')
        li.insert(1,"ranjit")
print(li)