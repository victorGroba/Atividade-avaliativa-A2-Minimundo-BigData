import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =============================
# 1. DADOS BRUTOS
# =============================

df = pd.read_csv("saude_doencas.csv")

print("\n" + "="*60)
print("        ANÁLISE DE DIABETES POR CIDADE – DADOS BRUTOS")
print("="*60)

print("\n> Informações da Tabela:\n")
print(df.info())

print("\n> Primeiras Linhas:\n")
print(df.head().to_string(index=False))

print("\n> Estatísticas Numéricas:\n")
print(df.describe())

# =============================
# 2. CÁLCULO DA TAXA POR 10 MIL
# =============================
df["taxa_10k"] = (df["casos_diabetes"] / df["populacao"]) * 10000

# =============================
# 3. CLASSIFICAÇÃO DO RISCO
# =============================
def classificar_risco(t):
    if t < 40:
        return "Baixo"
    elif t <= 70:
        return "Médio"
    else:
        return "Alto"

df["risco"] = df["taxa_10k"].apply(classificar_risco)

# =============================
# 4. TABELA FINAL ORGANIZADA
# =============================
df = df.sort_values("taxa_10k", ascending=False)

print("\n" + "="*60)
print("               TABELA FINAL COM TAXA & RISCO")
print("="*60 + "\n")

print(df.to_string(index=False))
print("\n" + "="*60 + "\n")


# =============================
# 5. GRÁFICO 1 – TAXA DE RISCO
# =============================

sns.set_theme(style="whitegrid")

plt.figure(figsize=(12, 7))

cores = {
    "Baixo": "#2ECC71",
    "Médio": "#F1C40F",
    "Alto":  "#E74C3C"
}

barplot = sns.barplot(
    data=df,
    x="cidade",
    y="taxa_10k",
    hue="risco",
    palette=cores,
    dodge=False
)

# labels acima das barras
for p in barplot.patches:
    barplot.annotate(
        f"{p.get_height():.1f}",
        (p.get_x() + p.get_width()/2., p.get_height()),
        ha='center',
        va='bottom',
        xytext=(0, 6),
        textcoords='offset points'
    )

plt.title("Taxa de Risco de Diabetes por Cidade (a cada 10 mil hab.)", fontsize=15)
plt.xlabel("Cidade")
plt.ylabel("Taxa por 10 mil hab.")
plt.legend(title="Nível de Risco")
plt.tight_layout()

# salvar o gráfico 1
plt.savefig("grafico_taxa_risco.png", dpi=300)
plt.close()


# =============================
# 6. GRÁFICO 2 – CASOS ABSOLUTOS
# =============================

plt.figure(figsize=(10, 6))

plt.bar(df["cidade"], df["casos_diabetes"], color="#4A90E2", edgecolor="black")

for i, v in enumerate(df["casos_diabetes"]):
    plt.text(i, v + 5, str(v), ha='center')

plt.title("Quantidade de Casos de Diabetes por Cidade", fontsize=15)
plt.xlabel("Cidade")
plt.ylabel("Casos de Diabetes")
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()

# salvar o gráfico 2
plt.savefig("grafico_casos_diabetes.png", dpi=300)
plt.close()

print("Gráficos gerados e salvos com sucesso!")
