from itertools import zip_longest


# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name=str, greeting_template=f"Hello, <name>"):
    greeting_template = f'Hello, {name}!'
    return greeting_template


def force(mass=float, body="earth"):
    bodies = ["MERCURY", "VENUS", "EARTH", "MOON", "MARS", "JUPITER", "SATURN", "URANUS", "NEPTUNE", "PLUTO", "SUN"]
    bodies = ([str(high).lower() for high in bodies])
    gravity = [3.7, 8.9, 9.8, 1.6, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7, 274.4]
    body_gravity = dict(zip_longest(bodies, gravity))
    return mass * body_gravity[body]


def pull(m1, m2, d):
    pull = 6.674e-11 * ((m1*m2)/d**2)
    return pull

