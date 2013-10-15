[aampy] [1]- a simple message downloader for a.a.m
===

[1]: https://github.com/rxcomm/aampy/  "aampy"

# Installation:

Edit aampy.py and change the constants at the top (GROUP, NEWSSERVER,
and NEWSPORT) per your liking prior to installation.

From the aampy directory, execute the command:

```
sudo python setup.py install
```

This will build an executable called aampy, and install it in /usr/local/bin.
It will also leave a copy of the aampy executable in the aampy directory.

# Usage

Create a file called ```hsubpass.txt``` with one nickname and hsub password per line,
with the nickname followed by a single space. The file ```hsubpass.txt``` must be
located in the directory you are running *aampy* from.

For example, you might try the following:

```
sam ThisIsMyHsubPassphrase
bob This hsub passphrase includes spaces
22 wonderfullife!
nickname One more time and we will be done
```
The nickname cannot contain any spaces. A single space should
follow the nickname and then a free-form hsub passphrase.

Then run *aampy* and it will download each message from a.a.m and test
to see if a match results with any of the hsub passphrases in your
hsubpass.txt file.  If a match occurs, it will add that message to the
file ```messages_<nickname>_<id>.txt```.
For example if aampy found two messages for nickname bob and one for nickname 22,
there would be two files, ```messages_bob_abcde.txt``` with two encrypted messages in it
and ```messages_22_12345.txt``` with a single encrypted message in it.  
