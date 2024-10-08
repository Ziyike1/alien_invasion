class Settings:
    """储存所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (255, 255, 255)
        self.ship_speed = 2.2
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 2.6
        self.bullet_width = 300 # 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed = 1.0
        self.drop_speed = 100 # 10
        self.fleet_direction = 1  # right = 1 , left = -1