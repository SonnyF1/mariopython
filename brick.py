from tkinter import *
root = Tk()
canvas = Canvas(root, height=200, width=200)
canvas.pack()


class Brick:
    def __init__(self, coins, centerx, centery, size, colour):
        self.coins = coins
        self.centerx = centerx
        self.centery = centery
        self.size = size
        self.colour = colour
        self.g = canvas.create_rectangle(self.centerx + (self.size/0.5), self.centery + (self.size/0.5), self.centerx - (self.size*0.5),self.centery - (self.size*0.5), fill=self.colour)
    def getcoins(self):
        return self.coins

    #for testing
    '''def changecoins(self):
        ccoins = input("How many coins should the block have ")
        while ccoins.isdigit() == False:
            ccoins = input("That wasn't a number, please input the number of coins ")
        ccoins = int(ccoins)
        self.coins = ccoins'''
    def WasHit(self):
        if self.coins != 0:
            self.coins = self.coins - 1
        if self.coins == 0:
            canvas.delete(self.g)
bricky = Brick(1, 100, 100, 50, 'brown')
bricky.changecoins()
bricky.WasHit()
mainloop()
