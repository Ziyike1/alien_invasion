import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self,game):
        """初始化飞船并设置其初始位置"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # """加载飞船图像并获得其外接矩形"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.midbottom = (400,600)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.rect.x += 1

        if self.moving_left:
            self.rect.x -= 1


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)