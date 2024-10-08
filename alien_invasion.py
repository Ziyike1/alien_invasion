import sys
from time import sleep
import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


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

        # 创建一个用于储存游戏统计信息的实例以及记分牌
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # 游戏启动后设置为False
        self.game_active = False

        # 创建play按钮
        self.play_button = Button(self, "Play")


    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()

            self._update_events()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """响应按下"""

        if event.key == pygame.K_p and not self.game_active:
            self._start_game()

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
        self.aliens.draw(self.screen)

        # 显示得分
        self.scoreboard.show_score()

        # 游戏处于非活动状态，则绘制play按钮
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """更新子弹的位置并消除消失的子弹"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_collisions()

    def _check_collisions(self):
        # 检查是否有子弹击中了外星人, 并删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)

        # 删除现有的子弹并创建新的外星舰队
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _create_alien(self, x_position, y_position):
        """创建一个外星人并将其加入舰队中"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """更新舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
             self._ship_hit()

        # 检测是否有外星人碰撞屏幕下边缘
        self._check_hit_bottom()


    def _create_fleet(self):
        """创建一个外星人舰队"""
        alien = Alien(self)
        self.aliens.add(alien)

        alien_width = alien.rect.width
        alien_height = alien.rect.height
        current_x = alien_width
        current_y = alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 1 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 1.5 * alien_width

            # 添加一行外星人后，重置x值并递增y值
            current_x = alien_width
            current_y += alien_height * 2

        # count = 0
        # while count < 7:
        #     new_alien = Alien(self)
        #     new_alien.x = alien.x + (count*100)
        #     new_alien.rect.x = new_alien.x
        #     self.aliens.add(new_alien)
        #     count += 1


    def _check_fleet_edges(self):
        """检测外星人碰撞屏幕边缘并采取相应措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """向下移动整个外星人舰队，并改变方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """响应飞船和外星人的碰撞"""

        if self.stats.ship_remains > 0:
            self.stats.ship_remains -= 1
            self.bullets.empty()
            self.aliens.empty()

            # 创建一个新的外星舰队
            self._create_fleet()
            self.ship.center_ship()

            # 暂停一段时间
            sleep(2)

        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_hit_bottom(self):
        """响应外星人碰撞屏幕的下边缘"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom > self.settings.screen_height + 10:
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """点击play按钮时开始新游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        """开始新游戏时的设置"""

        # 还原游戏设置
        self.settings.initialize_dynamic_settings()

        # 重置统计信息
        self.stats.reset_stats()
        self.game_active = True

        # 清空外星人列表和子弹列表
        self.bullets.empty()
        self.aliens.empty()

        # 创建一个新的外星舰队
        self._create_fleet()
        self.ship.center_ship()

        # 隐藏光标
        pygame.mouse.set_visible(False)


if __name__ == '__main__':
    # """创建游戏实例并运行游戏"""
    game = AlienInvasion()
    game.run_game()