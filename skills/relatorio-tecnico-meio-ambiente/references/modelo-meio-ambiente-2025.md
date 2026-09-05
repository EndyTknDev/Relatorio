# Modelo: relatório técnico de meio ambiente — queimadas e estiagem 2025

## Referência preservada

- Caminho na raiz do plugin: `template/RELATÓRIO TÉCNICO MEIO AMBIEMTE 2025 ATUALIZADO.docx`
  (o nome do arquivo contém a grafia `AMBIEMTE` e pode chegar ao disco em forma Unicode decomposta; o script localiza o modelo pelo hash, não pelo nome.)
- SHA-256: `97F9981989143E64104323BB6F065960B905F62122DA59EBB3FC8A6075952079`
- Tamanho observado: `717.596` bytes.
- O modelo é somente leitura. Gere relatórios exclusivamente a partir de uma cópia.
- Caso do modelo: município de Acará, Pará (PA), ano de referência 2025, data documental "17 de novembro de 2025". Nada disso é dado padrão.
- Esta é uma nova versão do modelo (o anexo fotográfico do final do relatório — antigos Anexo 2 e Anexo 3 — foi removido pelo responsável pela skill). O hash, o tamanho e toda esta referência foram atualizados a partir dela; se o hash divergir novamente no futuro, trate como mais uma nova versão e repita a inspeção.

## Estrutura apurada

- 10 seções (era 26 antes da remoção do anexo fotográfico), todas retrato: 2 contínuas e 8 com quebra para nova página.
- 94 parágrafos no corpo (era 218), 2 tabelas no Anexo 1, ambas com 4 colunas no padrão `Nº | Localidade | Nº | Localidade` (18 e 7 linhas, inalteradas).
- 6 arquivos de mídia: 3 usados no cabeçalho (repetidos entre as duas partes de cabeçalho) e 3 usados no corpo — exatamente as Figuras 1, 2 e 3 descritas abaixo. Não há mais imagens de anexo fotográfico.
- 2 partes de cabeçalho (`header1`, `header2`, ambas com as mesmas 3 imagens de identidade visual) e 4 partes de rodapé (a seção 1 declara variantes `even`, `default` e `first`; confirme com o usuário se essa distinção entre página par/ímpar/primeira é intencional).
- O arquivo carrega um rótulo de confidencialidade do Microsoft Purview (`docMetadata/LabelInfo.xml`) que imprime o texto "Classified - Confidential" nos rodapés. Esse texto não é conteúdo do relatório; não o trate como campo a preencher nem o remova por conta própria.
- Estilos reais em uso: `Heading 1` (6 ocorrências), `Heading 2` (3 ocorrências), `Body Text` (78) e `Table Paragraph` (101). Nesta versão os identificadores internos dos estilos estão em inglês (`Heading1`, `Heading2`, `BodyText`, `TableParagraph`); o nome visível no Word é o mesmo. Os títulos usam esses estilos `Heading` reais, com numeração automática vinculada — preserve esse comportamento.
- Uso extenso de formatação direta sobre os estilos. Não "limpe" essa formatação durante uma atualização comum.
- Os metadados do pacote declaram `9` páginas; confirme o número real por renderização antes de citar um total ao usuário.

## Figuras do corpo (substituíveis mediante arquivo do usuário)

O corpo do documento tem exatamente três imagens flutuantes, nesta ordem, cada uma seguida de uma legenda "Figura N." e uma linha "Fonte:":

| Figura | Conteúdo no modelo | Seção onde aparece | Relação | Mídia |
|---|---|---|---|---|
| 1 | Mapa de localização do município | Introdução | `rId6` | `media/image1.jpeg` |
| 2 | Gráfico de precipitação e temperatura | Precipitação e Temperatura | `rId11` | `media/image4.png` |
| 3 | Mapa de focos de queimadas | Justificativa | `rId13` | `media/image5.jpeg` |

- Essas três figuras são as únicas imagens de conteúdo do relatório; peça-as ao usuário como entradas obrigatórias (mapa de localização, gráfico climático, mapa de focos/eventos do tipo de desastre informado).
- Substitua apenas o conteúdo binário de cada mídia pela imagem fornecida, preservando a relação, o quadro, a posição, a proporção e a ancoragem existentes. Não mova, remova nem duplique o elemento de desenho.
- Ajuste a legenda de cada figura (texto "Figura N. <descrição>." e a linha "Fonte: <origem>.") para descrever a imagem realmente fornecida e sua fonte, mantendo o formato e a numeração do modelo.
- Não invente fonte, data ou local da figura; use exatamente o que o usuário informar sobre cada arquivo enviado.

## Sistema de página

- Tamanho A4, aproximadamente `8,27 × 11,69 pol.` em todas as seções.
- Margens: esquerda `0,20 pol.`, direita `0,49 pol.`, superior `1,18 pol.`, inferior `0,86 pol.` — inalteradas em relação à versão anterior.
- A seção 1 é contínua e define cabeçalho e as três variantes de rodapé. A seção 8 (grupo do Anexo 1) declara um novo par cabeçalho/rodapé (`rId14`/`rId15`); as demais herdam. Preserve essas relações.

## Ordem de conteúdo

