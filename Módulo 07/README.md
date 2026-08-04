<div class="hero-image">
    <div class="frame">
        <img src="assets/brunohenrique.png" alt="Fundamentos da Computação em Nuvem">
    </div>
</div>

# Módulo 7 - Fundamentos de Cloud e Bancos de Dado

Este módulo teve duas aulas com instrutores diferentes. Anotações de cada uma abaixo:
- **Aula 1** — Fundamentos da Computação em Nuvem (Bruno Schaden)
- **Aula 2** — Fundamentos de Bancos de Dados e Modelagem (Henrique Lucas)

---

# Módulo 7 - Aula 1 - Fundamentos da Computação em Nuvem
Anotações da aula sobre os fundamentos de Cloud Computing: definição técnica, características essenciais, modelos de serviço e de implantação, e como isso se aplica no dia a dia de quem trabalha com dados. Instrutor: Bruno Schaden, Team Lead Analytics Engineer na Indicium (formado em Economia, mais de 3 anos de Indicium, já passou por projetos nas verticais financeira, saúde e transporte/logística).

## O que já era esperado como pré-requisito

A aula não citou pré-requisitos técnicos formais — o Bruno partiu do zero, explicando cloud como conceito antes de entrar em qualquer provedor específico (AWS, Azure, GCP). Ajuda ter uma noção geral de infraestrutura (servidor, rede, armazenamento), mas não é obrigatório.

O foco da aula foi entender **o que é** cloud computing de fato — não ficar só na piada de "é o computador de outra pessoa" — e como ela se estrutura em características, modelos de serviço e modelos de implantação.

## O que aprendi

**Cloud não é só "o computador de outra pessoa"**

Essa piada (que o Bruno trouxe cheia de memes do LinkedIn) até ajuda a entender a ideia geral, mas é simplista demais. Ter um servidor remoto ou um data center terceirizado **não é**, necessariamente, cloud. Pra ser cloud de verdade, o serviço precisa bater as características essenciais definidas tecnicamente (ver abaixo).

**A definição técnica (NIST)**

A definição usada como base na aula vem do NIST (National Institute of Standards and Technology, dos EUA), no documento SP 800-145:

> A computação em nuvem é um modelo que permite um acesso amplo, conveniente e sob demanda via rede, a um conjunto compartilhado de recursos de computação configuráveis (redes, servidores, armazenamento, aplicativos e serviços), que podem ser rapidamente provisionados e liberados com mínimo esforço de gerenciamento ou interação do provedor de serviço.

Essa definição já entrega a estrutura toda da aula: **5 características essenciais**, **3 modelos de serviço** e **4 modelos de implantação**.

**Cloud em uma frase prática**

Cloud é computação como utilidade — igual energia elétrica. Você não compra a usina, paga pela energia que consome. Em cloud, você paga por compute, storage e rede conforme usa, e não pelo hardware em si.

## As 5 características essenciais

| Característica | O que significa na prática |
|---|---|
| **Autosserviço sob demanda** | Eu mesmo provisiono o que preciso (mais RAM, mais storage) sem precisar que alguém do provedor faça isso manualmente pra mim |
| **Amplo acesso via rede** | Acesso de qualquer lugar com internet, independente de dispositivo ou plataforma |
| **Agrupamento de recursos** | O provedor concentra os recursos (pool) e ajusta o provisionamento conforme a demanda |
| **Consumo medido de serviço** | Cobrança conforme o uso real — se aloco 10GB mas uso 4GB, pago pelos 4GB |
| **Elasticidade rápida** | O recurso já está disponível, é só alocar — RAM/storage aumentam ou diminuem em segundos, sem trocar hardware fisicamente |

## Os 3 modelos de serviço

| Modelo | Analogia do Bruno | O que o provedor cuida | O que eu cuido |
|---|---|---|---|
| **IaaS** (Infrastructure as a Service) | Alugar um terreno vazio — faço o que eu quiser nele | Rede, servidor físico, virtualização | SO, containers, runtime, dados, aplicação |
| **PaaS** (Platform as a Service) | Alugar uma cozinha industrial pronta — só chego e cozinho | Tudo até o runtime | Dados e aplicação |
| **SaaS** (Software as a Service) | Pedir comida pelo app — só uso | Praticamente tudo | Só uso e configuro |

