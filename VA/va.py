import tkinter as tk
import tkinter.ttk as ttk
import math as math
import random as rnd
import numpy as np

class Particle:

    def __init__(self, canvas, mean_mass=25, spread='default'):
        # mass distribution is lognormal
        # area A = sqrt(Mass) w/ density = pi
        std = {'tight':0.1, "small":0.25, 'moderate':0.5, 'broad':0.75, 'wide':1, 'default':1.2}
        self.canvas = canvas
        mu = np.log(mean_mass) - 0.5*std[spread]**2
        self.mass = np.random.lognormal(mu, std[spread])
        self.radius = math.sqrt(math.sqrt(self.mass))
        self.x = rnd.uniform(self.radius, float(self.canvas['width']) - self.radius)
        self.y = rnd.uniform(self.radius, float(self.canvas['height']) - self.radius)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.color = self.mass_to_color()

    def mass_to_color(self, min_mass=1, mid_mass=50, max_mass=100):
        # float to hexdec colormap

        # real large masses are just white
        if self.mass > 300:
            return "#ffffff"
        # make sure to stay within range no matter the mass
        mass = max(min(self.mass, max_mass), min_mass)

        if mass <= mid_mass:
            # go from turqoise to blue
            t = (mass - min_mass) / (mid_mass - min_mass)
            r = 0
            g = 255*(1-t)
            b = 255
        else:
            # from blue to red
            t = (mass - mid_mass) / (max_mass - mid_mass)
            r = 255*t
            g = 0
            b = 255*(1-t)

        return f"#{int(r):02x}{int(g):02x}{int(b):02x}"

    def update_position(self):
        # positional update from velocity
        self.x += self.vx
        self.y += self.vy
        self.canvas.move(self.id, self.vx, self.vy)
        
        r = self.radius
        restitution = 1.0

        # bouncy wall
        if self.x - r < 0:
            self.x = r
            self.vx = -self.vx * restitution
        elif self.x + r > int(self.canvas['width']):
            self.x = int(self.canvas['width']) - r
            self.vx = -self.vx * restitution

        if self.y - r < 0:
            self.y = r
            self.vy = -self.vy * restitution
        elif self.y + r > int(self.canvas['height']):
            self.y = int(self.canvas['height']) - r
            self.vy = -self.vy * restitution

    def update_velocity(self):
        # velocity updates from acc
        self.vx += self.ax
        self.vy += self.ay

