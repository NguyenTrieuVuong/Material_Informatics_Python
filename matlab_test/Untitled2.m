clc; clear all; close all;
p = @(x) exp(cos(x)); a=-pi;b=pi;
figure(1); ezplot(p,[a,b]); Fm = 2.8;
N = 2e5; x1 = a+(b-a)*rand(1,N); n = 35;
figure(2); hist(x1,n)
count = 0;
for k=1:N
    y1(k)=Fm*rand;
    if y1(k)<=p(x1(k))
        count=count+1; x2(count)=x1(k);
    end
end
figure(3); hist(x2,n) % Chua chuan hoa
figure(4);
% Chuan hoa ham PBXS ly thuyet
l = quad(p,a,b); syms x; 
pl = exp(cos(x))/l;
fplot(pl,[a b],'r'); hold on
% Chuan hoa PBXS roi rac
Ma = max(x2); Mi = min(x2);
[nx dx] = hist(x2, linspace(a,b,n));
bar(dx,n*nx/(length(x2)*(Ma-Mi))); shg