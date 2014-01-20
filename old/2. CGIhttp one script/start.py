#!/usr/bin/env python

import CGIHTTPServer
import os
import stat
text = "#!/usr/bin/env python\nprint 1"
file = open("cgi-bin/helloworld.py", "w")
file.write(text)
file.close()
st = os.stat('cgi-bin/helloworld.py')
os.chmod('cgi-bin/helloworld.py', st.st_mode | stat.S_IEXEC)
CGIHTTPServer.test()
print 2


