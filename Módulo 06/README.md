<div class="hero-image">
    <div class="frame">
        <img src="../assets/pedromuracchini.png" alt="Introdução e utilização de GenAI">
    </div>
</div>

# Módulo 6 - Introdução e utilização de GenAI
Anotações da aula sobre Inteligência Artificial Generativa (GenAI) e como ela se encaixa no dia a dia de quem trabalha com dados. Instrutor: [Pedro Muracchini](https://www.linkedin.com/in/pedro-muracchini/), Team Lead / AI Engineer na Indicium.

## O que já era esperado como pré-requisito

- Conhecimentos gerais de lógica de programação
- Conhecimentos gerais na linguagem Python
- Conhecimentos gerais em SQL

O foco da aula foi entender o uso de ferramentas de GenAI para geração de código SQL, análise de dados e uso no dia a dia — não construir modelos do zero.

## O que aprendi

**IA Preditiva x IA Generativa**

Isso ficou bem mais claro depois da aula: eu já usava "IA" como um termo genérico, mas GenAI é só um subconjunto dentro de Deep Learning, que por sua vez é um subconjunto de Machine Learning, que por sua vez é um subconjunto de IA como um todo.

```
Inteligência Artificial (bases de conhecimento, sistemas especialistas...)
 └── Machine Learning (SVM, árvores de decisão, clusterização...)
      └── Deep Learning (redes neurais, CNNs...)
           └── Generative AI (LLMs, redes adversariais/GANs...)
```

A capacidade de aprendizado da GenAI não se limita a texto: ela cobre desde linguagem humana e linguagens de programação até arte, química, biologia e outros assuntos complexos.

A diferença prática entre os dois mundos:

| Característica | IA Preditiva (Ex: ML Clássico) | IA Generativa (Ex: LLMs) |
|---|---|---|
| Objetivo principal | Fazer previsões, classificações ou clusterizações | Criar conteúdo novo e original |
| Tipo de pergunta | "Este e-mail é spam ou não?" (classificação) | "Escreva um e-mail de resposta para este cliente" (geração) |
| Exemplo | "Qual a chance deste cliente cancelar o plano?" (previsão) | "Gere 100 novas amostras de dados de clientes" (data augmentation) |
| Saída | Um número, uma categoria, um sim/não | Texto, código, imagem, áudio |
| Foco | Entender padrões **existentes** nos dados | Aprender a **estrutura** subjacente pra criar de novo |

**Como uma GenAI "aprende"**

Ela funciona aprendendo padrões a partir de grandes quantidades de dados estruturados e não estruturados, usando um tipo de rede neural chamado **Transformers**. Esse é o pulo do gato: os Transformers entendem o *contexto* das informações, analisando como cada palavra (ou elemento) se relaciona com as outras — e é assim que conseguem prever a próxima palavra, imagem ou som de forma coerente.

Resumindo: uma GenAI não "pensa" como um humano, ela reconhece padrões complexos e gera conteúdo novo com base no que aprendeu — coerente com o contexto, não necessariamente verdadeiro.

## Linha do tempo da IA (resumo)

Achei interessante ver o histórico todo, desde o Teste de Turing até os agentes de hoje:

- **1950** — Teste de Turing, ideia de máquinas que "pensam"
- **1956** — Conferência de Dartmouth, nascimento oficial do campo de IA
- **1961** — Unimate, primeiro robô industrial (GM)
- **1964** — ELIZA, primeiro chatbot da história
- **1966** — Shakey, primeiro robô móvel com visão computacional
- **1970-1990** — AI Winter, período de baixo investimento e interesse (~20 anos)
- **1990s** — Machine Learning: IA passa a aprender com dados, não só regras
- **2000s** — Big Data: mais dados, mais poder computacional e adoção em massa (empresas usando IA pra recomendação, busca, publicidade)
- **2010s** — Deep Learning: redes neurais profundas superam humanos em visão, fala e tradução
- **2017** — Paper "Attention Is All You Need", nascem os Transformers (base do GPT, BERT etc.)
- **2022** — Lançamento do ChatGPT, IA generativa se populariza
- **2025** — Agentes: IAs deixam de só responder e passam a executar tarefas completas com múltiplas ferramentas, de forma autônoma

## Onde a GenAI entra no dia a dia

As três ferramentas mais citadas em aula foram **ChatGPT**, **Claude** e **Gemini**. Separei os exemplos de prompt por categoria de uso:

**Tarefas técnicas**
```
Geração de código:
"Escreva um script PySpark para ler dados de um S3, aplicar a
transformação X e salvar no BigQuery."

Documentação:
"Gere a documentação (docstrings) para esta função Python."

Otimização:
"Analise esta query SQL e sugira uma forma mais performática."

Debug:
"Analise o erro apresentado e identifique o erro no meu código."
```

**Tarefas do dia a dia**
```
Construção de apresentações:
"Escreva um roteiro de 10 slides sobre o tema X."

Sumarização de documentos:
"Gere um resumo desse documento com seus principais pontos."

Refino de mensagens:
"Deixe esse e-mail com um tom enfático nas necessidades
definidas e sendo claro nos passos."

Brainstorm:
"Dê 10 ideias sobre o tema Y, com prós e contras de cada uma."
```

**Ferramentas integradas ao ecossistema Google**, que ajudam a ganhar produtividade sem sair do que já uso:

| Ferramenta | Uso prático |
|---|---|
| Gmail | Redigir, revisar ou adequar o tom de um e-mail (botão do Gemini direto no Gmail) |
| NotebookLM | Sintetizar PDFs, vídeos, transcrições e áudios; gerar resumos, flashcards, quiz, provas e até podcast sobre um assunto |
| Google Drive (Gemini) | Busca inteligente de arquivos com linguagem natural e criação automatizada de relatórios/apresentações |

## O profissional de dados com GenAI

**A pergunta que todo mundo faz: a IA vai me substituir?**

A resposta que ficou da aula foi **não** — a GenAI não veio para substituir profissionais, veio para potencializar habilidades. Ela automatiza tarefas repetitivas, acelera análises e gera ideias, liberando tempo pra atividades criativas e estratégicas (raciocínio, decisão, criatividade). Em vez de competir com a inteligência humana, ela trabalha em parceria. O risco real não é "ser substituído pela IA", é ser substituído por alguém que usa a IA melhor do que eu.

**Como a GenAI conecta áreas diferentes**

Achei esse o ponto mais prático da aula: hoje um especialista consegue "invadir" a área de outro especialista com ajuda da IA, sem precisar virar expert naquilo:

- Um **Engenheiro de Dados** pode usar GenAI pra gerar um script de EDA em R (tarefa normalmente de Cientista de Dados), pra entender os dados e validar pipelines mais rápido.
- Um **Analista de Dados** pode usar GenAI pra criar o scaffold de um pipeline simples no dbt (tarefa de Analytics Engineer) sem ser expert na ferramenta.
- Um **Cientista de Dados** pode usar GenAI pra montar um Power BI (tarefa de Analista de BI) e já deixar algo pronto para o colega continuar.

**O "Especialista-Generalista" (perfil em T)**

A ideia central: minha base técnica continua sendo o maior diferencial — o "traço vertical" do T, aprofundado numa área específica. A GenAI adiciona o "traço horizontal": uma camada de conhecimento raso em várias áreas diferentes, permitindo atuar de forma generalista com mais eficiência, entender melhor o trabalho do colega e facilitar a colaboração em equipe.

| Papel | Foco | Stack típica |
|---|---|---|
| Engenheiro de Dados | Construir e manter a arquitetura de dados | Python, PySpark, SQL, Cloud, Airflow, Docker |
| Cientista de Dados | Extrair insights preditivos e prescritivos | Python, Estatística, ML, MLOps, Dataviz |
| Analista de Dados | Visualizações e métricas para o negócio | BI, SQL, Excel, UX |
| Analytics Engineer | Limpar e transformar dados brutos | dbt, SQL, BI |
| AI Engineer | Desenvolver sistemas com IA embarcada | Python, LLM, Banco vetorial |

## Oportunidades e desafios

**A grande oportunidade: dados não estruturados**

Antes, analisar texto em massa era caro e lento — dava pra fazer no máximo uma busca por palavras-chave. Com GenAI, dá pra fazer isso com um prompt simples, num trabalho de horas em vez de meses:

```
Análise de sentimento em larga escala:
"Classificar 100.000 reviews de produtos em 'Positivo',
'Negativo' ou 'Neutro' com um simples prompt."

Extração de entidades (NER):
"A partir de uma análise de sentimento, identificar também
qual é o principal problema relatado em cada review."
```

**Os desafios que preciso ter em mente**

- **Alucinação** → a IA pode "inventar" respostas, funções ou fatos. Ela é otimizada pra ser coerente, não pra ser factual — mesmo com acesso a busca na web, os termos de uso dos provedores não garantem respostas verdadeiras. Tudo precisa ser validado.
- **Qualidade dos dados** → "garbage in, garbage out": se a entrada (PDFs escaneados, áudio com ruído) for de baixa qualidade, o insight gerado também será.
- **Segurança e privacidade** → não incluir dados sensíveis em prompts (e-mails de clientes, por exemplo). A garantia de não uso pra treinamento em ferramentas enterprise é **contratual, não técnica** — por padrão, assumir que os prompts podem ser lidos ou usados para treinamento.
- **Custo** → uso não supervisionado e não otimizado pode sair caro rápido, mesmo pra gigantes de tecnologia. Exemplo citado em aula: em 2026 a Uber gastou, em um único mês, o orçamento de tokens planejado pro ano inteiro.

**Velocidade de mudança**

O que antes era medido em anos hoje é medido em meses (ou semanas) — o modelo state-of-the-art de hoje pode ficar obsoleto em poucos meses. Por isso a adaptabilidade e o aprendizado contínuo viraram habilidade central, não só um "extra" — não vale a pena ficar preso a um único provedor/modelo favorito. Formas de acompanhar: newsletters (Medium, Towards Data Science), LinkedIn, participar dos DataGrupos de AI da Indicium, e trocar experiência com os colegas.

## Ética e responsabilidade

**Quem está ensinando quem?**

Ponto que me deixou pensando: um estudo de 2024 mostrou que um em cada sete artigos científicos de Biomedicina já apresentava indícios de uso de IA. O arXiv (maior indexador de artigos científicos do mundo) já pune isso: quem for pego usando referências criadas por IA num artigo pode ser **banido da plataforma por 6 meses**.

Isso levanta uma questão real — se os modelos são treinados com dados, e esses dados estão cada vez mais influenciados por conteúdo gerado por GenAI, existe um risco de "degradação" (os modelos aprendendo em cima de conteúdo que a própria IA inventou, sem compromisso com a realidade), como serão treinados os modelos futuros nesse ciclo?

**Boas práticas que preciso seguir**

- **Ser transparente** ao usar GenAI: citar fontes e reconhecer quando o conteúdo foi produzido com apoio de IA (não é nenhum demérito).
- **Revisar e validar tudo**: a IA pode alucinar código, fatos ou números — executar o código, validar os insights, checar os fatos. Um erro não validado pode se propagar (revisão de código, cliente, produção) e virar prejuízo real.
- **Não divulgar informações confidenciais** em prompts ou ferramentas, a menos que seja uma ferramenta privada e segura da empresa (contrato Enterprise). Por padrão, assumir que os prompts podem ser lidos ou usados para treinamento.
- **Não deixar a IA substituir o pensamento crítico**: ela automatiza, facilita, apoia — não decide por mim. A decisão de arquitetura, de abordagem, continua sendo minha.

## Ferramentas e tecnologias de GenAI

**Modelos fundacionais (principais LLMs)**

- Gemini (Google)
- ChatGPT / GPT (OpenAI)
- Claude (Anthropic)
- Llama (Meta, open source)
- Gemma (Google, open source)
- DeepSeek, Kimi (entre outros modelos fundacionais que foram surgindo)

**Ferramentas de qualidade de código** — integradas na IDE (VS Code, Jupyter) pra autocompletar e gerar código com contexto do repositório:

- Claude Code
- Cursor IDE

**Plataformas com IA "embarcada"** no stack de dados que já uso:

- Ask Gemini (Google Slides, Gmail, Drive — até o YouTube já tem IA integrada)
- Databricks AI (ex: "AI Functions")
- Power BI / Microsoft Fabric Copilot

**Tools que vão além de gerar texto**

- Deep Research → busca profunda na web, referências e dados em tempo real
- Aprendizado guiado (ex: NotebookLM integrado ao Gemini, focado em estudo)
- Criação de mídias (imagem e vídeo — ex: Nano Banana, Veo)
- Integração com plataformas de design (Canvas)
- Agentes que usam ferramentas de forma autônoma (ex: checar e-mails periodicamente e separar spam)

## Engenharia de Prompts

Não é "mágica", é a habilidade de dar instruções claras, contextuais e específicas pra IA. A qualidade da resposta é diretamente proporcional à qualidade do prompt ("garbage in, garbage out" também vale aqui).

**Os 4 pilares de um bom prompt (para dados):**

1. **Persona** → "Aja como um Engenheiro de Dados Sênior..."
2. **Contexto** → "Estou usando PostgreSQL. Minha tabela vendas tem as colunas [id, data, valor]..."
3. **Tarefa** → "Escreva uma query SQL que..."
4. **Formato** → "Retorne o resultado em formato JSON..." ou "Explique o código linha por linha."

**Prompt simples vs prompt com boas práticas**

Prompt simples:
```
Forneça uma query sql sobre as vendas na tabela vendas.
```
Resultado provável: `SELECT * FROM vendas;` — genérico, sem contexto.

Prompt com boas práticas:
```
Atue como um Analista de BI com vasta experiência em SQL.

Contexto: Tenho duas tabelas: pedidos(id_pedido, id_cliente,
data_pedido, valor) e clientes(id_cliente, nome, estado).

Tarefa: Escreva uma query SQL (para PostgreSQL) que mostre o
valor total de vendas agrupado por estado do cliente X, apenas
para o mês de Outubro de 2024.

Formato: Ordene do maior valor para o menor.
```
Resultado provável: query correta, formatada, usando JOIN, WHERE, GROUP BY e ORDER BY.

## Gems (Gemini)

Um Gem nada mais é do que um "super prompt": dedico um tempo escrevendo objetivo, contexto e preferências de saída pra ter uma instrução reutilizável, sem precisar reescrever tudo toda vez. É a mesma lógica por trás de agentes especialistas em produção. Outras ferramentas têm o equivalente com outro nome — por exemplo, o Claude chama isso de **Skills**.

Passo a passo pra criar um (usado em aula pro Gem "Lighthouse Tutor Assistant"):

1. Acessar [gemini.google.com/gems/view](https://gemini.google.com/gems/view) com o e-mail cadastrado.
2. No menu Gem Manager, clicar em "Criar um novo Gem" (ou pela sidebar, "Novo Gem").
3. No campo "Instruções", adicionar o prompt desejado.

## Praticando: criando o Gem "Lighthouse Tutor Assistant"

Comecei a montar esse Gem no Gemini como assistente de estudos (teaching assistant) pro Programa Lighthouse, focado em conceitos e boas práticas de Data Engineering.

Prompt usado no campo de instruções: [`lighthouse-ta-prompt.txt`](./lighthouse-ta-prompt.txt)

Passo a passo que segui (igual anotei antes, na seção de Gems):
1. Acessei o Gem Manager e cliquei em "Novo Gem"
2. Dei o nome **"Lighthouse Tutor Assistant"** pro Gem
3. Coloquei a descrição "Gem criada durante a aula de introdução a GenAI"
4. Colei o prompt no campo de instruções

Testei com dois prompts pra ver a diferença de comportamento:
- Uma pergunta aberta ("minha DAG do Airflow está com problema e não está funcionando, o que posso fazer?") → o Gem não deu a resposta pronta, foi por onde investigar (interface web, scheduler, boas práticas de validação) e perguntou qual o comportamento exato observado.
- Um pedido direto de solução ("estou com um problema no runner, me dê a solução") → mesmo sem contexto suficiente, o Gem tentou guiar o raciocínio de debug em vez de só entregar a resposta pronta — reforçando o papel de tutor, não de "resolvedor automático".

## Pra lembrar depois

- GenAI é um subconjunto de Deep Learning, focado em **gerar** conteúdo novo, não só prever/classificar
- Transformers (2017) são a base técnica por trás dos LLMs modernos como GPT e Claude
- GenAI não substitui o profissional, potencializa — o diferencial continua sendo a base técnica de cada especialista (perfil em T)
- A GenAI conecta áreas: dá pra "emprestar" competências de outras funções de dados com apoio da IA
- Alucinação, qualidade dos dados, privacidade e **custo** são os riscos práticos mais recorrentes (ex: caso da Uber estourando o orçamento anual de tokens em um mês)
- Sempre validar o que a IA gera — rodar o código, checar os fatos, nunca aceitar de olhos fechados
- Um bom prompt tem 4 pilares: Persona, Contexto, Tarefa e Formato
- Gems (e equivalentes como Skills, no Claude) são úteis pra reaproveitar instruções recorrentes
- Próxima aula: fundamentos de bancos de dados e cloud (criação/manipulação de tabelas em banco relacional e consultas SQL de negócio)

## Créditos

Conteúdo baseado na aula ministrada por **Pedro Muracchini**, Team Lead / AI Engineer na Indicium.
- 🔗 [LinkedIn](https://www.linkedin.com/in/pedro-muracchini/)
