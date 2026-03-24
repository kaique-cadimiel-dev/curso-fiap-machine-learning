from tabulate import tabulate
import locale
import json

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def read_data(path: str) -> dict:
    with open(path  , "r") as file:
        dados = json.load(file)
    return dados

def calcular_area() -> str:
    """
    Para calcular a area utiliza-se a formula b * a / 2
    """
    baseInput:float = float(input("Digite base em metro, formato inteiro: ").replace(".", ""))
    alturaInput:float = float(input("Digite altura em, formato inteiro: ").replace(".", ""))
    result: float = (baseInput * alturaInput) / 2
    
    return result

def calcular_manejo_de_insumos(cultura: str):
    """
    # 1. Converter área de m² para hectares
    hectares = area_m2 / 10000

    # 2. Calcular dose total de fosforo para a área
    dose_total_fosforo = dose_por_hectar * hectares

    # 3. Converter dose de fosforo em kg de fertilizante
    fertilizante_kg = dose_total_fosforo / (teor_fertilizante / 100)

    # Onde:
    # area_m2 = área do terreno em m²
    # dose_por_hectar = quantidade recomendada de fosforo por hectare
    # teor_fertilizante = % de fosforo no fertilizante
    """
    dados = read_data("./data.json")
    area = calcular_area()
    hectares = area / 10000
    dose_total_fosforo = dados[cultura]["qnt_fosforo_por_hectar_kg"] * hectares
    percentual_fertilizante = dados[cultura]["teor_fertilizante"] / 100
    fertilizante_kg = dose_total_fosforo / percentual_fertilizante

    return {
        "cultura": cultura,
        "area_m2": area,
        "hectares": hectares,
        "fosforo": dose_total_fosforo,
        "fertilizante": fertilizante_kg
    }

def mostrar_dados(vetor):
    """"
    Exibe os dados em formato de tabela utilizando a biblioteca tabulate.
    """
    if not vetor:
        print("\n⚠️ Nenhum dado cadastrado.\n")
        return

    tabela = []
    for i, item in enumerate(vetor):
        tabela.append([
            i,
            item["cultura"],
            f"{item['area_m2']:.2f}",
            f"{item['hectares']:.4f}",
            f"{item['fosforo']:.2f}",
            f"{item['fertilizante']:.2f}"
        ])

    print(tabulate(
        tabela,
        headers=["ID", "Cultura", "Área m²", "Hectares", "Fósforo (kg)", "Fertilizante (kg)"],
        tablefmt="grid"
    ))


def atualizar_dado(vetor):
    """"
    Atualiza dados existentes no vetor, solicitando ao usuário o ID do dado a ser atualizado e a nova cultura.
    Em seguida, recalcula os insumos com base na nova cultura e atualiza o vetor
    """
    mostrar_dados(vetor)
    try:
        index = int(input("Digite o ID para atualizar: "))
        cultura = input("Digite a nova cultura: ")
        vetor[index] = calcular_manejo_de_insumos(cultura)
        print("✅ Dado atualizado com sucesso!\n")
    except:
        print("❌ Erro ao atualizar.\n")


def deletar_dado(vetor):
    """
    Deleta um dado do vetor, solicitando ao usuário o ID do dado a ser removido. 
    Em seguida, remove o dado do vetor.
    """
    mostrar_dados(vetor)
    try:
        index = int(input("Digite o ID para deletar: "))
        vetor.pop(index)
        print("🗑️ Dado removido com sucesso!\n")
    except:
        print("❌ Erro ao deletar.\n")
