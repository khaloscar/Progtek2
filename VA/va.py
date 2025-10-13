import tkinter as tk
import tkinter.ttk as ttk
import math as math
import random as rnd
import numpy as np

class Particle:

    def __init__(self, canvas, mean_mass=20, spread='default', width=800, height=600):
        std = {'tight':0.1, "small":0.25, 'moderate':0.5, 'broad':0.75, 'wide':1, 'default':1.2}
        self.canvas = canvas
        mu = np.log(mean_mass) - 0.5*std[spread]**2
        self.mass = np.random.lognormal(mu, std[spread])
        self.radius = math.sqrt(self.mass)
        self.x = rnd.uniform(self.radius, width - self.radius)
        self.y = rnd.uniform(self.radius, height - self.radius)
        self.vx = rnd.uniform(-1,1)/2
        self.vy = rnd.uniform(-1,1)/2
        self.color = self.mass_to_color()

    def mass_to_color(self, min_mass=1, mid_mass=100, max_mass=200):
        # Clamp mass safely
        mass = max(min(self.mass, max_mass), min_mass)
  
        # Define RGB anchors
        c1 = (0, 255, 255)  # turquoise
        c2 = (0, 0, 255)    # blue
        c3 = (255, 0, 0)    # red

        if mass <= mid_mass:
            # Interpolate from c1 → c2
            t = (mass - min_mass) / (mid_mass - min_mass)
            r = int(c1[0] + t * (c2[0] - c1[0]))
            g = int(c1[1] + t * (c2[1] - c1[1]))
            b = int(c1[2] + t * (c2[2] - c1[2]))
        else:
            # Interpolate from c2 → c3
            t = (mass - mid_mass) / (max_mass - mid_mass)
            r = int(c2[0] + t * (c3[0] - c2[0]))
            g = int(c2[1] + t * (c3[1] - c2[1]))
            b = int(c2[2] + t * (c3[2] - c2[2]))

        return f"#{r:02x}{g:02x}{b:02x}"
    
    def update_position(self):
        self.x += self.vx
        self.y += self.vy
        self.canvas.move(self.id, self.vx, self.vy)

class Simulation:

    def __init__(self, root):
        self.root = root
        self.root.title('God damn balls! 🔴')
        
        # Screen settings 
        self.screen_width = 800
        self.screen_height = 600

        self.canvas = tk.Canvas(root,
                                width=self.screen_width,
                                height=self.screen_height,
                                bg='black')
        self.canvas.pack()

        # Standard particle generation, log-normal distribution of mass
        self.particles = []
        self.num_particles = 50
        self.mean_mass = 20

        # Buttons
        button_frame = tk.Frame(master=root, bg="#fef2c8")
        button_frame.pack(pady=10)

        self.start_button = ttk.Button(button_frame, text='Start', command=self.start_simulation)
        self.pause_button = ttk.Button(button_frame, text='Pause', command=self.pause_simulation)
        self.start_button.pack(side=tk.LEFT, padx=5), self.pause_button.pack(side=tk.LEFT, padx=5)
        # Inputs/settings

        self.running = False

    def create_particles(self):
        self.canvas.delete('all')
        self.particles.clear()
        for _ in range(self.num_particles):
            particle = Particle(
                canvas=self.canvas,
                mean_mass=self.mean_mass,
                spread='default',
                width=self.screen_width,
                height=self.screen_height)
            
            particle.id = self.canvas.create_oval(
                particle.x - particle.radius,
                particle.y - particle.radius,
                particle.x + particle.radius,
                particle.y + particle.radius,
                fill=particle.color
            )
            self.particles.append(particle)

    def move_particles(self):
        for particle in self.particles:
            particle.update_position()

    def start_simulation(self):
        self.running = True
        self.create_particles()
        self.root.after(10, self.update_simulation)

    def pause_simulation(self):
        self.running = False

    def update_simulation(self):
        if not self.running:
            return
        self.move_particles()
        self.root.update()
        self.root.after(10, self.update_simulation)
        

def main():

    window = tk.Tk()
    program = Simulation(window)
    window.mainloop()


if __name__ == "__main__":
    main()