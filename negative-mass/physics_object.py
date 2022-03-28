import numpy as np

class PhysicsObject:
    G = 6.67430 * 10**-11
    
    def __init__(self, mass, initial_position, initial_velocity = [0.0,0.0]):
        # in kg
        self.mass = mass
        # in m
        self.pos = np.array(initial_position)
        # in m/s
        self.v = np.array(initial_velocity)
        # in N
        self.forces = []

    def get_Fg (self, obj):
        # compute constants related to change in pos
        r = obj.pos - self.pos
        r_mag = np.dot(r, r)**0.5
        r_hat = r / r_mag
        
        # gravity force
        Fg = r_hat * PhysicsObject.G * self.mass * obj.mass / r_mag**2
        
        return Fg
    
    def add_pending_force(self, force):
        # add pending forces
        self.forces.append(force)
    
    def get_net_force(self):
        # sum pending forces
        return np.sum(self.forces, axis=0)
    
    def apply_forces(self, dt):
        # sum forces and clear
        net_force = self.get_net_force()
        
        self.forces = []
        
        # find acceleration
        a = net_force / self.mass
        
        # find new position and velocity given constant a
        delta_pos = 0.5 * a * dt**2 + self.v * dt
        self.pos += delta_pos
        self.v += a * dt
        
        return delta_pos