Exemplos citados: **SaaS** → Google Apps, Facebook, YouTube, Salesforce (curiosidade: o Salesforce foi o grande expoente do modelo SaaS desde 1988, antes da Amazon vir e dominar o mercado com a AWS). **PaaS** → Microsoft Azure, Google App Engine, Amazon SimpleDB/S3. **IaaS** → Amazon EC2, GoGrid, Flexiscale.

Comparando com **On-Premise** (minha máquina local, onde eu cuido de tudo — aplicação, dados, runtime, containers, SO, virtualização, servidor físico e rede), dá pra ver visualmente o quanto cada modelo tira responsabilidade de gerenciamento de mim e passa pro provedor.

## Os 4 modelos de implantação

- **Pública** → Azure, AWS, GCP. Foco em velocidade, escala e catálogo de serviços. O provedor cuida de tudo, eu pago um pouco mais pelo serviço, mas não preciso me preocupar com a infraestrutura.
- **Privada** → infraestrutura minha, controle extremo, geralmente um sistema mais legado dentro do meu próprio escritório/data center. Faz sentido, por exemplo, quando há restrição legal de onde os dados podem ficar armazenados.
- **Híbrida** → mistura de privada + pública. Uso a privada pra dados sensíveis (baixa latência, compliance) e a pública pra dados transacionais gerais que precisam de mais poder de processamento. Ferramentas citadas pra isso: Azure Stack, AWS Outposts e Anthos (do Google).
- **Multicloud** → uso serviços específicos de mais de um provedor público ao mesmo tempo (ex: dados no GCP + data lake na AWS), pra aproveitar o que cada um tem de melhor. Aumenta a complexidade, mas pode compensar dependendo do modelo de negócio.

## Vantagens operacionais da cloud

O Bruno listou 5 pilares de vantagem operacional: **Provisionamento, Conectividade, Controle de Acesso, Monitoramento e Orquestração**.

- **Provisionamento** → na infra tradicional, comprar e configurar um servidor levava dias/semanas/meses. Na cloud, isso acontece em minutos, só clicando.
- **Conectividade** → não basta criar uma máquina virtual, é preciso definir quem pode se conectar, por qual caminho e com quais restrições (ex: VPN com SSO via conta Google/Microsoft) — isso é uma barreira de segurança forte contra acesso não autorizado.
- **Controle de acesso** → determina quem (ou o quê, no caso de uma conta de serviço) pode acessar um recurso e quais operações pode realizar nele. O conceito central aqui é o de **acesso mínimo** (least privilege): dar só a permissão necessária pra pessoa/serviço fazer o trabalho dela, nada além disso. O Bruno deu o próprio exemplo: usou uma conta admin num projeto pessoal e acabou apagando o banco de dados inteiro sem querer — se tivesse usado uma conta com acesso restrito (só leitura/escrita nas tabelas certas, sem permissão de `DROP`), isso não teria acontecido. Na nuvem, esse controle é administrado por sistemas de **IAM** (Identity and Access Management).
- **Monitoramento** → acompanhamento contínuo de estado, desempenho, segurança e consumo dos recursos. Tem ligação direta com custo: se eu aumento a capacidade de processamento (ex: pra acelerar uma transformação de dados) e esqueço aquilo ligado, a fatura no fim do mês vem bem mais alta do que eu esperava. Monitorar é o que evita esse tipo de susto.
- **Orquestração** → coordenação automática de vários recursos, serviços e tarefas funcionando como um processo único (a analogia é literal: uma orquestra). Diferente de uma automação isolada (que executa uma tarefa só), a orquestração organiza várias automações, respeita as dependências entre elas (o que precisa terminar antes de outra coisa começar), dispara a próxima tarefa automaticamente quando a anterior termina, e tem uma boa resposta a falhas: se algo quebra no meio do processo, o resto não é executado, e dá pra saber exatamente onde e por que falhou.

## Provedores Cloud

O Bruno frisou que 95-96% do tempo a gente lida só com **clouds públicas** (AWS, Azure, GCP), então o foco foi nelas. Pra acessar os recursos de um provedor, quatro conceitos aparecem sempre: Conta, Regiões, Zonas e VPC.

