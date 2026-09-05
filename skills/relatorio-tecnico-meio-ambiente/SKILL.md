---
name: relatorio-tecnico-meio-ambiente
description: Gera relatórios técnicos DOCX da Secretaria Municipal de Meio Ambiente a partir do modelo preservado, adaptando município, UF, tipo do desastre (seca e estiagem, queimadas, enchentes, alagamentos, deslizamentos), ano, data, a caracterização do município, Apresentação, Precipitação e Temperatura, Justificativa, Diagnóstico, Conclusão, as Figuras 1 a 3, o Anexo 1 de localidades afetadas e as Referências, sem alterar a estilização. Use quando o usuário pedir um relatório técnico ambiental baseado nesse template; não use para outros tipos de documento.
---

# Relatório Técnico de Meio Ambiente

Use `template/RELATÓRIO TÉCNICO MEIO AMBIEMTE 2025 ATUALIZADO.docx` como autoridade de estrutura e aparência. Nunca edite um arquivo da pasta `template/` diretamente.

## Regras padrão obrigatórias

Antes de qualquer ação, leia e aplique integralmente [as regras padrão do plugin](../../rules/regras-padrao.md). As regras específicas abaixo complementam esse arquivo e não dispensam nenhuma de suas exigências.

## Antes de começar

1. Resolva a raiz do plugin dois níveis acima desta skill.
2. Leia [references/regras-gerais.md](references/regras-gerais.md) para qualquer relatório.
3. Leia [references/modelo-meio-ambiente-2025.md](references/modelo-meio-ambiente-2025.md) para este modelo. Esta versão não tem mais anexo fotográfico no final do relatório.
4. Confirme que o modelo ainda corresponde ao SHA-256 registrado na referência. Se divergir, trate-o como uma nova versão, refaça a inspeção e atualize a referência e o script antes de gerar documentos.
5. Peça os dados em blocos sucessivos — não solicite tudo de uma vez. Aguarde a resposta de cada bloco antes de abrir o próximo:
   1. **Identificação e enquadramento** (obrigatório antes de qualquer cópia): município; estado/UF; tipo do desastre ocorrido no município (por exemplo seca e estiagem, queimadas, enchentes, alagamentos, deslizamentos), que determina o enquadramento de todo o relatório; ano de referência; data do documento (por extenso e no formato AAAA-MM-DD).
   2. **Dados institucionais** (depois do bloco 1, apenas se diferentes do modelo): secretaria responsável e órgão parceiro (o modelo usa Secretaria Municipal de Meio Ambiente – SEMMA, em parceria com a Defesa Civil Municipal); responsável pela assinatura e cargo.
   3. **Anexo 1 — localidades afetadas** (depois do bloco 2): lista de localidades, como texto ou como planilha (`.xlsx`/`.csv`) anexada.
   4. **Figuras e identidade visual** (por último, depois dos três blocos acima): arquivo para a Figura 1 (mapa de localização do município), a Figura 2 (gráfico de precipitação e temperatura) e a Figura 3 (mapa de focos ou eventos do desastre informado); imagens institucionais do cabeçalho, ou confirmação para manter as do modelo. Peça as três figuras como entradas obrigatórias — elas são o conteúdo visual do relatório.
6. Para qualquer informação obrigatória dos blocos 1 a 3 que o usuário confirmar que não pode fornecer agora, substitua o campo correspondente pelo texto literal `[NECESSÁRIO INFORMAÇÃO]`, sem inventar nem completar com suposições. Confirme essa substituição com o usuário antes de prosseguir e, na entrega, liste todos os campos que ficaram marcados dessa forma. Isso não se aplica às Figuras 1 a 3, que são obrigatórias e seguem a regra compartilhada 4 quando o usuário não puder fornecê-las.
7. Não deduza esses dados, não use valores do modelo (caso de Acará-PA, 2025, com foco em queimadas e estiagem) e não substitua a data ausente pela data atual. Se qualquer item obrigatório do bloco 1 faltar, aguarde a resposta do usuário antes de iniciar a geração.
8. O modelo trata de queimadas e estiagem. Quando o tipo do desastre informado for outro, adapte o enquadramento do relatório a esse desastre em todas as seções, mantendo a estrutura, a ordem, os estilos e a quantidade de parágrafos, tabelas e seções do modelo. Não acrescente nem remova seções por causa da troca de desastre.

