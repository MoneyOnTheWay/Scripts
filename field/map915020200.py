# ParentID: 915020200
# ObjectID: 0
# Actived user ID: 1
# Character field ID when accessed: 915020200
#pt 4thjob by Jeff

Guardioso = 2159462


sm.lockInGameUI(True)

sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()

sm.sendNext("Open the door.")

sm.setSpeakerID(Guardioso)
sm.sendNext("Voice...check...")

sm.flipDialoguePlayerAsSpeaker()
sm.sendNext("I thought you were faster. Are you getting rusty?")

sm.setSpeakerID(Guardioso)
sm.sendNext("Intruder! Intruder! Shifting to battle mode. Destory the intruder!")

sm.flipDialoguePlayerAsSpeaker()
sm.sendNext("W-what? Hey, what's wrong with you? I own you!")

sm.setSpeakerID(Guardioso)
sm.sendNext("Destory the intruder.")

sm.setSpeakerID(Guardioso)
sm.sendNext("ELIMINATE!")

sm.lockInGameUI(False)

sm.removeNpc(Guardioso)
sm.spawnMob(9001047, 294, 182, False, 1800000)

sm.dispose()