1. Título e Introdução, com a caracterização geográfica e demográfica do município e a Figura 1 (mapa de localização).
2. Apresentação.
3. Precipitação e Temperatura, com a Figura 2 (gráfico) e nota sobre médias climatológicas.
4. Justificativa, incluindo contexto estadual das queimadas, a subseção `Estiagem x Seca dos Rios` e a Figura 3 (mapa de focos/eventos).
5. Diagnóstico, com a subseção `Diagnóstico da Situação em <Município> (<ano>):` e seus parágrafos-tópico.
6. Conclusão.
7. Anexo 1 — Levantamento das localidades afetadas (duas tabelas).
8. Parágrafo de encerramento do monitoramento e linha de data.
9. Bloco de assinatura (cargo, município-UF, ano).
10. Referências.

**Não existe mais anexo fotográfico entre os itens 7 e 8** (os antigos Anexo 2 "Imagens de locais com estiagem" e Anexo 3 "Exemplos de áreas queimadas" foram removidos desta versão). Não peça nem insira fotografias de anexo por padrão; se o usuário pedir explicitamente para reintroduzi-las, trate como uma inserção nova a negociar (posição, tamanho, legenda), já que a estrutura atual não reserva mais esse espaço.

## Mapa de substituições

- **Município, UF e ano:** substituir em todas as ocorrências pertinentes do corpo, cabeçalhos, rodapés, legendas, linha de data, assinatura e Referências.
- **Figuras 1, 2 e 3:** substituir pelas imagens fornecidas pelo usuário (mapa de localização, gráfico climático, mapa de focos/eventos), seguindo a tabela de relações acima e atualizando as respectivas legendas e fontes.
- **Introdução:** substituir área territorial, percentual estadual, regiões, distância da capital, coordenadas da sede e população estimada pelos dados verificados do município informado, mantendo as fontes entre parênteses.
- **Apresentação:** adaptar objetivo, secretaria, órgão parceiro e ano.
- **Precipitação e Temperatura:** adaptar o regime de chuvas e temperaturas, os meses de menor precipitação, as faixas térmicas e a fonte; manter a nota metodológica sobre médias climatológicas.
- **Justificativa:** adaptar o histórico local e os dados de contexto estadual (percentuais, hectares, fontes). Preservar o conteúdo conceitual de `Estiagem x Seca dos Rios`, adaptando apenas menções geográficas.
- **Diagnóstico:** adaptar o texto de abertura e cada parágrafo-tópico da subseção, mantendo a mesma quantidade e a mesma função de cada tópico (Focos Registrados, Ações de Fiscalização, Contexto Estadual, Prognóstico de Risco, Trabalho de Campo).
- **Conclusão:** adaptar a síntese, a análise de vulnerabilidade, os impactos à saúde, a base legal e as recomendações à localidade informada, mantendo a lógica e a quantidade de parágrafos.
- **Anexo 1:** substituir a lista de localidades pela fornecida pelo usuário, inclusive quando vier como planilha (`.xlsx`/`.csv`) anexada. Preserve as duas tabelas de 4 colunas e a estrutura `Nº | Localidade | Nº | Localidade`; a quantidade de linhas acompanha o tamanho da lista fornecida. Avise o usuário se a mudança de tamanho alterar visivelmente a paginação.
- **Assinatura:** alterar nome e cargo apenas com dados e pedido do usuário; adaptar município-UF e ano.
- **Referências:** atualizar a estatística municipal, a URL de previsão do tempo, a URL do IBGE Cidades e as datas de acesso, conferindo em fonte oficial.
- **Demais conteúdos:** preservar. Não alterar assunto, órgão emissor, numeração de figuras, cabeçalhos, rodapés, logos ou paginação sem pedido explícito. Não mexer no texto do rótulo de confidencialidade, se presente.
- **Estilização:** preservar integralmente; faça as substituições dentro dos elementos existentes, mantendo as propriedades de parágrafo, execução e célula.

## Limitações da inspeção

A inspeção estrutural foi feita a partir do pacote OOXML. A inspeção visual página a página não foi concluída porque não havia conversor DOCX/PDF disponível no ambiente. O número de páginas nos metadados (9) não é garantidamente exato; confirme por renderização. Uma renderização completa é obrigatória antes de entregar qualquer relatório derivado quando houver um renderizador disponível.

## Gates de fidelidade

- Compare o SHA-256 do modelo antes e depois; deve permanecer idêntico.
- Preserve as 10 seções e a geometria de página, salvo alteração solicitada.
- Preserve as 2 tabelas do Anexo 1 com 4 colunas cada; a quantidade de linhas acompanha os dados fornecidos.
- Preserve os 2 cabeçalhos e as variantes de rodapé, as 3 imagens institucionais, o campo `PAGE` e as relações internas não editadas.
- Confirme que as três Figuras do corpo foram substituídas pelas imagens fornecidas, com legenda e fonte coerentes, e que nenhuma mantém o conteúdo ilustrativo de Acará-PA sem autorização.
- Confirme que município, UF, ano e data foram atualizados em todas as ocorrências pertinentes.
- Confirme que apenas os blocos textuais autorizados foram modificados e que nenhum dado factual de Acará-PA permaneceu como conteúdo do novo relatório.
- Confirme que nenhuma propriedade visual do template foi alterada.
