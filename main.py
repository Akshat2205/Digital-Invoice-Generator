



from browser import document, console, bind

productprice = document['price']
productquantity = document['quantity']
totalprice = document['total']
form = document.select('form')

totalprice.value = int(productprice.value) * int(productquantity.value)

@bind(form, "input")
def update_value(arg):
	totalprice.value = int(productprice.value) * int(productquantity.value)

'''
yourname = document['name']
button = document['btn']
outputname = document['printName']

def show(event):
	console.log("Your Name: ", yourname.value)
	outputname.value = yourname.value

button.bind("click", show)
'''
button = document['subbut']
mastertotal = document['gtotal']

def onClick(event):
	grandTotal = int(totalprice.value) + int(totalprice.value) * (5 / 100)
	mastertotal.value = grandTotal

button.bind("click", onClick)


