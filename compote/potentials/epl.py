import numpy as np
from scipy.special import hyp2f1


class EPL:

    def __init__(self, phi, theta, f, theta_E, gamma):
        """
        :param phi: angular coordinate
        :param theta: radial coordinate
        :param f: axis ratio (between 0 and 1)
        :param theta_E: Einstein radius
        :param gamma: index of the power law
        """
        self.phi = phi
        self.theta = theta
        self.f = f
        self.theta_E = theta_E
        self.gamma = gamma

    def potential(self, phi, theta, f, theta_E, gamma, *args):
        """
        EPL potential from Tessore and Metcalf 2015 (https://arxiv.org/abs/1507.01819), eqn 14 with coordinate transformation given in eqn 5
        Their R is my theta and their \varphi is my phi.
        :param phi: angular coordinate
        :param theta: radial coordinate
        :param f: axis ratio (between 0 and 1)
        :param theta_E: Einstein radius
        :param gamma: index of the power law
        :return: The EPL potential evaluated at the given values
        """
        b = self.theta_E*np.sqrt(self.f)
        t = self.gamma-1
        prefactor = 1/(2-t)
        alpha = ((2*b)/(1+self.f))*((b/self.theta)**(t-1))*(np.exp(1j*self.phi))*(hyp2f1(1, t/2, 2-(t/2), -((1-self.f)/(1+self.f))*np.exp(1j*2*self.phi))) # eqn 14
        z_coordinate = (self.theta/self.f)*np.cos(self.phi) + 1j*self.theta*np.sin(self.phi)
        potential = prefactor*(((z_coordinate*np.conjugate(alpha)) + (np.conjugate(z_coordinate)*alpha))/2)
        return potential
