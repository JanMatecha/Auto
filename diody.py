import machine
import time
def setPin(pin):
    P = machine.Pin(pin,machine.Pin.OUT)
    return P

def setPins(pins):
    P=[]
    for pin in pins:
       P.append(setPin(pin))
    return P

def pinOn(p):
    p.value(1)

def pinOff(p):
    p.value(0)

	
def pinsOn(P):
    for p in P:
        p.value(1)

def pinsOff(P):
    for p in P:
        p.value(0)

def blik(N, P):
    n=0
    while n < N:
        pinsOn(P)
        time.sleep(1)
        pinsOff(P)
        time.sleep(1)
        n=n+1

def blikUp(N, P):
    n=0
    while n < N:
	for p in P:
            pinOn(p)
            time.sleep(1)
        pinsOff(P)
        time.sleep(1)
        n=n+1

def blikDown(N, P):
    n=0
    while n < N:
        pinsOn(P)
	for p in P:
            time.sleep(1)
            pinOff(p)
        time.sleep(1)
        n=n+1

#P=setPins([12,13,14,15])
#blik(1,P)

#blikUp(1,P)
#blikDown(1,P)




