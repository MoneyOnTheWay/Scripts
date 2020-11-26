# ObjectID: 1000000
# ParentID: 2159461
# Actived user ID: 1
# Character field ID when accessed: 915020101
# Object Position Y: -71
# Object Position X: -82
# Phantom 3rd job adv
#1142377 - 3rd medal	|	1352102 -lv30 2ndary
if sm.hasQuest(25110):
    sm.giveItem(1142377)
    sm.giveAndEquip(1352102)
    sm.startQuestNoCheck(25110)
    sm.startQuestNoCheck(25111)
    sm.addMaxHP(300)
    sm.addMaxMP(150)
    sm.jobAdvance(2411)
    sm.sendSay("There you are!")
    sm.warp(100000000)
    sm.completeQuest(25110)
    sm.completeQuest(25111)
	
else:
    sm.chat("You are not 2st job Phantom.")
    sm.warp(100000000)
sm.dispose()
