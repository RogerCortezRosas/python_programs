

class laclase:

    def __init__(self,lista):
        for i in lista:
            if(i != int):
                raise ValueError("Error el valor ",i," no es un entero")
            else:
                self.lista = lista
        
    
    def Grados (self,origen="Celsius",destino="Farenheit"):
     if origen == "Celsius":
        if destino == "Farenheit":
            for c in self.lista:
               F = c*(9/5)+32
               print(c," grados Celsius son ",F," Grados Farenheit")
        elif destino == "Kelvin":
             for c in self.lista:
               K = c + 273.15
               print(c," grados Celsius son ",K," Grados Kelvin")
        
    def Funcion (self):
        x = 1
        repite = 1
        repite_final = 0
        elemneto_mayor = 0
        z = 0
        while z < len(self.lista):
            while x <len(self.lista):
                if self.lista[z] == self.lista[x]:
                    repite +=1
                x+=1
            if repite > repite_final:
                repite_final = repite
                elemneto_mayor = self.lista[z]
            repite=1
            x = z+2
            z+=1
        return  elemneto_mayor ,repite_final

    
    def primo(self,nro):
        es_primo = True  # Variable para almacenar el resultado de la verificación de número primo
        for i in range(2, nro):  # Iteración sobre los números desde 2 hasta nro-1
            if nro % i == 0:  # Verificación si nro es divisible por i (no es primo)
                es_primo = False  # Se marca la variable como False indicando que el número no es primo
                break  # Se rompe el bucle ya que no es necesario continuar la verificación
        return es_primo  # Se devuelve el resultado de la verificación de número primo

    def listaPrimos(self):
        newLista = []
        for c in self.lista:
            varBool = self.primo(c)
            if varBool == True and c not in newLista:
                newLista.append(varBool)
            elif varBool == False and c not in newLista:
                newLista.append(varBool)
    
        return newLista