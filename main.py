import graficos

def escolhe_grafico():
    while True:
        boas_vindas()
        grafico = int(input("Opção escolhida:"))
        if grafico == 0:
            print("Saindo...")
            break
        abrir_grafico(grafico)

def boas_vindas():
    print("*******************************")
    print("*****Escolha sua análise*******")
    print("*******************************")
    print("(1) Gráficos Principais (2) Filtrar Despesa (3) Comparar Despesa  (0) Sair")

def abrir_grafico(grafico):
    if grafico == 1:
        print("Gráficos principais")
        graficos.principais()
    elif grafico == 2:
        print("Filtrar despesa")
        graficos.graficos_filtrar_categorias()
    elif grafico == 3:
        print("Comparar despesa")
        graficos.graficos_comparar_categorias()
    elif grafico == 0:
        print("Saindo...")
    else:
        print("Escolha uma opção válida")

if __name__ == "__main__":
    escolhe_grafico()
