import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船所发射的子弹的类"""

    def __init__(self, game):
        """在飞船的位置创建一个子弹对象"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = game.settings.bullet_color

        # 在(0,0)处创建一个子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)