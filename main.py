




import browser
from browser import document, console, bind

productprice = document['price']
productquantity = document['quantity']
totalprice = document['total']
form = document.select('form')

totalprice.value = int(productprice.value) * int(productquantity.value)

@bind(form, "input")
def update_value(arg):
	totalprice.value = int(productprice.value) * int(productquantity.value)

yourname = document['name']
button = document['btn']

def show(ev):
	browser.console.log("Your Name: ", yourname.value)

button.bind("click", show)