import numpy as np


class SIE:

    def __init__(self):
        pass

    def potential(self, phi, theta, f, theta_E):
        """
        SIE potential from Kormann et al 1994, eqn 26a
        :param phi: angular coordinate
        :param theta: radial coordinate
        :param f: axis ratio () < f < 1; f -> 1 yields an SIS)
        :param theta_E: Einstein radius
        :return: The SIE potential evaluated at the given values
        """
        f_prime = np.sqrt(1-f**2.)
        prefactor = (np.sqrt(f)*theta)/f_prime
        sin_term = np.sin(phi)*np.arcsin(f_prime*np.sin(phi))
        cos_term = np.cos(phi)*np.arcsinh((f_prime/f)*np.cos(phi))
        potential = theta_E*prefactor*(sin_term+cos_term)
        return potential
