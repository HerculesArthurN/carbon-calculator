from emissions import calcular_emissoes
import matplotlib.pyplot as plt

def entrada_usuaria():
    print("=== Calculadora de Pegada de Carbono ===")
    km = float(input("Quantos km você dirige por semana? "))
    kwh = float(input("Quantos kWh você consome por semana? "))
    carne = int(input("Quantas refeições com carne você faz por semana? "))
    return km, kwh, carne

def mostrar_resultados(emissoes: dict):
    print("\n--- Resultados ---")
    for categoria, valor in emissoes.items():
        if categoria != "total":
            print(f"{categoria.capitalize()}: {valor:.2f} kg CO₂/semana")
    print(f"Total: {emissoes['total']:.2f} kg CO₂/semana")

def gerar_grafico(emissoes: dict):
    categorias = ["Transporte", "Energia", "Alimentação"]
    valores = [emissoes["transporte"], emissoes["energia"], emissoes["alimentacao"]]

    plt.bar(categorias, valores, color=["#4CAF50", "#2196F3", "#FFC107"])
    plt.title("Pegada de Carbono por Categoria (kg CO₂/semana)")
    plt.ylabel("kg CO₂")
    plt.tight_layout()
    plt.show()

def main():
    km, kwh, carne = entrada_usuaria()
    emissoes = calcular_emissoes(km, kwh, carne)
    mostrar_resultados(emissoes)
    gerar_grafico(emissoes)

if __name__ == "__main__":
    main()
