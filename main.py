# This code was created by Isaiah Garcia
# Sources:
    # Chris Cozort
    # Chris Bradfield - content from kids can code: http://kidscancode.org/blog/'
    # http://www.codingwithruss.com/pygame/how-to-create-a-health-bar-in-pygame/

# Goals:
    # 2D raft inspired survival game
    # food, water, and health bar
    # enemies
    # items to collect

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import os
from settings import *
from sprites import *

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Cooldown():
        def __init__(self):
            self.current_time = 0
            self.event_time = 0
            self.delta = 0
        def ticking(self):
            self.current_time = (pg.time.get_ticks())/1000
            self.delta = self.current_time - self.event_time
        def timer(self):
            self.current_time = (pg.time.get_ticks())/1000


class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Survival Game")
        self.clock = pg.time.Clock()
        self.running = True
        self.htcd = Cooldown()
        self.hpcd = Cooldown()

    def new(self):
        # create a group for all sprites
        self.all_sprites = pg.sprite.Group()
        self.all_bars = pg.sprite.Group()
        # instantiate classes
        self.health_bar = HealthBar(25, 570, 200, 25, 100, (255,0,0))
        self.health_bar.hp = 100
        self.food_bar = HealthBar(25, 535, 200, 25, 100, (255,165,0))
        self.food_bar.hp = 100
        self.water_bar = HealthBar(25, 500, 200, 25, 100, (0,0,255))
        self.water_bar.hp = 100
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)
        self.run()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.htcd.ticking()
        self.hpcd.ticking()
        self.all_sprites.update()
        if pg.key.get_pressed()[pg.K_q]:
            self.health_bar.hp -= 10
        if self.htcd.delta > 1:
            self.htcd.event_time = pg.time.get_ticks()/1000
            self.food_bar.hp -= 3
            self.water_bar.hp -= 4
        if self.water_bar.hp <= 0 and self.hpcd.delta > 1:
            self.hpcd.event_time = pg.time.get_ticks()/1000
            self.health_bar.hp -= 3
        elif self.water_bar.hp and self.food_bar.hp <= 0 and self.hpcd.delta > 0.1:
            self.hpcd.event_time = pg.time.get_ticks()/1000
            self.health_bar.hp -= 5

        

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # draw the background screen
        self.screen.fill(WHITE)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.health_bar.draw(self.screen)
        self.water_bar.draw(self.screen)
        self.food_bar.draw(self.screen)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

g = Game()
while g.running:
    g.new()

pg.quit()
