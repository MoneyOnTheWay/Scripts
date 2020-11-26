# ParentID: 915020100
# ObjectID: 0
# Actived user ID: 1
# Character field ID when accessed: 915020100
Dust = 9001046 #dusk dwarf
if sm.hasMobsInField():
 sm.dispose()
else:
 sm.spawnMob(Dust, 420, 182, False, 25000)
sm.dispose()