class Simulation:

    def __init__(self, root):
        self.root = root
        self.root.title('God damn balls! 🔴')
        
        # Screen settings px
        self.screen_width = 2560
        self.screen_height = 1200

        # Standard particle generation, log-normal distribution of mass
        # Standard values
        self.particles = []
        self.num_particles = 50
        self.mean_mass = 25
        self.G = 0.5
        self.dt = 0.016
        self.sim_hz = tk.DoubleVar(value=32)

        self.running = False
        self.after_id = None

        self.top_frame = tk.Frame(root, width=self.screen_width)
        self.top_frame.pack()
        title_label = tk.Label(master=self.top_frame, text='God damn balls! 🔴', font=('Arial',12))
        title_label.pack()
        cheat_hint_label = tk.Label(master=self.top_frame, text="Hint: ← ↓ → ↑", font=('Arial',8))
        cheat_hint_label.pack()
        self.money_label = tk.Label(master=self.top_frame, text="", font=('Arial',10))
        self.money_label.pack()

        self.canvas = tk.Canvas(root,
                                width=self.screen_width,
                                height=self.screen_height,
                                bg='black')
        self.canvas.pack()

        self.bottom_frame = tk.Frame(root, bg="#fef2c8")
        self.bottom_frame.pack()

        # Buttons / sliders / settings / entries

        # slider
        slider_frame = tk.Frame(master=self.bottom_frame, bg="#fef2c8", width=25)
        slider_frame.pack(side=tk.RIGHT)
        slider_entry = tk.Scale(slider_frame,
                                    from_=1000, to=0.5, resolution=0.5, 
                                    orient='vertical', variable=self.sim_hz,
                                    label='Simulation speed'
                                    )
        slider_entry.set(32)
        slider_entry.pack()

        # buttons
        button_frame = tk.Frame(master=self.bottom_frame, bg="#fef2c8")
        button_frame.pack(side=tk.RIGHT,pady=10)

        self.start_button = ttk.Button(button_frame, text='Start', command=self.start_simulation)
        self.pause_button = ttk.Button(button_frame, text='Pause', command=self.pause_simulation)
        self.start_button.pack(side=tk.LEFT, padx=5), self.pause_button.pack(side=tk.LEFT, padx=5)
        self.pause_button.config(state="disabled")

        # entries

        input_frame = tk.Frame(master=self.bottom_frame, bg="#fef2c8")
        input_frame.pack(side=tk.RIGHT, pady=10)

        mean_frame = tk.Frame(input_frame, bg="#fef2c8", width=25)
        mean_frame.pack()
        self.mean_entry = tk.Entry(mean_frame, fg="black", bg="white", width=25)
        self.mean_label = tk.Label(mean_frame, text=f'Mean mass (1-200) | Current: {self.mean_mass}', bg="#fef2c8")

        n_particles_frame = tk.Frame(input_frame, bg="#fef2c8", width=25)
        n_particles_frame.pack()
        self.n_particles_entry = tk.Entry(n_particles_frame, fg="black", bg="white", width=25)
        self.n_particles_label = tk.Label(n_particles_frame, text=f'N particles (1-200) | Current: {self.num_particles}', bg="#fef2c8")

        self.mean_label.pack(), self.mean_entry.pack(padx=5) 
        self.n_particles_label.pack(), self.n_particles_entry.pack(padx=5)

        # Cheats and $$$ label thingy majingy
        self.money = 0
        self.history = ['']*4
        root.bind_all('<Key>', self.on_key)


    def on_key(self, event):
        # press correct keys in correct order get many roubles
        k = event.keysym
        if k in ["Left", "Down", "Right", "Up"]:
            self.history = self.history[1:] + [k]

            if self.history == ["Left", "Down", "Right", "Up"]:
                self.money += 250000
                self.history = ['']*4
                self.money_label.config(text=f'{self.money} ₽₽₽', fg='black')

    def create_particles(self):
        self.canvas.delete('all')
        self.particles.clear()
        for _ in range(self.num_particles):
            particle = Particle(
                canvas=self.canvas,
                mean_mass=self.mean_mass,
                spread='default')
            
            particle.id = self.canvas.create_oval(
                particle.x - particle.radius,
                particle.y - particle.radius,
                particle.x + particle.radius,
                particle.y + particle.radius,
                fill=particle.color
            )
            self.particles.append(particle)

    def update_particles(self):
        # update acc
        # update vel
        # update pos
        self.update_acc()
        for particle in self.particles:
            particle.update_velocity()
            particle.update_position()

    def update_acc(self):
        particles = self.particles
        n_particles = len(particles)
        # maybe unneccessary
        ax, ay = [0]*n_particles, [0]*n_particles

        i = 0
        while i < len(particles):
            p1 = particles[i]
            j = i+1
            while j < len(particles):
                p2 = particles[j]
                
                # F = G m1 m2 / dist*2, force direction given by vec (x2-x1)/dist -> F = Gm1m2(x2-x1)/dist**3
                # a1 = Gm2(x2-x1)/dist**3
                # a2 = -Gm1(x2-x1)/dist**3
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                dist = math.sqrt((dx)**2 + (dy)**2)
    
                facx, facy = self.G*dx/dist**3, self.G*dy/dist**3
                ax[i] += facx*p2.mass
                ay[i] += facy*p2.mass
                ax[j] += -facx*p1.mass
                ay[j] += -facy*p1.mass

                j += 1
            i += 1
        
        # All acc for ea particle done, now update each particle obj.
        for i, p in enumerate(particles):
            p.ax, p.ay = ax[i], ay[i]

    def start_simulation(self):
        self._stop_loop()
        mean_entry = self.mean_entry.get()

        # try to convert user input to numbers, 
        # if error or outsided hardcoded range 
        # go to default value or range boundary
        try:
            mean_entry = float(mean_entry)
            mean_entry = min(max(mean_entry,1), 200)
            self.mean_mass = mean_entry
        except ValueError:
            self.mean_mass = 25
            pass
        n_particles_entry = self.n_particles_entry.get()
        try:
            n_particles_entry = int(n_particles_entry)
            n_particles_entry = min(max(1, n_particles_entry), 200)
            self.num_particles = n_particles_entry
        except ValueError:
            self.num_particles = 50

        # button updates
        self.mean_label.config(text=f'Mean mass (1-200) | Current: {self.mean_mass}')
        self.n_particles_label.config(text=f'N particles (1-200) | Current: {self.num_particles}')
        self.pause_button.config(state="normal", text="Pause")
        self.start_button.config(text="Restart")

        self.running = True
        self.create_particles()
        self._schedule_next()

    def _schedule_next(self):
        # hz to milisec
        milisec = 1000/self.sim_hz.get()
        self.after_id = self.root.after(int(milisec), self.update_simulation)

    def _stop_loop(self):
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

    def pause_simulation(self):
        if self.running:
            self.running = False
            self.pause_button.config(text='Play')
            self._stop_loop()
        else:
            self.running = True
            self.pause_button.config(text='Pause')
            self._schedule_next()

    def handle_particle_collision(self):
        # [p0, p1, p2, ..., pn-1]
        # pass into function self.particles[1:] ? 
        # is p2 pos + radius within p1 circle?
        i = 0
        particles = self.particles
        while i < len(particles):
            p1 = particles[i]
            j = i+1
            merged = False
            while j < len(particles):
                p2 = particles[j]
                if self.check_particle_collision(p1, p2):
                    self.merge_particle_params(p1,p2)
                    self.canvas.itemconfig(p1.id, fill=p1.color, outline='')
                    self.canvas.coords(p1.id, p1.x - p1.radius, p1.y - p1.radius, p1.x + p1.radius, p1.y + p1.radius)

                    self.canvas.delete(p2.id)
                    particles.pop(j)
                    merged = True
                else:
                    j += 1
            if not merged:
                i += 1

    def check_particle_collision(self, p1: Particle,p2: Particle) -> bool:
        # collide if dist**2 <= total radius **2
        center_distance  = (p1.x - p2.x)**2 + (p1.y - p2.y)**2
        total_radius = (p1.radius + p2.radius)**2
        if center_distance <= total_radius:
            return True
        else:
            return False
    
    def merge_particle_params(self, p1:Particle, p2: Particle):
        # New particle params
        new_mass = p1.mass + p2.mass
        new_radius = math.sqrt(math.sqrt(new_mass))
        new_x  = (p1.mass * p1.x + p2.mass * p2.x)/new_mass
        new_y  = (p1.mass * p1.y + p2.mass * p2.y)/new_mass
        new_vx = (p1.mass * p1.vx + p2.mass * p2.vx)/new_mass
        new_vy = (p1.mass * p1.vy + p2.mass * p2.vy)/new_mass

        # Update p1
        p1.mass = new_mass
        p1.color = p1.mass_to_color()
        p1.radius = new_radius
        p1.x, p1.y = new_x, new_y
        p1.vx, p1.vy = new_vx, new_vy

    def update_simulation(self):
        if not self.running:
            return
        self.update_particles()
        self.handle_particle_collision()
        self._schedule_next()
        


def main():

    window = tk.Tk()
    program = Simulation(window)
    window.mainloop()

if __name__ == "__main__":
    main()