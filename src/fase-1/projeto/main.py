import os
from utils import (
    calcular_manejo_de_insumos, 
    mostrar_dados, 
    atualizar_dado, 
    deletar_dado, 
    salvar_csv,
    carregar_csv
)

def menu():
    vetor_dados = carregar_csv()
    print("🚀 Bem-vindo ao Sistema de \nManejo de Insumos Agrícolas!")
    while True:
        print("""
========= MENU =========
1 - Inserir dados
2 - Listar dados
3 - Atualizar dados
4 - Deletar dados
5 - Ver Estatísticas (R)
6 - Ver Previsão do Tempo (R)
0 - Sair
========================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cultura = input("Digite a cultura (ex: soja): ")
            try:
                resultado = calcular_manejo_de_insumos(cultura)
                vetor_dados.append(resultado)
                salvar_csv(vetor_dados)
                print("✅ Dados inseridos e salvos em CSV!\n")
            except KeyError:
                print(f"❌ Cultura '{cultura}' não encontrada no banco de dados.\n")
            except Exception as e:
                print(f"❌ Erro ao inserir dados: {e}\n")

        elif opcao == "2":
            mostrar_dados(vetor_dados)

        elif opcao == "3":
            atualizar_dado(vetor_dados)
            salvar_csv(vetor_dados)

        elif opcao == "4":
            deletar_dado(vetor_dados)
            salvar_csv(vetor_dados)

        elif opcao == "5":
            print("\n📊 Executando análise estatística em R...\n")
            os.system("Rscript analise.R")

        elif opcao == "6":
            cidade = input("Digite o nome da cidade (ex: Belo Horizonte,MG): ")
            if cidade:
                print(f"\n🌤️ Buscando previsão do tempo para: {cidade}...\n")
                os.system(f'Rscript wheater.r "{cidade}"')
            else:
                print("❌ Nome da cidade inválido!")

        elif opcao == "0":
            print("👋 Saindo do programa...")
            break

        else:
            print("❌ Opção inválida!\n")

if __name__ == "__main__":
    menu()