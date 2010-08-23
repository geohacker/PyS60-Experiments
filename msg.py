import messaging, appuifw

num = appuifw.query(u"Recipient Number:", "text", u"")

if num.__contains__('9995191312') or num.__contains__('9846492504') or num.__contains__('9895393809') or num.__contains__('9447343753') or num.__contains__('9567152115'):
	appuifw.note(u"Invalid Number!", "error")
else:
	choice = select()
	if choice == 0:
	  #call function to repeat message
	elif choice == 1:
	  #call function to A-Z
	elif choice == 2:
	  #call function to multiply message
	elif choice == 3:
	  #call function to 1-N
	elif choice == None:
	  appuifw.note(u"Aborted")

def select():

    options = [u"Repeat a message", u"A-Z", u"Multiply a message", u"1-N"]
    index = appuifw.popup_menu(options, u"Templates:")
    return index	

def rptmsg(num):
	import messaging
	import appuifw as ui

	info = ui.query( u'Count:' )
	msg=ui.query(u'Message:','text',u'this is a text message')
	for i in range(0,int(info[0])):
	  messaging.sms_send(num,msg)

	   
	  
  
def multiply(num):
	import messaging
	import appuifw as ui

	info = ui.query(u'Count:' )
#num=ui.query(u'Number:','text')
	msg=ui.query(u'Message:','text',u'this is a text message')

	for i in range(1,int(info[0])):
	  copy=msg*i
	  messaging.sms_send(num,msg)


def a2z(num):
	import messaging
	import appuifw as ui
	msg="A"
	al="A"
	for i in range(0,26):
	   messaging.sms_send(num,msg)
	   al=chr(ord(al)+1)
	   msg = msg+al
	  
def oneton(num):
	import messaging
	import appuifw as ui
	info = ui.query(u'Count:' )
	for i in range(0,info):
	   messaging.sms_send(num,str(i+1))
	   