**Conta** → é o ambiente administrativo onde organizo tudo que tenho na cloud: usuários, grupos, assinaturas, departamentos, ambientes separados. É um acesso extremamente restrito, mas que enxerga e controla tudo — a analogia do Bruno foi "o presidente/CEO do teu serviço".

**Regiões** → localização geográfica onde o serviço fica hospedado. A escolha da região importa por três motivos:
- **Preço** → regiões com data centers maiores custam menos. Exemplo citado: armazenar dados em São Paulo custava, na última verificação, quase o dobro do preço de armazenar no US East 1 (Virgínia).
- **Latência** → quanto mais longe fisicamente a região, maior o tempo de resposta (o "lag"). Se a aplicação não depende de tempo real, isso pode não importar; se depende, é um fator decisivo na escolha entre, por exemplo, São Paulo e Virgínia.
- **Segurança/regulação** → é preciso escolher bem onde os dados ficam. Riscos físicos existem (um desastre natural, uma manutenção que trava a região inteira — como o apagão da AWS US East 1 que derrubou boa parte da internet mundial) e, no caso do Brasil, há legislação que restringe o armazenamento de dados pessoais fora do país — o que pode tornar uma cloud privada local mais viável que uma pública no exterior, dependendo do caso.

Uma região não é "um prédio só": é uma estrutura geográfica formada por vários data centers diferentes que se comunicam entre si. Os provedores usam códigos padronizados pra identificar cada uma (ex: `sa-east-1`, `us-east-1`, `eu-west-1`), o que já entrega de cara onde ela fica.

**Zonas** (Availability Zones) → subdivisões independentes dentro de uma região. O objetivo principal é **isolamento de falhas**: se a zona A falha ou entra em manutenção, a zona B continua ativa atendendo os usuários, então uma aplicação distribuída entre múltiplas zonas absorve a falha local sem ficar fora do ar. Importante: as zonas **não** são isoladas por completo — elas são interligadas por redes de alta velocidade e baixa latência, o que permite configurar uma VPC conversando entre mais de uma zona.

**VPC** (Virtual Private Cloud) → minha rede privada virtual dentro da cloud, isolada dos outros clientes do provedor. Na prática, funciona como uma espécie de VPN pensada pra cloud.

## Ranking de provedores cloud (dados estimados até Q4/2025)

| Provedor | Regiões | Zonas | Market Share |
|---|---|---|---|
| Amazon Web Services (AWS) | 39 | 123 | 28% |
| Microsoft Azure | 70+ | 126+ | 21% |
| Google Cloud Platform (GCP) | 42 | 127 | 14% |
| Alibaba Cloud | 29 | 94 | 4% |
| Oracle Cloud | 45 | 55 | 3% |
| IBM Cloud | 13 | 39 | 2% |
| Tencent Cloud | 22 | 64 | 2% |
| OVHcloud | 19 | 23 | <1% |
| DigitalOcean | 9 | 13 | <1% |
| Linode | 31 | 31 | <1% |

Curiosidade citada em aula: a Amazon apostou nesse modelo desde ~2004/2005 ("constroem o marketplace de vocês, hospedam na gente, a gente mantém"), o que ajudou a consolidar sua liderança de mercado até hoje.

## Pra lembrar depois

- Cloud só é cloud de verdade se bater as 5 características essenciais — ter servidor remoto ou data center terceirizado não basta
- A definição do NIST é a referência técnica: 5 características, 3 modelos de serviço, 4 modelos de implantação
- IaaS = terreno vazio, PaaS = cozinha industrial pronta, SaaS = pedir comida no app — quanto mais alto na pilha, menos eu gerencio
- Os 4 modelos de implantação (pública, privada, híbrida, multicloud) resolvem necessidades diferentes de controle, custo e compliance
- Provisionamento, conectividade, controle de acesso (IAM + acesso mínimo), monitoramento e orquestração são as 5 vantagens operacionais da cloud frente ao on-premise
- Escolher região é um trade-off entre preço, latência e segurança/regulação — não é só "pegar a mais barata"
- Zonas existem pra isolar falhas: uma zona cair não deve derrubar a aplicação inteira, já que elas ficam interligadas por rede de alta velocidade
- AWS lidera em market share (~28%), mas Azure tem mais regiões — cada provedor tem pontos fortes diferentes

---

