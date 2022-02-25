import pymunk
import pymunk.pygame_util
import pygame
from pymunk.vec2d import Vec2d

space = pymunk.Space()
space.gravity = 0, 100
b0 = space.static_body
#b0 = (100,0)

def info(body):
    print(f'm={body.mass:.0f} moment={body.moment:.0f}')
    cg = body.center_of_gravity
    print(cg.x, cg.y)

class Box:
    def __init__(self, p0=(10, 10), p1=(690, 690), d=2):
        x0, y0 = p0
        x1, y1 = p1
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for i in range(4):
            segment = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%4], d)
            segment.elasticity = 1
            segment.friction = 1
            space.add(segment)

# class Polygon:
#     def __init__(self, pos, vertices, density=0.1):
#         self.body = pymunk.Body(1, 100)
#         self.body.position = pos

#         shape = pymunk.Poly(self.body, vertices)
#         shape.density = 0.1
#         shape.elasticity = 1
#         space.add(self.body, shape)

class Rectangle:
    def __init__(self, pos, size):
        self.body = pymunk.Body()
        self.body.position = pos

        shape = pymunk.Poly.create_box(self.body, size)
        shape.density = 1000
        shape.elasticity = 1
        shape.friction = 1
        space.add(self.body, shape)
        

def draw_polygon(self, verts:[10,10],radius: 10) -> None:
    ps = [pygame(v, self.surface) for v in verts]
    ps += [ps[0]]


class Poly:

    def __init__(self, pos, size):
        self.body = pymunk.Body()
        self.body.position = pos

        shape = pymunk.Poly(self.body, size)
        shape.density = 1000
        shape.elasticity = 1
        shape.friction = 1
        space.add(self.body, shape)
        
class Segment:
    def __init__(self, p0, v, radius=10, center_of_gravity = (0,0), density=0.01):
        self.body = pymunk.Body()
        self.body.position = p0
        self.radius = radius
        self.v = v
        self.body.center_of_gravity = center_of_gravity
        self.shape = pymunk.Segment(self.body, (0, 0), self.v, radius)
        self.shape.density = density
        self.shape.elasticity = 0
        self.shape.filter = pymunk.ShapeFilter(group=1)
        self.shape.color = (0, 255, 0, 0)
        space.add(self.body, self.shape)

        
class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 700))
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.image.save(self.screen, 'shape.png')

            self.screen.fill((220, 220, 220))
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.01)

        pygame.quit()
        


    
p = Vec2d(400,400)
v = Vec2d(350,0)

Box()
body = pymunk.Body(mass=100, moment=1000)
body.position = (350, 200)
body.apply_impulse_at_local_point((100,0), (0, 1))



class Draw:
    def __init__(self,p0, vx1,vy1,vx2,vy2,vx3,vy3,vx4,vy4, radius=10, center_of_gravity = (0,0), density=0.01):
        self.body = pymunk.Body()
        self.body.position = p0
        s1 = pymunk.Segment(self.body, vx1, vy1 , radius=radius)
        s1.density = density
        s2 = pymunk.Segment(self.body, vx2, vy2, radius=radius)
        s2.density = density
        s3 = pymunk.Segment(self.body, vx3,vy3, radius=radius)
        s3.density = density
        s4 = pymunk.Segment(self.body, vx4,vy4, radius=radius)
        s4.density = density
        sfinal = space.add(self.body, s1,s2,s3,s4)
        


# s1 = pymunk.Segment(body, (-50,0), (0,0), radius=10)
# s2 = pymunk.Segment(body, (0, 0), (0, 100), radius=10)
# s3 = pymunk.Segment(body, (-50, 100), (0, 100), radius=10)
# s4 = pymunk.Segment(body, (50, 100), (0, 100), radius=10)

# s1.density = 100
# s2.density = 100
# s3.density = 100
# s4.density = 100


# sfinal = space.add(body, s1,s2,s3,s4)


S1 = Draw((350, 200),(-50,0), (0,0),(0, 0), (0, 100),(-50, 100), (0, 100),(50, 100), (0, 100))


class PinJoint:
    def __init__(self, b, b2, a=(0, 0), a2=(0, 0)):
        joint = pymunk.constraints.PinJoint(b, b2, a, a2)
        space.add(joint)
        
PinJoint(b0, S1.body, v)


info(body)
App().run()