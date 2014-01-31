class Entity:

    def __init__(self,username, team, hero):
        self.username = username
        self.team = team
        self.hero = hero
        self.level = 1
        self.coordX = 0
        self.coordY = 0

    def setPosition(self, x, y, terrain_sprite, window):
        self.getSprite().x = (x * 3) + terrain_sprite.x
        self.getSprite().y = (y * 3) + terrain_sprite.y
        self.coordX = x
        self.coordY = y

    def setSprite(self,sprite):
        self.sprite = sprite

    def getSprite(self):
	return self.sprite

    def respawn(self,terrain_sprite,window):   
        """Set up player spawn points based on player's team"""
        if(self.team == "Dire"):
            self.setPosition(182,164,terrain_sprite,window)
        if(self.team == "Radiant"):
            self.setPosition(-182,-164,terrain_sprite,window)

