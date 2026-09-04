# Modelo: relatório técnico de meio ambiente — queimadas e estiagem 2025

## Referência preservada

- Caminho na raiz do plugin: `template/RELATÓRIO TÉCNICO MEIO AMBIEMTE 2025 ATUALIZADO.docx`
  (o nome do arquivo contém a grafia `AMBIEMTE`; o script localiza o modelo pelo hash, não dependa do nome.)
- SHA-256: `CC824F0B892219EA8BE95200C5E08D1C3383B56B0DAFC0CADF29691375A9E4D7`
- Tamanho observado: `6.939.045` bytes.
- O modelo é somente leitura. Gere relatórios exclusivamente a partir de uma cópia.
- Caso do modelo: município de Acará, Pará (PA), ano de referência 2025, data documental "17 de novembro de 2025". Nada disso é dado padrão.

## Estrutura apurada

- 218 parágrafos no corpo (inclui os parágrafos internos das tabelas, estilo `TableParagraph`).
- 26 elementos `sectPr` (25 quebras de seção mais o `sectPr` final), todos retrato.
- 2 tabelas no Anexo 1, ambas com 4 colunas no padrão `Nº | Localidade | Nº | Localidade` (18 e 7 linhas).
- 70 arquivos de mídia; 17 imagens em linha e 53 flutuantes/ancoradas no corpo.
- 5 partes de cabeçalho (`header1`, `header3` e `header5` com três imagens de identidade visual cada; `header2` e `header4` vazios) e 5 partes de rodapé, cada rodapé com um campo `PAGE` e uma imagem de brasão.
- Nenhuma nota de rodapé, nota de fim ou controle de conteúdo. Um hyperlink no corpo (Referências).
- Estilos reais em uso: `Ttulo1` (heading 1, 6 ocorrências), `Ttulo2` (heading 2, 3 ocorrências), `Corpodetexto` (Body Text, 178) e `TableParagraph` (101). Ao contrário de outros modelos do plugin, os títulos aqui usam estilos `Heading`; preserve esse comportamento.
- Uso extenso de formatação direta sobre os estilos. Não "limpe" essa formatação durante uma atualização comum.

## Sistema de página

- Tamanho A4, aproximadamente `8,27 × 11,69 pol.` em todas as seções.
- Margens: esquerda `0,20 pol.`, direita `0,49 pol.`, inferior `0,86 pol.` em todas as seções.
- Margem superior `1,18 pol.` na maioria das seções e `0,26 pol.` nas seções que iniciam páginas de anexo fotográfico.
- A seção 1 é contínua e define cabeçalho e rodapé próprios (`rId7`/`rId8`). As seções seguintes herdam, exceto pontos em que novas referências de cabeçalho/rodapé são declaradas (por exemplo seções 11, 14, 16 e 19). Preserve essas relações.

## Ordem de conteúdo

1. Título e Introdução, com a caracterização geográfica e demográfica do município e o Mapa de localização (Figura 1).
2. Apresentação.
3. Precipitação e Temperatura, com gráfico (Figura 2) e nota sobre médias climatológicas.
4. Justificativa, incluindo contexto estadual das queimadas e a subseção `Estiagem x Seca dos Rios`, e o Mapa de focos de queimadas (Figura 3).
5. Diagnóstico, com a subseção `Diagnóstico da Situação em <Município> (<ano>):` e seus parágrafos-tópico.
6. Conclusão.
7. Anexo 1 — Levantamento das localidades afetadas (duas tabelas).
8. Anexo 2 — Imagens de locais com estiagem (seção fotográfica).
9. Anexo 3 — Exemplos de áreas queimadas (seção fotográfica).
10. Parágrafo de encerramento do monitoramento e linha de data.
11. Bloco de assinatura (cargo, município-UF, ano).
12. Referências.

## Mapa de substituições

