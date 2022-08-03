
from random import choice
from re import A
import pygame as pg
import tile
import json

#import sys; sys.path.append('Z:\\Code\\waveFunction\\images')

vec = pg.Vector2

TILESIZE = (32, 32)
NUMOFTILES = (20, 20)
DIM = (TILESIZE[0]*NUMOFTILES[0], TILESIZE[1]*NUMOFTILES[1])
FPS = 20
CLOCK = pg.time.Clock()

images_folder = 'maps'
fpsEnabled = False


class Sim():
    def __init__(self) -> None:
        pg.init()
        self.disp = pg.display.set_mode(DIM)
        
        with open(f'{images_folder}\\data.json', 'r') as f:
            data = json.load(f)
            self.tiles = [tile.Tile(f'{x}.png', data[x]['sides'], r) for x in data for r in data[x]['rotations']]
            data = None

        self.setup()
        self.mainloop()


    def mainloop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    self.setup()

            self.update()

            for cell in self.grid.grid:
                self.disp.blit(cell.image, cell.rect)
            
            if fpsEnabled: CLOCK.tick(FPS)
            pg.display.update()


    def setup(self):
        self.grid = tile.Grid(self.tiles)
        return

    def update(self):
        avaliable = [cell for cell in self.grid.grid if len(cell.options) > 1]
        if avaliable == []: return

        avaliable.sort(key= lambda y: len(y.options))

        lowestval = len(avaliable[0].options)
        lowestOptions = [c for c in avaliable if len(c.options) == lowestval]

        cell = choice(lowestOptions)
        cell.calcOptions(self.grid, self.tiles)
        cell.tileSet(choice(cell.options))

        for cell in self.grid.grid: cell.calcOptions(self.grid, self.tiles)


    def quit(self):
        pg.quit()
        quit()


if __name__ == '__main__':
    Sim()