# Módulo 7 - Aula 2 - Fundamentos de Bancos de Dados e Modelagem
Anotações da aula sobre fundamentos e conceitos de modelagem de bancos de dados: histórico, tipos de dados, SGBDs, banco de dados relacional, data warehouses e modelos de entidade-relacionamento/normalização. Instrutor: Henrique Lucas, AI Engineer na Indicium (bacharel em Engenharia de Software pela UTFPR, ~1 ano de Indicium, já participou de projetos com IA generativa e deu palestras sobre o tema).

## O que já era esperado como pré-requisito

A aula assume que eu já vi as aulas anteriores de análise de algoritmos, SQL e computação em nuvem. A partir daqui a ideia é aprofundar os conceitos que rodeiam bancos de dados: o que são, quais características os definem, o que são SGBDs, os principais tipos e plataformas existentes hoje.

## O que aprendi

**O que é um banco de dados**

Definição usada em aula, da Oracle:

> Um banco de dados é uma coleção organizada de informações — ou dados — estruturadas, normalmente armazenadas eletronicamente em um sistema de computador.

O "normalmente armazenadas eletronicamente" importa: a humanidade lida com dados há muito mais tempo do que existem computadores — só que a forma de armazenar e gerenciar mudou bastante.

**Um pouco de história**

Linha do tempo resumida do que veio antes do banco de dados como eu conheço hoje:

| Período | O que aconteceu |
|---|---|
| Tempos antigos | Egípcios já controlavam estoque, entrada e saída de materiais na construção das pirâmides. Governos e indústrias (Guerra Fria, expansão industrial) ampliaram a necessidade de armazenar e controlar grandes volumes de dados |
| 1950s | Criação das fitas magnéticas — armazenamento **sequencial**: pra acessar um dado no meio, era preciso "rodar" tudo desde o início |
| 1960s | Armazenamento em disco magnético — permitiu acesso **direto** à memória, sem precisar navegar sequencialmente. Nessa época os modelos de banco ainda eram hierárquicos ou de rede, parecidos com um sistema de pastas (pasta pai com pastas filho); pra fazer uma consulta, era preciso conhecer toda a estrutura |
| 1970s | Edgar F. Codd propõe o **modelo relacional**: em vez de organizar pela estrutura lógica do banco, organizar pela visão dos dados em si. Donald Chamberlin e Raymond Boyce lançam a primeira versão da linguagem de consulta, batizada SEQUEL (depois renomeada SQL por questão de direito autoral) |
| 1980s | Adoção em massa do modelo relacional e do SQL. Também surgem os primeiros conceitos de **Data Warehouse** (a ideia já existia, a escala em massa veio depois) |
| 1990s | MySQL/PostgreSQL, popularização da WWW, surgem OLAP (processamento analítico) e ORM (mapeamento objeto-relacional) |
| 2006-2010 | Data Lakes, NoSQL, e a computação em nuvem ganha força (ex: lançamento do S3 da AWS) |

**Quais são os tipos de dados**

| Tipo | Características | Exemplo |
|---|---|---|
| **Estruturados** | Formato rígido/fixo, tabular (linhas e colunas), com chaves relacionais. Fáceis de endereçar e mapear em campos pré-definidos, muito eficazes para análise | Dados relacionais num banco SQL |
| **Semiestruturados** | Têm alguma organização (propriedades), mas não moram num banco relacional. Fáceis de expandir e representar conceitos mais complexos e dinâmicos | JSON, XML |
| **Não estruturados** | Sem organização pré-definida nem modelo fixo. Existem majoritariamente na internet hoje e crescem cada vez mais | PDF, Word, vídeo, imagem, texto livre |

Importante: um tipo pode ser convertido pro outro (forçar estrutura num dado não estruturado, ou representar um dado estruturado de forma não estruturada) — a linha entre eles não é rígida.

Dentro do NoSQL (que lida bem com dados semi/não estruturados), existem quatro modelos principais: **key-value** (chave e valor, tipo cache), **column-family**, **graph** (nós conectados por relações, muito usado hoje pra mapear contexto para modelos de linguagem) e **document** (documentos, geralmente mapeáveis pra JSON).

**O que são SGBDs (Sistemas de Gerenciamento de Banco de Dados)**

Um SGBD é o conjunto de programas que permite ao usuário criar, editar, atualizar, armazenar e recuperar dados em tabelas, sem precisar saber os detalhes técnicos de cada camada por trás.

