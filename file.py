# -*- coding: utf-8 -*-
"""Tarea2ACyMN.ipynb

Pregunta 1. Un carpintero está acomodando las tablas que tiene en su taller. Por alguna extraña razón, quiere arreglarlas de la más pequeña a la más grande tal que cada tabla sea más grande que la anterior por exactamente 1 unidad (arbitraria). Es posible que para cumplir su cometido, el carpintero necesite agregar tablas adicionales. Haz una función que calcule el número mínimo de tablas que necesitará.

Ejemplo:

Para un arreglo de tablas tablas=[7,3,4,9], el resultado de la función debería ser 3 ya que el necesitaría tablas de tamaño 5,6 y 8.

Reglas:
- No pueden usar paquetes
- Los elementos del arreglo de entrada solo serán números enteros positivos.
- El arreglo de entrada puede contener de 1 a 10 elementos.
- Un elemento del arreglo de entrada puede medir de 0 a 20 unidades.
- La salida de la función sólo debe de ser un número entero.
"""

def contartablas(lista): 
    tablas=list(set(lista)) #Elimina posibles repeticiones.
    return max(tablas)-min(tablas)-(len(tablas)-1)

lista=[3,7,4,9]
print(f'Esto es una prueba. Faltan {contartablas(lista)} tablas.')

"""Pregunta 2. Dadas dos strings, hacer una función que encuentre el número de caractéres en común.

Ejemplo:

Sea s1='ccell' y s2='czlcc', la salida de la función debería ser 3 ya que hay dos c y una l en común.

Reglas:
- No pueden usar paquetes.
- Las strings de entrada solo contendran letras en minúsculas sin incluir la ñ.
- Las strings de entrada solo podrán tener de 1 a 15 caractéres.
- La salida solo será un entero.
"""

def letrascomunes(grupo1,grupo2):
    grupo1_list=list(grupo1)
    grupo2_list=list(grupo2)
    
    grupo1_list.sort()
    grupo2_list.sort()
    
    contador=0
    last_found=-1
    for i in range(0,len(grupo1_list)):
        for j in range(last_found+1,len(grupo2_list)):
            if grupo1_list[i]==grupo2_list[j]:
                contador+=1
                last_found=j
                break
    
    return contador

s1='ccell'
s2='czlcc'
letrascomunes(s1,s2)

"""Pregunta 3. Cierto dueño supersticioso de una caferería aborda todos los días el transporte público para ir a su negocio (todo esto antes de la pandemia). Cada vez que aborda cierto transporte público, el hombre recibe un boleto con un número de serie. El considera que tendrá un buen día si la suma de la primera mitad de los dígitos del número de serie es igual a la suma de los dígitos de la segunda mitad. Dado un número de serie n, hacer una función que le diga si tendrá un buen día o no. 

Ejemplo:

Si el número de serie es n=2341, entonces la función debería de regresar True. Para el número de serie n=248028 la función debería de regresar False.

Reglas:
- No pueden usar paquetes.
- El entero que se dará a la función será un número positivo con un número par de digitos.
- El entero de entrada podrá tomar un valor mínimo de 10 y un valor máximo de $10^6$.
- La salida del programa debe de ser un booleano: True o False.
"""

def suerte(ticket):
    ticket=f'{ticket}'
    ticket_list_str=list(ticket)
    ticket_list_int=[int(ticket_list_str[i]) for i in range(0,len(ticket_list_str))]
    
    suma=0
    for i in range(0,int(len(ticket_list_int)/2)):
        suma+=ticket_list_int[i]-ticket_list_int[len(ticket_list_int)-1-i]
    
    return suma==0

#Este algoritmo funciona aún si el boleto tiene una cantidad impar de digitos o números muy grandes.
boleto=1349224
suerte(boleto)

"""Pregunta 4. Una señora gusta de coleccionar tarros de galletas. Al organizar sus tarros por tamaño en su vitrina de exhibición, se da cuenta que hay algunos lugares que no puede ocupar dado que la madera de esos entrepaños está en mal estado y sus tarros podrían caerse (dado que ha gastado mucho dinero en los tarros, no puede comprar un nuevo mueble). Haz una función que ordene los tarros sin que ocupen los entrepaños en mal estado.

Ejemplo:

Para un arreglo de entrada tarros=[-1,15,19,17,-1,-1,16,18], la salida del programa debería de ser tarros=[-1,15,16,17,-1,-1,18,19].

Reglas:

- No pueden usar paquetes.
- Los entrepaños dañados son representados con un -1, por lo que esos elementos no se pueden mover de posición en el arreglo de entrada. Todos los demás números serán positivos y representarán la altura de los tarros de galletas en una unidad arbitraria.
- Los tarros pueden medir de 0 a 1000. Un cero representa que ahí no pondrá ningún tarro.
- El arreglo de entrada puede contener de 1 a 1000 elementos.
- La salida debe de ser un arreglo con los -1 intactos y los tarros acomodados por altura, del más chico al más grande.
"""

