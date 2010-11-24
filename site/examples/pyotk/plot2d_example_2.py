# This example demonstrates invoking the L-BFGS-B algorithm 
# and plotting the results with constraints.

from pyotk.native import *
from pyotk.plot2d import *
from pyotk.testproblems import *

# Initialize the trigonometric test function with 
# two variables and its plotting ranges.
f = Trigonometric(n=2)
x1 = -1
x2 = 1
y1 = -0.5
y2 = 1
z1 = f.plot_spec.z_range[0]
z2 = f.plot_spec.z_range[1]
z_logscale = f.plot_spec.z_logscale

# Initialize the L-BFGS-B algorithm with default parameters.
s = LBFGSB()

# Setup the upper and lower bounds in x- and y-direction.
C = BoundConstraints(2)
C.types[0] = BoundType.both
C.types[1] = BoundType.both
C.L = [-0.3, -0.3]
C.U = [0.3, 0.3]

# Call the driver routine and plot results.
x0 = (-0.75, 0.75)
results = minimize(s, DefaultSolverSetup(), f.otk_instance, 
                   f.stopcrit, x0, C, 0, False)
plot_iterates_on_contours(results, x1, x2, y1, y2, z1, z2)