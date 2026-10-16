# 14. Multithreading

Processadores modernos possuem dezenas de núcleos, mas os scripts Python padrão que você escreveu até agora rodam tudo um passo de cada vez (sincronamente). Vamos mudar isso.

## 1. Introdução
Multithreading é a técnica de dividir a execução de um programa em múltiplas "Threads" (linhas de execução) que funcionam ao mesmo tempo. Imagine um restaurante onde, em vez de um único cozinheiro preparar o prato, a sobremesa e o suco em sequência, três cozinheiros trabalham nas três tarefas simultaneamente.

## 2. Desenvolvendo a Fundação
Até agora, todo script possuía apenas a Thread Principal (Main Thread). Se seu código pedisse para baixar um arquivo gigante da internet na linha 10, a linha 11 ficava paralisada até o download acabar.

## 3. Necessidade de Multithreading
Usamos Multithreading primariamente quando nosso código sofre bloqueios que não dependem da CPU:
- Fazer downloads de várias URLs ao mesmo tempo.
- Manter a Interface Gráfica destravada enquanto um cálculo demorado acontece no fundo.
- Ler múltiplos arquivos gigantes simultaneamente.

## 4. Módulo de Threading
O Python possui um módulo embutido excelente para lidar com threads, chamado exatamente de `threading`. Ele simplifica absurdamente a complexidade de gerenciar processos.

```python
import threading
import time

def tarefa_demorada(nome):
    print(f"Tarefa {nome} começou!")
    time.sleep(2) # Simula um bloqueio/download de 2 segundos
    print(f"Tarefa {nome} terminou!")
```

## 5. Implementando Multithreading
Para colocar uma tarefa rodando de forma assíncrona, passamos a função para a classe `Thread` e chamamos o método `.start()`.

```python
# Em vez de chamar a função diretamente, criamos as Threads:
thread_1 = threading.Thread(target=tarefa_demorada, args=("Download A",))
thread_2 = threading.Thread(target=tarefa_demorada, args=("Download B",))

# Damos a largada! As duas começam juntas.
thread_1.start()
thread_2.start()

print("Programa Principal continuou a rodar, não foi bloqueado!")
```

## 6. Problema com a Thread Principal
Quando você roda o código acima, notará que o script Python pode fechar (ou apresentar o último print) antes que as Threads no fundo terminem. Se a Main Thread for finalizada, as threads filhas podem sofrer.

Para fazer a Thread Principal "esperar" que as filhas terminem antes de dar o programa como finalizado, usamos o método `.join()`.

```python
# O código trava aqui e espera a thread_1 finalizar
thread_1.join() 
# Espera a thread_2 finalizar
thread_2.join()

print("Todas as tarefas simultâneas acabaram com segurança. Adeus!")
```

---
*Próximo Módulo:* [[15. Projeto Dois - Biblioteca|15_Projeto_Dois_Biblioteca]]
