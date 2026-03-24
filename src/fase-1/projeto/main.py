from tabulate import tabulate
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def calcular_area() -> str:
    """
    Para calcular a area utiliza-se a formula b * a / 2
    """
    baseInput:float = float(input("Digite base em metro, formato inteiro: ").replace(".", ""))
    alturaInput:float = float(input("Digite altura em, formato inteiro: ").replace(".", ""))
    result: float = (baseInput * alturaInput) / 2
    headers = ["Área", "Altura", "Result"]
    dados = [
        [
            baseInput, 
            alturaInput,
            result
        ]
    ]
    table = tabulate(dados, headers, tablefmt="grid")
    
    return table

print(calcular_area())
