from mycroft import MycroftSkill, intent_file_handler
from random import randint

# global i = 0
players = ['Andrey', 'Katya']
parts = ['right hand', 'left hand', 'right foot', 'left foot']
colors = ['blue', 'green', 'yellow', 'red', 'air']

def r_generator(max_int):
    return randint(0, max_int)

def spin_twister():
    # global i
    i = 0
    res = "Player %s, put %s on the %s" % (players[i%2], parts[r_generator(3)], colors[r_generator(4)])
    # i+=1
    return res

class TwisterPlayer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('start.twister.intent')
    def handle_start_twister(self, message):
        self.speak_dialog('start.twister')

    @intent_file_handler('stop.twister.intent')
    def handle_stop_twister(self, message):
        self.speak_dialog('stop.twister')

    @intent_file_handler('spin.twister.intent')
    def handle_spin_twister(self, message):
        self.speak_dialog('spin.twister')
        action = spin_twister()
        self.speak_dialog('action.twister', {'action': action})


def create_skill():
    return TwisterPlayer()

