class State(object):

    TITLE_SCREEN = True
    HIGH_SCORES_SCREEN = False
    GAME_PLAY = False
    GAME_OVER = False
    INSTRUCTIONS = False
    PAUSE = False
    GAME_PLAY_STARTED = False
    CURRENT_STATE = ''

    def change(self, state):
        self.CURRENT_STATE = state

        if self.CURRENT_STATE == 'title':
            self.TITLE_SCREEN = True
            self.HIGH_SCORES_SCREEN = False
            self.GAME_PLAY = False
            self.GAME_OVER = False
            self.INSTRUCTIONS = False

        if self.CURRENT_STATE == 'highscores':
            self.TITLE_SCREEN = False
            self.HIGH_SCORES_SCREEN = True
            self.GAME_PLAY = False
            self.GAME_OVER = False
            self.INSTRUCTIONS = False

        if self.CURRENT_STATE == 'gameplay':
            self.TITLE_SCREEN = False
            self.HIGH_SCORES_SCREEN = False
            self.GAME_PLAY = True
            self.GAME_OVER = False
            self.INSTRUCTIONS = False

        if self.CURRENT_STATE == 'gameover':
            self.TITLE_SCREEN = False
            self.HIGH_SCORES_SCREEN = False
            self.GAME_PLAY = False
            self.GAME_OVER = True
            self.INSTRUCTIONS = False
            
        if self.CURRENT_STATE == 'instructions':
            self.TITLE_SCREEN = False
            self.HIGH_SCORES_SCREEN = False
            self.GAME_PLAY = False
            self.GAME_OVER = False
            self.INSTRUCTIONS = True