#!/usr/bin/env python
"""
aampy- a simple message downloader for a.a.m

Copyright (C) 2013 by David R. Andersen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

For more information, see https://github.com/rxcomm/encoDHer
"""


import nntplib
import time
import hsub
import email
import string
import sys

GROUP = 'alt.anonymous.messages'
NEWSSERVER = 'localhost'
NEWSPORT = 119

try:
    ans = raw_input('How many days of '+GROUP+' history do you want to scan? ')
    DAYSHISTORY = float(ans)
except ValueError:
    print 'Response must be a number!'
    sys.exit(1)

def aam():
    timeStamp = time.time() - DAYSHISTORY * 86400
    YYMMDD = time.strftime('%y%m%d', time.gmtime(timeStamp))
    HHMMSS = time.strftime('%H%M%S', time.gmtime(timeStamp))

    try:
        hsubpassphrases = readDict("hsubpass.txt")
    except IOError:
        print 'hsubpass.txt file not found - exiting!'
        sys.exit(1)

    # connect to server
    server = nntplib.NNTP(NEWSSERVER,NEWSPORT)

    server.newnews(GROUP, YYMMDD, HHMMSS, '.newnews')

    with open ('.newnews', 'r') as f:
        ids=f.read().splitlines()

        for msg_id in ids:
            try:
                resp, id, message_id, text = server.article(msg_id)
            except (nntplib.error_temp, nntplib.error_perm):
                pass # no such message (maybe it was deleted?)
            text = string.join(text, "\n")

            message = email.message_from_string(text)
            match = False

            for nick, passphrase in hsubpassphrases.items():
                #print passphrase, msg_id
                for label, item in message.items():
                    if label == 'Subject':
                        match = hsub.check(passphrase,item)
                        #if match: write message to file
                        if match:
                            print 'Found a message for nickname '+nick
                            with open('message_'+nick+'_'+message_id[1:6]+'.txt', "w") as f:
                                f.write(message.as_string()+'\n')
                                print 'encrypted message stored in message_'+nick+'_'+message_id[1:6]+'.txt'


    print 'End of messages.'

def readDict(file):
    with open(file, 'r') as f:
        d = dict(line.strip().split(' ', 1) for line in f)
    return d

if __name__ == '__main__':
    aam()
