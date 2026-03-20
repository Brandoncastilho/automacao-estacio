import requests
import json

def bypass():
      print("--- Automacao Estacio Universal ---")

    # Coleta de dados
      token = input("Digite seu Bearer Token: ").replace("Bearer ", "")
      theme_id = input("Digite o Theme ID (ex: 02817): ")

    # IDs capturados para o tema de exemplo
      example_components = ["60381612", "60381615", "60381614", "60381613", "60381616", "60381617"]

    components_input = input("Digite os IDs dos componentes separados por virgula (ou Enter para exemplos): ")

    if not components_input:
              components = example_components
else:
          components = [c.strip() for c in components_input.split(",")]

    url = "https://apis.estudante.estacio.br/rest/conclusoes"
    headers = {
              "Authorization": f"Bearer {token}",
              "Content-Type": "application/json",
              "Origin": "https://estudante.estacio.br",
              "Referer": "https://estudante.estacio.br/"
    }

    for comp_id in components:
              payload = {
                            "componentId": comp_id,
                            "themeId": theme_id,
                            "ncId": "introducao"
              }

        print(f"Tentando concluir componente {comp_id}...")
        try:
                      response = requests.post(url, headers=headers, json=payload)
                      if response.status_code in [200, 201]:
                                        print(f"  [OK] Componente {comp_id} concluido com sucesso!")
        else:
                print(f"  [ERRO] Falha: {response.status_code}")
        except Exception as e:
            print(f"  [ERRO] Excecao: {e}")

    print("\nProcesso finalizado.")

if __name__ == "__main__":
      bypass()
