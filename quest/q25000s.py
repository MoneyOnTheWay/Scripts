sm.setSpeakerID(1402000)
response = sm.sendAskAccept("Please Proceed")
if response:
    sm.warp(915000200)
    sm.sendSayOkay("I wish you luck.")
else:
    sm.sendNext("Okay then.")
sm.dispose()