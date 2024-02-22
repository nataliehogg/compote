import numpy as np
from scipy.special import hyp2f1


class EPL:

    def __init__(self):
        pass

    def potential(self, phi, theta, f, theta_E, gamma):
        """
        EPL potential from Tessore and Metcalf 2015 (https://arxiv.org/abs/1507.01819), eqn 14 with coordinate transformation given in eqn 5
        :param phi: angular coordinate
        :param theta: radial coordinate
        :param f: axis ratio (between 0 and 1)
        :param theta_E: Einstein radius
        :param gamma: index of the power law
        :return: The EPL potential evaluated at the given values
        """
        b = theta_E*np.sqrt(f)
        t = gamma-1
        prefactor = 1/(2-t)
        theta_1 = theta*np.cos(phi)
        theta_2 = theta*np.sin(phi)
        R = np.sqrt((f**2.)*(theta_1**2.) + theta_2**2.)
        phi_ell = np.arctan2(theta_2, f*theta_1)
        alpha = ((2*b)/(1+f))*((b/R)**(t-1))*(np.exp(1j*phi_ell))*(hyp2f1(1, t/2, 2-(t/2), -((1-f)/(1+f))*np.exp(1j*2*phi_ell))) # eqn 14
        z_coordinate = (R/f)*np.cos(phi_ell) + 1j*R*np.sin(phi_ell)
        potential = prefactor*(((z_coordinate*np.conjugate(alpha)) + (np.conjugate(z_coordinate)*alpha))/2)
        return potential
