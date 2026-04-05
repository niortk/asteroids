import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_state, log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        # must override
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        # must override
        self.position += self.velocity * dt
    
    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius
    
    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)  #<=====generating new random angle 
            new_velocity_1 = self.velocity.rotate(angle)  #<=====new velocity vector for rotation on first object
            new_velocity_2 = self.velocity.rotate(-angle) #<=====new velocity vector for rotation on second object
            new_radius = self.radius - ASTEROID_MIN_RADIUS #<=====new radius for new spawned objects

            new_Asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_Asteroid_1.velocity = new_velocity_1 * 1.2

            new_Asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_Asteroid_2.velocity = new_velocity_2 * 1.2