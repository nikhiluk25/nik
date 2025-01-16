% 11111111111111111111111111111111111111111111111111

x = pi/5;
LHS = cos(x/2)^2;
RHS = (tan(x) + sin(x)) / (2 * tan(x));
disp(['LHS: ', num2str(LHS)]);
disp(['RHS: ', num2str(RHS)]);
if abs(LHS - RHS) < 1e-10
   disp('The identity holds true.');
else
   disp('The identity does not hold.');
end

% 22222222222222222222222222222222222222222222222222

To = 120; Ts = 38; k = 0.45; t = 3; 
T = Ts + (To - Ts) * exp(-k * t);
T

% 3333333333333333333333333333333333333333333333333

m = [2, 4, 5, 10, 20, 50];    
F = [12.5, 23.5, 30, 61, 117, 294]; 
g = 9.81;   
mu = F ./ (m * g);
mu_avg = mean(mu);
mu
mu_avg

% 44444444444444444444444444444444444444444444444444

r = 120; l = 250; rpm = 500; omega = 2 * pi * rpm / 60;
t = linspace(0, 2*pi/omega, 1000);
theta = omega * t;
x = r * cos(theta) + sqrt(l^2 - (r * sin(theta)).^2);
v = gradient(x) ./ gradient(t); 
a = gradient(v) ./ gradient(t); 
plot(t, x, 'b', t, v, 'r', t, a, 'g'); grid on;
legend('Position (mm)', 'Velocity (mm/s)', 'Acceleration (mm/s^2)');
xlabel('Time (s)'); title('Piston Position, Velocity, and Acceleration');

% 55555555555555555555555555555555555555555555555555

v0 = 250; theta = 65; v_wind = 30; g = 9.81;
t_flight = 2*v0*sin(theta)/g; 
t = linspace(0, t_flight , 1000); 
z = v0 * sin(theta) * t - 0.5 * g * t.^2;
y = v0 * cos(theta) * t;                 
x = v_wind * t;                          
plot3(0*t, y, z, 'b', x, y, z, 'r'); 
grid on; xlabel('West (m)'); ylabel('North (m)'); zlabel('Height (m)');
legend('No Wind', 'With Wind'); title('Projectile Trajectory');

% 66666666666666666666666666666666666666666666666666

b = 300000; w = 25000; r = 0.05; inf = 0.02; y = 0;
while b > 0
    y = y + 1; 
    b = b * (1 + r) - w;
    B(y) = b; 
    W(y) = w; 
    w = w * (1 + inf);  
end
plot(1:y, W, 'r', 1:y, [300000 B(1:end-1)], 'b');  
xlabel('Year'); ylabel('Amount ($)'); grid on;
legend('Withdrawals', 'Balance'); title('Withdrawals and Balance');

% 7777777777777777777777777777777777777777777777777

singers = {'John', 'Mary', 'Tracy', 'Mike', 'Katie', 'David'};
randomOrder = randperm(length(singers));
disp('The random performance order is:');
for i = 1:length(singers)
   disp([num2str(i),'. ' singers{randomOrder(i)}]);
   % fprintf('%d. %s\n', i, singers{randomOrder(i)});
end
% disp(singers(randperm(length(singers))));

% 8888888888888888888888888888888888888888888888888

% projectile.m
function [h_max, d_max] = projectile(v0, theta)
    g = 9.81;
    theta = deg2rad(theta);
    h_max = (v0^2 * sin(theta)^2) / (2 * g);
    d_max = (v0^2 * sin(2 * theta)) / g;
    T = v0 * 2 * sin(theta) / g;
    t = linspace(0, T, 100);
    x = v0 * cos(theta) * t; 
    y = v0 * sin(theta) * t - 0.5 * g * t.^2;  
    plot(x, y); grid on;
    xlabel('Horizontal Distance (m)'); ylabel('Vertical Distance (m)');  
end

% ak8.m
[v0, theta] = deal(230, 39);
[h, d] = projectile(v0, theta);
fprintf('Max Height: %.2f m, Max Distance: %.2f m\n', h, d);

% 99999999999999999999999999999999999999999999999

function thickness = box_thickness(weight)
    L = 24; W = 12; H = 4;    
    specific_weight = 0.101;   
    eq = @(x) specific_weight * (L*W*H - (L-2*x)*(W-2*x)*(H-x)) - weight;
    thickness = fzero(eq, 0.1); 
end
thickness = box_thickness(15);
thickness








PROGRAMMING MATLAB FUNDAMENTALS

