<div class="hero-image">
    <div class="frame">
        <img src="../assets/arthurcerqueira.png" alt="Banner do Módulo 8 - Fundamentos de engenharia de dados">
    </div>
</div>

# Módulo 8 - Introdução à Engenharia de Dados

Anotações da aula sobre os fundamentos da engenharia de dados: pipelines, ingestão, ETL vs ELT, orquestração e o papel do engenheiro de dados no dia a dia. Instrutor: [Arthur Cerqueira Farias](https://www.linkedin.com/in/arthur-cerqueira-665626226/), Data Engineer na Indicium (migrou de carreira, veio da área de frontend).

## O que aprendi

**O que é Engenharia de Dados**

De forma simples, a engenharia de dados é responsável por fazer com que os dados saiam de um lugar e cheguem organizados, confiáveis e prontos para uso em outro lugar. Numa empresa, os dados podem estar espalhados de várias formas (aplicativos, CRM, API, bancos de dados, logs de aplicação) e, se ninguém for responsável por isso, o dado até existe, mas nunca vira informação.

Dá pra dividir a área em cinco grandes fundamentos:

- **Coleta** → integra múltiplas fontes (APIs, bancos, arquivos, streams) com qualidade e rastreabilidade.
- **Armazenamento** → define modelagem e camadas (data lake, data warehouse) para dados brutos e tratados, com escalabilidade.
- **Processamento** → cria pipelines para transformar e consolidar dados em lote e em tempo real.
- **Orquestração & Automação** → agenda, monitora e recupera falhas de jobs, garantindo confiabilidade.
- **Governança & Segurança** → catálogo, linhagem, schema, controle de acesso e compliance (inclui anonimização de campos sensíveis).

## O que são pipelines de dados

Pipeline = cano. É a mesma lógica de um sistema hidráulico: o dado entra sujo numa ponta, percorre o "cano" passando por transformações/etapas de processamento conectadas entre si, e sai tratado na outra ponta.

Segundo a AWS, implementar pipelines de dados eficazes é essencial para que empresas tenham insights precisos e em tempo real, já que isso garante que os dados fluam de forma contínua e confiável entre sistemas, evitando silos de informação.

## Ingestão de dados

Coleta + Armazenamento formam a **ingestão de dados**, que é o centro de uma arquitetura de analytics: é aqui que o dado sai da fonte (ex: CRM) e chega num ambiente de destino (data warehouse, data lake, data mart).

Existem dois tipos principais:

| | Batch | Streaming |
|---|---|---|
| Processamento | Em blocos | Contínuo |
| Mecanismo | Agendamento (schedule) | Filas (queues) |
| Volume | Alto volume | Baixo volume |
| Complexidade | "Simples" de executar | Alta complexidade |
| Uso no mercado | Maioria das implementações | Minoria das implementações |
| Desafios | Menores | Escalabilidade, ordenamento, consistência, tolerância |

**Batch em D-1**: a tabela nunca está atualizada com os dados de hoje, só com os de ontem. O pipeline dispara depois que o dia termina (ex: meia-noite e meia) e processa tudo que aconteceu naquele dia. É o tipo mais comum de ingestão, embora streaming venha ganhando importância por lidar com dados mais críticos em tempo real (ex: pagamentos, pedidos, eventos de aplicação).

## ETL vs ELT

Duas siglas, uma troca de ordem entre Extração, Carregamento (Load) e Transformação:

- **ETL** (Extract, Transform, Load) → os dados são extraídos, transformados "on the go" e só depois carregados já prontos no data warehouse. Era o padrão antes de existirem estruturas modernas de transformação.
- **ELT** (Extract, Load, Transform) → os dados são extraídos, carregados brutos no data warehouse/data lake, e só depois transformados conforme a necessidade, diretamente no armazenamento final.

O ELT é mais atrativo hoje porque o dado bruto salvo (ex: camada bronze) pode ser reaproveitado para várias demandas diferentes. Já no ETL, o dado sai transformado para uma necessidade específica e fica "mocado", com pouca versatilidade para outros usos.

**Arquitetura medalhão** (mencionada dentro do fluxo ELT):

- **Bronze** → dado bruto, extraído da fonte sem transformação (ou com transformação mínima).
- **Silver (prata)** → dado já transformado a partir da bronze.
- **Gold (ouro)** → dado final, pronto para dashboards e aplicações.
- **Diamond** (em alguns casos) → dado ainda mais refinado, geralmente específico para uma ação ou fluxo de trabalho pontual.

### Comparação ETL x ELT

| | ETL | ELT |
|---|---|---|
| Paradigma central | "Armazenar e processar dados é caro" | "Flexibilidade, aproximação com áreas de negócio e redução de tempo de desenvolvimento gera resultado" |
| Tempo de carregamento e transformação | Alto (sistemas distintos aumentam o tempo) | Baixo (sistema de carregamento integrado) |
| Tempo de manutenção | Alto (baixa modularidade e linhagem dificultam) | Baixo (alta modularidade e linhagem facilitam) |
| Usabilidade | Baixa (estrutura monolítica) | Alta (divisão flexível entre estruturas) |

## O que é orquestração

Orquestração é uma abordagem sistemática para coordenar e automatizar processos complexos e cadeias de tarefas, permitindo integrar e gerenciar aplicações, automações e sistemas em diferentes ambientes.

Tipos de orquestração:

- **Orquestração de dados** → coleta, processamento, transformação e entrega de dados para sistemas de análise e BI (a principal para o engenheiro de dados).
- **Orquestração de serviços** → coordenação de microsserviços, redes, APIs e serviços de dados.
- **Orquestração de containers** → automatiza provisionamento, implantação, rede e ciclo de vida de containers (Docker, Kubernetes).
- **Orquestração de nuvem** → coordenação de recursos de computação em nuvem (servidores, armazenamento, redes).

**Ferramentas de orquestração de dados** citadas em aula: Azure Data Factory (ADF), Apache Airflow, Astro (Airflow gerenciado), Dagster e Databricks Workflows. Databricks e Airflow foram apontados como os mais usados no mercado hoje, junto com o ADF.

**Benefícios da orquestração de dados**:

- **Gerenciamento de workloads** → evita gargalos, garante desempenho mais consistente e reduz risco de falhas.
- **Alta escalabilidade de tarefas** → permite dimensionar recursos para volumes de dados e novas fontes crescentes.
- **Flexibilidade** → dependências entre tarefas ficam claras e centralizadas no mesmo ambiente (ex: transformação só roda depois que a ingestão terminar com sucesso).
- **Redução de custos** → automatiza processos manuais e supervisão, reduzindo custo operacional.
- **Monitoramento** → acompanhamento contínuo dos fluxos, permitindo identificar e resolver problemas rapidamente (inclusive com alertas automáticos, tipo e-mail).
- **Clareza de falha** → visualização do pipeline facilita identificar, prevenir e resolver erros.

## O papel do Engenheiro de Dados

Na prática, o engenheiro de dados garante que toda a engrenagem funcione. Principais responsabilidades:

- **Extração e carga de dados (EL)** → buscar dados em bancos, APIs, arquivos, sistemas internos e carregar tudo para um ambiente de dados.
- **Provisionamento de infraestrutura** → criar clusters, storage, permissões, ambientes de dev e produção.
- **Criação e manutenção de pipelines** → construir os fluxos que movem os dados e mantê-los funcionando ao longo do tempo.
- **Orquestração dos fluxos** → garantir que cada etapa rode na hora certa, respeitando dependências.
- **Agendamento de deploys** → publicar novas versões dos pipelines, atualizar código, subir melhorias.
- **Monitoramento das execuções** → acompanhar falhas, tempos de execução, volumes de dados, gargalos.
- **Rastreabilidade** → saber de onde veio o dado, quando foi carregado e o que aconteceu com ele em cada etapa.

Na visão geral apresentada, o Data Engineer é responsável principalmente por **EL (extração e carregamento)**, **Cloud (provisionamento de infraestrutura)** e **Deploys (agendamento de tarefas)** — a modelagem em si (dbt, transformação em SQL) fica mais a cargo do Analytics Engineer.

### Perguntas-chave antes de começar um projeto

Essas perguntas praticamente definem toda a arquitetura da solução, então valem uma call de discovery antes de escrever qualquer linha de código:

1. **Com que frequência os dados vão ser utilizados?** → define o ritmo do pipeline (tempo real, hora em hora, diário, mensal). Nem todo problema precisa ser em tempo real — assumir isso sem necessidade gera custo desnecessário.
2. **Qual o volume de dados que será extraído?** → define a escala (megabytes vs terabytes) e se é preciso pensar em processamento distribuído, particionamento e paralelismo.
3. **Como os dados são alterados na fonte?** → full refresh (traz tudo de novo, simples mas caro/lento), incremental (busca só registros novos, geralmente via data de criação ou ID crescente) ou upsert (lida com novos registros e atualizações de existentes).
4. **Qual stack de tecnologias melhor se encaixa?** → não existe stack perfeita, existe a adequada pro problema (orçamento, maturidade do time, escalabilidade futura, complexidade do negócio).
5. **Como meu pipeline se comporta em cenários reais?** → o que acontece se uma extração falhar, se o volume dobrar, se a fonte mudar o esquema? Pipelines resilientes precisam falhar de forma controlada, permitir reprocessamento e se adaptar à evolução dos dados.

### Boas práticas

- **Princípio do privilégio mínimo (PoLP)** → liberar apenas as permissões que o usuário precisa para executar sua tarefa, limitando o acesso a recursos e dados críticos.
- **Legibilidade de código** → código limpo e variáveis bem nomeadas facilitam o entendimento imediato e servem de base para futuras replicações de pipelines parecidos.
- **Gerenciamento de versão** → um bom controle de versão facilita e reduz o tempo na resolução de problemas.
- **Qualidade dos dados** → garantir que os dados sejam abrangentes, consistentes, confiáveis e oportunos em todas as camadas do pipeline.
- **Foco no valor de negócio** → o dado fluindo tranquilamente entre as camadas é o que permite ao engenheiro de dados gerar valor real pro negócio — a tecnologia é meio, não fim.

## Termos que preciso lembrar

- **Pipeline de dados** → fluxo/cano pelo qual o dado passa da origem até o destino, sofrendo transformações no caminho.
- **Batch** → ingestão em lote, agendada, geralmente em D-1.
- **Streaming** → ingestão em tempo real, contínua, via filas.
- **ETL** → Extract, Transform, Load (transforma antes de carregar).
- **ELT** → Extract, Load, Transform (carrega bruto e transforma depois).
- **Camada bronze/silver/gold(/diamond)** → níveis de refinamento do dado na arquitetura medalhão.
- **Orquestração** → coordenação automatizada de tarefas e suas dependências (agendamento, monitoramento, recuperação de falhas).
- **Full refresh / Incremental / Upsert** → estratégias diferentes de atualização de uma tabela a partir da fonte.
- **PoLP (Principle of Least Privilege)** → princípio do privilégio mínimo.

## Pra lembrar depois

- Engenharia de dados = alicerce de uma plataforma de dados; se divide em coleta, armazenamento, processamento, orquestração/automação e governança/segurança
- Pipeline de dados é o fluxo completo desde a extração até o destino final, como um sistema de canos
- Ingestão = coleta + armazenamento; pode ser batch (mais comum, D-1) ou streaming (mais complexo, tempo real)
- ETL transforma antes de carregar; ELT carrega bruto e transforma depois — ELT é mais flexível e é o padrão mais usado hoje
- Arquitetura medalhão: bronze (bruto) → silver (transformado) → gold (pronto pro negócio)
- Orquestradores (Airflow, Databricks Workflows, ADF, Dagster, Astro) cuidam de agendamento, dependências, monitoramento e redução de custo operacional
- O engenheiro de dados é responsável principalmente por EL, infraestrutura em cloud e deploys/agendamento
- Antes de codar qualquer pipeline: perguntar frequência, volume, forma de atualização da fonte, stack adequada e comportamento em cenários de falha
- Boas práticas: privilégio mínimo, código legível, versionamento, qualidade de dados e foco em valor de negócio

## Referências
- [AWS - O que é um pipeline de dados](https://aws.amazon.com/pt/what-is/data-pipeline/)
- [Apache Airflow](https://airflow.apache.org/)
- [Databricks Workflows](https://www.databricks.com/product/workflows)

## Créditos
Conteúdo baseado na aula ministrada por **Arthur Cerqueira Farias**, Data Engineer na Indicium.
- 🔗 [LinkedIn](https://www.linkedin.com/in/arthur-cerqueira-665626226/)
