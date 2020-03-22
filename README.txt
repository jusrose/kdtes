k.ey d.irect t.ext e.nryption s.system
This is a module and program to encrypt text with the key being the only available text to be used
Installation
unzip and navigate to the folder and run python setup.py install
usage
'''python
import kdtes
c = kdtes.init("<your 11 char key here>")
if c.getSucces():
    crypt = c.getCryptInstance()
    c.encrypt("text")
    crypt.encrypt("text")
    c.decrypt("text")
    crypt.decrypt("text")
'''
