def add(a, b):
	return a + b
def divide(a, b):
	if b == 0:
 		raise ValueError("Деление на ноль невозможно")
	return a / b
a = int(intput())
b = int(intput())
print(add(a,b))
print(divide(a,b))
