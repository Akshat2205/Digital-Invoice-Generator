



from browser import document, console, bind

productprice 	= document['price']
productquantity = document['quantity']
totalprice 		= document['total-value']
form 			= document['form']
radio 			= document['gst']
mastertotal 	= document['gtotal']
submit 			= document['subbut']
resetpage       = document['reset']

mastertotal.value 		= 0
productprice.value 		= 0
productquantity.value 	= 0
totalprice.value		= 0
gst = 0

@bind(form, "input")
def update_value(event):

	global gst
	gst = int(radio.children[1].value)
	totalprice.value = int(productprice.value) * int(productquantity.value) 
	mastertotal.value = int(totalprice.value) + int(totalprice.value) * int(gst) / 100

@bind(submit, "click")
def print_slip(event):
	console.log('print the slip from printer')

@bind(resetpage, "click")
def reset_values(ev):
	mastertotal.value 		= 0
	productprice.value 		= 0
	productquantity.value 	= 0
	totalprice.value		= 0
	gst = 0