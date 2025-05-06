Este repositório reúne utilitários simples para facilitar o uso de modelos YOLO em diferentes etapas do pipeline de visão computacional, desde a organização dos dados até a inspeção visual das inferências.


## Descrição dos scripts

- **testar_modelo_yolo.py**  
  Abre um vídeo e executa a inferência do seu modelo YOLO.  
  - Permite ajustar a taxa de FPS para se ajustar à taxa de FPS do vídeo.  
  - Desenha caixas e labels no frame para visualizar resultados em tempo real.

- **checar_confianca_yolo.py**  
  Exibe, em cada bounding box, o nome da classe e o score de confiança.  
  - Útil para avaliar limiares de corte e performance qualitativa das detecções.

- **checar_informacoes_yolo.py**  
  Carrega um arquivo `.pt` de modelo YOLO e imprime:  
  - A lista de classes detectáveis (`model.names`).  
  - O número total de parâmetros do modelo.  
  - O tamanho de entrada esperado (`imgsz`).

- **renomear_imagens.py**  
  Padroniza o nome de todas as imagens (`.jpg`/`.png`) em um diretório, seguindo o formato:
    ```
    base_name_1.jpg, base_name_2.jpg, ...
    ```  
  - Ordena os arquivos alfabeticamente antes de renomear.  
  - Garante nomes únicos adicionando sufixos se necessário.

## Instalação

1. Clone o repositório:
    ```
    git clone https://github.com/seu-usuario/yolo-utils.git
    ```
2. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