## Pesquisa de apoio

- Antes de redigir cada seção principal, pesquise o município e o contexto do tipo de desastre informado em fontes oficiais.
- Priorize prefeitura e secretaria municipal de meio ambiente, secretaria estadual de meio ambiente, IBGE, órgão estadual de estatística, Defesa Civil e serviços meteorológicos (INMET, Climatempo). Para seca e estiagem ou queimadas, consulte também INPE/Programa Queimadas (BDQueimadas) e MapBiomas (Monitor do Fogo); para enchentes, alagamentos e deslizamentos, consulte órgãos hidrológicos e de monitoramento (ANA, CPRM/SGB, CEMADEN) e boletins de chuva.
- Use a pesquisa para validar e contextualizar os dados fornecidos pelo usuário, sem substituir o relato municipal e sem criar alegações não comprovadas.
- Não invente números, percentuais, hectares, focos, coordenadas, população, distâncias, datas, ações ou bases legais. Não reaproveite como fatos os dados de Acará-PA presentes no modelo.
- Na entrega, apresente ao usuário as fontes externas efetivamente usadas. Não adicione ao DOCX uma seção nova de fontes além da lista de Referências já existente, salvo pedido explícito.

## Fluxo de trabalho

1. Use a data do documento para criar o destino `outputs/<Mês> <Ano>/`, com o mês em português e inicial maiúscula. Use `scripts/criar_saida.py` para preparar a cópia do modelo.
2. Trabalhe somente na cópia de saída.
3. Substitua município, estado/UF, ano e data em todas as ocorrências pertinentes, inclusive cabeçalhos, rodapés, legendas de figuras, linha de data, bloco de assinatura e Referências.
4. Ajuste o enquadramento do relatório ao tipo do desastre informado. O modelo é escrito para queimadas e estiagem; quando o desastre for outro, substitua as menções ao fenômeno, seus efeitos, causas, indicadores e legendas de figuras pelos termos e conteúdos correspondentes ao desastre informado (por exemplo enchentes, alagamentos ou deslizamentos), sem mudar a estrutura, a ordem das seções, os estilos, o título do documento nem a quantidade de parágrafos, tabelas e seções.
5. Adapte somente os blocos textuais abaixo, preservando a estrutura, a ordem, o tom institucional, a quantidade de parágrafos físicos e a extensão aproximada do modelo:
   - **Introdução** — caracterização do município: estado, área territorial (km² e percentual do estado), regiões (integração, meso e microrregião, regiões geográficas intermediária e imediata), distância até a capital, coordenadas geográficas da sede e população estimada, cada dado com a fonte correspondente.
   - **Apresentação** — objetivo do relatório, secretaria responsável, órgão parceiro, município, ano e o tipo do desastre monitorado.
   - **Precipitação e Temperatura** — regime de chuvas e temperaturas do município no ano, meses relevantes para o desastre informado (de menor precipitação para seca e queimadas; de maior precipitação para enchentes e deslizamentos), faixas de temperatura, fonte, e a nota sobre médias climatológicas e série histórica.
   - **Justificativa** — histórico do desastre informado no município; contexto estadual com indicadores e fontes pertinentes; fatores locais que agravam o desastre; chamadas às figuras. Na subseção conceitual (`Estiagem x Seca dos Rios` no modelo), preserve a função de distinguir conceitos correlatos, adaptando-a ao desastre informado quando necessário e mantendo menções geográficas coerentes.
   - **Diagnóstico** — diagnóstico do município no ano e a subseção `Diagnóstico da Situação em <Município> (<ano>):`, mantendo a mesma quantidade e a mesma função dos parágrafos-tópico do modelo (no modelo: Focos Registrados, Ações de Fiscalização, Contexto Estadual, Prognóstico de Risco, Trabalho de Campo), reescritos para o desastre informado.
   - **Conclusão** — síntese dos impactos ecológicos, sociais e econômicos; correlação com os fatores que originam o desastre; vulnerabilidade socioambiental do município; impactos à saúde pública; base legal e planos aplicáveis; fecho com recomendações. Mantenha a quantidade de parágrafos do modelo.
   - **Anexo 1 — localidades afetadas** — substitua a lista pelas localidades informadas pelo usuário, inclusive quando vier como planilha `.xlsx`/`.csv`. Preserve as duas tabelas e a estrutura de quatro colunas (`Nº | Localidade | Nº | Localidade`); a quantidade de linhas acompanha o tamanho da lista fornecida. Avise o usuário se a mudança de tamanho alterar visivelmente a paginação.
   - **Linha de data e bloco de assinatura** — `<Município>-<UF>, <data por extenso>.`, cargo, `<Município>-<UF>.` e ano. Só altere nome e cargo se o usuário fornecer.
   - **Referências** — atualize a estatística municipal, a URL de previsão do tempo do município, a URL do IBGE Cidades do município e as datas de acesso, conferindo cada endereço em fonte oficial.
