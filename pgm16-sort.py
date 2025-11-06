d = {2:"b",1:"a",3:"c"}
print(d)
asc = dict(sorted(d.items()))
print("Ascending:",asc)
desc = dict(sorted(d.items(),reverse=True))
print("Descending:",desc)
