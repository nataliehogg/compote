import numpy as np
from scipy.integrate import quad
import pandas as pd


class Calculate:

    def __init__(self):
        pass

    def integrand(self, phi, potential, orders):
        '''
        Computes the integrand.
        '''
        exp_term = np.exp(-1j*orders*phi)
        I = exp_term*potential
        return I

    def coefficients(self, potential, orders, *args):
        '''
        Performs the integration and returns the coefficients and the integration error.
        '''
        integral = [quad(lambda phi: self.integrand(phi, potential(phi, *args), order), 0.0, 2.*np.pi) for order in orders]
        divide = np.array(integral)/(2*np.pi)
        result = divide[:,0]
        error  = divide[:,1]
        return result, error

    def results_dataframe(self, result, error, orders, to_latex=False):
        '''
        Collects the results and errors in a dataframe, can be converted to a LaTeX table.
        '''

        potential_dict = {'c_n': result, 'error': error}

        potential_df = pd.DataFrame(potential_dict, index=orders)

        if to_latex == True:
            potential_df = potential_df.to_latex()
        else:
            pass

        return potential_df
