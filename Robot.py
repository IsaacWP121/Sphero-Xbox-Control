import kulka

class robot:
    def __init__(self, MAC):
        self.speed = int
        self.direction = int
        self.conn = kulka.Kulka(MAC)
    
    def roll(self):
        self.conn.roll(self.speed, self.direction)

    def update(self, speed, direction):
        self.speed = speed
        self.direction = direction
    
    def set_rgb(self, red, green, blue):
        self.conn.set_rgb(red, green, blue)