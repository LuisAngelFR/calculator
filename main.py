# ls
#  dividir.py   main.py   multplicacion.py   README.md   resta.py   suma_avanzada.py   sumar.py

import sumar as s
import resta as r
import multiplicacion as m
import dividir as d
import suma_avanzada as sa

def show_menu():
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")
  print("5. Suma avanzada")
  print("6. Salir")
  return input("Opción: ")

def main():

  options = {
    "1": s.sumar,
    "2": r.resta,
    "3": m.multiplicacion,
    "4": d.dividir,
    "5": sa.suma_avanzada
  }

  while True:
    option = show_menu()
    if option == "6":
      print("Adiós")
      break
    if option in options:
      try:
        if option == "5":
          n = int(input("Número de elementos: "))
          args = [float(input(f"Elemento {i+1}: ")) for i in range(n)]
          result = options[option](*args)
        else:
          a = float(input("a: "))
          b = float(input("b: "))
          result = options[option](a, b)
        
        print(f"Resultado: {result}")
      except ValueError as e:
        print(e)
    else:
      print("Opción inválida")

if __name__ == "__main__":
  main()