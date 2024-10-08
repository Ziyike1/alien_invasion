import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self,game):
        """初始化飞船并设置其初始位置"""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # """加载飞船图像并获得其外接矩形"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.midbottom = (400,600)

        # 在飞船的属性x中储存一个浮点数
        self.x = float(self.rect.x)

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 使用浮点数x的值来更新飞船位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 根据self.x更行rect对象
        self.rect.x = self.x


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """将飞船位置居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)