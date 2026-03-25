library(httr2);
library(dotenv)

load_dot_env()

# Captura argumentos da linha de comando
args <- commandArgs(trailingOnly = TRUE)
cidade <- if (length(args) > 0) args[1] else "Belo Horizonte,MG"

apiKey = Sys.getenv("API_KEY")

url <- "https://api.hgbrasil.com/weather"
req <- request(url) |>
  req_url_query(
    key=apiKey,
    city_name=cidade) |>
  req_perform()
  
res <- resp_body_json(req)

# Extraindo e mostrando os dados solicitados
cat("\n--- Previsão do Tempo ---\n")
cat("Cidade:", res$results$city, "\n")
cat("Data:", res$results$date, "\n")
cat("Temperatura:", res$results$temp, "°C\n")
cat("Condição:", res$results$description, "\n")
cat("-------------------------\n")