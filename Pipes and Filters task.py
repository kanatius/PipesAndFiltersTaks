import re

#funçoes

#as funções servem como filtros, fazendo a modificação na entrada e gerando uma saída 
def addHead(texto):
  response = re.search("<head>.*</head>", texto) #verfica se ja tem <head></head>
  if(response == None): #se não achou, adiciona o head
    return "<head></head>\n" + texto;
  return texto;

def addBody(texto):
  response = re.search("<body>.*</body>", texto)  #verfica se ja tem <body></body>
  if(response == None): #se não achou, adiciona o body
    return "<body>" + texto + "</body>\n";
  return texto

def addHtml(texto):
  response = re.search("<!DOCTYPE html>.*</html>", texto) #verfica se ja tem <!DOCTYPE html></html>
  if(response == None): #se não achou, adiciona o doctype
    return "<!DOCTYPE html>" + texto + "</html>\n"
  return texto


texto = '<div class="conteudo-post"><h1 class="h1mobile">Melhores praias do Nordeste: 25 lugares que você precisa conhecer após a quarentena</h1>' + '<p>Temos <a href="https://www.melhoresdestinos.com.br/melhores-praias-do-brasil.html" data-wpel-link="internal" rel="follow">praias</a> lindas no Brasil todo e isso todo mundo sabe, né? E quais seriam as melhores praias do <a href="https://www.melhoresdestinos.com.br/melhores-destinos-nordeste-brasileiro.html" data-wpel-link="internal" rel="follow">Nordeste</a> brasileiro? O conceito é relativo, afinal, temos praias para todo gosto em nosso litoral, capazes de agradar gregos e troianos.</p><div class="banner1-post-promo-wrapper-celular" style="height:250px; width:300px;margin:0 auto;">' + '<p>O Nordeste é a região com o maior litoral em nosso país, tem paisagens variadas, dunas, encontro de rios com o mar, falésias, piscinas naturais e maravilhosos pontos para mergulho, ricos em vida marinha. Essa diversidade permite que os viajantes encontrem também praias com resorts ou pousadas econômicas, praias cheia de gente e outras praticamente vazias… Uma dessas dezenas de praias da região (ou várias) certamente irá agradá-lo!</p>'+ '<p>Fizemos uma lista com as praias que mais gostamos nessa região do país, que englobam diferentes estados e características! Vamos àquelas que elegemos as melhores praias do Nordeste! Os números não são uma colocação!</p></div>'

texto2 = texto #cópia para realização de teste


texto = addBody(texto) #

texto = addHead(texto) #a entrada de dados no filtro vem diretamente de outro filtro, caracterizando Pipes

texto = addHtml(texto) #



texto2 = addBody(texto2) #

texto2 = addHtml(texto2) # a sequencia dos filtros causa uma saída diferente

texto2 = addHead(texto2) #



print(texto) #texto com os filtros na sequencia correta

print(texto2) #texto com os filtros na sequencia errada - tag head antes do doctype
