class Settings:
    """储存所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (255, 255, 255)
        self.ship_speed = 2.2
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 2.6
        self.bullet_width = 3 # 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed = 1.0
        self.drop_speed = 10 # 10
        self.fleet_direction = 1  # right = 1 , left = -1

        # 游戏难度递增
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化游戏的难度递增设置"""
        self.ship_speed = 2.2
        self.bullet_speed = 2.6
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        """提高游戏难度"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
