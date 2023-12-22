import pandas as pd
import matplotlib.pyplot as plt
import funcoes as fc

excel_file_path = 'DESPESAS.xlsx'
excel_data = pd.read_excel(excel_file_path, sheet_name=None)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

def graficos_totais():
    total_gastos, total_salarios, total_sobra = fc.gastos_totais(excel_data, meses)
    df_totais = pd.DataFrame({'Tipo': ['Gastos', 'Sobras', 'Salários'],
                            'Valor': [total_gastos, total_sobra, total_salarios]})
    plt.figure(figsize=(12, 6))

    # Gráfico de pizza - Gastos e Sobras
    plt.subplot(1, 2, 1)
    autotexts = plt.pie(df_totais['Valor'][:2], labels=df_totais['Tipo'][:2], autopct='%1.1f%%', colors=['blue', 'orange'], startangle=140)
    plt.title('Proporção entre Sobras e Total de Gastos')
    # Adiciona os valores no centro do gráfico
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(12)

    # Gráfico de Barras - Salários, Gastos e Sobras
    plt.subplot(1, 2, 2)
    bars = plt.bar(df_totais['Tipo'], df_totais['Valor'], color=['green', 'blue', 'orange'])
    plt.title('Salários, Gastos e Sobras Totais')

    # Adiciona os valores acima das barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 2), ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.show()

def graficos_mensais():
    total_meses, sobras_meses = fc.gastos_mensais(excel_data, meses)
    df_meses = pd.DataFrame({'Mês': meses, 'Total': total_meses, 'Sobras': sobras_meses})

    # Gráfico de linha
    plt.figure(figsize=(10, 6))
    plt.plot(df_meses['Mês'], df_meses['Total'], marker='o', color='blue', label='Total de Gastos')
    plt.xlabel('Mês')
    plt.ylabel('Valor')
    plt.title('Gastos Mensais - Total de Gastos')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Gráfico de linha - Gastos/Sobras
    plt.figure(figsize=(10, 6))
    plt.plot(df_meses['Mês'], df_meses['Sobras'], marker='o', color='orange', label='Sobras')
    plt.plot(df_meses['Mês'], df_meses['Total'], marker='o', color='blue', label='Total de Gastos')
    plt.xlabel('Mês')
    plt.ylabel('Valor')
    plt.title('Gastos Mensais - Sobras')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Gráfico de barras - Total de Gastos e Sobras
    plt.figure(figsize=(10, 6))
    plt.bar(df_meses['Mês'], df_meses['Total'], color='blue', label='Total de Gastos')
    plt.bar(df_meses['Mês'], df_meses['Sobras'], color='orange', label='Sobras', bottom=0)
    for i, (total, sobra) in enumerate(zip(df_meses['Total'], df_meses['Sobras'])):
        plt.text(i, (total + sobra) / 2, f'{total:.2f}', ha='center', va='center', color='white', fontsize=8)
    plt.xlabel('Mês')
    plt.ylabel('Valores')
    plt.title('Gastos Mensais - Total de Gastos e Sobras')
    plt.legend()
    plt.grid(True)
    plt.show()

def graficos_investimentos():
    total_meses = fc.total_investido(excel_data, meses)
    df_meses = pd.DataFrame({'Mês': meses, 'Total': total_meses,})

    plt.figure(figsize=(12, 6))
    # Gráfico de linha
    plt.subplot(1, 2, 1)
    plt.plot(df_meses['Mês'], df_meses['Total'], marker='o', color='blue', label='Total investido por mês')
    plt.xlabel('Mês')
    plt.ylabel('Valor')
    plt.title('Investimentos Mensais')
    plt.text('Total Anual', df_meses['Total'].sum(), f'{df_meses["Total"].sum():.2f}', ha='center', va='bottom')
    plt.legend()
    plt.grid(True)

    # Gráfico de barra anual
    plt.subplot(1, 2, 2)
    bars = plt.bar(['Total Anual'], [df_meses['Total'].sum()], color='green')
    plt.xlabel('Ano')
    plt.ylabel('Valor')
    plt.title('Investimentos Totais no Ano')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    plt.legend()
    plt.show()

