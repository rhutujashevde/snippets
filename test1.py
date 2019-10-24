someArray = [ { 'size': 'large', 'shape': 'circle', 'color': 'red'}, { 'size': 'small', 'shape': 'rectangle', 'color': 'blue' }, { 'shape': 'rectangle', 'color': 'green' } ] 
#print the color of the element when 'size' exists in that element

for i in someArray:
    if 'size' in i.keys():
        print(i['color'])