




import browser
from browser import document, console, bind

multiplicand = document['a']
multiplier = document['b']
product = document['c']
form = document.select('form')

product.value = int(multiplicand.value) * int(multiplier.value)

@bind(form, "input")
def update_value(arg):
    product.value = int(multiplicand.value) * int(multiplier.value)
