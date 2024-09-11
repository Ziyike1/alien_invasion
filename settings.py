class Settings:
    """储存所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        self.ship_speed = 2.2

        # 子弹设置
        self.bullet_speed = 2.6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3