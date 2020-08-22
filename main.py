



from browser import document, console, bind

productprice = document['price']
productquantity = document['quantity']
totalprice = document['total']
form = document.select('form')

totalprice.value = int(productprice.value) * int(productquantity.value)

radio = document['gst']
mastertotal = document['gtotal']
mastertotal.value = 0
productprice.value = 0
productquantity.value = 0

# console.log(radio.children[3].children[0].value)

@bind(form, "input")
def update_value(arg):
	totalprice.value = int(productprice.value) * int(productquantity.value)
	gst = 0

	if radio.children[1].children[0].checked:gst = int(radio.children[1].children[0].value)
	if radio.children[2].children[0].checked:gst = int(radio.children[2].children[0].value) 
	if radio.children[3].children[0].checked:gst = int(radio.children[3].children[0].value)

	console.log(gst)
	grandTotal = int(totalprice.value) + int(totalprice.value) * (int(gst) / 100)
	mastertotal.value = grandTotal
