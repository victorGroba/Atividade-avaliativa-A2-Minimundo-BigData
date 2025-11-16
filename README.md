# 📊 Análise de Diabetes por Cidade  
Trabalho de Banco de Dados – Minimundo 6

Este projeto realiza uma análise completa dos casos de diabetes por cidade, incluindo:  
- Importação e exploração dos dados  
- Cálculo da taxa de casos por 10 mil habitantes  
- Classificação do risco por cidade  
- Geração de tabelas analisadas no terminal  
- Criação e salvamento de gráficos automaticamente  

---

## 📁 Estrutura do Projeto

Trabalho BD/
│
├── projeto_diabetes.py        
├── saude_doencas.csv          
├── grafico_taxa_risco.png     
├── grafico_casos_diabetes.png 
├── requirements.txt           
└── README.md                  

---

## 📦 Requisitos

Antes de rodar o projeto, instale as dependências:

```
pip install -r requirements.txt
```

Ou manualmente:

```
pip install pandas matplotlib seaborn
```

---

## ▶️ Como Executar

1. Certifique-se de que todos os arquivos estejam na mesma pasta.  
2. Abra o terminal dentro da pasta do projeto:

```
PS C:\Users\SeuUsuario\Desktop\Trabalho BD>
```

3. Execute:

```
python projeto_diabetes.py
```

---

## 📊 Funcionalidades

### ✔ 1. Importação e exploração dos dados  
- Info geral  
- Primeiras linhas  
- Estatísticas  

### ✔ 2. Cálculo  
Taxa por 10 mil habitantes:

```
(casos_diabetes / populacao) * 10000
```

### ✔ 3. Classificação do risco  
| Taxa | Risco |
|------|--------|
| < 40 | Baixo |
| 40–70 | Médio |
| > 70 | Alto |

### ✔ 4. Tabela no terminal  
Com: cidade, população, casos, taxa, risco colorido.

### ✔ 5. Gráficos gerados automaticamente
Salvos como:

- `grafico_taxa_risco.png`
- `grafico_casos_diabetes.png`

---

## 👥 Integrantes & Tarefas

| Integrante | Tarefa | Ferramenta |
|-----------|--------|------------|
| 1. Dados Brutos | Importar e explorar o CSV | Pandas |
| 2. Cálculo | Taxa por 10 mil hab. | Pandas |
| 3. Classificação | Criar coluna de risco | Pandas |
| 4. Visualização | Gráficos | Seaborn / Matplotlib |
| 5. Apresentação | Tabela final e slides | Pandas + Canva/PowerPoint |

---

## ✔ Observações

- O CSV deve estar na mesma pasta do script.  
- O script salva os gráficos automaticamente.  
- Compatível com qualquer PC (inclusive do professor).  

---

## 🏁 Conclusão

O projeto entrega:
- Análise completa  
- Tabela bem formatada  
- Dois gráficos  
- Visual profissional no terminal  
- Código simples e claro  

