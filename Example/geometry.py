import cmath, math

class Geometry:

    @staticmethod
    def bhaskara_roots(a, b, c):
        """Find roots using Bhaskara method"""
        delta = b**2 - 4*a*c
        x_1 = (-b + cmath.sqrt(delta)) / 2*a
        x_2 = (-b - cmath.sqrt(delta)) / 2*a

        return x_1, x_2


    @staticmethod
    def rad_to_degrees(rad):
        degrees = rad*180 / math.pi
        return degrees
    @staticmethod
    def not_used():
        not_used_data = 123  # Unused variable

        if True == False:
            print('nothing')

        return True

    # A very long line:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad

# TODO for pylint badge



