import math

def f(x):#συνάρτηση για τον υπολογισμό της τιμής της συνάρτησης  
    return math.exp(math.sin(x)*math.sin(x)*math.sin(x))+x**6-2*x**4-x**3-1;#επιστοφή της τιμής της συνάρτησης

def paragogosf(x):#1η παράγωγος της συνάρτησης
    return 3*math.exp(math.sin(x)*math.sin(x)*math.sin(x))*math.sin(x)*math.sin(x)*math.cos(x)+6*x**5-8*x**3-3*x**2;

def  NewtonRaphson(a):#συνάρτηση για τον υπολογισμό της ρίζας της συνάρτησης στο [a,b]
    i=0;#αριθμός επαναλήψεων
    e=0.000005;#(1/2)*(10^(-5))
    x0=a;#ορισμός αρχικού σημείου
    x1=x0-f(x0)/paragogosf(x0);
    i+=1;
    while(math.fabs(x1-x0)>e):
        x0=x1;
        x1=x0-f(x0)/paragogosf(x0);
        i+=1;
    print("Έγιναν",i,"επαναλήψεις:")    
    return x1;    
    
print("Οι ρίζες της συνάρτησης είναι οι εξής:")
print('');
print(NewtonRaphson(-1));#ρίζα της συνάρτησης στο [-2,-1] 
print('-----------------------')
print(NewtonRaphson(1)); #ρίζα της συνάρτησης στο [-1,1]
print('-----------------------')
print(NewtonRaphson(2));#ρίζα της συνάρτησης στο [1,2]