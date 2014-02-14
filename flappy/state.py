class State(object):

    titleScreenMode = True
    highScoreScreenMode = False
    gamePlayScreenMode = False
    gameOverScreenMode = False
    instructionsScreenMode = False
    pause = False
    gamePlayScreenModeStarted = False
    currentState = ''

    def change(self, state):
        self.currentState = state

        if self.currentState == 'title':
            self.titleScreenMode = True
            self.highScoreScreenMode = False
            self.gamePlayScreenMode = False
            self.gameOverScreenMode = False
            self.instructionsScreenMode = False

        if self.currentState == 'highscores':
            self.titleScreenMode = False
            self.highScoreScreenMode = True
            self.gamePlayScreenMode = False
            self.gameOverScreenMode = False
            self.instructionsScreenMode = False

        if self.currentState == 'gameplay':
            self.titleScreenMode = False
            self.highScoreScreenMode = False
            self.gamePlayScreenMode = True
            self.gameOverScreenMode = False
            self.instructionsScreenMode = False

        if self.currentState == 'gameover':
            self.titleScreenMode = False
            self.highScoreScreenMode = False
            self.gamePlayScreenMode = False
            self.gameOverScreenMode = True
            self.instructionsScreenMode = False
            
        if self.currentState == 'instructions':
            self.titleScreenMode = False
            self.highScoreScreenMode = False
            self.gamePlayScreenMode = False
            self.gameOverScreenMode = False
            self.instructionsScreenMode = True