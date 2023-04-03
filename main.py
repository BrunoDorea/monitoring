import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# configurando o gráfico
figure, ax = plt.subplots()
ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
ax.set_title('Uso de CPU e Memória')
ax.set_xlabel('Tempo')
ax.set_ylabel('Uso (%)')
cpu_line, = ax.plot([], [], label='CPU', color='orange')
mem_line, = ax.plot([], [], label='Memória', color='red')
disk_line, = ax.plot([], [], label='Disco', color='blue')
ax.legend()

# add textos aos valores da cpu e memória
cpu_text = ax.text(0.77, 0.7, '', transform=ax.transAxes)
mem_text = ax.text(0.77, 0.6, '', transform=ax.transAxes)
disk_text = ax.text(0.77, 0.5, '', transform=ax.transAxes)

# função de atualização do gráfico
def update_chart(frame):
    # obter informações de uso da cpu
    cpu = psutil.cpu_percent()

    # obter informações de uso de memória
    memory = psutil.virtual_memory()
    memory_percent = memory.percent

    # obter informações de uso de disco
    disk_usage = psutil.disk_usage("/")

    # add os dados ao gráfico
    cpu_line.set_data(list(range(frame)), [cpu] * frame)
    mem_line.set_data(list(range(frame)), [memory_percent] * frame)
    disk_line.set_data(list(range(frame)), [disk_usage] * frame)

    # att textos com os valores da cpu e memória
    cpu_text.set_text(f'CPU: {cpu:.1f}%')
    mem_text.set_text(f'Memória: {memory_percent:.1f}%')
    disk_text.set_text(f"Uso de disco: {disk_usage.percent}%")

    return cpu_line, cpu_text, mem_line, mem_text, disk_line, disk_text

# add animação ao gráfico
animation = FuncAnimation(figure, update_chart, frames=1, interval=10, blit=True)

# estilizando gráfico
for line in [cpu_line, mem_line]:
    line.set_linewidth(2)
    line.set_marker('o')
    line.set_markersize(5)

# Estiliza o fundo do gráfico
ax.set_facecolor('#F5F5F5')

plt.show()
