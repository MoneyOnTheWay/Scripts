# ParentID: 915020201
# ObjectID: 0
# Actived user ID: 1
# Character field ID when accessed: 915020201
#by Jeff  ptariaroom

sm.lockInGameUI(True)

sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()

sm.sendNext("Aria's Portrait... I was wondering if I'd run into you.")
sm.sendNext("You always were too concerned about everybody else...And now you give me the skill book i was looking for. What a dear.")
sm.giveItem(1142377) #sm.giveAndEquip(1352101)
sm.jobAdvance(2412)
sm.addMaxHP(300)
sm.addMaxMP(150)
sm.warp(100000000)
sm.completeQuest(25120)
sm.dispose()

else:
    sm.chat("You are not 3rd job Phantom.")
    sm.warp(100000000)
sm.dispose()

sm.lockInGameUI(False)
sm.dispose()
