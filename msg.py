import messaging, appuifw

num = appuifw.query(u"Recipient Number:", "text", u"")

if num.__contains__('9995191312') or num.__contains__('9846492504') or num.__contains__('9895393809') or num.__contains__('9447343753') or num.__contains__('9567152115'):
	appuifw.note(u"Invalid Number!", "error")
else:
	choice = select()


def select():

    options = [u"Repeat a message", u"A-Z", u"Multiply a message", u"1-N"]
    index = appuifw.popup_menu(items, u"Templates:")
    return index	

