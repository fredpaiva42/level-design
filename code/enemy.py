import pygame
from tiles import AnimatedTile
from random import randint


class Enemy(AnimatedTile):
    def __init__(self, size, x, y, path ,type):
        super().__init__(size, x, y, path)
        self.alive = True
        self.frame_index = 0
        self.animation_speed = 0.5
        if type == 'run':
            self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3, 5)

    def move(self):
        self.rect.x += self.speed

    def reverse_image(self):
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def update(self, shift):
        if self.alive:
            self.rect.x -= shift
        self.animate()
        if self.alive:
            self.move()
        self.reverse_image()

class Boss(Enemy):
    def __init__(self, size, x, y, path ,type):
        super().__init__(size, x, y, path, type)
        self.total_hp = 150
        self.hp = 150
        self.speed = 2

        # health bar
        self.bar_max_width = 300
        self.bar_height = 8

    def show_boss_health(self, display_surface):
        current_health_ratio = self.hp / self.total_hp
        current_bar_width = self.bar_max_width * current_health_ratio
        pygame.draw.rect(display_surface, '#FF0044', (550,120,int(current_bar_width),20))
