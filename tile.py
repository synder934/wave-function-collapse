
from _main import *
import pygame as pg



class Tile(pg.sprite.Sprite):
    def __init__(self, fileName: str, sides: list[int, int, int, int], rotation: int = 0) -> None:
        super().__init__()
        self.image = pg.image.load(f'{images_folder}\\'+fileName)
        self.image = pg.transform.rotate(self.image, rotation)
        self.image = pg.transform.scale(self.image, TILESIZE)
        self.sides = sides[int(rotation/90):] + sides[:int(rotation/90)]
        self.options = []



class Grid():
    def __init__(self, tiles) -> None:
        self.tiles = tiles
        self.grid = [Cell((x,y), tiles) for x in range(0, DIM[0], TILESIZE[0]) for y in range(0, DIM[1], TILESIZE[1])]



class Cell(pg.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], tiles) -> None:
        super().__init__()
        self.image = pg.image.load('empty.png')
        self.image = pg.transform.scale(self.image, TILESIZE)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.sides = [0,0,0,0]
        self.rect.topleft = self.pos
        self.tile = None
        self.options = [t for t in tiles]
        self.adjCords = [
            (self.pos[0], self.pos[1]-TILESIZE[1]),
            (self.pos[0]+TILESIZE[0], self.pos[1]),
            (self.pos[0], self.pos[1]+TILESIZE[1]),
            (self.pos[0]-TILESIZE[0], self.pos[1])
        ]
        self.adj = []
        pass

    def clicked(self, tile, grid, tiles):
        print(self.options)
        pass


    def tileSet(self, tile:Tile):
        self.tile = tile
        self.image = tile.image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.sides = tile.sides.copy()



    def calcOptions(self, grid:Grid, tiles):
        if self.tile != None:
            self.options = [self.tile]
            return


        self.options = [t for t in tiles]

        self.adj = [c for c in grid.grid if c.pos in self.adjCords] if self.adj == [] else self.adj

        for cell in self.adj:

            if cell.pos == self.adjCords[0]:
                if cell.sides[2] == 0: pass
                else:
                    self.options = [tile for tile in self.options if tile.sides[0] == cell.sides[2][::-1]]


            elif cell.pos == self.adjCords[1]:
                if cell.sides[3] == 0: pass
                else:
                    self.options = [tile for tile in self.options if tile.sides[1] == cell.sides[3][::-1]]


            elif cell.pos == self.adjCords[2]:
                if cell.sides[0] == 0: pass
                else:
                    self.options = [tile for tile in self.options if tile.sides[2] == cell.sides[0][::-1]]


            elif cell.pos == self.adjCords[3]:
                if cell.sides[1] == 0: pass
                else:
                    self.options = [tile for tile in self.options if tile.sides[3] == cell.sides[1][::-1]]    

        if len(self.options) == 1:
            self.tileSet(self.options[0])


    def update(self, grid, tiles) -> None:
        self.calcOptions(grid, tiles)

        pass
        






    


