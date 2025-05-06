from ultralytics import YOLO
import cv2
import os


'''
Este código auxilia a checagem visual de um modelo YOLO observando as detecções sobre um vídeo.
Por padrão, a taxa de FPS está em 30. Caso seu video seja diferente, ajustar na variável TARGET_FPS.
'''


# Força Qt a usar X11 (caso necessário em Wayland)
os.environ["QT_QPA_PLATFORM"] = "xcb"

# =============================================================================
# Parâmetros de entrada — ajuste conforme necessário
# =============================================================================
VIDEO_PATH = "seu_video.mp4"     # caminho para o vídeo de teste
MODEL_PATH = "seu_modelo.pt"     # caminho para o arquivo .pt do seu modelo
TARGET_FPS = 30                   # taxa desejada de reprodução (quadros por segundo)

def main():
    # Calcula o delay em milissegundos entre quadros
    delay_ms = int(1000 / TARGET_FPS)

    # Cria janela
    window_name = "YOLO Test"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # Abre o vídeo
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print(f"[ERRO] Não foi possível abrir o vídeo: {VIDEO_PATH}")
        return

    # Carrega o modelo YOLO
    try:
        model = YOLO(MODEL_PATH)
        print("[OK] Modelo carregado com sucesso.")
    except Exception as e:
        print(f"[ERRO] Falha ao carregar o modelo: {e}")
        cap.release()
        return

    # Loop principal
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[INFO] Fim do vídeo ou erro ao ler quadro.")
            break

        # Inferência
        results = model(frame)

        # Desenha detecções
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls_id = int(box.cls[0])
                cls_name = r.names.get(cls_id, str(cls_id))
                label = f"{cls_name}: {conf:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, label, (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

        # Exibe o quadro e aguarda 'delay_ms'
        key = cv2.imshow(window_name, frame) or cv2.waitKey(delay_ms) & 0xFF
        if key == ord('q'):
            break

    # Libera recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
