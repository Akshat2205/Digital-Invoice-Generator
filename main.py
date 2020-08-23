



from browser import document, console, bind

productprice 	= document['price']
productquantity = document['quantity']
totalprice 		= document['total-value']
form 			= document['form']
radio 			= document['gst']
mastertotal 	= document['gtotal']
submit 			= document['subbut']

mastertotal.value 		= 0
productprice.value 		= 0
productquantity.value 	= 0
totalprice.value		= 0


@bind(form, "input")
def update_value(event):

	gst = 0
	if radio.children[2].checked: gst = int(radio.children[2].value)
	if radio.children[4].checked: gst = int(radio.children[4].value) 
	if radio.children[6].checked: gst = int(radio.children[6].value)

	totalprice.value = int(productprice.value) * int(productquantity.value) 
	mastertotal.value = int(totalprice.value) + int(totalprice.value) * int(gst) / 100

@bind(submit, "click")
def print_slip(event):
	console.log('print the slip from printer')
