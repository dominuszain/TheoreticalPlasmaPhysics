// code of zain ul abideen
clear; clc;

// setting up trivial values for constants.
q = 1; m = 1; qm = q ./ m;

ex = 1; ey = 0; ez = 0;
bx = 0; by = 1; bz = 0;

t = [0 : 0.1 : 10]

// setting up the differential equations.
function [dxdt]=f(t, x)
    dxdt = [x(4,:); x(5,:); x(6,:);
    qm .* (ex + x(5,:) .* bz - x(6,:) .* by); 
    qm .* (ey + x(6,:) .* bx - x(4,:) .* bz);
    qm .* (ez + x(4,:) .* by - x(5,:) .* bx)]
endfunction

// setting up the initial conditions.
to = 0
xo = [0; 0; 0; 0; 1; 0]
// xo = [x; y; z; vx; vy; vz]

//solving the differential equations.
x = ode(xo, to, t, f)

// plotting the results.
scatter3d(x(1,:), x(2,:), x(3,:))

// see the relevant paper for more insight.