def ordenartarros(tarros):
    mask=[tarros[i]!=-1 for i in range(0,len(tarros))]
    
    solo_tarros=[]
    for i in range(0,len(tarros)):
        if mask[i]:
            solo_tarros.append(tarros[i])
            
    solo_tarros.sort()
    
    j=0
    for i in range(0,len(tarros)):
        if mask[i]:
            tarros[i]=solo_tarros[j]
            j+=1
    
    return tarros

tarros=[-1,15,19,17,-1,-1,16,18]
ordenartarros(tarros)

"""Pregunta 5. Dada una string, hacer una función que escriba al revés las palabras que estén dentro de paréntesis. Puede haber paréntesis dentro de paréntesis.

Ejemplos:
- Para ’(cap)’, la salida de la función debe de ser ’pac’

- Para ’lol(cap)rap’, la salida de la función debe de ser ’lolpacrap’

- Para ’lol(cap)rap(tam)’, la salida de la función debe de ser ’lolpacrapmat’

- Para ’lol(cap(rap))tam’, la salida de la función debe de ser ’lolrappactam’. Esto se debe a que ’lol(cap(rap))tam’ se transforma a ’lol(cappar)tam’ y esto se transforma en ’lolrappactam’.

Reglas:
- No pueden usar paquetes.
- La string de entrada solo tend´ra letras en minúsculas sin incluir la ñ.
- Todos los paréntesis tendrán su pareja correspondiente.
- La string de entrada podrá estar vacía. Por el contrario, podrá contener hasta 50 caractéres.
- La salida de la función debe de ser la string transformada.

"""

def volteo(string):
    while '(' in string:
        parentesis1=string.rfind('(')
        parentesis2=string.find(')',parentesis1+1)
        string=string[:parentesis1]+string[parentesis1+1:parentesis2][::-1]+string[parentesis2+1:]
    return string;
volteo('lol(cap(rap))tam')

"""Pregunta 6.
Dada una string que contiene espacios, hacer un función que sustituya los espacios por guiones medios.

Ejemplo:

Dada la string s1 = ’esto es una string’, la salida de la función debe de ser ’esto-es-una-string’.

Reglas:
- No pueden usar paquetes.
- La string de entrada contendrá espacios y podrá contener de 1 a 10 palabras separadas por espacios.
- La salida de la función debe de ser la string transformada.
"""

def sp2sc(string):
  string_mod = string.replace (" ", "-")
  return string_mod

sp2sc('Esto es una prueba donde pondremos: hola mundo')

"""Pregunta 9. Seguir las siguientes instrucciones para generar las gráficas que se piden.
En todos los puntos se debe de generar la gráfica que se pide. Por la naturaleza de las preguntas, pueden usar paquetes.
1. Generar tres conjuntos de mil números aleatorios que sigan una distribución normal. Cada conjunto debe estar centrado en diferentes valores (μ1, μ2, μ3) y con diferentes anchuras (σ1, σ2, σ3). Cada conjunto debe de ser guardado en una variable diferente.
2. Hacer un histograma donde se muestren las tres distribuciones correspondientes a los tres conjuntos de n ́umeros aleatorios. Las distribuciones deben de estar acomodadas de acuerdo a su anchura.
3. Repetir el histograma del punto anterior y a ̃nadir l ́ıneas verticales que represente el valor correspondiente μn en la cual se encuentran centradas las distribuciones.
4. Hacer una gráfica de scatter donde se muestren las tres diferentes distribuciones con un color diferente. Agregar una leyenda donde diga que color corresponde a que distribución.
5. Hacer un una gráfica que incluya todas las gráficas anteriores en una misma figura. Cada subplot debe de tener su propio título, también la figura principal debe de tener su título correspondiente.
"""

import numpy as np
import matplotlib.pyplot as plt


