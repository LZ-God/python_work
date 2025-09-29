import sys
import pygame
from settings import Settings
from pea_shooter import PeaShooter

class Pvz1:
    """初始化游戏并且创建游戏资源"""
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        self.pea_shooter=PeaShooter(self)
    def run_game(self):
        """设置游戏持续运行的循环"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            self.pea_shooter.update()

    def _check_events(self):
        """响应键鼠事件"""
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    self._check_keydown(event)
                elif event.type==pygame.KEYUP:
                    self._check_keyup(event)
         
    def _check_keydown(self,event):
         """响应按下"""
         if event.key==pygame.K_UP:
            self.pea_shooter.move_up=True
         elif event.key==pygame.K_DOWN:
            self.pea_shooter.move_down=True
         elif event.key==pygame.K_RIGHT:
            self.pea_shooter.move_right=True
         elif event.key==pygame.K_LEFT:
            self.pea_shooter.move_left=True
         elif event.key==pygame.K_ESCAPE:
             sys.exit()

    def _check_keyup(self,event):
        """响应把键抬起"""
        if event.key==pygame.K_UP:
            self.pea_shooter.move_up=False
        elif event.key==pygame.K_DOWN:
            self.pea_shooter.move_down=False
        elif event.key==pygame.K_RIGHT:
            self.pea_shooter.move_right=False
        elif event.key==pygame.K_LEFT:
            self.pea_shooter.move_left=False 


    def _update_screen(self):
         """更新屏幕"""
         self.screen.fill(self.settings.bg_color)
         self.pea_shooter.blitme()
         pygame.display.flip()



if __name__=='__main__':
    pvz1=Pvz1()
    pvz1.run_game()