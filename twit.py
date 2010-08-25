#PyS60-Experiments by geohacker
#Simple twitter app to *update* status.

import sys
import appuifw


#you need to have simplejson together with decoder, encoder modules.
#http://wordmobi.googlecode.com/files/simplejson_2.0.8_s60.zip
#Copy it to a comfortable location and import the path as below.

sys.path.append('e:\Python\libs')
import urllib
import simplejson as json

#Avoids urllib prompting for username and password.

class _FancyURLopener(urllib.FancyURLopener):

    def __init__(self, usr, pwd):
        urllib.FancyURLopener.__init__(self)
        self.usr = usr
        self.pwd = pwd

#required. as to handle the prompt produced by http.
    def prompt_user_passwd(self, host, realm):
        return (self.usr,self.pwd)

#twitter function to update

class TwitterApi(object):
    def __init__(self, tw_usr, tw_pwd):
        self._tw_usr, self._tw_pwd = tw_usr, tw_pwd
 
    def _get_urlopener(self):
        return _FancyURLopener(self._tw_usr, self._tw_pwd)

    def update(self, stat_msg):
        params = urllib.urlencode({"status":stat_msg})
        url = "http://twitter.com/statuses/update.json"
        f = self._get_urlopener().open(url, params)
        d = f.read()
        return json.loads(d)

if __name__=="__main__":
	app = TwitterApi("username","password")
	stat = appuifw.query(u'Whats happening?','text',u'')
	app.update(stat)
	appuifw.note(u"Status Updated", "conf")


