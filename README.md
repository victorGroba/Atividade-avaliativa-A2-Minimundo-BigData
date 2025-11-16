# Análise de Casos de Diabetes por Cidade

Este projeto realiza uma análise simples e direta sobre dados de diabetes em diferentes cidades.  
O objetivo é calcular a taxa de casos por 10 mil habitantes, classificar o nível de risco e gerar gráficos ilustrativos.

---

## 📌 O que o script faz

O arquivo `projeto_diabetes.py` executa as seguintes etapas:

### 1. Leitura dos dados  
Lê o arquivo `saude_doencas.csv` e exibe:
- Estrutura da tabela
- Primeiras linhas
- Estatísticas básicas dos dados numéricos

### 2. Cálculo  
Cria uma nova coluna chamada **taxa_10k**, usando a fórmula:

```
(casos_diabetes / populacao) * 10000
```

### 3. Classificação do risco  
Cada cidade recebe uma classificação de risco baseada na taxa:

| Taxa por 10 mil hab. | Risco |
|----------------------|--------|
| < 40                 | Baixo  |
| 40 a 70              | Médio  |
| > 70                 | Alto   |

### 4. Tabela Final  
O script exibe uma tabela organizada mostrando:
- Cidade  
- Casos  
- População  
- Taxa por 10 mil habitantes  
- Classificação do risco  

### 5. Geração de Gráficos  
Dois gráficos são criados e salvos automaticamente no projeto:

1. **grafico_taxa_risco.png**  
   - Exibe a taxa por 10 mil habitantes  
   - Colorido por nível de risco  

2. **grafico_casos_diabetes.png**  
   - Mostra a quantidade total de casos por cidade  

---

## 📁 Arquivos do Projeto

```
projeto_diabetes.py        # Script principal
saude_doencas.csv          # Base de dados analisada
grafico_taxa_risco.png     # Gráfico gerado automaticamente
grafico_casos_diabetes.png # Segundo gráfico gerado
README.md                  # Documentação do projeto
```

---

## ▶️ Como Executar

1. Certifique-se de que todos os arquivos estejam na mesma pasta.  
2. Instale as dependências obrigatórias:

```
pip install pandas matplotlib seaborn
```

3. Execute o script:

```
python projeto_diabetes.py
```

Os gráficos serão gerados automaticamente na pasta do projeto.

---

## ✔️ Conclusão

Este projeto permite visualizar rapidamente:
- A taxa de diabetes por cidade  
- A classificação de risco  
- Comparação visual com gráficos  

É uma solução simples, clara e fácil de apresentar, cobrindo análise básica e visualização de dados.
