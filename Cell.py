class Cell:
    state = False
    neighbors = 0
    position = (0, 0)

    def __init__(self, state, position_x = 0, position_y = 0) -> None:
        self.state = state
        self.position = position_x, position_y


    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state
    

    def setPosition(self, posX, posY):
        self.position = (posX, posY)

    def getPosition(self):
        return self.position
     