def graficos_filtrar_categorias():
    print("(1) Escolher categoria (2) Pesquisar um termo")
    option = int(input("Opção escolhida: "))
    categorias = fc.get_categorias(excel_data)
    if option == 1:
        # Exibe as categorias disponíveis
        print("Categorias disponíveis:")
        for categoria, numero in categorias.items():
            print(f"{numero}: {categoria}")
        numero_categoria = int(input("Escolha o número correspondente à categoria desejada: "))
        if numero_categoria in categorias.values():
            filtro = [categoria for categoria, numero in categorias.items() if numero == numero_categoria][0].upper()
            
        total_meses = fc.total_filtro_categoria(excel_data, meses, filtro)
        df_meses = pd.DataFrame({'Mês': meses, 'Total': total_meses,})
    elif option == 2:
        filtro=input('Digite o termo: ').upper()
        total_meses = fc.total_filtro_termo(excel_data, meses, filtro)
        df_meses = pd.DataFrame({'Mês': meses, 'Total': total_meses,})
    else:
        print('Opção inválida!')

    plt.figure(figsize=(12, 6))
    # Gráfico de linha
    plt.subplot(1, 2, 1)
    plt.plot(df_meses['Mês'], df_meses['Total'], marker='o', color='blue', label='')
    plt.xlabel('Mês')
    plt.ylabel('Valor')
    plt.title(f'Gastos Mensais com {filtro}')
    plt.text('Total Anual', df_meses['Total'].sum(), f'{df_meses["Total"].sum():.2f}', ha='center', va='bottom')
    plt.legend()
    plt.grid(True)

    # Gráfico de barra - Valor total do ano
    plt.subplot(1, 2, 2)
    bars = plt.bar(['Total Anual'], [df_meses['Total'].sum()], color='green', label='')
    plt.xlabel('Ano')
    plt.ylabel('Valor')
    plt.title(f'Gastos com {filtro} Totais no Ano')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    plt.legend()
    plt.tight_layout() 
    plt.show()

def graficos_comparar_categorias():
    print("(1) Comparar entre categorias (2) Comparar entre termos de pesquisa")
    option = int(input("Opção escolhida: "))
    categorias = fc.get_categorias(excel_data)
    if option == 1:
        print("Categorias disponíveis:")
        for numero, categoria in categorias.items():
            print(f"{numero}: {categoria}")
        numero_categoria1 = int(input("Escolha o número correspondente à primeira categoria desejada: "))
        numero_categoria2 = int(input("Escolha o número correspondente à segunda categoria desejada: "))
        
        if numero_categoria1 in categorias.values() and numero_categoria2 in categorias.values():
            filtro1 = [categoria for categoria, numero in categorias.items() if numero == numero_categoria1][0].upper()
            filtro2 = [categoria for categoria, numero in categorias.items() if numero == numero_categoria2][0].upper()
            print(f'Comparando {filtro1} e {filtro2}')
            total_meses_filtro1, total_meses_filtro2, total_soma = fc.comparar_categorias(excel_data, meses, filtro1, filtro2)
            df_meses = pd.DataFrame({'Mês': meses, f'Total {filtro1}': total_meses_filtro1, f'Total {filtro2}': total_meses_filtro2, 'Total Soma': total_soma})
        else:
            print('Opção inválida!')
    elif option == 2:
        filtro1 =input('Digite o termo 1: ').upper()
        filtro2 =input('Digite o termo 2: ').upper()
        total_meses_filtro1, total_meses_filtro2, total_soma = fc.comparar_termos(excel_data, meses, filtro1, filtro2)
        df_meses = pd.DataFrame({'Mês': meses, f'Total {filtro1}': total_meses_filtro1, f'Total {filtro2}': total_meses_filtro2, 'Total Soma': total_soma})

    else:
        print('Opção inválida!')

    plt.figure(figsize=(12, 6))
    # Gráfico de linha
    plt.subplot(1, 3, 1)
    plt.plot(df_meses['Mês'], df_meses[f'Total {filtro1}'], marker='o', color='blue', label=f'Total {filtro1}')
    plt.plot(df_meses['Mês'], df_meses[f'Total {filtro2}'], marker='o', color='orange', label=f'Total {filtro2}')
    plt.xlabel('Mês')
    plt.ylabel('Valor')
    plt.title(f'Comparação: {filtro1} e {filtro2}')
    plt.legend()
    plt.grid(True)

    # Gráfico de barra - valor total mensal
    plt.subplot(1, 3, 2)
    plt.bar(df_meses['Mês'], df_meses[f'Total {filtro1}'], color='blue', label=f'Total {filtro1}')
    plt.bar(df_meses['Mês'], df_meses[f'Total {filtro2}'], color='orange', label=f'Total {filtro2}', bottom=df_meses[f'Total {filtro1}'])
    plt.xlabel('Mês')
    plt.ylabel('Valor')
    plt.title(f'Somas mensais: {filtro1} e {filtro2}')

    # Gráfico de barra - valor total do ano Somado    
    plt.subplot(1, 3, 3)
    bars3 = plt.bar(['Total Soma'], [df_meses['Total Soma'].sum()], color='green', width=0.25)
    plt.xlabel('Ano')
    plt.ylabel('Valor')
    plt.title(f'Total Anual de {filtro1} e {filtro2}')

    for bar in bars3:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    plt.legend()
    plt.tight_layout() 
    plt.show()

def principais():
        graficos_mensais()
        graficos_investimentos()
        graficos_totais()
