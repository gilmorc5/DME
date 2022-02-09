# Charles Gilmore
# 01/28/2022
# Project 1: DME
###################################

# Sample T-inputs 1862 1874 ; Sample R-inputs 2024 2036

# Def's
def findtdiff(tpulse1, tpulse2):
    if tpulse1 < tpulse2:
        tdifference = tpulse2 - tpulse1
    elif tpulse1 > tpulse2:
        tdifference = tpulse1 - tpulse2
    else:
        tdifference = 'Invalid pulse times'
    return tdifference
def findrdiff(rpulse1, rpulse2):
    if rpulse1 < rpulse2:
        rdifference = rpulse2 - rpulse1
    elif rpulse1 > rpulse2:
        rdifference = rpulse1 - rpulse2
    else:
        rdifference = 'Invalid pulse times'
    return rdifference
def fruitDetect(tchannel, rchannel):
    if tchannel != rchannel:
        print("FRUIT DETECTED")
def garbleDetect(tpulse2, rpulse1):
    if ((rpulse1 - tpulse2) < 50):
        print("GARBLE DETECTED")
def tchanneldetect(tdifference):
    if tdifference == 12:
        tchannel = 'X'
    elif tdifference == 36:
        tchannel = 'Y'
    elif tdifference == 24:
        tchannel = 'W'
    elif tdifference == 21:
        tchannel = 'Z'
    else:
        tchannel = 'GARBLE'
    return tchannel
def rchanneldetect(rdifference): 
    if rdifference == 12:
        rchannel = 'X'
    elif rdifference == 30:
        rchannel = 'Y'
    elif rdifference == 24:
        rchannel = 'W'
    elif rdifference == 15:
        rchannel = 'Z'
    else:
        rchannel = 'GARBLE'
    return rchannel   
def displayDist(tpulse1, rpulse1, rchannel, tchannel):
    time = rpulse1 - tpulse1
    dist_nm = (time - 50)/12.3
    if (rchannel == 'GARBLE') | (tchannel == 'GARBLE'):
        if time > 2510:
            print("No Reply")
    elif time < 50:
        print()
    elif time > 2510:
        print("No Reply")
    else:
            print("Distance: %.2f" % dist_nm + " nmi's")
###################################################3
# MAIN CODE BLOCK

# User input of transmitted pulses
tpulse1 = int(input("Pulse 1: "))
tpulse2 = int(input("Pulse 2: "))

# User input of Received pulses
rpulse1 = int(input("Pulse 3: "))
rpulse2 = int(input("Pulse 4: "))
print() 

# Find the difference of two pulses to determine Channel
tdifference = findtdiff(tpulse1, tpulse2)
rdifference = findrdiff(rpulse1, rpulse2)

#Identify the Channel type X/Y of Transmission 
print("Sent (Channel): " + tchanneldetect(tdifference))

#Identify the Channel type X/Y of Received signals
print("Received (Channel): " + rchanneldetect(rdifference))

# FRUIT & Garble Detection
# Variables to send to def to compare, check if FRUIT detected
tchannel = tchanneldetect(tdifference)
rchannel = rchanneldetect(rdifference)

# Print if FRUIT or GARBLE is detected, else do nothing
fruitDetect(tchannel, rchannel)
garbleDetect(tpulse2, rpulse1)

# Display the distance calculation to DME Station
displayDist(tpulse1, rpulse1, rchannel, tchannel)    
