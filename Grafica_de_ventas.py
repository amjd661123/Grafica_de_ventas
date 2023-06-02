import matplotlib.pyplot as plt

def ventas(inical,final):
    ventas = []
    años = []
    for i in range(inicial, final +1):
        años.append(i)
        ventas.append(int(input(f'Ingresa las ventas del año {i}: ')))
    return años, ventas

inicial = int(input("Año inicial: "))
final = int(input("Año final: "))

# Datos
x, y = ventas(inicial,final)

# Gráfico de líneas
fig, ax = plt.subplots()
ax.plot(x, y,color = "r", marker = "o", markersize = 5)
ax.set_title('Ventas anuales')
ax.set_xlabel('Año')
ax.set_xticks(range(inicial,final))
ax.set_ylabel('Ventas')
plt.show() 
