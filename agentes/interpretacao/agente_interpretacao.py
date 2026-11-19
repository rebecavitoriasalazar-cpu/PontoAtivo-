
class AgenteInterpretacao:

    def interpretar(self, pergunta):

        pergunta_original = pergunta
        pergunta = pergunta.lower().strip()

        # Identificar perguntas sobre esportes
        if any(p in pergunta for p in [
            "esporte",
            "esportes",
            "modalidade",
            "modalidades",
            "atividade esportiva",
            "atividades esportivas",
            "esportiva",
            "esportivas"
        ]):
            acao = "pesquisar_esportes"

        # Identificar perguntas sobre cadastro
        elif any(p in pergunta for p in [
            "cadastro",
            "cadastrar",
            "inscrição",
            "inscrições"
        ]):
            acao = "consultar_cadastro"

        # Identificar perguntas sobre inclusão
        elif any(p in pergunta for p in [
            "inclusão",
            "inclusivo",
            "inclusiva",
            "acessibilidade"
        ]):
            acao = "pesquisar_inclusao"

        # Caso não identifique a intenção
        else:
            acao = "intencao_nao_identificada"

        return {
            "pergunta_original": pergunta_original,
            "acao_identificada": acao,
            "status": "interpretado"
        }


if __name__ == "__main__":

    agente = AgenteInterpretacao()

    pergunta = input("Digite sua pergunta: ")

    resultado = agente.interpretar(pergunta)

    print("\nResultado da interpretação:")
    print(resultado)
