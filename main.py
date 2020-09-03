



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


# tax calculation variables
tax             = document['gst']
sgst            = document['sgst']
cgst            = document['cgst']
totaltax        = document['totaltax']

mastertotal.value 		= 0
productprice.value 		= 0
productquantity.value 	= 0
totalprice.value		= 0
gst = 0
item = ''


@bind(form, "input")
def update_value(event):

	global gst
	gst = int(tax.value)
	taxsgst = float(gst /2)
	taxcgst = float(gst / 2)

	totalprice.value = int(productprice.value) * int(productquantity.value) 
	mastertotal.value = int(totalprice.value) + int(totalprice.value) * int(gst) / 100
	
	# total tax
	totaltax.value = int(totalprice.value) * int(gst) / 100 
	sgst.value = taxsgst
	cgst.value = taxcgst

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
	tax.value       = 0
	sgst.value      = 0
	cgst.value      = 0
	totaltax.value  = 0

	products.value  = ""
	item = ''


@bind(additem, "click")
def additem(ev):
	global item
	item = str(products.value)
	console.log(item)
	products.value = item