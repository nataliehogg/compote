# :strawberry: `compote` (Coefficients Of Multipoles of lensing POTEntials)

The `compote` package computes the coefficients of the multipolar expansion of a lensing potential.

![pika-1708114906974-1x](https://github.com/nataliehogg/compote/assets/32572654/6cca71d4-9367-412d-a5cd-49ab6e7563ee)

Figure: the difference between the first thirteen coefficients of an elliptical power law (EPL) lensing potential and a singular isothermal ellipse (SIE) lensing potential for different values of the axis ratio $f$, computed and plotted with `compote`. When $f\rightarrow 1$, the singular isothermal sphere is recovered.

## Physics

Strong gravitational lens galaxies are typically described by elliptical mass distributions. However, an elliptical lensing potential will have contributions from higher-order multipoles beyond the monopole and the quadrupole term which describes an ellipse. To understand how relevant these higher-order modes may be, we want to compute the multipole coefficients
$c_n(\theta) = \frac{1}{2\pi} \int_0^{2\pi} \mathrm{d} \varphi e^{-in\varphi} \psi(\theta, \varphi)$, where $\psi(\theta, \varphi)$ is the given potential. The `compote` package can perform this calculation for the EPL and SIE potentials, with trivial extensibility to other cases.

## Usage

First import and instantiate the potential whose coefficients you wish to calculate, passing its parameter values:
```
from compote.potentials.epl import EPL

phi = 0.8
theta = 1
f = 7/8
theta_E = 1
gamma = 2

epl = EPL(phi, theta, f, theta_E, gamma)
```

Then, import and instantiate the Calculate class, pass the number of orders to be computed and get the result:
```
from compote.calculate.calculate import Calculate

c = Calculate()

orders = range(0, 12)

c_epl, error_epl = c.coefficients(epl.potential, orders, theta, f, theta_E, gamma)
```

You can view the results as a `pandas` dataframe or as a LaTeX table for convenience:
```
dataframe = c.results_dataframe(c_epl, error_epl, orders)

latex = c.results_dataframe(c_epl, error_epl, orders, to_latex=True)

print(dataframe)

print(latex)
```

And lastly you can plot your results with the Plot class:
```
from compote.plots.plots import Plot

p = Plot()

plot_kwargs = {'color': 'maroon', 'ls': ' ', 'marker': 'x', 'label': 'EPL'}

p.coefficient_plot(c_epl, orders, plot_kwargs,  title='my amazing compote plot')
```

An example notebook demonstrating how to use `compote` can be found [here](https://github.com/nataliehogg/compote/blob/main/example_notebook.ipynb).

## Contribution

To contribute to the code, please fork the repository, create a branch with your modification and then open a [pull request](https://github.com/nataliehogg/compote/pulls).

## Name
*Compôte* is a stewed fruit dessert.
