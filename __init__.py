from mycroft import MycroftSkill, intent_file_handler
from random import randint
import os
from os.path import expanduser

home = expanduser("~")
players = ['Andrei', 'Katja']
parts = ['right hand', 'left hand', 'right foot', 'left foot']
colors = ['blue', 'green', 'yellow', 'red', 'air']

def r_generator(max_int):
    return randint(0, max_int)

def spin_twister(i):
    res = "Player %s, put %s on the %s" % (players[i%2], parts[r_generator(3)], colors[r_generator(4)])
    return res

class TwisterPlayer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('start.twister.intent')
    def handle_start_twister(self, message):
        self.speak_dialog('start.twister')
        open(os.path.join(home, "iter.txt"), "w").write('0')

    @intent_file_handler('stop.twister.intent')
    def handle_stop_twister(self, message):
        self.speak_dialog('stop.twister')
        os.system("rm ~/iter.txt")

    @intent_file_handler('spin.twister.intent')
    def handle_spin_twister(self, message):
        self.speak_dialog('spin.twister')
        iter = int(open(os.path.join(home, "iter.txt"), "r").read())
        action = spin_twister(iter)
        self.speak_dialog('action.twister', {'action': action})
        open(os.path.join(home, "last_action.txt"), "w").write(action)
        iter +=1
        open(os.path.join(home, "iter.txt"), "w").write(str(iter))
        
    @intent_file_handler('repeat.twister.intent')
    def handle_repeat_twister(self, message):
        last_action =  open(os.path.join(home, "last_action.txt"), "r").read()
        self.speak_dialog('repeat.twister', {'last_action': last_action})

def create_skill():
    return TwisterPlayer()

