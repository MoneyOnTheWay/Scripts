# ObjectID: 0
# Character field ID when accessed: 260010601
# Actived user ID: 1
# ParentID: 260010601
""""
2410 <= chr.getJob() <= 2411
sm.warp(915020100, 1)
sm.chat("There is no going back!")


Dust = 9001046 #dusk dwarf
if not sm.hasQuest(25102):
    sm.startQuestNoCheck(25102)
    sm.spawnMob(Dust, 420, 182, False, 300000)
sm.dispose()
"""

if sm.hasMobsInField():
    sm.chat("There is no going back!")
else:
    sm.chat("There is no going back!")
sm.dispose()


