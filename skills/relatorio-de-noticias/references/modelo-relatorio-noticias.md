# Modelo — Relatório de Notícias

## Arquivo de referência

- Modelo: `template/RELATÓRIO DE NOTÍCIAS.docx`
- SHA-256: `6EFFB346244CD5F94F0D51F731DD0525681B5C0B472D3FB674D665AF6D2C4605`
- O nome pode estar gravado em formas Unicode diferentes. Localize o arquivo pelo hash, não apenas pela grafia.

## Estrutura preservada

- 27 parágrafos no corpo.
- 2 seções.
- Nenhuma tabela.
- 2 imagens no cabeçalho.
- 3 imagens no corpo, uma para cada notícia.
- Título dividido em três parágrafos com o estilo `Heading 1`: `RELATÓRIO`, `DE`, `NOTÍCIAS`.
- Subtítulo no parágrafo seguinte: `<Desastre> no municipio de <Município>/<UF>`.
- Ano em parágrafo próprio.

O cabeçalho contém duas imagens e repetições do texto institucional. Atualize todas as ocorrências visíveis e internas do estado e do município, sem recriar o cabeçalho.

## Blocos de notícia

Cada bloco contém um hiperlink visível, uma captura da matéria e um parágrafo vazio imediatamente posterior reservado para a legenda:

1. primeiro link no parágrafo 10, captura no parágrafo 11 e legenda no parágrafo 12;
2. segundo link no parágrafo 15, captura no parágrafo 16 e legenda no parágrafo 17;
3. terceiro link no parágrafo 21, captura no parágrafo 22 e legenda no parágrafo 23.

Os índices são apenas referências de inspeção desta versão. Antes de editar, confirme a estrutura e localize os elementos por tipo, relação e ordem, evitando depender exclusivamente dos números dos parágrafos.

## Mídias da versão inspecionada

- `word/header1.xml` relaciona as duas imagens do cabeçalho aos arquivos `word/media/image1.png` e `word/media/image2.png`.
- O corpo relaciona as três capturas aos arquivos `word/media/image3.png`, `word/media/image4.jpg` e `word/media/image5.png`.
- Preserve os elementos de desenho, extensões, posição e relacionamentos; troque apenas o conteúdo binário da mídia e, se necessário, seu tipo no pacote OOXML.

Ao substituir uma imagem por formato diferente, atualize corretamente a extensão, o relacionamento e `[Content_Types].xml`. Sempre valide que o pacote abre sem reparo.

## Regras editoriais

- O relatório padrão contém exatamente três notícias.
- A data do relatório define o limite máximo de publicação das fontes.
- A primeira notícia deve ser a mais específica para o município; as demais podem ampliar para o estado e o país quando necessário.
- Os links devem ser diretos, verificáveis e clicáveis.
- A captura deve mostrar conteúdo suficiente para identificar a matéria correspondente.
- Cada captura deve ser seguida pela legenda `Figura <n> — <Título da matéria>. Fonte: <Veículo>, <DD/MM/AAAA>.`, com numeração de 1 a 3 e dados confirmados na própria página.
- Use os parágrafos vazios já existentes para as legendas; não adicione novos parágrafos nem aplique um novo estilo.
- Não adicione legenda às imagens do cabeçalho.
- Não copie textos extensos das notícias. O modelo registra o link e uma evidência visual da página.
