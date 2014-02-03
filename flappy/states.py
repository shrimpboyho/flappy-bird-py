# set up screen transitioning
titleScreenMode = True
highScoreScreenMode = False
gamePlayScreenMode = False
gameOverScreenMode = False
instructionsScreenMode = False
pause = False

def changeState(state):
    global titleScreenMode
    global highScoreScreenMode
    global gamePlayScreenMode
    global gameOverScreenMode
    global instructionsScreenMode

    if(state == 'title'):
	titleScreenMode = True
        highScoreScreenMode = False
        gamePlayScreenMode = False
        gameOverScreenMode = False
	instructionsScreenMode = False
    if(state == 'highscores'):
	titleScreenMode = False
        highScoreScreenMode = True
        gamePlayScreenMode = False
        gameOverScreenMode = False
	instructionsScreenMode = False
    if(state == 'gameplay'):
	titleScreenMode = False
        highScoreScreenMode = False
        gamePlayScreenMode = True
        gameOverScreenMode = False
	instructionsScreenMode = False
    if(state == 'gameover'):
	titleScreenMode = False
        highScoreScreenMode = False
        gamePlayScreenMode = False
        gameOverScreenMode = True
	instructionsScreenMode = False
    if(state == 'instructions'):
	titleScreenMode = False
        highScoreScreenMode = False
        gamePlayScreenMode = False
        gameOverScreenMode = False
	instructionsScreenMode = True