list1 = np.random.normal(loc = -10, scale = 3, size = 1000)
list2 = np.random.normal(loc = 0, scale = 6, size = 1000)
list3 = np.random.normal(loc = 10, scale = 8, size = 1000)
fig, ax = plt.subplots()
plt.hist(list1, alpha = 0.7, bins = 50)
plt.hist(list2, alpha = 0.7, bins = 50)
plt.hist(list3, alpha = 0.7, bins = 50)
plt.xlabel("Distribución de 1000 datos", 
           family='serif', 
           color='r', 
           weight='normal', 
           size = 16,
           labelpad = 6)
plt.ylabel("Datos", 
           family='serif', 
           color='r', 
           weight='normal', 
           size = 16,
           labelpad = 6)
ax.set_title('Problema 9', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
plt.show()

fig, ax = plt.subplots()

plt.hist(list1, alpha = 0.7, bins = 50)
plt.hist(list2, alpha = 0.7, bins = 50)
plt.hist(list3, alpha = 0.7, bins = 50)

xpoints = [-10, 0, 10]

colors = ['c', 'r', 'g']

for p, c in zip(xpoints, colors):

    plt.axvline(p,c = c)

plt.xlabel("Distribución de 1000 datos", 
           family='serif', 
           color='r', 
           weight='normal', 
           size = 16,
           labelpad = 6)
plt.ylabel("Datos", 
           family='serif', 
           color='r', 
           weight='normal', 
           size = 16,
           labelpad = 6)
ax.set_title('Histograma de la distribución de 1000 datos', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
plt.show()

y = range(1, 1001)
fig, ax = plt.subplots()
ax.scatter(list1, y, marker = "x", c= "blue", alpha = 0.5, label = "centrado en -10")
ax.scatter(list2, y, marker = "o", c= "orange", alpha = 0.5, label = "centrado en 0")
ax.scatter(list3, y, marker = "+", c= "green", alpha = 0.5, label = "centrado en 10")
plt.xlim(-25, 40)
plt.ylim(0, 1100)
plt.legend()
ax.set_title('Scatter de la distribución de 1000 datos', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
plt.xlabel("Distribución de 1000 datos", 
           family='serif', 
           color='r', 
           weight='normal', 
           size = 16,
           labelpad = 6)
plt.ylabel("Número de datos", 
           family='serif', 
           color='r', 
           weight='normal', 
           size = 16,
           labelpad = 6)
plt.show

"""Pregunta 11. Sabemos que el sistema oscilante mas simple que conocemos es una masa y un
resorte. Aplicando la segunda ley de Newton F = ma a la masa, podemos obtener las ecuaciones
de movimiento del sistema:

donde ω0 =
p
k/m es la frecuencia natural de oscilación. Las soluciones a esta ecuación de movimiento es:

x(t) = xm cos(ω0t + φ)

Donde xm es la amplitud de oscilación y φ es la constance de fase de la oscilación.

1. Hacer una imagen que muestre la posición de tres diferentes diferentes objetos que sigan la ecuación antes descrita con frecuencias naturales de ω0, 2ω0 y 3ω0. Suponer que todos los
objetos tienen las misma amplitud de oscilación y la misma constante de fase.
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})

class oscilacion():
    """
    Clase que simula una masa en movimiento oscilatorio
    """
    def __init__(self, w, A=1, phi=np.pi/2):
        self.A = A
        self.phi = phi
        self.w = w
        

    def pos1_x(self, t):
        res1 = self.A * np.cos(self.w*t+self.phi)
        return res1
    
    def pos2_x(self, t):
        res2 = self.A * np.cos(2*self.w*t+self.phi)
        return res2
        
    def pos3_x(self, t):
        res3 = self.A * np.cos(3*self.w*t+self.phi)
        return res3 

    def make_sim(self):

        time_vec = np.linspace(0, 50, 150)
        x1 = self.pos1_x(time_vec)
        x2 = self.pos2_x(time_vec)
        x3 = self.pos3_x(time_vec)
        
        self.plot_results(x1, x2, x3)


    def plot_results(self, x1, x2, x3):
        
        time_vec = np.linspace(0, 50, 150)
        fig, ax=plt.subplots(figsize=(15,7))
        ax.set_xlabel('Tiempo(s)')
        ax.set_ylabel('Distancia(m)')
        plt.title('Gráfica 1.' )

        plt.plot(time_vec, x1, label='Objeto 1 con w', color="violet")
        plt.plot(time_vec, x2, label="Objeto 2 con 2w", color="black")
        plt.plot(time_vec, x3, label="Objeto 3 con 3w", color="skyblue")
        plt.legend(loc='best')
        plt.xlim(0,50)

g1 = oscilacion(w=.25)
g1.make_sim()

"""

```
# Tiene formato de código
```

2. Suponer que tenemos un objeto que oscila de acuerdo a la ecuación de movimiento antes planteada. Con una frecuencia natural de ω0 y una constante de fase φ. Suponiendo que el sistema inicialmente est ́a en reposo pero desplazado una distance xm del equilibrio, realizar una figuar con tres subplots donde se muestre:
La energía cinética
La energía potencial
La energía total

Pueden utilizar cualquier paquete que necesitan, exceptuando aquellos que generen automáticamente las gráficas requeridas."""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})

class oscilacion2():
    """
    Clase que simula una masa en movimiento oscilatorio
    """
    def __init__(self, w, A=1, phi=np.pi/2):
        self.A = A
        self.phi = phi
        self.w = w
        
    def kin_x(self, t):
        res1 = (self.A**2 * np.sin(self.w*t+self.phi)**2)*(self.w**2)/2
        return res1
        
    def pot_x(self, t):
        res2 = (self.A**2 * np.cos(self.w*t+self.phi)**2)*(self.w**2)/2
        return res2 
       
    def make_sim(self):

        time_vec = np.linspace(0, 50, 150)
        x1 = self.kin_x(time_vec)
        x2 = self.pot_x(time_vec)

        normalizar=x1+x2
        x1=x1/normalizar
        x2=x2/normalizar
        
        self.plot_results(x1, x2, x1+x2)


    def plot_results(self, x1, x2, x3):
        
        time_vec = np.linspace(0, 50, 150)
        
        fig, axs = plt.subplots(3, figsize=(15,25))
        
        fig.suptitle('Gráficas de Energía' )

        axs[0].plot(time_vec,x1, color="blue")
        axs[0].set_title("Energía Cinética")
        axs[0].set_xlabel('Tiempo [s]')
        axs[0].set_ylabel('Energía [J]')

        axs[1].plot(time_vec,x2, color="m")
        axs[1].set_title('Energía Potencial')
        axs[1].set_xlabel('Tiempo [s]')
        axs[1].set_ylabel('Energía [J]')

        axs[2].plot(time_vec,x3, color="gold")
        axs[2].set_title("Energía Total")
        axs[2].set_xlabel('Tiempo [s]')
        axs[2].set_ylabel('Energía [J]')
        
        #plt.xlim(0,50)

g2 = oscilacion2(w=.25)
g2.make_sim()

"""Pregunta 12. Encontrar las soluciones de las siguientes ecuaciones con uno de los tres métodos
vistos en clase (indicar con que método están encontrando las soluciones). Pueden usar paquetes.
1. x − 2x − 5 = 0 en [1, 4]
2. x − cos x = 0 en [0, π/2]
3. x + 3x − 1 = 0 en [−3, −2]
4. x − 0.8 − 0.2 sin x = 0 en [0, π/2]
"""

import numpy as np
class root():
    
    def __init__(self, f, a, b, F, N=25):
        self.f = f
        self.a = a
        self.b = b
        self.N = N
        self.F = F


    def bis_method(self):
        if self.f(self.a)*self.f(self.b) >= 0:
            print(f'No se encontró solución en el intervalo [{self.a},{self.b}] para la función f(x)={self.F}')
            return None
        else:
            a_n = self.a
            b_n = self.b
            for n in range(1, self.N+1):
                m_n = (a_n + b_n)/2
                f_m_n = self.f(m_n)
                if self.f(a_n)*f_m_n < 0:
                    a_n = a_n
                    b_n = m_n
                elif self.f(b_n)*f_m_n < 0:
                    a_n = m_n
                    b_n = b_n
                elif f_m_n == 0:
                    print(f'La solución es exacta, con x={m_n}')
                    return m_n
                else:
                    print('El método de bisección falló')
                    return None
            print(f'La solución de la función f(x)={self.F} en el intervalo [{self.a},{self.b}] es x={m_n}')
            return m_n
    

def print_sol12():
    
    print('Resolviendo las ecuaciones  1, 2, 3 y 4 del inciso 12 en los intervalos indicados mediante el método de la bisección se obtiene lo siguiente ')
    
    f1= lambda x: x-2*x-5
    f2= lambda x: x-np.cos(x)
    f3= lambda x: x+3*x-1
    f4= lambda x: x-0.8-0.2*np.sin(x)
    
    inter1= [1,4]
    
    inter2= [0,np.pi/2]
    
    inter3= [-3,-2]
    
    F1='x-2*x-5'
    F2='x-cos(x)'
    F3='x+3*x-1'
    F4='x-0.8-0.2*sin(x)'
    
    r1 = root(f=f1, a=inter1[0], b=inter1[1], F=F1)
    r2 = root(f=f2, a=inter2[0], b=inter2[1], F=F2)
    r3 = root(f=f3, a=inter3[0], b=inter3[1], F=F3)
    r4 = root(f=f4, a=inter2[0], b=inter2[1], F=F4)
    
    Aprox1 = r1.bis_method()
    Aprox2 = r2.bis_method()
    Aprox3 = r3.bis_method()
    Aprox4 = r4.bis_method()

print_sol12()



"""Pregunta 13. Encontrar las soluciones con una precisión de al menos 10^−5 para las siguientes ecuaciones con cualquier método de los visto en clase. No pueden usar paquetes que resuelvan las ecuaciones, pueden usar el paquete numpy pero no las rutinas de este para encontrar las soluciones.
1. 2x cos 2x − (x − 2) = 0 en [2, 3] y en [3, 4]
2. (x − 2) − ln x = 0 en [1, 2] y en [e, 4]
3. e^x − 3x = 0 en [0, 1] y en [3, 5]
4. sin x − e^(−x) = 0 en [0, 1] y en [6, 7]
"""

import numpy as np
class root():
    
    def __init__(self, f, a, b, N=25):
        self.f = f
        self.a = a
        self.b = b
        self.N = N
        

    def sec_method(self):
        if self.f(self.a)*self.f(self.b) >= 0:
            print(f'en el intervalo [{self.a},{self.b}] no se encontró solución ')
            return None
        else:
            a_n = self.a
            b_n = self.b
            for n in range(1, self.N+1):
                m_n = a_n - self.f(a_n) * (b_n - a_n) / (self.f(b_n) - self.f(a_n))
                f_m_n = self.f(m_n)
                if self.f(a_n)*f_m_n < 0:
                    a_n = a_n
                    b_n = m_n
                elif self.f(b_n)*f_m_n < 0:
                    a_n = m_n
                    b_n = b_n
                elif f_m_n == 0:
                    print(f'en el intervalo[{self.a},{self.b}] la solución es exacta con x={"{0:.5f}".format(m_n)}')
                    return m_n
                else:
                    print('El método de la secante falló')
                    return None
            print(f'en el intervalo [{self.a},{self.b}] se encontró la solución con x={"{0:.5f}".format(m_n)}')
            return m_n

def print_sol13():
    
    print('Resolviendo las ecuaciones  1, 2, 3 y 4 del inciso 13 en los intervalos indicados mediante el método de la secante se obtiene lo siguiente ')
    
    f1= lambda x: 2*x*np.cos(2*x)-(x-2)
    f2= lambda x: (x-2)-np.log(x)
    f3= lambda x: np.exp(x)-3*x
    f4= lambda x: np.sin(x)-np.exp(-x)
    
    in1_1= [2,3]
    in1_2= [3,4]
    
    in2_1= [1,2]
    in2_2= [np.exp(1),4]
    
    in3_1= [3,5]
    in3_2= [0,1]
    
    in4_1= [0,1]
    in4_2= [6,7]
    
    r1_1 = root(f=f1, a=in1_1[0], b=in1_1[1])
    r1_2 = root(f=f1, a=in1_2[0], b=in1_2[1])
    r2_1 = root(f=f2, a=in2_1[0], b=in2_1[1])
    r2_2 = root(f=f2, a=in2_2[0], b=in2_2[1])
    r3_1 = root(f=f3, a=in3_1[0], b=in3_1[1])
    r3_2 = root(f=f3, a=in3_2[0], b=in3_2[1])
    r4_1 = root(f=f4, a=in4_1[0], b=in4_1[1])
    r4_2 = root(f=f4, a=in4_2[0], b=in4_2[1])
    
    print('Para la función f(x)=2xcos(2x)-(x-2):')
    Aprox1_1 = r1_1.sec_method()
    Aprox1_2 = r1_2.sec_method()
    
    print('Para la función f(x)=(x-2)-ln(x):')
    Aprox2_1 = r2_1.sec_method()
    Aprox2_2 = r2_2.sec_method()
    
    print('Para la función f(x)=e^x-3x:')
    Aprox3_1 = r3_1.sec_method()
    Aprox3_2 = r3_2.sec_method()
    
    print('Para la función f(x)=sin(x)-e^(-x):')
    Aprox4_1 = r4_1.sec_method()
    Aprox4_2 = r4_2.sec_method()
    
print_sol13()

