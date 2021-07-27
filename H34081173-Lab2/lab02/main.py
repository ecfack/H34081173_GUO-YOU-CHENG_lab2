import pygame
import time

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization

# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))

enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (HP_WIDTH, HP_HEIGHT))

hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))

hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))

continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_HEIGHT))

muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_HEIGHT))

pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_HEIGHT))

sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))

# ...(to be done)


# set the title
pygame.display.set_caption("My first game")
# ... (to be done)


class Game:
    def __init__(self):
        # window
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # ...(to be done)

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            # event loop
                # ... (to be done)
            self.clock.tick(FPS)

            #enevt判定
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            # draw background
            #背景位置和渲染
            background_posX=0
            background_posY=0
            self.window.blit(background_image, (background_posX, background_posY))
            # ...(to be done)

            # draw enemy and health bar
            #敵人位置和渲染
            enemy_posX=0
            enemy_posY=WIN_HEIGHT//2-10
            self.window.blit(enemy_image, (enemy_posX,enemy_posY))

            #敵人血條位置和渲染
            HP_bar_shape=[0, WIN_HEIGHT/2-20, 50, 5]
            pygame.draw.rect(self.window, RED, HP_bar_shape)
            # ...(to be done)

            # draw menu (and buttons)
            #menu背景的空間資訊和渲染
            menu_background_shape=[0,0,WIN_WIDTH,100]
            pygame.draw.rect(self.window,BLACK,menu_background_shape)

            #button的位置設定和渲染
            btn_posY=0
            btn_muse_posX=WIN_WIDTH-(BTN_WIDTH*4)
            self.window.blit(muse_image,(btn_muse_posX,btn_posY))

            btn_sound_posX=WIN_WIDTH-(BTN_WIDTH*3)
            self.window.blit(sound_image,(btn_sound_posX,btn_posY))

            btn_conti_posX=WIN_WIDTH-(BTN_WIDTH*2)
            self.window.blit(continue_image,(btn_conti_posX,btn_posY))
            
            btn_pause_posX=WIN_WIDTH-BTN_WIDTH
            self.window.blit(pause_image,(btn_pause_posX,btn_posY))

            #HP位置設定和渲染
            for i in range(0,2):
                for j in range(0,5):
                    HP_posX=WIN_WIDTH/2-2*HP_WIDTH+j*HP_WIDTH
                    HP_posY=HP_HEIGHT*i

                    if(i*5+j<self.hp):
                        self.window.blit(hp_image,(HP_posX,HP_posY))
                    else:
                        self.window.blit(hp_gray_image,(HP_posX,HP_posY))
            # (... to be done)


            # draw time
            #時間單位處理
            duration=pygame.time.get_ticks()
            duration_sec=str((duration//1000)%60).zfill(2)
            duration_min=str((duration//1000)//60)

            #timer文字處理
            timer_font=pygame.font.SysFont("simhei",50)
            timer_text=timer_font.render(duration_min+":"+duration_sec,True,WHITE,BLACK)

            #timer的位置設定和渲染
            timer_posX=0
            timer_posY=WIN_HEIGHT-30
            self.window.blit(timer_text,(timer_posX,timer_posY))
            # ...(to be done)

            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()



