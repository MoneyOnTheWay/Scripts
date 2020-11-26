"""
# Free market
map = sm.getReturnField()

if map == 0 or map == 910000000:
    sm.chat("mapid:{}".format(map))
    sm.chat("(Portal) Cannot find your previous map ID, warping to Henesys.")
    map = 100000000
    portal = 0

if "910001000" in sm.getQRValue(9999):
    sm.setQRValue(9999, "")
    map = 910001000
    portal = 2

sm.warpNoReturn(map, portal)
"""

# Free market
oldFieldID = sm.getReturnField()
if oldFieldID == 0 or oldFieldID == 910000000:
    sm.chat("(Portal) Cannot find your previous map ID, warping to Henesys.")
    map = 100000000
    portal = 0
else:
    map = oldFieldID
    portal = 0
sm.warpNoReturn(map, portal)
sm.dispose()
