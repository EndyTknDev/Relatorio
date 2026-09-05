# Modelo: Relatório da Saúde — Estiagem

## Referência preservada

- Caminho na raiz do plugin: `template/RELATORIO DA SAÚDE ESTIAGEM.docx`. O nome pode estar armazenado em forma Unicode decomposta; localize o arquivo pelo hash.
- SHA-256: `E9C60D1AF3C91C7E5FA46ABC2F69702DE0F397A3E8288EB1711827C16E044FDB`.
- Tamanho observado: `106.628` bytes.
- Caso do modelo: Acará, Pará (PA), ofício nº 1588/2025, datado de 17 de novembro de 2025.
- O arquivo é somente leitura. Toda geração começa por uma cópia.
- Esta é uma nova versão do modelo (o anexo fotográfico foi removido pelo responsável pela skill). O hash, o tamanho e toda esta referência foram atualizados a partir dela; se o hash divergir novamente no futuro, trate como mais uma nova versão e repita a inspeção antes de gerar saídas.

## Estrutura visual

- 16 seções, todas em orientação retrato: 3 contínuas (a primeira e as duas que sucedem os grupos de tabelas de medicamentos) e 13 com quebra para nova página.
- 155 parágrafos de nível superior no corpo (fora de tabelas) e 8 tabelas.
- O pacote não declara de forma confiável o número de páginas nos metadados; confirme a contagem real por renderização antes de citar um total ao usuário.
- Estilos utilizados: `Normal`, `Body Text`, `List Paragraph`, `Heading 1` a `Heading 5` e `Table Paragraph`, com formatação direta adicional. Nesta versão os identificadores internos dos estilos estão em inglês (`BodyText`, `Heading4`, `Heading5`, `ListParagraph`, `TableParagraph`); o nome visível no Word continua o mesmo.
- Os títulos correntes usam principalmente `Heading 4` e `Heading 5`. O separador do anexo final usa `Heading 1` seguido de `Heading 2` (título do anexo) e depois `Heading 3` (subtítulo da seção de atendimento).
- Um cabeçalho herdado por todas as seções contém três imagens institucionais (`image1.png`, `image2.png`, `image3.png`) e texto central.
- Rodapé: a seção 1 declara três variantes (`even`, `default`/ímpar e `first`). Confirme com o usuário se essas três variantes devem permanecer distintas ou se a distinção entre página par/ímpar/primeira foi introduzida sem intenção ao editar o arquivo — isso muda o que aparece em cada página e vale a pena revisar antes de preencher. O rodapé padrão contém endereço, CEP, município/UF e e-mail, com dois relacionamentos externos `mailto:` para o mesmo endereço.
- O arquivo carrega um rótulo de confidencialidade do Microsoft Purview (`docMetadata/LabelInfo.xml`) que imprime o texto "Classified - Confidential" nos rodapés. Esse texto não faz parte do conteúdo do relatório; não o trate como dado a preencher e não o remova por conta própria — ele é controlado pela política de rótulos do Microsoft 365 do usuário.
- Não há comentários, alterações controladas, campos de mala direta ou controles de conteúdo. Os rodapés usam campo `PAGE` para numeração automática.
- **O anexo fotográfico (separador, mapa de focos/eventos e três fotografias) foi removido desta versão do modelo.** Não peça mapa nem fotografias por padrão.

## Ordem das páginas

1. Ofício, assunto, plano, Justificativa e Impactos da Estiagem na Saúde.
2. Objetivos e Estrutura de Retaguarda Hospitalar.
3. Capacidade de Resposta, Recursos Necessários e Orçamento Estimado.
4. Conclusão.
5. Medicamentos injetáveis (2 tabelas).
6. Medicamentos orais e tópicos (3 tabelas).
7. Soluções e materiais (2 tabelas).
8. Separador `ANEXO` / `PLANILHA DE ATENDIMENTO NAS UNIDADES`.
9. Atendimentos agregados por unidade (1 tabela), encerramento e assinatura.

Não existe mais separador nem páginas de anexo fotográfico entre os itens 4 e 5. Localize os elementos pelo texto do título e pela ordem relativa, não por número fixo de página ou de parágrafo — esta versão reindexou praticamente todos os parágrafos em relação à anterior.

## Mapa de substituições textuais

Localize cada bloco pelo título ou pelo texto de abertura, na ordem abaixo, e não por número de parágrafo (a reindexação desta versão tornou marcadores fixos pouco confiáveis):

