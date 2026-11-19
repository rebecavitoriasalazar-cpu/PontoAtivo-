# AGENTE 1 — INTERPRETAÇÃO
## Projeto PontoAtivo

### 1. Apresentação

O Agente de Interpretação é responsável por receber as perguntas dos usuários, analisar suas solicitações e identificar a intenção principal de cada mensagem.

Ele funciona como a primeira etapa do fluxo de agentes inteligentes do PontoAtivo.

### 2. Objetivo

Identificar o que o usuário deseja realizar e transformar sua pergunta em uma ação padronizada, facilitando a comunicação com os demais agentes do sistema.

### 3. Funcionamento

O agente executa as seguintes etapas:

1. Recebe a pergunta em linguagem natural.
2. Armazena a pergunta original.
3. Normaliza o texto para análise.
4. Identifica palavras e expressões relacionadas à intenção.
5. Define a ação correspondente.
6. Retorna os dados estruturados para utilização pelo próximo agente.

### 4. Intenções identificadas

O agente possui quatro classificações principais:

- `pesquisar_esportes`: perguntas relacionadas a esportes, modalidades e atividades esportivas.
- `consultar_cadastro`: solicitações relacionadas a cadastro e inscrição.
- `pesquisar_inclusao`: perguntas relacionadas à inclusão e acessibilidade.
- `intencao_nao_identificada`: utilizada quando não é possível reconhecer uma das intenções previstas.

### 5. Estrutura de entrada

O agente recebe uma pergunta escrita pelo usuário.

Exemplo:

"Quais esportes existem em Brasília?"

### 6. Estrutura de saída

O agente retorna um dicionário contendo:

- pergunta_original;
- acao_identificada;
- status.

### 7. Tecnologias utilizadas

- Python;
- Programação orientada a objetos;
- Estruturas condicionais;
- Manipulação de strings;
- Testes automatizados com assert.

### 8. Testes realizados

Foram desenvolvidos sete cenários de teste, contemplando:

1. Pesquisa de esportes.
2. Identificação de atividades esportivas.
3. Consulta de cadastro.
4. Solicitação de inscrição.
5. Identificação de atividades inclusivas.
6. Consulta sobre acessibilidade.
7. Pergunta fora das categorias previstas.

Os sete testes foram executados com sucesso.

### 9. Integração com os demais agentes

O Agente de Interpretação representa a primeira etapa do fluxo de processamento.

Após identificar a intenção do usuário, retorna uma ação padronizada que poderá ser encaminhada ao Agente 2 — Pesquisa.

A integração definitiva depende do alinhamento do formato de comunicação entre os agentes.

### 10. Considerações finais

O desenvolvimento do Agente de Interpretação estabelece a base para o processamento de linguagem natural dentro do projeto PontoAtivo, permitindo organizar as solicitações dos usuários e direcioná-las conforme suas intenções.