clc; clear all; close all;
N = 1000000;
X1 = rand(1,N); X2 = rand(1,N);
n = 100;
figure(1); hist(X1,n);
figure(2); hist(X2,n);

Y1 = sqrt(-2*log(X2)).*cos(2*pi*X1);
Y2 = sqrt(-2*log(X2)).*sin(2*pi*X1);

figure(3); hist(Y1,n);
figure(4); hist(Y2,n);
figure(5); f=@(x) exp(-(x.^2)/2)./sqrt(2*pi); 
fplot(f,[-5 5],'r'); hold on
quad(f,-5,5);
a = min(Y1); b = max(Y1);
[ny nx] = hist(Y1,linspace(a,b,n));
bar(nx,n*ny/(N*(b-a)));