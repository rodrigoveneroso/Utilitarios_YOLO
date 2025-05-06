from ultralytics import YOLO
import cv2
import os


'''
Este código auxilia a checagem visual da confiança das detecções de um modelo YOLO sobre um vídeo.
Para passar frame por frame, apertar tecla 'n' ou a barra de espaço. Segurando as teclas, eles passam rapidamente.
'''


os.environ["QT_QPA_PLATFORM"] = "xcb"
VIDEO_PATH = "video.mp4"          # caminho para o vídeo de teste
MODEL_PATH = "modelo_yolo.pt"     # caminho para o arquivo .pt do seu modelo

def main():
    # cria a janela antes do loop
    window_name = "YOLO Test"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # opcional: cv2.resizeWindow(window_name, 1280, 720)

    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print(f"[ERRO] Vídeo não pode ser aberto: {VIDEO_PATH}")
        return

    try:
        model = YOLO(MODEL_PATH)
        print("Modelo carregado com sucesso.")
    except Exception as e:
        print(f"[ERRO] Falha ao carregar o modelo: {e}")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Fim do vídeo ou erro de leitura.")
            break

        results = model(frame)
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

        cv2.imshow(window_name, frame)
        key = cv2.waitKey(0) & 0xFF
        if key in (ord('n'), ord(' ')):
            continue
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
