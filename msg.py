import messaging, appuifw

num = appuifw.query(u"Recipient Number:", "text", u"")

if num.__contains__('9995191312') or num.__contains__('9846492504'):
	appuifw.note(u"Invalid Number!", "error")
else:
	choice = select()


def select():
    options = [
