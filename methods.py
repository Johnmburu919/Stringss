#string methods
x="hello world"
print(len(x))
print(x.upper())
print(x.lower())
print(x.replace('h','y'))

#capitalize
txt = "welcome, and welcome to python programming."
y= txt.capitalize()
print (y)
 
 #center
txt = "ball"
z = txt.center(80)
print(z)

#count
txt = "I love programming, programming is my favorite hobby programming is good"
a = txt.count("programming")
print(a)

#format
txt = "For only {price:.3f} shillings!"
print(txt.format(price = 65))

#istitle
txt = "Hello, And Welcome To My World!"
b = txt.istitle()
print(b)
