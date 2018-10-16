# Classificação multi-classe de imagens

É preciso criar um dataset de imagens, para fazer os testes eu utilizei 400
imagens para treinamento e 100 imagens para validação do modelo, faço download
das imagens do `Flickr` e depois manualmente seleciono as imagens e coloco em
`validation`.  
  
E pra utilizar o script para fazer download de arquivos no `Flickr` é preciso
criar as variáveis de ambientes `FLICKR_API_KEY` e `FLICKR_SECRET`.

### Instalar dependências
 
```bash
$ pip install -r requirements.txt
```

### Ferramentas
 
baixar_imagens_flickr.py -> Uso para fazer os datasets de imagens.  
treinar_modelo.py -> Fazer o treinamento do modelo preditivo.  
classificar_imagem.py -> Faz a classificação de alguma imagem a partir do que
foi treinado.  


