class Player:

    def __init__(self,username, team, hero):
        self.username = username
        self.team = team
        self.hero = hero
        self.level = 1
        self.coordX = 0
        self.coordY = 0

    def teleport(self, x, y, terrain_sprite, window):
        terrain_sprite.x = window.width/2
        terrain_sprite.y = window.height/2
        terrain_sprite.x -=  3 * x
        terrain_sprite.y -= 3 * y
        self.coordX = x
        self.coordY = y

    def setSprite(self,sprite):
        self.sprite = sprite

    def getSprite(self):
	return self.sprite

    def respawn(self,terrain_sprite,window):   
        """Set up player spawn points based on player's team"""
        if(self.team == "Dire"):
            self.teleport(182,164,terrain_sprite,window)
        if(self.team == "Radiant"):
            self.teleport(-182,-164,terrain_sprite,window)
