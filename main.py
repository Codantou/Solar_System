from vpython import *

Sun = sphere(pos=vector(0, 0, 0), radius=100,
             texture="https://upload.wikimedia.org/wikipedia/commons/b/b4/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg")
Mercury = sphere(pos=vector(190, 0, 0), radius=38,
                 texture="https://upload.wikimedia.org/wikipedia/commons/3/30/Mercury_in_color_-_Prockter07_centered.jpg")
Venus = sphere(pos=vector(400, 0, 0), radius=44,
               texture="https://upload.wikimedia.org/wikipedia/commons/1/19/Cylindrical_Map_of_Venus.jpg")
Earth = sphere(pos=vector(600, 0, 0), radius=60, texture=textures.earth)
Mars = sphere(pos=vector(750, 0, 0), radius=33,
              texture="https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg")
Jupiter = sphere(pos=vector(1000, 0, 0), radius=80,
                 texture="https://upload.wikimedia.org/wikipedia/commons/e/e2/Jupiter.jpg")
Saturn = sphere(pos=vector(1300, 0, 0), radius=70,
                texture="https://upload.wikimedia.org/wikipedia/commons/b/b4/Saturn_%28planet%29_large.jpg")
Uranus = sphere(pos=vector(1450, 0, 0), radius=39,
                texture="https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg")
Neptune = sphere(pos=vector(1600, 0, 0), radius=38,
                 texture="https://upload.wikimedia.org/wikipedia/commons/5/56/Neptune_Full.jpg")
Earth.v = vector(0, -100, 0)
t = 0
dt = 0.01
alpha = 15
while t < 2400:
    rate(10)
    Mercury.rotate(angle=0.00350, axis=vector(0, 1, 0), origin=Mercury.pos)
    Venus.rotate(angle=0.00244, axis=vector(0, 1, 0), origin=Venus.pos)
    Earth.pos = Earth.pos - vector(600*sin(50*t), 600*cos(50*t), 0)
    Earth.rotate(angle=0.0408, axis=vector(0, 1, 0), origin=Earth.pos)
    Mars.rotate(angle=0.0439, axis=vector(0, 1, 0), origin=Mars.pos)
    Jupiter.rotate(angle=0.0541, axis=vector(0, 1, 0), origin=Jupiter.pos)
    Saturn.rotate(angle=0.0460, axis=vector(0, 1, 0), origin=Saturn.pos)
    Uranus.rotate(angle=0.0750, axis=vector(0, 1, 0), origin=Uranus.pos)
    Neptune.rotate(angle=0.0490, axis=vector(0, 1, 0), origin=Neptune.pos)
    t += dt
