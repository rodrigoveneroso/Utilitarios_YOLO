from ultralytics import YOLO


'''
Este script lista informações disponíveis em um modelo YOLO (.pt),

Inclui classes, número de parâmetros e tamanho de entrada esperado.
'''


# Caminho para o modelo YOLO
MODEL_PATH = "modelo.pt"

# Carrega o modelo
model = YOLO(MODEL_PATH)

# Nomes das classes
print("\nClasses detectáveis (model.names):")
print(model.names)

# Número de classes
print(f"\nNúmero de classes: {len(model.names)}")

# Número total de parâmetros
total_params = sum(p.numel() for p in model.model.parameters())
print(f"\nTotal de parâmetros no modelo: {total_params:,}")

# Tamanho de entrada esperado
if hasattr(model.model, 'args') and 'imgsz' in model.model.args:
    print(f"\nTamanho de entrada esperado (imgsz): {model.model.args['imgsz']}")
else:
    print("\nTamanho de entrada esperado: padrão (geralmente 640x640)")
