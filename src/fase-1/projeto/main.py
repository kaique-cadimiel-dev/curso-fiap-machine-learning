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

    return tabulate([
        ["Área (m²)", f"{area:.2f}"],
        ["Área (hectares)", f"{hectares:.4f}"],
        ["Dose total de fosforo (kg)", f"{dose_total_fosforo:.2f}"],
        ["Quantidade de fertilizante (kg)", f"{fertilizante_kg:.2f}"]
    ], headers=["Métrica", "Valor"], tablefmt="grid")


# print(calcular_area())
print(calcular_manejo_de_insumos("soja"))