Ele se organiza em **três camadas**:
- **Camada de consulta** → onde eu escrevo a query/transação (a mais abstrata, depende totalmente das outras duas)
- **Camada de processamento** → o motor que otimiza e executa a consulta
- **Camada de armazenamento** → onde os dados (e os metadados sobre eles) realmente ficam gravados fisicamente

Numa visão mais ampla, um SGBD também é pensado em **três níveis**:
1. **Nível interno/físico** → como os arquivos e índices são de fato gravados no disco
2. **Nível conceitual/lógico** → a estrutura global do banco: tabelas, regras, relacionamentos
3. **Nível externo/visões** → recortes personalizados da informação pra diferentes usuários/aplicações

Esses níveis existem pra garantir **abstração** (cada camada esconde a complexidade da anterior) e **independência de dados**: mudar o nível físico não deveria afetar o lógico, e mudar o lógico não deveria quebrar as visões (é possível adicionar colunas numa tabela sem quebrar queries que já existiam, por exemplo).

**Componentes de um SGBD**

| Componente | O que faz |
|---|---|
| **Motor de banco de dados** | Gerencia o armazenamento, a recuperação e a manipulação dos dados (o CRUD: create, read, update, delete) |
| **Processador de consultas** | Interpreta a query SQL e define o que exatamente deve ser retornado |
| **Otimizador de consultas** | Avalia diferentes estratégias de execução e escolhe a mais barata/eficiente (toda query tem um custo de tempo e recursos) |
| **Gestor de transações** | Garante as propriedades ACID em cada transação, do início ao fim |
| **Gestor de armazenamento** | Cuida da alocação e do acesso físico aos dados em disco |

**Propriedades ACID**

Sigla pra atomicidade, consistência, isolamento e durabilidade — as características que garantem que uma transação de banco de dados seja confiável mesmo com milhares/milhões de acessos concorrentes:

- **Atomicidade** → a transação ocorre por inteiro ou não ocorre — não existe meio-termo. Se der `commit`, foi validada e vale; se algo falhar, dá `rollback` e nada é alterado.
- **Consistência** → antes e depois da transação, as regras definidas no esquema (tipos de dado, se aceita nulo, gatilhos, deleção em cascata etc.) continuam sendo respeitadas. Exemplo dado: ao deletar uma conversa de um chat, o ideal é que as mensagens dela sejam deletadas em cascata junto, senão ficam mensagens "órfãs".
- **Isolamento** → transações concorrentes não podem se atropelar. Exemplo clássico do caixa eletrônico: eu e um amigo temos R$ 1.000 numa conta conjunta; se os dois sacamos ao mesmo tempo (R$ 200 e R$ 300) sem isolamento, o banco pode "esquecer" a primeira subtração e deixar o saldo em R$ 700 em vez de R$ 500 — como se R$ 200 tivessem evaporado.
- **Durabilidade** → depois que a transação é confirmada, o dado tem que continuar lá, resistindo a falhas do sistema. Por isso a importância de redundância/backup: se o dado estiver só num HD e ele quebrar, os dados se perdem.

**Principais SGBDs do mercado**

- **Relacionais (RDBMS)**: MySQL, PostgreSQL, Oracle Database, SQL Server, IBM DB2 — todos trabalham com a estrutura tabular (linhas e colunas) e majoritariamente SQL, mas cada um tem suas particularidades de sintaxe.
- **NoSQL**: MongoDB (documentos), Cassandra (estabilidade/escalabilidade), Redis (cache em memória, chave-valor — rápido, mas mais caro por usar RAM), CouchDB.

**Formas de interagir com um banco de dados**

- **Terminal de comandos** (CMD/PowerShell/shell) → a forma mais primordial, ainda muito usada quando só existe acesso via shell (ex: numa instância na nuvem sem interface gráfica). Não tem correção de sintaxe nem autocomplete, então exige mais conhecimento técnico.
- **Aplicativos nativos da web** → como o console do próprio provedor, Snowflake, Databricks. Sempre têm um editor de query, área de resultados tabulares e navegação entre bancos/schemas.
- **Aplicativos independentes** → como o DBeaver, que é open source, gratuito, roda local e se conecta a diferentes tipos de banco (relacional ou não).

## Banco de dados relacional