- **Município, UF e ano:** substituir em todas as ocorrências pertinentes do corpo, cabeçalhos, rodapés, legendas, linha de data, assinatura e Referências.
- **Tipo do desastre:** o modelo é escrito para queimadas e estiagem. Quando o desastre informado for outro (enchentes, alagamentos, deslizamentos, etc.), reescrever as menções ao fenômeno, causas, efeitos, indicadores e legendas de figuras para esse desastre em todas as seções, preservando estrutura, ordem, estilos, título do documento e a contagem de parágrafos, tabelas e seções. A subseção `Estiagem x Seca dos Rios` mantém a função de distinguir conceitos correlatos, adaptada ao desastre informado.
- **Introdução:** substituir área territorial, percentual estadual, regiões, distância da capital, coordenadas da sede e população estimada pelos dados verificados do município informado, mantendo as fontes entre parênteses.
- **Apresentação:** adaptar objetivo, secretaria, órgão parceiro e ano.
- **Precipitação e Temperatura:** adaptar o regime de chuvas e temperaturas, os meses de menor precipitação, as faixas térmicas e a fonte; manter a nota metodológica sobre médias climatológicas.
- **Justificativa:** adaptar o histórico local e os dados de contexto estadual (percentuais, hectares, fontes). Preservar o conteúdo conceitual de `Estiagem x Seca dos Rios`, adaptando apenas menções geográficas.
- **Diagnóstico:** adaptar o texto de abertura e cada parágrafo-tópico da subseção, mantendo a mesma quantidade e a mesma função de cada tópico (Focos Registrados, Ações de Fiscalização, Contexto Estadual, Prognóstico de Risco, Trabalho de Campo).
- **Conclusão:** adaptar a síntese, a análise de vulnerabilidade, os impactos à saúde, a base legal e as recomendações à localidade informada, mantendo a lógica e a quantidade de parágrafos.
- **Anexo 1:** substituir a lista de localidades pela fornecida pelo usuário, preservando as duas tabelas de 4 colunas e a numeração. Confirmar antes de acrescentar ou remover linhas.
- **Anexos 2 e 3:** preservar. Só alterar fotografias mediante arquivos e autorização do usuário, mantendo dimensões, proporção e âncora.
- **Assinatura:** alterar nome e cargo apenas com dados e pedido do usuário; adaptar município-UF e ano.
- **Referências:** atualizar a estatística municipal, a URL de previsão do tempo, a URL do IBGE Cidades e as datas de acesso, conferindo em fonte oficial.
- **Demais conteúdos:** preservar. Não alterar assunto, órgão emissor, numeração de figuras, cabeçalhos, rodapés, logos ou paginação sem pedido explícito.
- **Estilização:** preservar integralmente; faça as substituições dentro dos elementos existentes, mantendo as propriedades de parágrafo, execução e célula.

## Limitações da inspeção inicial

A inspeção estrutural foi feita a partir do pacote OOXML. A inspeção visual página a página não foi concluída porque não havia conversor DOCX/PDF disponível no ambiente. Número exato de páginas (o pacote declara 21), recortes, sobreposições e o posicionamento das 53 imagens flutuantes permanecem não verificados. Uma renderização completa é obrigatória antes de entregar qualquer relatório derivado quando houver um renderizador disponível.

## Gates de fidelidade

- Compare o SHA-256 do modelo antes e depois; deve permanecer idêntico.
- Preserve os 26 `sectPr` e a geometria de página, salvo alteração solicitada.
- Preserve as 2 tabelas do Anexo 1 com 4 colunas cada.
- Preserve os 5 cabeçalhos e 5 rodapés, o campo `PAGE`, as imagens institucionais e as relações internas não editadas.
- Verifique os anexos fotográficos página a página para evitar deslocamento de imagens flutuantes.
- Confirme que município, UF, ano e data foram atualizados em todas as ocorrências pertinentes.
- Confirme que o relatório está enquadrado no tipo de desastre informado e que nenhuma menção a queimadas ou estiagem permaneceu quando o desastre for outro.
- Confirme que apenas os blocos textuais autorizados foram modificados e que nenhum dado factual de Acará-PA permaneceu como conteúdo do novo relatório.
- Confirme que nenhuma propriedade visual do template foi alterada.
