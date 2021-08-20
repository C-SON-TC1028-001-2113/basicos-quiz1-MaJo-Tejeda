import math
def main():
   #escribe tu código abajo de esta línea
    #Desarrolla un programa en Python que calcule la distancia entre dos puntos del plano cartesiano.
    #Los mensajes para recibir las 4 entradas deben ser **"x1=    y1=     x2=   y2=   ** respectivamente "
    #El mensaje para la salida debe ser **"distancia= **"
    
    x1 = float(input('Introduce valor x1: ')
    y1 = float(input('Introduce valor y1: ')      
    x2 = float(input('Introduce valor x2: ')       
    y2 = float(input('Introduce valor y2: ')               

      a = (x2-x1)^2 
      b = (y2-y1)^2         
      c = a+b 
          
               
       print('distancia=  '+ str(float(math.sqrt(c)))        
               
if __name__ == '__main__':
    main()