- **Ofício:** número e ano do ofício, sigla do órgão, município, estado e data.
- **PARA:** destinatário.
- **Assunto:** assunto, desastre/situação observada, município e estado.
- **Título do plano** (`PLANO DE RESPOSTA À/AO <situação> – MUNICÍPIO DE <MUNICÍPIO>`).
- **Justificativa:** dois parágrafos de contexto local.
- **Impactos da estiagem na saúde:** bloco extenso dividido pelos subtítulos Doenças Transmitidas pela Água Contaminada, Doenças Respiratórias, Doenças Relacionadas à Má Nutrição, Doenças Transmitidas por Vetores, Doenças Relacionadas ao Calor e Problemas de Saúde Mental. Cada risco tem um parágrafo de descrição e um parágrafo de "Tratamento".
- **Objetivos.**
- **Estrutura de Retaguarda Hospitalar.**
- **Capacidade de Resposta e Recursos Necessários.**
- **Orçamento Estimado.**
- **Conclusão.**
- **Tabelas de medicamentos e materiais** (ver seção "Tabelas").
- **Anexo — Planilha de Atendimento nas Unidades** (ver seção "Tabelas") e o parágrafo de encerramento que a segue.
- **Fecho:** "Atenciosamente," e a assinatura (`Secretário Municipal de Saúde`, a adaptar conforme o responsável informado).
- **Cabeçalho:** município, Secretaria Municipal de Saúde e Gabinete do Secretário.
- **Rodapé:** endereço, CEP, município/UF, e-mail visível e dois destinos `mailto:`. Não mexa no texto do rótulo de confidencialidade, se presente.

## Tabelas

- **Tabelas 0 e 1:** 24 itens de medicamentos injetáveis (itens 1–24, divididos entre as duas tabelas); quatro colunas `ITEM | DESCRIÇÃO DOS PRODUTOS | UND | QTD`.
- **Tabelas 2 a 4:** medicamentos orais e tópicos, itens 1–64; mesmas quatro colunas. A numeração do modelo contém lacunas (por exemplo, salta de 46 para 49) e não constitui lista clínica oficial.
- **Tabelas 5 e 6:** soluções parenterais e materiais, itens 1–10; mesmas quatro colunas. A primeira linha da tabela 6 continua a descrição iniciada na última linha da tabela 5 — preserve essa quebra de linha física ao editar.
- **Tabela 7:** 16 linhas e 8 colunas: `Uf | Ibge | Municipio | Unidade de Saúde - CNES | Tipo Unidade | Desc Unidade | SET/2025 | AGO/2025`.
- As tabelas 0–6 são editáveis somente com listas e quantidades aprovadas pela gestão de saúde/farmácia. A tabela 7 é editável somente com dados agregados de atendimento e códigos confirmados.
- Preserve grades, larguras, bordas, repetição visual, alinhamentos e continuidade entre páginas. **A estrutura de colunas (`ITEM | DESCRIÇÃO DOS PRODUTOS | UND | QTD` e as 8 colunas da tabela 7) é fixa; a quantidade de linhas não é** — se a relação fornecida pelo usuário tiver mais ou menos itens que o modelo, ajuste o número de linhas mantendo as colunas, os cabeçalhos e a formatação de cada célula, e confirme com o usuário quando a diferença for grande o suficiente para mudar visivelmente a paginação.
- Quando a relação de medicamentos vier como planilha (`.xlsx`) anexada pelo usuário, use-a como fonte de dados apenas: leia item, descrição, unidade e quantidade de cada linha e escreva-os nas tabelas do DOCX no mesmo layout de quatro colunas do modelo. Não anexe nem incorpore o arquivo `.xlsx` original dentro do `.docx`.

## Sistema de página

- Tamanho: `7.562.850 × 10.693.400` EMU (`8,27 × 11,69 pol.`).
- Margens: superior `1,81 pol.`, direita `0,39 pol.`, inferior `0,76 pol.` e esquerda `0,49 pol.`.
- Distâncias: cabeçalho `0,42 pol.` e rodapé `0,64 pol.`.
- Preserve as 16 seções e a herança do cabeçalho e das variantes de rodapé descritas acima.

## Gates de fidelidade

- O template mantém o hash `E9C60D1AF3C91C7E5FA46ABC2F69702DE0F397A3E8288EB1711827C16E044FDB`.
- A saída mantém 16 seções, 155 parágrafos de nível superior e 8 tabelas, salvo alteração autorizada (inclusive a inclusão de anexo fotográfico, se pedida explicitamente).
- Permanecem três imagens institucionais no cabeçalho. Nenhuma imagem de corpo (mapa/fotografia) é esperada por padrão nesta versão.
- O e-mail visível do rodapé coincide com os dois destinos `mailto:`.
- As tabelas de medicamentos e materiais mantêm as quatro colunas do modelo, e a tabela de atendimento mantém as oito; a quantidade de linhas corresponde à lista fornecida pelo usuário.
- Nenhum conteúdo do caso de Acará permanece indevidamente em relatório de outro município.
- Renderize e inspecione todas as páginas geradas antes da entrega, mesmo sem um número de páginas de referência confiável nos metadados.