Componentes principais: **tabelas, colunas, linhas, campos, chave primária, chave estrangeira, índices, restrições de integridade e consultas**.

- **Chave primária (PK)** → campo único que identifica uma linha (registro) da tabela. Não precisa ser o campo "mais óbvio" (o CPF pode até ser único, mas a chave primária pode ser outro identificador, como um ID sequencial ou aleatório).
- **Chave estrangeira (FK)** → é a chave primária de uma tabela sendo referenciada em outra, pra representar o relacionamento entre elas (ex: a tabela de produtos referencia o CPF do cliente que comprou). Isso garante consistência (não dá pra inserir um produto "solto", sem cliente relacionado) e melhora a performance das consultas.
- **Campos** → cada coluna define um tipo de dado e suas restrições (ex: `char(50)` limita a 50 caracteres; `int` só aceita inteiro; `float` aceita casas decimais).
- **Índices** → aceleram a busca ao agrupar fisicamente os dados por um critério (ex: por data), parecido com o sumário de um livro. Sem índice, uma busca é um **full-scan** — o sistema varre linha por linha, com custo O(N). Com índice bem definido, a busca vira O(1) ou O(logN): o sistema já sabe em qual "página" de dados procurar, sem precisar ir um por um.

**Banco relacional x planilha (Excel)**

| | Banco de dados relacional | Excel/planilha |
|---|---|---|
| Foco | Volume, velocidade de acesso, gerenciamento centralizado | Flexibilidade e reprodutibilidade para análises simples |
| Consistência | O esquema barra a inserção de um tipo errado (ex: texto onde deveria ser float) — a transação falha | É fácil "furar" a regra de um tipo de coluna sem perceber |
| Volume | Suporta quantidades muito grandes de dados sem perder performance | Tem limite de linhas/arquivo e fica lento com bases grandes |

Um fluxo comum no dia a dia: consultar o banco relacional, baixar o resultado em CSV e abrir no Excel pra manipular manualmente — as duas ferramentas se complementam, não competem.

**As sublinguagens do SQL**

| Sigla | Nome | Serve para | Comandos |
|---|---|---|---|
| **DDL** | Linguagem de Definição de Dados | Criar, alterar e deletar objetos (tabelas, esquemas) | `CREATE`, `ALTER`, `DROP` |
| **DML** | Linguagem de Manipulação de Dados | Inserir, atualizar e deletar registros | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** | Linguagem de Consulta de Dados | Buscar dados sem alterar nada — a menos arriscada das cinco | `SELECT` |
| **DCL** | Linguagem de Controle de Dados | Autorização e acesso — quem pode ver/alterar o quê | `GRANT`, `REVOKE` |
| **DTL** | Linguagem de Controle de Transações | Controlar o início, confirmação e desfazimento de uma transação | `BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK` |

O DTL é especialmente útil em operações sensíveis (ex: um hotfix em produção que vai alterar muitos registros): dá pra rodar a transação, conferir o resultado, e só then decidir entre `COMMIT` ou `ROLLBACK`.

## Data Warehouses

**OLTP vs OLAP**

| Característica | Bancos Transacionais (OLTP) | Data Warehouse (OLAP) |
|---|---|---|
| Propósito | Operações do dia a dia (vendas, cadastros) | Análise estratégica e relatórios |
| Foco | Velocidade de escrita e integridade (ACID) | Velocidade de leitura e agregação |
| Estrutura | Altamente normalizada (muitas tabelas) | Desnormalizada (Star Schema/Snowflake) |
| Armazenamento | Geralmente em linhas | Geralmente colunar |

**Armazenamento linear x colunar**

No armazenamento **linear** (tradicional), os dados são gravados em disco sequencialmente por registro (linha inteira por linha inteira) — bom pra transações do dia a dia, mas ineficiente se eu quiser só uma coluna específica de milhões de linhas (preciso varrer tudo).

No armazenamento **colunar**, cada coluna é agrupada fisicamente separada das outras — então buscar "todos os nomes de clientes", por exemplo, vira uma leitura direta daquele bloco, sem precisar navegar linha por linha. É por isso que data warehouses e soluções analíticas tendem a usar esse modelo.

