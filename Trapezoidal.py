import math;

def fx(x):#συνάρτηση για τον υπολογισμό της τιμής τoυ ημιτόνου  
    return math.sin(x);#επιστοφή της τιμής της συνάρτησης
    
def integralf(x,f):#συνάρτηση για τον υπολογισμό του ολοκληρώματος της συνάρτησης του ημιτόνου
    fd=0;
    for i in range(n):
       fd+=((f[i]+f[i+1])/2)*(x[i+1]-x[i]);
    return fd;   
        

#άκρα διαστήματος [a,b]
a=0;
b=math.pi/2;
ba=b-a;#Μήκος διαστήματος ολοκλήρωσης
numberPoints=11;#Πλήθος σημείων
n=numberPoints-1;#Πλήθος υποδιαστημάτων    
rangeSpaces=(b-a)/n;#Εύρος υποδιαστημάτων
x=[];#λίστα με τα x για k=0,...,n
x0=0;
for k in range(n+1):
    x.append(x0+k*(rangeSpaces));

f=[];#Λίστα με τις τιμές της συνάρτησης για i=0,...,n
for i in x:
    f.append(fx(i));
fxdx=integralf(x,f);#Προσεγγιστική τιµή του ολοκληρώµατος της συνάρτησης του ημιτόνου
M=1;#Μέγιστο σε απόλυτη τιμή της δεύτερης παραγώγου του ημιτόνου
e=(((b-a)**3)/(12*n**2))*M;#Σφάλμα προσέγγισης
print("Η προσεγγιστική τιμή του ολοκληρώματος της συνάρτησης του ημιτόνου με τη μέθοδο του Τραπεζίου είναι",fxdx);
print("Το σφάλμα προσέγγισης είναι |e|<=",e);
