b=str(input('введите слово  ' ))
a={'mather':'мама',
   'father':'папа',
   'sisrter':'сестра',
   'brazer':'брат'
}

#a=a.items()

print(a)
for i,z in a.items():
    if i==b:
        print(z)
    if z==b:
        print(i)