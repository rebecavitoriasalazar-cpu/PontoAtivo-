
from agente_interpretacao import AgenteInterpretacao

agente = AgenteInterpretacao()

# Lista de testes
testes = [
    {
        "pergunta": "Quais esportes existem em Brasília?",
        "esperado": "pesquisar_esportes"
    },
    {
        "pergunta": "Quero conhecer atividades esportivas no DF.",
        "esperado": "pesquisar_esportes"
    },
    {
        "pergunta": "Como faço meu cadastro?",
        "esperado": "consultar_cadastro"
    },
    {
        "pergunta": "Quero realizar minha inscrição.",
        "esperado": "consultar_cadastro"
    },
    {
        "pergunta": "Quais atividades são inclusivas?",
        "esperado": "pesquisar_inclusao"
    },
    {
        "pergunta": "Quero saber sobre acessibilidade.",
        "esperado": "pesquisar_inclusao"
    },
    {
        "pergunta": "Qual é a previsão do tempo?",
        "esperado": "intencao_nao_identificada"
    }
]

aprovados = 0
reprovados = 0

print("INICIANDO TESTES DO AGENTE DE INTERPRETAÇÃO")
print("-" * 50)

for numero, teste in enumerate(testes, start=1):

    resultado = agente.interpretar(teste["pergunta"])

    acao_obtida = resultado["acao_identificada"]
    acao_esperada = teste["esperado"]

    print(f"\nTESTE {numero}")
    print("Pergunta:", teste["pergunta"])
    print("Ação obtida:", acao_obtida)

    if acao_obtida == acao_esperada:
        print("RESULTADO: APROVADO")
        aprovados += 1
    else:
        print("RESULTADO: REPROVADO")
        reprovados += 1

print("\n" + "=" * 50)
print("RESUMO DOS TESTES")
print("Total:", len(testes))
print("Aprovados:", aprovados)
print("Reprovados:", reprovados)

if reprovados == 0:
    print("\nTODOS OS TESTES FORAM APROVADOS!")
else:
    print("\nALGUNS TESTES PRECISAM DE CORREÇÃO.")
