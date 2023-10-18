import cv2



imagem_entrada = "21577.jpg"  # Substitua pelo caminho da sua imagem
fator_brilho = float(input("Digite o fator de brilho (1.0 para a mesma, <1.0 para escurecer, >1.0 para clarear): "))


ajustar_brilho=lambda imagem,fator_brilho: print("Imagem não encontrada.") if cv2.imread(imagem) is None else cv2.imshow("Imagem Ajustada", cv2.convertScaleAbs(cv2.imread(imagem), alpha=fator_brilho, beta=0)) or cv2.waitKey(0) or cv2.destroyAllWindows()

ajustar_brilho(imagem_entrada,fator_brilho)
