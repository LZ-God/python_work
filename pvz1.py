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
        self.move_right=False
        self.move_left=False
        self.move_up=False
        self.move_down=False
    def run_game(self):
        """设置游戏持续运行的循环"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """响应键鼠事件"""
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
    
    def _update_screen(self):
         """更新屏幕"""
         self.screen.fill(self.settings.bg_color)
         self.pea_shooter.blitme()
         pygame.display.flip()



if __name__=='__main__':
    pvz1=Pvz1()
    pvz1.run_game()