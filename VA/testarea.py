import numpy as np
import matplotlib.pyplot as plt

def mass_to_color(mass, min_mass=1, mid_mass=50, max_mass=100):
    if mass> 300:
        return "#ffffff"
    # Clamp mass safely
    mass = max(min(mass, max_mass), min_mass)

    # Define RGB anchors
    c1 = (0, 255, 255)  # turquoise
    c2 = (0, 0, 255)    # blue
    c3 = (255, 0, 0)    # red

    if mass <= mid_mass:
        # Interpolate from c1 → c2
        t = (mass - min_mass) / (mid_mass - min_mass)
        r = 0
        g = 255*(1-t)
        b = 255
    else:
        # Interpolate from c2 → c3
        t = (mass - mid_mass) / (max_mass - mid_mass)
        r = 255*t
        g = 0
        b = 255*(1-t)

    return f"#{int(r):02x}{int(g):02x}{int(b):02x}"

def print_hex(text, hex_color):
    # Remove the leading "#" and parse
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    # Create the ANSI true-color escape sequence
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

for i in range(-150, 150):
    print(mass_to_color(i))

print()
print(mass_to_color(65.6))
print(mass_to_color(106.56432423423))

a = ['ass', 'class', 'fast', 'last']
for i, e in enumerate(a):
    print(f'{i} and {e}')





################################
##      OLD BUT GOLD BITCH    ##
################################

if False:
    def mass_to_color_3pt(mass, min_mass=101, max_mass=201):
        # Clamp mass safely
        mass = max(min(mass, max_mass), min_mass)

        # Define RGB anchors
        c1 = (0, 255, 255)  # turquoise
        c2 = (0, 0, 255)    # blue
        c3 = (255, 0, 0)    # red

        if mass <= max_mass//2:
            # Interpolate from c1 → c2
            t = (mass - min_mass) / (max_mass//2 - min_mass)
            r = int(c1[0] + t * (c2[0] - c1[0]))
            g = int(c1[1] + t * (c2[1] - c1[1]))
            b = int(c1[2] + t * (c2[2] - c1[2]))
        else:
            # Interpolate from c2 → c3
            t = (mass - max_mass//2) / (max_mass - max_mass//2)
            r = int(c2[0] + t * (c3[0] - c2[0]))
            g = int(c2[1] + t * (c3[1] - c2[1]))
            b = int(c2[2] + t * (c3[2] - c2[2]))

        return f"#{r:02x}{g:02x}{b:02x}"

    def mass_to_color_4pt(mass, min_mass=101, max_mass=201):
        # Clamp to range
        m = max(min(mass, max_mass), min_mass)

        # Normalize 0–1
        t = (m - min_mass) / (max_mass - min_mass)

        # Define anchors
        c1 = (0, 255, 255)   # turquoise
        c2 = (0, 0, 255)     # blue
        c3 = (255, 0, 255)   # magenta
        c4 = (255, 0, 0)     # red

        # Divide gradient into three equal parts
        if t < 1/3:
            # turquoise → blue
            t2 = t / (1/3)
            r = int(c1[0] + (c2[0] - c1[0]) * t2)
            g = int(c1[1] + (c2[1] - c1[1]) * t2)
            b = int(c1[2] + (c2[2] - c1[2]) * t2)
        elif t < 2/3:
            # blue → magenta
            t2 = (t - 1/3) / (1/3)
            r = int(c2[0] + (c3[0] - c2[0]) * t2)
            g = int(c2[1] + (c3[1] - c2[1]) * t2)
            b = int(c2[2] + (c3[2] - c2[2]) * t2)
        else:
            # magenta → red
            t2 = (t - 2/3) / (1/3)
            r = int(c3[0] + (c4[0] - c3[0]) * t2)
            g = int(c3[1] + (c4[1] - c3[1]) * t2)
            b = int(c3[2] + (c4[2] - c3[2]) * t2)

        return f"#{r:02x}{g:02x}{b:02x}"

    def print_hex(text, hex_color):
        # Remove the leading "#" and parse
        hex_color = hex_color.lstrip("#")
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        # Create the ANSI true-color escape sequence
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    values = [1]
    values += [i*10 for i in range(1,11)]
    values = [i for i in range(1,301)]
    print(values)
    i = 1
    for c in values:
        color3pt = mass_to_color_3pt(c)
        color3pt = print_hex(color3pt, color3pt)

        color4pt = mass_to_color_4pt(c)
        color4pt = print_hex(color4pt, color4pt)

        print(f'{i} | 3pt: {color3pt} | 4pt: {color4pt}')
        i +=1

if False:
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = screen_width/3
    window_height = screen_height/3

    window_pos_x = (screen_width - window_width)//2
    window_pos_y = (screen_height - window_height)//2

    frame1 = tk.Frame(master=window, width=int(window_width), height=150, bg="lightgrey")
    frame1.pack(side=tk.TOP)

    frame2 = tk.Frame(master=window, width=int(window_width-200), height=int(window_width-200), bg="#fef2c8")
    frame2.pack(side=tk.LEFT)

    frame3 = tk.Frame(master=window, width=200, height=int(window_width-200), bg='lightgray')
    frame3.pack(side=tk.LEFT) 

    window.title('Is this centered??')
    window.geometry(newGeometry=f"{int(window_width)}x{int(window_width-200)+150}+{int(window_pos_x)}+{int(window_pos_y)}")