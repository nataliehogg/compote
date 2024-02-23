import numpy as np


class Boxy:

    def __init__(self):
        pass

    def potential(self, phi, theta, a_4):
        """
        Boxy potential from van de Vyvere et al 2021 (https://arxiv.org/abs/2112.03932)
        :param phi: angular coordinate
        :param theta: radial coordinate
        :return: The boxy potential evaluated at the given values
        """
        m = 4 # boxy/disky is always an octupole
        phi_4 = np.pi/4 # boxyness is defined as being when phi = 45 deg
        prefactor = 1/(1-m**2.)
        potential = prefactor*theta*a_4*np.cos(m*(phi - phi_4))
        return potential

class Disky:

    def __init__(self):
        pass

    def potential(self, phi, theta, a_4):
        """
        Disky potential from van de Vyvere et al 2021 (https://arxiv.org/abs/2112.03932)
        :param phi: angular coordinate
        :param theta: radial coordinate
        :return: The disky potential evaluated at the given values
        """
        m = 4 # boxy/disky is always an octupole
        phi_4 = 0. # diskyness is defined as being when phi = 0 deg
        prefactor = 1/(1-m**2.)
        potential = prefactor*theta*a_4*np.cos(m*(phi - phi_4))
        return potential
