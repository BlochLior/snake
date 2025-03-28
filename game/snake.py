# snake movement, growth and turning mechanics; snake logic
from game.constants import pygame
from game.constants import SNAKE_SPEED, COLOR_PINK

class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, position, segment_before=None, segment_after=None, is_head=False, is_tail=False):
        super().__init__()  # Initialize the parent class
        self.is_head = is_head
        self.is_tail = is_tail
        self.segment_before = segment_before
        self.segment_after = segment_after
        self.position = position

class Snake(SnakeSegment):
    def __init__(self, score=0, direction=(0, -1), speed=SNAKE_SPEED):
        self.head = SnakeSegment(is_head=True, position=(100, 100))
        self.tail = SnakeSegment(is_tail=True, position=(100, 110))
        self.segments = [self.head, self.tail]
        self.segment_count = len(self.segments)
        self.speed = speed
        self.score = score
        self.direction = direction
        self.update_segment_position()
    
    def move(self):
        # store the positions of all existing segments:
        previous_positions = [segment.position for segment in self.segments]

        # move head in current direction:
        new_x = self.head.position[0] + self.direction[0]
        new_y = self.head.position[1] + self.direction[1]
        self.head.position = (new_x, new_y)

        for i in range(1, len(self.segments)):
            self.segments[i].position = previous_positions[i - 1]
        self.update_segment_position()

    def change_direction(self, new_direction):
        # prevent reverse movement:
        if (
            self.direction[0] != -self.direction[0] or
            self.direction[1] != -self.direction[1]
        ):
            self.direction = new_direction

    def draw_snake(self, screen):
        for segment in self.segments:
            # can update later to make head and tail look diff
            pygame.draw.rect(screen, COLOR_PINK,
                                pygame.Rect(
                                    segment.position[0],
                                    segment.position[1],
                                    10,
                                    10
                                )
                            )

    def update_segment_position(self):
        for i in range(len(self.segments)):
            if i == 0:
                self.segments[i].segment_after = self.segments[1]
                continue
            if i == len(self.segments) - 1:
                self.segments[i].segment_before = self.segments[i - 1]
                break
            self.segments[i].segment_before = self.segments[i - 1]
            self.segments[i].segment_after = self.segments[i + 1]

    def add_segment(self):
        new_position = self.tail.position
        self.segments.append(SnakeSegment(position=new_position))
        self.update_segment_position()

    def check_food_colision(self, food):
        if self.head.position == food.position:
            self.add_segment()
            self.score += 1
            return True
        return False