#a = "sample_string"
a = input("Enter your string: ")
b = []
c = ''
for i in range(len(a), 0, -1):
    b.append(a[i-1])
#print(b)
c = c.join(b)
print(c)