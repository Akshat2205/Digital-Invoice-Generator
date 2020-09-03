



from browser import document, console, bind

productprice 	= document['price']
productquantity = document['quantity']
totalprice 		= document['total-value']
form 			= document['form']
mastertotal 	= document['gtotal']
submit 			= document['subbut']
resetpage       = document['reset']
products        = document['prodes']
additem         = document['buttonitem']

# tax variables
tax   			= document['taxitem']

mastertotal.value 		= 0
productprice.value 		= 0
productquantity.value 	= 0
totalprice.value		= 0
gst = 0
item = ''


@bind(form, "input")
def update_value(event):

	global gst
	gst = int(tax.children[0].children[0].value)
	igst = int(tax.children[1].children[0].value)
	cgst = int(tax.children[2].children[0].value)

	totalprice.value = int(productprice.value) * int(productquantity.value) 
	mastertotal.value = int(totalprice.value) + int(totalprice.value) * int(gst) / 100

'''

@bind(submit, "click")
def print_slip(event):
	console.log('print the slip from printer')

'''

# Reset page contents
@bind(resetpage, "click")
def reset_values(ev):
	mastertotal.value 		= 0
	productprice.value 		= 0
	productquantity.value 	= 0
	totalprice.value		= 0
	
	# tax
	gst = 0
	tax.children[0].children[0].value = 0
	tax.children[1].children[0].value = 0
	tax.children[2].children[0].value = 0

	products.value = ""
	
	for x in range(0, 3):
		tax.children[x].value = 0
	item = ''


@bind(additem, "click")
def additem(ev):
	global item
	item = str(products.value)
	console.log(item)
	products.value = item