# Módulo 3 — Introdução à SQL

Ciclo básico Lighthouse | Instrutora: Corina Bachmann (Team Lead Analytics Engineer)

## 📌 Sobre o módulo

Este módulo cobre os fundamentos da linguagem SQL, com prática usando o banco de dados **Northwind** (importadora fictícia de alimentos), simulando um cenário de onboarding como Analista Júnior de Dados.

### Tópicos abordados
- O que é SQL e para que serve (DDL, DML, DCL, DTL)
- Modelo relacional e tipos de dados
- Consultas básicas (`SELECT`, `DISTINCT`, `ORDER BY`, `LIMIT`)
- Filtros e operadores (comparação, lógicos, aritméticos) com `WHERE`
- Funções de agregação (`SUM`, `COUNT`, `AVG`, `MAX`, `MIN`) e `GROUP BY`
- Junção de tabelas (`INNER`, `LEFT`, `RIGHT`, `FULL`, `CROSS JOIN`)
- União de tabelas (`UNION` e `UNION ALL`)

### Ferramenta utilizada
Conexão via **DBeaver** com o banco Northwind (Postgres na nuvem ou SQLite local).

---

## 🗂️ Estrutura das queries (`script.sql`)

### Task A — Nome e preço de todos os produtos

```sql
-- Nome e preço de todos os produtos
select ProductName, UnitPrice
from Product
order by UnitPrice desc;
```

### Task B — Produtos com mais de 20 unidades em estoque e custam mais de 50 reais

```sql
-- Produtos com mais de 20 unidades no estoque,
-- e custam mais de 50 reais
select ProductName, UnitPrice, UnitsInStock
from Product p
where p.UnitsInStock > 20
and p.UnitPrice > 50;
```

### Task C — Valor total vendido por produto e valor médio dos pedidos

```sql
-- Valor total vendido por produto
select ProductId, sum(UnitPrice * Quantity) as valorTotal
from OrderDetail
group by ProductId
order by valorTotal;

-- Valor médio dos pedidos
select avg(UnitPrice * Quantity) as valorMedio
from OrderDetail;
```

### Task D — Produtos com o nome da categoria (join)

```sql
-- Product + Category
select Product.ProductName, Product.CategoryId, Category.CategoryName
from Product
inner join Category
on Product.CategoryId = Category.Id
order by Category.CategoryName;
```

### Atividade final — Top 3 categorias que mais geraram receita

```sql
-- 3 categorias de produtos que mais geraram receita
select c.CategoryName, sum(od.UnitPrice * od.Quantity) as valorTotal
from OrderDetail od
inner join Product p
on od.ProductId = p.Id
inner join Category c
on p.CategoryId = c.Id
group by c.CategoryName
order by valorTotal desc
limit 3;
```

---

## ▶️ Como executar

1. Instale o [DBeaver](https://dbeaver.io/)
2. Conecte-se ao banco Northwind (Postgres na nuvem ou SQLite local)
3. Abra o arquivo [`script.sql`](./script.sql) e execute as queries na ordem desejada

---

## 📚 Referência rápida — Ordem de uma consulta SQL

```sql
SELECT coluna_1, coluna_2, ...
FROM tabela_1
JOIN tabela_2 ON tabela_1.fk = tabela_2.pk
WHERE condições
GROUP BY coluna_1, coluna_2, ...
HAVING condições (agregadas)
ORDER BY coluna_1, coluna_2 desc, ...
LIMIT número_de_linhas
```