6. Substitua as Figuras 1, 2 e 3 do corpo pelas imagens fornecidas pelo usuário no bloco 4 (mapa de localização, gráfico climático e mapa de focos/eventos, respectivamente — ver a tabela de relações em [references/modelo-meio-ambiente-2025.md](references/modelo-meio-ambiente-2025.md)). Troque apenas o conteúdo binário de cada mídia, preservando a relação, o quadro, a posição, a proporção e a ancoragem existentes. Ajuste a legenda ("Figura N. ...") e a linha "Fonte: ..." de cada uma para descrever a imagem e a origem informadas pelo usuário, sem inventar dado algum sobre elas.
7. Não há mais anexo fotográfico no final do relatório (antigos Anexo 2 e Anexo 3). Não peça nem insira fotografias de anexo por padrão. Se o usuário pedir explicitamente para reintroduzi-las, trate como uma inserção nova a negociar com ele (posição, tamanho, legenda), deixando claro que isso altera a estrutura do modelo atual.
8. Não altere nenhuma outra parte do documento, inclusive órgão emissor, numeração de figuras, cabeçalhos, rodapés, logos, campo de número de página, seções ou paginação, salvo pedido explícito do usuário. Não mexa no texto do rótulo de confidencialidade do rodapé, se presente.
9. Não invente fatos novos. Não mude números, valores, quantidades, ações, datas secundárias ou bases legais sem dados e pedido explícitos do usuário.
10. Preserve integralmente a estilização do template: estilos `Heading 1`, `Heading 2`, `Body Text` e `Table Paragraph`, fontes, tamanhos, cores, negritos, alinhamentos, espaçamentos, margens, quebras, seções, ancoragens e posições de imagens.
11. Faça substituições dentro das execuções (`runs`) e células existentes, reproduzindo suas propriedades. Não reconstrua o documento e não substitua `paragraph.text` ou `cell.text` de forma a apagar a formatação interna.
12. Antes da entrega, confira que apenas as alterações autorizadas foram realizadas, que nenhuma menção a queimadas ou estiagem sobrou quando o desastre informado for outro, e que as três Figuras e suas legendas correspondem às imagens fornecidas. Renderize todas as páginas para inspeção visual quando o ambiente permitir; se não permitir, conclua as verificações estruturais disponíveis e informe a limitação.
13. Confirme que o arquivo original da pasta `template/` permanece byte a byte inalterado.

## Saída

- Entregue sempre um arquivo `.docx` final dentro da pasta mensal correta, com a estilização padrão do template preservada.
- O nome sugerido é `RELATORIO TECNICO MEIO AMBIENTE - <DESASTRE> - <MUNICIPIO> - <AAAA-MM-DD>.docx`.
- Nunca sobrescreva uma saída existente sem autorização explícita. Diferencie revisões com sufixos como `- RASCUNHO`, `- REVISAO 01` ou `- FINAL`.
- Não deixe arquivos de inspeção, PDFs ou imagens de QA dentro de `outputs/`.
