import threading
import time

def tarefa_demorada(nome):
    print(f"Tarefa {nome} começou!")
    time.sleep(2) # Simula um bloqueio/download de 2 segundos
    print(f"Tarefa {nome} terminou!")

thread_1 = threading.Thread(target=tarefa_demorada, args=("Download A",))
thread_2 = threading.Thread(target=tarefa_demorada, args=("Download B",))

# Damos a largada! As duas começam juntas.
thread_1.start()
thread_2.start()

print("Programa Principal não foi bloqueado, mas está esperando os downloads...")

# O código trava aqui e espera as threads
thread_1.join() 
thread_2.join()

print("Todas as tarefas simultâneas acabaram com segurança.")
