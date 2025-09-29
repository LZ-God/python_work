import pygame
class PeaShooter:
    def __init__(self,pvz1):
        """初始化豌豆射手及其初始位置"""
        self.screen=pvz1.screen
        self.screen_rect=pvz1.screen.get_rect()
        self.pea_shooter_image=pygame.image.load(r"D:\python-work\job\pvz1\pea_shooter.png")
        self.pea_shooter_rect=self.pea_shooter_image.get_rect()
        self.pea_shooter_rect.midleft=self.screen_rect.midleft
    
    def blitme(self):
        """在指定位置绘制豌豆射手"""
        self.screen.blit(self.pea_shooter_image,self.pea_shooter_rect)
        