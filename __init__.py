from mycroft import MycroftSkill, intent_file_handler


class TwisterPlayer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('player.twister.intent')
    def handle_player_twister(self, message):
        self.speak_dialog('player.twister')


def create_skill():
    return TwisterPlayer()

