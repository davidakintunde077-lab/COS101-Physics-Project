"""
COS 101 Physics Project: Five physics formulas.
"""

def acceleration(final_velocity, initial_velocity, time):
    """a = (v - u) / t"""
    if time == 0:
        raise ValueError("Time cannot be zero.")
    return (final_velocity - initial_velocity) / time


def momentum(mass, velocity):
    """p = m * v"""
    return mass * velocity


def frequency(period):
    """f = 1 / T"""
    if period == 0:
        raise ValueError("Period cannot be zero.")
    return 1 / period


def wave_speed(frequency, wavelength):
    """v = f * wavelength"""
    return frequency * wavelength


def gravitational_force(G, mass1, mass2, distance):
    """F = G * m1 * m2 / r**2"""
    if distance == 0:
        raise ValueError("Distance cannot be zero.")
    return (G * mass1 * mass2) / (distance ** 2)


if __name__ == "__main__":
    print("Acceleration:", acceleration(20, 5, 3), "m/s^2")
    print("Momentum:", momentum(2, 10), "kg m/s")
    print("Frequency:", frequency(0.5), "Hz")
    print("Wave speed:", wave_speed(5, 2), "m/s")
    print("Gravitational force:", gravitational_force(6.674e-11, 5, 10, 2), "N")
