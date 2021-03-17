#importar as bibliotecas

import streamlit as st
import numpy as np
import cv2
import imutils
import argparse
from PIL import Image, ImageEnhance

def rotacao(grau, imagem):
    st.sidebar.image(imagem.rotate(grau, expand=True), width=150)

def rotacao_filtros(grau, imagem):
    rotated = imutils.rotate_bound(imagem, grau*-1)
    st.image(rotated, width=300)



def rotacao_blur(grau, imagem):
    rotated = imutils.rotate_bound(imagem, grau * -1)
    st.image(rotated, width=300, channels="BGR")



def main():


    st.subheader("Carregar arquivo de imagem")
    image_file = st.file_uploader("Escolha uma imagem ", type=["jpg", "jpeg", "png"])
    our_image = Image.open("../image/empty.jpg")



    st.sidebar.header("Photo Filtros")
    st.sidebar.info('100% em python')
    st.sidebar.markdown("App para aplicar filtros em imagens, utilizando OpenCV")
    opcoes = ['Preto e Branco', 'Negativo', 'Desenho', 'Contorno', 'Blur']
    grau = st.sidebar.slider("Rotação", 0, 360, 90, step=10)
    opcoes_filtro = st.sidebar.radio("Filtros", opcoes)

    if image_file is not None:
        #pega a imagem e guarda na variável
        our_image = Image.open(image_file)
        st.sidebar.text("Imagem Original")
        rotacao(grau, our_image)


    if opcoes_filtro == 'Preto e Branco':
        convert_image = np.array(our_image.convert('RGB'))
        gray_image = cv2.cvtColor(convert_image, cv2.COLOR_RGB2GRAY)
        rotacao_filtros(grau, gray_image)




    elif opcoes_filtro == "Negativo":
        convert_image = np.array(our_image.convert('RGB'))
        gray_image = cv2.cvtColor(convert_image, cv2.COLOR_RGB2GRAY)
        inv_gray_image = 255 - gray_image
        rotacao_filtros(grau, inv_gray_image)


    elif opcoes_filtro == "Blur":
        niveis = st.sidebar.slider("Kernel(n x n)", 3, 77, 9, step=2)
        convert_image = np.array(our_image.convert('RGB'))
        imagem_blur = cv2.cvtColor(convert_image, cv2.COLOR_RGB2BGR)
        blur_image = cv2.GaussianBlur(imagem_blur, (niveis, niveis), 0, 0)
        rotacao_blur(grau, blur_image)


    elif opcoes_filtro == "Contorno":
        convert_image = np.array(our_image.convert('RGB'))
        convert_image = cv2.cvtColor(convert_image,cv2.COLOR_RGB2BGR)
        blur_image = cv2.GaussianBlur(convert_image, (11, 11), 0)
        canny = cv2.Canny(blur_image, 10, 15)
        rotacao_filtros(grau, canny)



    elif opcoes_filtro == "Desenho":
        convert_image = np.array(our_image.convert('RGB'))
        gray_image = cv2.cvtColor(convert_image, cv2.COLOR_RGB2GRAY)
        inv_gray_image = 255 - gray_image
        blur_image = cv2.GaussianBlur(inv_gray_image, (71, 71), 0, 0)
        sketch_image = cv2.divide(gray_image, 255 - blur_image, scale=265)
        rotacao_filtros(grau, sketch_image)



if __name__ == '__main__':
    main()





























