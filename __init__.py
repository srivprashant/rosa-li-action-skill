from mycroft import MycroftSkill, intent_file_handler


class RosaLiAction(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('action.li.rosa.intent')
    def handle_action_li_rosa(self, message):
        self.speak_dialog('action.li.rosa')


def create_skill():
    return RosaLiAction()