**Vantagens de um Data Warehouse**
- **Estrutura otimizada** → modelos dimensionais (star schema) pensados pra consultas analíticas complexas
- **Desempenho aprimorado** → projetado pra grandes volumes em consultas analíticas
- **Histórico de dados** → mantém o passado pra comparações e tendências ao longo do tempo
- **Integração de dados** → agrega dados de várias fontes numa visão unificada
- **Facilidade de acesso** → estrutura organizada, mais simples de consultar
- **Modelagem flexível** → se adapta às necessidades específicas de análise de cada organização

## Modelos de Entidade-Relacionamento (ER) e Normalização

**Modelo ER**

Serve pra visualizar e diagramar uma solução de dados pensando em **entidades** (o que vira tabela), seus **atributos** (o que vira coluna) e os **relacionamentos** entre elas — sem entrar ainda no detalhe técnico de como isso vai ser armazenado fisicamente.

A notação usada pra representar o relacionamento entre entidades é a "pé de galinha". Os quatro tipos principais de relacionamento:

| Notação | Tipo | Exemplo |
|---|---|---|
| ── | Um para um | Cada cliente pertence a exatamente uma cidade, e vice-versa (caso específico, raramente reflete a realidade) |
| ─➤ | Muitos para um | Uma cidade pode ter diversos clientes |
| ➤──➤ | Muitos para muitos | Diversos países podem se relacionar com diversas cidades (dependendo do modelo) |
| ➤○─ | Zero ou muitos para um | Pode existir uma cidade sem nenhum cliente associado ainda |

**Normalização**

É o grau de redundância/repetição que eu decido manter no modelo — uma escolha de design, não uma regra fixa:

- **Mais normalizado** → maior consistência, performance de escrita e integridade. Bom para bancos transacionais (OLTP).
- **Menos normalizado** (mais redundante) → mais fácil de entender e mais rápido pra consultas analíticas, porque evita muitos `JOIN`s. Bom para data warehouses (OLAP).

**Star Schema vs Snowflake Schema**

Os dois são formas de organizar um data warehouse em volta de uma **tabela fato** (o dado que eu quero analisar, ex: vendas) cercada de **tabelas dimensão** (os diferentes ângulos pra agregar aquele dado: data, produto, local, representante etc.):

- **Star Schema** → cada dimensão é uma tabela só, ligada direto à tabela fato — parece uma estrela. Mais simples, mais redundante.
- **Snowflake Schema** → quando uma dimensão tem categorias e subcategorias (ex: cliente com dados demográficos e dados de pagamento em tabelas separadas), ela se desdobra em mais tabelas — parece um floco de neve. Mais normalizado, menos redundância, mas mais complexo de navegar/consultar.

A escolha entre os dois é uma decisão de design que deveria ser pensada já no planejamento da modelagem, não como um ajuste posterior.

## Pra lembrar depois

- Um banco de dados é uma coleção organizada de dados, normalmente armazenada eletronicamente — mas a ideia de organizar/controlar dados é muito anterior aos computadores
- O modelo relacional (Codd, anos 70) trocou "pensar na estrutura do banco" por "pensar na visão dos dados" — e é a base do SQL até hoje
- Dados existem em três naturezas: estruturados (tabular), semiestruturados (JSON/XML) e não estruturados (PDF, imagem, vídeo) — e dá pra converter entre eles
- Um SGBD se organiza em camadas (consulta, processamento, armazenamento) e níveis (físico, lógico, externo) justamente pra que uma mudança numa camada não quebre as outras
- ACID (Atomicidade, Consistência, Isolamento, Durabilidade) é o que garante que uma transação seja confiável mesmo com acessos concorrentes
- Chave primária identifica um registro; chave estrangeira representa o relacionamento entre tabelas; índices aceleram a busca (O(N) sem índice vira O(1)/O(logN) com índice)
- OLTP (transacional, normalizado, foco em escrita) e OLAP (analítico, desnormalizado, foco em leitura) resolvem problemas diferentes — por isso data warehouses existem separados dos bancos operacionais
- Armazenamento colunar favorece consultas analíticas; armazenamento em linha favorece transações do dia a dia
- Normalização é um trade-off: mais normalizado = mais consistente e íntegro; menos normalizado = mais rápido de consultar e entender
- Star Schema (simples, uma tabela por dimensão) e Snowflake Schema (dimensões desdobradas em subcategorias) são as duas formas padrão de modelar um data warehouse

## Referências
- Definição de banco de dados: Oracle