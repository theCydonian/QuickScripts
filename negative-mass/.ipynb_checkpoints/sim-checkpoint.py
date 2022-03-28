import numpy as np
import cv2 as cv

class Simulation:
    def __init__(self, 
                 objs, 
                 step_size=20):
        
        self.objs = objs
        # in ms
        self.step_size = step_size
    
    def step(self):
        # compute gravity forces between each pair
        for i in range(len(self.objs)):
            for j in range(len(self.objs))[i+1:]:
                obj1 = self.objs[i]
                obj2 = self.objs[j]
                
                F_g = obj1.get_Fg(obj2)
                
                obj1.add_pending_force(F_g)
                obj2.add_pending_force(-1 * F_g)
        
        x = []
        y = []
        # apply forces
        for obj in self.objs:
            obj.apply_forces(self.step_size / 1000)
            x.append(obj.pos[0])
            y.append(obj.pos[1])

        return x,y

    def get_positions(self):
        x = []
        y = []
        # apply forces
        for obj in self.objs:
            x.append(obj.pos[0])
            y.append(obj.pos[1])

        return x,y