# Regras gerais do relatório técnico de meio ambiente

## Integridade dos modelos

- Arquivos em `template/` são somente leitura e constituem a fonte oficial de estrutura e aparência.
- Todo novo relatório começa como uma cópia em `outputs/<Mês> <Ano>/`.
- Registre e compare o SHA-256 do modelo antes e depois do trabalho.
- Uma alteração intencional do modelo exige nova versão, nova inspeção e atualização da referência e do script correspondentes.

## Organização das saídas

- O padrão de pasta é `outputs/<Mês> <Ano>/`, por exemplo `outputs/Novembro 2025/`.
- O mês deve ser escrito em português, com inicial maiúscula e sem número prefixado.
- A data do documento informada pelo usuário determina a pasta. Não inicie o trabalho e não use a data atual enquanto município, estado/UF, tipo do desastre, ano de referência e data do documento não tiverem sido fornecidos.
- O nome sugerido é `RELATORIO TECNICO MEIO AMBIENTE - <DESASTRE> - <MUNICIPIO> - <AAAA-MM-DD>.docx`.
- Não sobrescreva arquivos existentes. Diferencie revisões com sufixos como `- RASCUNHO`, `- REVISAO 01` ou `- FINAL`, conforme o estágio informado pelo usuário.

## Conteúdo e linguagem

- Peça os dados em blocos sucessivos, não tudo de uma vez: primeiro identificação e enquadramento (município, estado/UF, tipo do desastre, ano de referência, data do documento); depois o conteúdo textual (caracterização do município, situação, diagnóstico, conclusão); depois o Anexo 1 (lista de localidades, aceita também como planilha `.xlsx`/`.csv`); e só por último as Figuras 1–3 e a identidade visual do cabeçalho/rodapé. Os cinco campos de identificação são obrigatórios antes de iniciar qualquer cópia.
- O tipo do desastre (por exemplo seca e estiagem, queimadas, enchentes, alagamentos, deslizamentos) varia conforme o município e define o enquadramento de todo o relatório. O modelo foi redigido para queimadas e estiagem; quando o desastre for outro, reescreva as menções ao fenômeno, causas, efeitos, indicadores e legendas para esse desastre, sem alterar estrutura, ordem, estilos, título nem a quantidade de parágrafos, tabelas e seções.
- Para qualquer campo obrigatório que o usuário confirmar que não pode fornecer no momento, use o marcador literal `[NECESSÁRIO INFORMAÇÃO]` no lugar do dado, sem inventar nem completar por suposição. Confirme essa substituição com o usuário antes de prosseguir e liste, na entrega, todos os campos marcados dessa forma.
- Faça apenas o que o usuário pedir. Para o fluxo padrão deste modelo, limite as mudanças a município, UF, tipo do desastre, ano, data, caracterização do município na Introdução, Apresentação, Precipitação e Temperatura, Justificativa, Diagnóstico, Conclusão, as Figuras 1 a 3, o Anexo 1 (localidades afetadas) e Referências.
- Use português brasileiro formal, claro, objetivo e institucional.
- Separe fato observado, estimativa, avaliação técnica, ação executada e recomendação.
- Preserve a grafia oficial de órgãos, municípios, programas, unidades de conservação e comunidades.
- Escreva siglas por extenso na primeira ocorrência, seguida da sigla entre parênteses.
- Mantenha datas, quantidades, coordenadas, percentuais e valores consistentes em todo o documento.
- Não invente pessoas atingidas, focos de queimada, hectares, prejuízos, ações, custos, localidades, coordenadas, população, datas, equipes, fotografias ou fundamentos legais. Não altere dados factuais do modelo sem input e pedido explícito.
- Dados geográficos e demográficos (área, população, regiões, coordenadas, distâncias) devem ser conferidos em fonte oficial, preferencialmente IBGE e o órgão estadual de estatística.
- Dados de queimadas e clima devem ser conferidos em fontes oficiais como INPE/Programa Queimadas, MapBiomas (Monitor do Fogo), INMET, secretaria estadual de meio ambiente e Defesa Civil.
- Leis, decretos, planos e outros atos normativos devem ser verificados em fonte oficial quando forem incluídos ou atualizados.

## Privacidade e evidências

- Inclua somente dados pessoais necessários à finalidade administrativa do relatório.
- Não exponha documentos pessoais, endereços completos ou informações sensíveis sem necessidade e autorização.
- As Figuras 1 a 3 do corpo (mapa, gráfico e mapa) são as únicas imagens de conteúdo do relatório e devem ser substituídas pelas fornecidas pelo usuário; não invente nem reutilize as do caso de Acará sem autorização. Não há mais anexo fotográfico no final do relatório — não peça nem insira fotografias de anexo por padrão; faça isso somente se o usuário pedir explicitamente e fornecer os arquivos, tratando como inserção nova.
- Quando houver legenda, identifique local, data e contexto sem expor pessoas vulneráveis desnecessariamente.

## Fidelidade e qualidade

- Preserve integralmente o sistema visual do modelo: estilos (`Heading 1`, `Heading 2`, `Body Text`, `Table Paragraph`), fontes, tamanhos, cores, destaques, alinhamentos, espaçamentos, tamanho e orientação de página, margens, cabeçalhos, rodapés, logos, campo de número de página, quebras, seções e posicionamento de imagens.
- Não normalize estilos, converta títulos, reconstrua o documento ou aplique melhorias visuais. A estilização do template não deve ser modificada.
- Evite mudanças em partes internas não relacionadas ao conteúdo solicitado.
- Revise todas as páginas renderizadas, especialmente as Figuras 1 a 3 e suas legendas, as quebras de seção, os cabeçalhos e os rodapés.
- Confirme que não existem texto cortado, sobreposição, imagens deformadas, páginas vazias indevidas ou conteúdo residual do caso de Acará-PA.
- Se a renderização não estiver disponível, execute auditorias estruturais e informe que a inspeção visual ficou pendente.

## Checklist de entrega

- O modelo original continua com o mesmo hash.
- A saída está na pasta de mês e ano correspondente à data do documento.
- Município, UF, tipo do desastre, ano, data e os blocos autorizados foram adaptados.
- O enquadramento do relatório corresponde ao desastre informado e não sobrou menção a queimadas ou estiagem quando o desastre for outro.
- Nenhuma parte fora do escopo solicitado foi modificada.
- Números, percentuais, coordenadas, população, datas, nomes e bases legais foram conferidos em fonte oficial.
- As duas tabelas do Anexo 1 mantiveram as 4 colunas; a quantidade de linhas corresponde à lista fornecida (inclusive quando veio por planilha).
- As Figuras 1 a 3 foram substituídas pelas imagens fornecidas, com legendas e fontes coerentes; nenhum anexo fotográfico foi adicionado sem pedido explícito.
- Todo campo marcado como `[NECESSÁRIO INFORMAÇÃO]` foi confirmado com o usuário e está listado na entrega.
- Cabeçalhos, rodapés, logos, campo de número de página, seções e paginação foram preservados.
- As Referências foram atualizadas para o município e conferidas.
- A saída não sobrescreveu outro arquivo.
