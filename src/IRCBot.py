# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import bootUpChecks
import socket
import time

__author__ = "Sylos"
__date__ = "$Aug 30, 2015 12:28:36 AM$"
firstServer = irc.veuwer.com
def getServer():
    return firstServer
bc = bootUpChecks
running = true


setUpNick()
if __name__ == "__main__":
    server = getServer()
    ircsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ircsock.connect((server, PORT))
    while(running):
        if(bc.login()):
            print ("Success")
