from __future__ import division
import math

PI = math.pi

MAP = [[1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 1, 1],
       [1, 1, 1, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1]]

m = None
p = None


class Ray:
    def __init__(self, coords, angle, map_obj):
        self.x = coords[0] 
        self.y = coords[1]
        self.angle = angle
        self.map_obj = map_obj
        
        self._color = color(125, 204, 123)    
    
    def cast(self, _n=0):
        x_direction = 1
        y_direction = 1
        
        if cos(radians(self.angle)) < 0:
            x_direction = -1
            
        if sin(radians(self.angle)) < 0:
            y_direction = -1
        
        # Closest vertical line
        d_to_vertical = 0
        
        if ceil(self.x) == self.x:
            d_to_vertical = abs(1 / cos(radians(self.angle)))
        else:
            d_to_vertical = abs((ceil(self.x) - self.x) / cos(radians(self.angle)))
        
        stroke(color(255, 0, 0))
        fill(color(0, 255, 255))
        circle(d_to_vertical * (self.map_obj.w / self.map_obj.map_size[0]), x_direction, 20)
        
        # Closest horizontal line
        if ceil(self.y) == self.y:
            d_to_horizontal = abs(1 / cos(radians(90 - self.angle)))
        else:
            d_to_horizontal = abs((ceil(self.y) - self.y) / cos(radians(90 - self.angle)))
        
        stroke(color(0, 255, 0))
        fill(color(255, 0, 255))
        circle(d_to_horizontal * (self.map_obj.h / self.map_obj.map_size[1]), y_direction, 20)
        
        # Find pointed tiles
        v_pointed_tile = ()
        h_pointed_tile = ()
        
        ## Vertical line tile
        v_pointed_coords = (
                            floor(self.x) + 1,
                            self.y + sin(radians(self.angle)) * d_to_vertical
                            )
        
        
        if x_direction == 1:            
            v_pointed_tile = (
                            v_pointed_coords[0],
                            floor(v_pointed_coords[1])
                            )
        else:
            if floor(self.x) == self.x:
                v_pointed_tile = (
                                v_pointed_coords[0] - 3,
                                floor(v_pointed_coords[1])
                                )
            else:
                v_pointed_tile = (
                                v_pointed_coords[0] - 2,
                                floor(v_pointed_coords[1])
                                )
        
        ## Horziontal line tile
        h_pointed_coords = (
                            self.x + (cos(radians(self.angle)) * d_to_horizontal),
                            floor(self.y) + 1
                            )
        
        if y_direction == 1:
            h_pointed_tile = (
                            floor(h_pointed_coords[0]),
                            h_pointed_coords[1]
                            )
        else:
            if floor(self.y) == self.y:
                h_pointed_tile = (
                                floor(h_pointed_coords[0]),
                                h_pointed_coords[1] - 3
                                )
            else:
                h_pointed_tile = (
                                floor(h_pointed_coords[0]),
                                h_pointed_coords[1] - 3
                                )
        
        # Draw complete line   
        d = 500
        
        stroke(self._color)
        line(0, 0, d, 0)

class Map:
    def __init__(self, map_data, coords, w, h):
        self.map_data = map_data
        self.x = coords[0]
        self.y = coords[1]
        self.w = w
        self.h = h
        
        self.map_size = (len(map_data[0]), len(map_data))
        
        self.background_color = color(0)
        self.tile_color = color(255)
        
        self._c_background_color = find_complementary(self.background_color)
        self._c_tile_color = find_complementary(self.tile_color)
        
    def draw(self):  
        w_fraction = self.w / self.map_size[0]
        h_fraction = self.h / self.map_size[1]
        
        noStroke()
        for j, row in enumerate(self.map_data):
            current_y = h_fraction * j
            for i, tile in enumerate(row):
                current_x = w_fraction * i
                if tile == 0:
                    stroke(self._c_background_color)
                    fill(self.background_color)
                elif tile == 1:
                    stroke(self._c_tile_color)
                    fill(self.tile_color)
                rectMode(CORNER)
                rect(current_x, current_y, w_fraction, h_fraction)
                
    @classmethod
    def convert_to_display_coords(cls, coords, map_obj):
        x = coords[0]
        y = coords[1]
        
        display_x = (x / map_obj.map_size[0]) * map_obj.w
        display_y = (y / map_obj.map_size[1]) * map_obj.h
        
        return (display_x, display_y)
        

class Player:
    _size = 30
    _color = color(128, 0, 255)
    
    def __init__(self, coords, angle, map_obj):
        self.x = coords[0] # In-map x coord, considering each block is 1 unit wide
        self.y = coords[1] # In-map y coord, considering each block is 1 unit high
        self.angle = angle
        self.map_obj = map_obj
        
    def draw(self):   
        display_coords = Map.convert_to_display_coords([self.x, self.y], self.map_obj)
        display_x = display_coords[0]
        display_y = display_coords[1]
        
        translate(display_x, display_y) # Translate is used so the square rotates around its center
        rotate(radians(self.angle))
        
        self.cast_rays()
        
        stroke(0, 0, 0, 0)
        fill(self._color)
        
        rectMode(CENTER)
        square(0, 0, self._size)
        
    def cast_rays(self):
        new_ray = Ray([self.x, self.y], self.angle, self.map_obj)
        new_ray.cast()
        

def find_complementary(c):
    r = red(c)
    g = green(c)
    b = blue(c)
    
    c_r = 255 - r
    c_g = 255 - g
    c_b = 255 - b
    
    return color(c_r, c_g, c_b)
                            

def setup():
    global m, p, p2
    size(768, 768)
    
    m = Map(MAP, [0, 0], width, height)
    p = Player([4, 3.5], 0, m)
    
def draw():
    ## Draw
    m.draw()
    p.draw()
    
    p.angle = p.angle + 0.2
    
    print
    
