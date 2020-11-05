#slicing
b = "Hello, World!"
print(b[2:5])

#slicing negativo
b = "Hello, World!"
print(b[-5:-2])


#busca
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

txt = "The book is on the table"
x = "ain" not in txt
print(x)

print()
print()

#formatação
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print('\n\n')