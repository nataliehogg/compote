import numpy as np


class SIE:

    def __init__(self, phi, theta, f, theta_E):
        """
        :param phi: angular coordinate
        :param theta: radial coordinate
        :param f: axis ratio (between 0 and 1)
        :param theta_E: Einstein radius
        """
        self.phi = phi
        self.theta = theta
        self.f = f
        self.theta_E = theta_E

    def potential(self, phi, theta, f, theta_E):
        """
        SIE potential from Kormann et al 1994, eqn 26a
        :param phi: angular coordinate
        :param theta: radial coordinate
        :param f: axis ratio () < f < 1; f -> 1 yields an SIS)
        :param theta_E: Einstein radius
        :return: The SIE potential evaluated at the given values
        """
        f_prime = np.sqrt(1-self.f**2.)
        prefactor = (np.sqrt(self.f)*self.theta)/f_prime
        sin_term = np.sin(self.phi)*np.arcsin(f_prime*np.sin(self.phi))
        cos_term = np.cos(self.phi)*np.arcsinh((f_prime/self.f)*np.cos(self.phi))
        potential = self.theta_E*prefactor*(sin_term+cos_term)
        return potential
