import pygame
from settings import Settings
class PeaShooter:
    def __init__(self,pvz1):
        """初始化豌豆射手及其初始位置"""
        self.screen=pvz1.screen
        self.screen_rect=pvz1.screen.get_rect()
        self.pea_shooter_image=pygame.image.load(r"D:\python-work\job\job\pvz1\image\pea_shooter.png")
        self.pea_shooter_rect=self.pea_shooter_image.get_rect()
        self.pea_shooter_rect.midleft=self.screen_rect.midleft
        self.settings=Settings()
        self.x=float(self.pea_shooter_rect.x)
        self.y=float(self.pea_shooter_rect.y)
        self.move_right=False
        self.move_left=False
        self.move_up=False
        self.move_down=False

    def update(self):
        """根据移动标志来调整豌豆射手的位置"""
        if self.move_right and self.pea_shooter_rect.right<self.screen_rect.right:
            self.x+=self.settings.pea_shooter_speed
        if self.move_left and self.pea_shooter_rect.left>0:
            self.x-=self.settings.pea_shooter_speed
        if self.move_up and self.pea_shooter_rect.top>0:
            self.y-=self.settings.pea_shooter_speed
        if self.move_down and self.pea_shooter_rect.bottom<self.screen_rect.bottom:
            self.y+=self.settings.pea_shooter_speed

        self.pea_shooter_rect.x=self.x
        self.pea_shooter_rect.y=self.y
    
    def blitme(self):
        """在指定位置绘制豌豆射手"""
        self.screen.blit(self.pea_shooter_image,self.pea_shooter_rect)
        