1.
A = [2, 5, 8, 11, 14, 17;
3, 6, 9, 12, 15, 18;
4, 7, 10, 13, 16, 19;
5, 8, 11, 14, 17, 20;
6, 9, 12, 15, 18, 21];
B = [5, 10, 15, 20, 25, 30;
30, 35, 40, 45, 50, 55;
55, 60, 65, 70, 75, 80];
v = [99, 98, 97, 96, 95, 94, 93, 92, 91];
A(1, 3:6) = B(1, 1:4);
A(3, 3:6) = B(2, 1:4);
A(4, 3:6) = v(5:8);
A(5, 3:5) = B(3, 3:5);
disp(A);
Output:
>> matlab
Warning: Function class has the same name as a MATLAB built-in. We suggest you rename
the function to avoid a potential name conflict.
2 5 5 10 15 20
3 6 9 12 15 18
4 7 30 35 40 45
5 8 95 94 93 92
6 9 65 70 75 21



2.
Force1 = 400; angle1 = 20;
Force2 = 500; angle2 = 30;
Force3 = 700; angle3 = 143;
angle1 = deg2rad(angle1);
angle2 = deg2rad(angle2);
angle3 = deg2rad(angle3);
Force1_x = Force1 * cos(angle1);
Force1_y = Force1 * sin(angle1);
Force2_x = Force2 * sin(angle2);
Force2_y = Force2 * cos(angle2);
Force3_x = Force3 * cos(angle3);
Force3_y = Force3 * sin(angle3);
Net_Force_x = Force1_x + Force2_x + Force3_x;
Net_Force_y = Force1_y + Force2_y + Force3_y;
Resultant_Force = sqrt(Net_Force_x^2 + Net_Force_y^2);
Resultant_Angle = rad2deg(atan2(Net_Force_y, Net_Force_x));
disp(['Net Force X = ', num2str(Net_Force_x), ' N']);
disp(['Net Force Y = ', num2str(Net_Force_y), ' N']);
disp(['Magnitude of Resultant Force = ', num2str(Resultant_Force), ' N']);
disp(['Angle of Resultant Force = ', num2str(Resultant_Angle), ' degrees']);

3)

y = x.^3 - 2*x.^2 + x;
disp('Values of y for corresponding x:');
disp(y);

4.
x = [-3, -2, -1, 0, 1, 2, 3];
y = (x.^2 - 2) ./ (x + 4);
disp('Values of y for corresponding x:');
disp(y);

5.
v = [3, -2, 4];
u = [5, 3, -1];
result_a = v .* u;
result_b = v * u';
result_c = v' * u;
disp('Result of (a):');
disp(result_a);
disp('Result of (b):');
disp(result_b);
disp('Result of (c):');
disp(result_c);
6.
% Define the vectors
u = [-3, 8, -2];
v = [6.5, -5, -4];
dot_product_a = sum(u .* v);
dot_product_b = u * v';
dot_product_c = dot(u, v);
disp('Dot product calculated in three ways:');
disp('(a) Using element-by-element calculation and sum:');
disp(dot_product_a);
disp('(b) Using row and column vector with matrix multiplication:');
disp(dot_product_b);
disp('(c) Using MATLAB built-in dot function:');
disp(dot_product_c);


7.
func = @(x) 3*x.^3 - 26*x + 10; % Original equation: 3x^3 - 26x + 10
func_first = @(x) 9*x.^2 - 26; % First derivative: 9x^2 - 26
func_second = @(x) 18*x;
x_range = -2:0.1:4;
y_values = func(x_range);
dy_values = func_first(x_range);
d2y_values = func_second(x_range);
figure;
plot(x_range, y_values, 'r', 'LineWidth', 2);
hold on;
plot(x_range, dy_values, 'g', 'LineWidth', 2);
plot(x_range, d2y_values, 'b', 'LineWidth', 2);
hold off;
xlabel('x-axis');
ylabel('y-axis');
title('Graph of 3x^3 - 26x + 10 and its Derivatives');
legend('Equation: 3x^3 - 26x + 10', 'First Derivative', 'Second Derivative');
grid on;


8.
f = @(x) sqrt(abs(cos(3*x))) + sin(4*x).^2;
fplot(f, [-2, 2]);
xlabel('x');
ylabel('f(x)');
title('Plot of f(x) = sqrt(|cos(3x)|) + sin^2(4x)');
grid on;

9.
t = linspace(0, 2*pi, 500);
x = 1.5 * sin(5 * t);
y = 1.5 * cos(3 * t);
figure;
plot(x, y, 'b', 'LineWidth', 2);
axis([-2 2 -2 2]);
xlabel('x');
ylabel('y');
title('Plot of Parametric Equations: x = 1.5sin(5t), y = 1.5cos(3t)');


10.
R = 4;
L = 1.3;
V = 12;
t1 = linspace(0, 0.5, 500);
t2 = linspace(0.5, 2, 500);
i1 = (V / R) * (1 - exp(-R * t1 / L));
i2 = exp(-R * (t2 - 0.5) / L) * (V / R) * (exp(R * 0.5 / L) - 1);
t = [t1, t2];
i = [i1, i2];
figure;
plot(t, i, 'b', 'LineWidth', 2);
xlabel('Time (s)');
ylabel('Current i(t) (A)');
title('Current
