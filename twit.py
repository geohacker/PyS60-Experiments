import sys
import appuifw
sys.path.append('e:\Python\libs')
import urllib
import simplejson as json

class _FancyURLopener(urllib.FancyURLopener):

    def __init__(self, usr, pwd):
        """ Set user/password for http and call base class constructor
        """
        urllib.FancyURLopener.__init__(self)
        self.usr = usr
        self.pwd = pwd
 
    def prompt_user_passwd(self, host, realm):
        """ Basic auth callback
        """
        return (self.usr,self.pwd)

class TwitterApi(object):
    """ Twitter API basic class
    """
    def __init__(self, tw_usr, tw_pwd):
        """ Set user/password for twitter
        """
        self._tw_usr, self._tw_pwd = tw_usr, tw_pwd
 
    def _get_urlopener(self):
        """ Return an urlopener with authentication support
        """
        return _FancyURLopener(self._tw_usr, self._tw_pwd)

    def update(self, stat_msg):
        """ Update twitter with new status message
        """
        params = urllib.urlencode({"status":stat_msg})
        url = "http://twitter.com/statuses/update.json"
        f = self._get_urlopener().open(url, params)
        d = f.read()
        return json.loads(d)

if __name__=="__main__":
	app = TwitterApi("geohacker","ohmyGODubuntu")
	stat = appuifw.query(u'Whats happening?','text',u'')
	app.update(stat)
	appuifw.note(u"Status Updated", "conf")


