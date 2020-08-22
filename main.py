



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

g5 = document.getElementById('gst5')
g12 = document.getElementById('gst12')
g18 = document.getElementById('gst18')
# console.log("g5 raw: ", g5)

def onClick(event):
	grandTotal = int(totalprice.value) + int(totalprice.value) * (int(g5.value) / 100)
	mastertotal.value = grandTotal

button.bind("click", onClick)

