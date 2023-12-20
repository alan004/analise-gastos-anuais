import numpy as np

def converter_para_float(valor):
    try:
        return float(''.join(c for c in str(valor) if c.isdigit() or c == '.').replace(',', '.'))
    except (ValueError, TypeError):
        return np.nan

def get_categorias(excel_data):
    categorias = excel_data['Categorias']['Categorias'].unique()
    categorias_sorted = sorted(categorias)
    categorias_dict = {categoria: indice for indice, categoria in enumerate(categorias_sorted)}
    return categorias_dict

def gastos_totais(excel_data, meses):
    soma_gastos_total = 0
    soma_salarios_total = 0

    for mes in meses:
        if mes in excel_data:
            df_gastos = excel_data[mes]['Total de gastos']
            df_salarios = excel_data[mes]['Salario']
            df_gastos = df_gastos.apply(converter_para_float)
            df_salarios = df_salarios.apply(converter_para_float)
            soma_gastos_mes = df_gastos.iloc[0]
            soma_salarios_mes = df_salarios.iloc[0]

            soma_salarios_total += soma_salarios_mes
            soma_gastos_total += soma_gastos_mes
            soma_sobram_total = soma_salarios_total - soma_gastos_total

    return soma_gastos_total, soma_salarios_total, soma_sobram_total

def gastos_mensais(excel_data, meses):
    gastos_mensais = []
    sobras_mensais = []
    for mes in meses:
        if mes in excel_data:
            df_gastos = excel_data[mes]['Total de gastos']
            df_sobras = excel_data[mes]['Sobra dos gastos']
            df_gastos = df_gastos.apply(converter_para_float)
            df_sobras = df_sobras.apply(converter_para_float)
            soma_gastos_mes = df_gastos.iloc[0]
            soma_sobras_mes = df_sobras.iloc[0]
            gastos_mensais.append(soma_gastos_mes)
            sobras_mensais.append(soma_sobras_mes)
        else:
            gastos_mensais.append(np.nan)
    return gastos_mensais, sobras_mensais

def total_investido(excel_data, meses):
    total_investido = []
    for mes in meses:
        if mes in excel_data:
            df_investido = excel_data[mes][(excel_data[mes]['Despesa'].str.upper() == 'INVESTIMENTOS')]
            soma_investido_mes = df_investido['Valor'].sum()
            sobras_mes = excel_data[mes]['Sobra dos gastos'].iloc[0]
            if sobras_mes > 0:
                soma_investido_mes += sobras_mes
            total_investido.append(soma_investido_mes)
        else:
            total_investido.append(np.nan)
    return total_investido

def total_filtro_categoria(excel_data, meses, filtro):
    total_filtrado = []
    for mes in meses:
        if mes in excel_data:
            df_total_filtrado = excel_data[mes][(excel_data[mes]['Despesa'].str.upper() == filtro) ]      
            soma_total_mes = df_total_filtrado['Valor'].sum()
            total_filtrado.append(soma_total_mes)
        else:
            total_filtrado.append(np.nan)
    return total_filtrado

def total_filtro_termo(excel_data, meses, filtro):
    total_filtrado = []
    for mes in meses:
        if mes in excel_data:
            df_total_filtrado = excel_data[mes][(excel_data[mes]['Detalhes'].str.upper().str.contains(filtro))]      
            soma_total_mes = df_total_filtrado['Valor'].sum()
            total_filtrado.append(soma_total_mes)
        else:
            total_filtrado.append(np.nan)
    return total_filtrado

def comparar_categorias(excel_data, meses, filtro1, filtro2):
    total_filtrado1 = []
    total_filtrado2 = []
    for mes in meses:
        if mes in excel_data:
            df_total_filtrado1 = excel_data[mes][(excel_data[mes]['Despesa'].str.upper() == filtro1)]      
            soma_total_mes1 = df_total_filtrado1['Valor'].sum()

            df_total_filtrado2 = excel_data[mes][(excel_data[mes]['Despesa'].str.upper() == filtro2)]      
            soma_total_mes2 = df_total_filtrado2['Valor'].sum()

            total_filtrado1.append(soma_total_mes1)
            total_filtrado2.append(soma_total_mes2)
        else:
            total_filtrado1.append(np.nan)
            total_filtrado2.append(np.nan)
    total_soma = [sum(x) for x in zip(total_filtrado1, total_filtrado2)]
    return total_filtrado1, total_filtrado2, total_soma

def comparar_termos(excel_data, meses, filtro1, filtro2):
    total_filtrado1 = []
    total_filtrado2 = []
    for mes in meses:
        if mes in excel_data:
            df_total_filtrado1 = excel_data[mes][(excel_data[mes]['Detalhes'].str.upper().str.contains(filtro1))]      
            soma_total_mes1 = df_total_filtrado1['Valor'].sum()

            df_total_filtrado2 = excel_data[mes][(excel_data[mes]['Detalhes'].str.upper().str.contains(filtro2))]      
            soma_total_mes2 = df_total_filtrado2['Valor'].sum()

            total_filtrado1.append(soma_total_mes1)
            total_filtrado2.append(soma_total_mes2)
        else:
            total_filtrado1.append(np.nan)
            total_filtrado2.append(np.nan)
    total_soma = [sum(x) for x in zip(total_filtrado1, total_filtrado2)]
    return total_filtrado1, total_filtrado2, total_soma
