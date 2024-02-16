import numpy as np
from scipy.integrate import quad
import pandas as pd


class Calculate:

    def __init__(self):
        pass

    def integrand(self, phi, potential, orders):
        """
        Computes the integrand in the equation for the multipole coefficients.
        :param phi: angular coordinate (integrated over)
        :param potential: an instance of a potential from the potentials module
        :param orders: the list of orders to be computed
        :return: The integrand
        """
        exp_term = np.exp(-1j*orders*phi)
        I = exp_term*potential
        return I

    def coefficients(self, potential, orders, *args):
        """
        Performs the integration.
        :param phi: angular coordinate (integrated over)
        :param potential: an instance of a potential from the potentials module
        :param orders: the list of orders to be computed
        :param *args: any other arguments taken by specific potentials.
        :return: The integral result and the integration error
        """
        integral = [quad(lambda phi: self.integrand(phi, potential(phi, *args), order), 0.0, 2.*np.pi) for order in orders]
        divide = np.array(integral)/(2*np.pi)
        result = divide[:,0]
        error  = divide[:,1]
        return result, error

    def results_dataframe(self, result, error, orders, to_latex=False):
        """
        Takes the result of an integration and formats it as a pandas dataframe, which can be output in LaTeX.
        :param result: an array of multipole coefficients
        :param error: an array of integration errors associated with the computed coefficients
        :param orders: the list of orders computed
        :param to_latex: Bool, if True, prints the resulting dataframe as a LaTeX table.
        """

        potential_dict = {'c_n': result, 'error': error}

        potential_df = pd.DataFrame(potential_dict, index=orders)

        if to_latex == True:
            potential_df = potential_df.to_latex()
        else:
            pass

        return potential_df
