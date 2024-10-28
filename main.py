from math import *
import pprint

from matplotlib.pyplot import plot, show

def approximate_integral(expression: str, xi: int,yi: int,
                         sampling_length: int, cals_per_point: int,
                         LB: int, UB: int):
    f = convert(expression)
    step_length = sampling_length / cals_per_point

    domain = LB, UB
    sampled_F_after_xi = [yi]
    sampled_F_before_xi = [yi]

    xs_after_xi = [xi]
    xs_before_xi = [xi]
    x = xi
    while x < domain[1]:
        # approximate F(x) using F(x) = F(xi) + deltaF
        # roughly = F(xi) + sum(dF/dx * delta_x) at different points
        change_in_F = 0  # approximate change in F over
        #               (xi + delta_x, xi + delta_x + sampling_length)
        for step in range(0, cals_per_point):  # left hand riemann sum
            change_in_F += f(x + step * step_length) * step_length

        sampled_F_after_xi += [sampled_F_after_xi[-1] + change_in_F]
        xs_after_xi += [x + sampling_length]
        x += sampling_length
    x = xi
    while x > domain[0]:
        # approximate F(x) using F(x) = F(xi) + deltaF
        # roughly = F(xi) + sum(dF/dx * delta_x) at different points
        change_in_F = 0  # approximate change in F over
        #               (xi - delta_x - sampling_length, xi + delta_x)
        for step in range(1, cals_per_point + 1):  # left hand riemann sum
            change_in_F += f(x - step * step_length) * step_length
        sampled_F_before_xi += [sampled_F_before_xi[-1] - change_in_F]
        xs_before_xi += [x - sampling_length]
        x -= sampling_length
    xs_before_xi.reverse()
    sampled_F_before_xi.reverse()
    plot(
        xs_before_xi[0: -1] + xs_after_xi,
        sampled_F_before_xi[0:-1] + sampled_F_after_xi,
    )
    show()

def convert(expression: str):
    expression = expression.replace('^', '**')
    return lambda x: eval(expression)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    approximate_integral("cos(x ^ 2)", 0, 0, 0.05, 10, -10, 10)
