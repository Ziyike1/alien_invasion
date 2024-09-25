class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, game):
        """初始化统计信息"""
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        """初始化运行期间可能变化的统计信息"""
        self.ship_remains = self.settings.ship_limit
