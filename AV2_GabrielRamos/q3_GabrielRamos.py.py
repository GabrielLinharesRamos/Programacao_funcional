import cv2

def ajustar_brilho_imagem(imagem, fator_brilho):
    # Carregar a imagem de entrada
    img = cv2.imread(imagem)

    if img is None:
        print("Imagem não encontrada.")
        return

    # Ajustar o brilho da imagem
    imagem_ajustada = cv2.convertScaleAbs(img, alpha=fator_brilho, beta=0)

    # Mostrar a imagem original e a imagem ajustada
    cv2.imshow("Imagem Original", img)
    cv2.imshow("Imagem Ajustada", imagem_ajustada)

    # Aguardar o usuário pressionar uma tecla e fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    imagem_entrada = "/4ed58f9bb19fde847296c5dcf5d34db4.jpg"  # Substitua pelo caminho da sua imagem
    fator_brilho = float(input("Digite o fator de brilho (1.0 para a mesma, <1.0 para escurecer, >1.0 para clarear): "))

    ajustar_brilho_imagem(imagem_entrada, fator_brilho)
