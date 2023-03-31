![](analise\_sent\_verb.001.png)

**Evaluation Only. Created with Aspose.Words. Copyright 2003-2023 Aspose Pty Ltd.**

**Análise de Sentimentos em Verbos - Amor de Perdição (Camilo Castelo Branco)**

Utilizando o comando *tagger* da ferramenta **linguakit** - no terminal - para analisar as entidades presentes no arquivo *"Camilo-Amor\_de\_Perdicao.txt"*, criei um documento de extenção .tag - *"enty\_amor\_de\_perdicao.tag"* - para receber o output deste comando e armazenar os seus resultados.

In [ ]:

linguakit tagger pt **-**nec Camilo**-**Amor\_de\_Perdicao**.**txt **>** enty\_amor\_de\_perdicao**.**tag

Em seguida - ainda no terminal - utilizei uma soma dos comandos *"grep"* and *"sort"* para procurar (grep) por todas as entidades do tipo VMI - verbo - em *"enty\_amor\_de\_perdicao.tag"*, ordená-las (sort) pela sua quantidade de ocorrências e gravar esses resultados em um arquivo de extensão .csv - *"verb\_amor\_de\_perdicao.csv"* -

In [ ]:

grep VMI enty\_amor\_de\_perdicao**.**tag **|** sort **|** uniq **-**c **|** sort **-**n **>** verb\_amor\_de\_perdicao**.**csv

Após isso, fiz o upload do arquivo *"verb\_amor\_de\_perdicao.csv"* no Google Sheets, ordenei a lista de ocorrências em ordem decrescente e assim fiz um gráfico de barras para vizualizar os 15 verbos que mais aparecem no livro *"Camilo-Amor\_de\_Perdicao.txt"*

![chart.svg](analise\_sent\_verb.002.png)

Em seguida, utilizei o comando *sent* - também da ferramenta **linguakit** - para analisar o sentimento dos verbos listados em *"verb\_amor\_de\_perdicao.csv"* e salvar o output em outro arquivo de extensão .csv *"verb\_sent\_perdicao.csv"*

In [ ]:

linguakit sent pt verb\_amor\_de\_perdicao**.**csv **>** verb\_sent\_perdicao**.**csv

Por fim, fiz a limpeza dos dados em *"verb\_sent\_perdicao.csv"* criando um filtro para vizualizar somente os verbos que tivessem um sentimento positivo ou negativo atribuído a eles, e os ordenei em seguida por ordem descescente. Assim, podemos vizualizar - entre os verbos que mais ocorrem no livro - aqueles que tem algum sentimento agregado ao mesmo, e qual sentimento é esse.

![chart%20%281%29.svg](analise\_sent\_verb.003.png)
**Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/**
