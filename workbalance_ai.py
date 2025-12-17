# FIAP GS PYTHON 2025

# Claudio A. C. Junior
# Luna R.
# Rodrigo W. Giorgi

import numpy as np
from datetime import datetime

def calcular_media_horas(lista_colaboradores):
    """Retorna a média de horas trabalhadas"""
    if not lista_colaboradores:
        return 0.0
    total_horas = sum(colab['horas'] for colab in lista_colaboradores)
    return total_horas / len(lista_colaboradores)

def maior_estresse(lista_colaboradores):
    """Retorna o nome do colaborador com maior nível de estresse"""
    if not lista_colaboradores:
        return None
    max_estresse = max(colab['estresse'] for colab in lista_colaboradores)
    for colab in lista_colaboradores:
        if colab['estresse'] == max_estresse:
            return colab['nome']
    return None

def colaboradores_produtivos(lista_colaboradores):
    """Retorna os nomes dos que realizaram 5 ou mais tarefas"""
    return [colab['nome'] for colab in lista_colaboradores if colab['tarefas'] >= 5]

def alerta_equilibrio(lista_colaboradores):
    """Retorna os colaboradores com estresse >= 4 e pausas <= 1"""
    return [colab['nome'] for colab in lista_colaboradores if colab['estresse'] >= 4 and colab['pausas'] <= 1]

def feedback(colaborador):
    """Gera uma mensagem personalizada com base no estresse e produtividade"""
    nome = colaborador['nome']
    estresse = colaborador['estresse']
    tarefas = colaborador['tarefas']
    pausas = colaborador['pausas']
    
    if estresse <= 2 and tarefas >= 5:
        return f"{nome}: ótimo desempenho! Continue equilibrando suas pausas."
    elif estresse >= 4 and pausas <= 1:
        return f"{nome}: alta carga e poucas pausas. Sugestão: reorganize suas tarefas."
    elif estresse >= 3:
        return f"{nome}: nível de estresse elevado. Considere mais pausas para manter o equilíbrio."
    else:
        return f"{nome}: bom equilíbrio geral. Mantenha o foco na produtividade."

def salvar_relatorio(relatorio, feedbacks):
    """Salva o relatório em um arquivo com data e hora"""
    try:
        with open('relatorio_workbalance.txt', 'a', encoding='utf-8') as f:
            f.write(f"Data e Hora da Execução: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(relatorio)
            f.write("\n\nFeedbacks Personalizados:\n")
            for fb in feedbacks:
                f.write(fb + "\n")
        print("Relatório salvo com sucesso em 'relatorio_workbalance.txt'.")
    except Exception as e:
        print(f"Erro ao salvar o relatório: {e}")

def main():
    colaboradores = []
    
    for i in range(5):
        print(f"\nColetando dados do colaborador {i+1}:")
        
        nome = input("Nome: ").strip()
        if not nome:
            print("Nome não pode ser vazio. Tente novamente.")
            i -= 1
            continue
        
        dept = input("Departamento: ").strip()
        
        # Validação de horas
        while True:
            try:
                horas = float(input("Horas trabalhadas no dia: "))
                if horas < 0:
                    raise ValueError("Horas devem ser positivas.")
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Tente novamente.")
        
        # Validação de pausas
        while True:
            try:
                pausas = int(input("Pausas realizadas (quantidade): "))
                if pausas < 0:
                    raise ValueError("Pausas devem ser não negativas.")
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Tente novamente.")
        
        # Validação de estresse
        while True:
            try:
                estresse = int(input("Nível de estresse percebido (1 a 5): "))
                if not (1 <= estresse <= 5):
                    raise ValueError("Estresse deve estar entre 1 e 5.")
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Tente novamente.")
        
        # Validação de tarefas
        while True:
            try:
                tarefas = int(input("Tarefas concluídas: "))
                if tarefas < 0:
                    raise ValueError("Tarefas devem ser não negativas.")
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Tente novamente.")
        
        colaborador = {
            "nome": nome,
            "dept": dept,
            "horas": horas,
            "pausas": pausas,
            "estresse": estresse,
            "tarefas": tarefas
        }
        colaboradores.append(colaborador)
    
    # Cálculos com NumPy
    horas_array = np.array([colab['horas'] for colab in colaboradores])
    media_horas = np.mean(horas_array)
    desvio_horas = np.std(horas_array)
    media_estresse = np.mean([colab['estresse'] for colab in colaboradores])
    
    # Chamadas de funções
    media_horas_func = calcular_media_horas(colaboradores)
    maior_estressado = maior_estresse(colaboradores)
    produtivos = colaboradores_produtivos(colaboradores)
    alertas = alerta_equilibrio(colaboradores)
    
    # Gerar feedbacks
    feedbacks = [feedback(colab) for colab in colaboradores]
    
    # Relatório
    relatorio = f"""RELATÓRIO WORKBALANCE AI
-------------------------
Média de horas trabalhadas: {media_horas:.1f}h
Desvio padrão de horas: {desvio_horas:.1f}
Média de estresse: {media_estresse:.1f}
Colaborador mais estressado: {maior_estressado if maior_estressado else 'Nenhum'}
Colaboradores com 5+ tarefas: {produtivos}
Alerta de equilíbrio: {alertas}
"""
    
    print(relatorio)
    print("\nFeedbacks Personalizados:")
    for fb in feedbacks:
        print(fb)
    
    # Salvar relatório
    salvar_relatorio(relatorio, feedbacks)

if __name__ == "__main__":
    main()
