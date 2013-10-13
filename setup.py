import zipfile
import os
import pwd

with zipfile.ZipFile('aampy', 'w', zipfile.ZIP_DEFLATED) as z:
    z.write('__main__.py')
    z.write('aampy.py')
    z.write('hsub.py')

with open('aampy', 'r+') as z:
    zipdata = z.read()
    z.seek(0)
    z.write('#!/usr/bin/env python\n'+zipdata)

user = os.getenv('SUDO_USER')
uid, gid = pwd.getpwnam(user)[2:4]
os.chown('aampy', uid, gid)
os.chmod('aampy',0755)
os.system('cp aampy /usr/local/bin/aampy')
print 'aampy executable copied to /usr/local/bin/aampy'
