# analise.R
# Script para calcular estatísticas básicas dos dados de manejo de insumos

if (!file.exists("dados.csv")) {
  stop("Arquivo 'dados.csv' não encontrado. Insira alguns dados no sistema primeiro.")
}

# Carregar os dados
dados <- read.csv("dados.csv", encoding = "UTF-8")

if (nrow(dados) == 0) {
  stop("O arquivo 'dados.csv' está vazio.")
}

# Selecionar colunas numéricas
colunas_numericas <- c("area_m2", "hectares", "fosforo", "fertilizante")

cat("
========= ESTATÍSTICAS DOS DADOS =========
")

for (coluna in colunas_numericas) {
  cat("
Coluna:", coluna, "
")
  media <- mean(dados[[coluna]], na.rm = TRUE)
  desvio <- sd(dados[[coluna]], na.rm = TRUE)
  
  cat("  Média: ", round(media, 4), "
")
  cat("  Desvio Padrão: ", round(desvio, 4), "
")
}

cat("
==========================================
")
