import numpy as np
from matplotlib import rc, pyplot as plt
from fractions import Fraction

rc('text', usetex=True)
rc('font', family='serif')
rc('font', size=18)

class Plot:

    def __init__(self):
        pass

    def coefficient_plot(self, coeffs, orders, kwargs, title=None):
        """
        This function plots the coefficients as a function of their order.
        :param coeffs: a list or array of multipole coefficients
        :param orders: a list of orders at which the coefficients were computed
        :param kwargs: plotting kwargs
        :return None:
        """

        fig, ax = plt.subplots(1, 1, figsize=(8,4))

        if title is not None:
            ax.set_title(r'{}'.format(title))
        else:
            pass

        ax.plot(orders, coeffs, **kwargs)

        ax.set_xlabel(r'$n$')
        ax.set_ylabel(r'$c_n$')

        ax.legend()

        plt.show()

        return None

    def difference_plot(self, coeffs1, coeffs2, orders,
                        kwargs1, kwargs2, kwargsdiff, title=None):
        """
        This function plots the coefficients of two different profiles as a function of their order, along with the absolute difference.
        :param coeffs1: a list or array of multipole coefficients for the first profile
        :param coeffs2: a list or array of multipole coefficients for the second profile
        :param orders: a list of orders at which the coefficients were computed
        :param kwargs1: plotting kwargs for the first profile coefficients
        :param kwargs2: plotting kwargs for the second profile coefficients
        :param kwargsdiff: plotting kwargs for the difference between the first and second profile coefficients
        :return None:
        """

        difference = np.abs(np.subtract(coeffs1, coeffs2))

        fig, ax = plt.subplots(2, 1, sharex=True, sharey=False, figsize=(12,7))

        if title is not None:
            ax.set_title(r'{}'.format(title))
        else:
            pass

        ax[0].plot(orders, coeffs1, **kwargs1)
        ax[0].plot(orders, coeffs2, **kwargs2)

        ax[1].plot(orders, difference, **kwargsdiff)

        ax[1].axhline(0, ls = '--', color = 'k', alpha=0.4)

        ax[1].set_xlabel(r'$n$')

        ax[0].set_ylabel(r'$c_n(\theta=1)$')
        ax[1].set_ylabel(r'$|c_{n, 1} - c_{n,2}|$')

        ax[0].legend()

        plt.show()

        return None
