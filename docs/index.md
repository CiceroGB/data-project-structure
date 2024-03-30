# Doc ETL join Excels

## Descrição

O projeto em unificar planilhas xlsx em uma única.

## Fluxo

```mermaid
    flowchart LR
        subgraph ETL [Pipeline]
            A[Multiplos Arquivos Excel] --> B(Extract: extract_from_excel)
            B[Extract: extract_from_excel] --> | Gera uma lista de Datafranes| C(Transformation: consolidate_dataframes)
            C[Transformation: consolidate_dataframes] -->|Gera um Datafrane Consolidado| D(Load: Converte para Excel)
            D[Load: Converte para Excel] --> |Salva o consolidado em Excel| E(Pasta Output: Um arquivo único Excel)
        end
```


## ETL

### ::: app.etl.extract

### ::: app.etl.load

### ::: app.etl.transform

### ::: app.etl.pipeline
