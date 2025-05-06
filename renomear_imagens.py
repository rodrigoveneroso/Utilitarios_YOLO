import os


'''
Este script renomeia todas as imagens (.png ou .jpg) em uma pasta seguindo o padrão:
exemplo_1.jpg, exemplo_2.jpg, ...

Ideal para organizar datasets de treinamento de modelos YOLO, todos com um mesmo padrão.
'''


IMAGES_DIRECTORY = r'/home/rodrigo/Desktop/treinamentos/nome_pasta/images/train'  # Caminho da pasta com as imagens
BASE_NAME = 'exemplo'  # Nome base desejado para as imagens renomeadas

def rename_images(directory, base_name):
    # Listar os arquivos da pasta
    files = os.listdir(directory)

    # Filtrar arquivos .png e .jpg
    images = [f for f in files if f.lower().endswith(('.png', '.jpg'))]

    # Ordenar alfabeticamente
    images.sort()

    # Renomear imagens
    for i, filename in enumerate(images):
        extension = '.jpg' if filename.lower().endswith('.jpg') else '.png'
        new_name = f"{base_name}_{i + 1}{extension}"

        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)

        count = 1
        while os.path.exists(dst):
            new_name = f"{base_name}_{i + 1}_{count}{extension}"
            dst = os.path.join(directory, new_name)
            count += 1

        os.rename(src, dst)
        print(f"Renomeado: {filename} -> {new_name}")

# Executar renomeação
rename_images(IMAGES_DIRECTORY, BASE_NAME)
