import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            # (0,0), pygame.FULLSCREEN
        )
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_events()
            self.bullets.update()
            self.clock.tick(60)

    def _check_events(self):
        """倾听键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_events(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()

    def fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

if __name__ == '__main__':
    # """创建游戏实例并运行游戏"""
    game = AlienInvasion()
    game.run_game()
