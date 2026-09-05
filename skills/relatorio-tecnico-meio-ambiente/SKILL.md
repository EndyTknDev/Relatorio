---
name: relatorio-tecnico-meio-ambiente
description: Gera relatórios técnicos DOCX da Secretaria Municipal de Meio Ambiente a partir do modelo preservado, adaptando município, UF, tipo do desastre (seca e estiagem, queimadas, enchentes, alagamentos, deslizamentos), ano, data, a caracterização do município, Apresentação, Precipitação e Temperatura, Justificativa, Diagnóstico, Conclusão, o Anexo 1 de localidades afetadas e as Referências, sem alterar a estilização. Use quando o usuário pedir um relatório técnico ambiental baseado nesse template; não use para outros tipos de documento.
---

# Relatório Técnico de Meio Ambiente

Use `template/RELATÓRIO TÉCNICO MEIO AMBIEMTE 2025 ATUALIZADO.docx` como autoridade de estrutura e aparência. Nunca edite um arquivo da pasta `template/` diretamente.

## Regras obrigatórias compartilhadas

1. Preserve integralmente toda a estrutura e toda a estilização do template durante a cópia, o preenchimento, a substituição de imagens e a verificação. Não acrescente, remova, duplique, reorganize ou reconstrua seções, páginas, parágrafos, tabelas, linhas, células, cabeçalhos, rodapés, quebras, campos, imagens ou espaços reservados. Preserve estilos, fontes, tamanhos, cores, destaques, alinhamentos, recuos, espaçamentos, margens, bordas, paginação, ancoragens, dimensões e posições. Faça somente substituições localizadas nos elementos existentes. Se os dados não couberem na estrutura disponível, peça ao usuário que os ajuste; não altere a estrutura.
2. Antes de solicitar os dados, verifique se mensagens anteriores da conversa já contêm inputs relacionados a este documento. Se houver, não os reutilize silenciosamente: pergunte se o usuário deseja reaproveitá-los e apresente todos os valores candidatos no formato `Campo: valor`. Aguarde a confirmação e depois solicite apenas os dados ausentes ou substituições desejadas.
3. Antes de qualquer pesquisa externa, pergunte se o usuário prefere enviar o contexto, os dados e as fontes ou se autoriza o agente a pesquisar as informações. Apresente claramente as duas possibilidades e aguarde a escolha. Se o usuário enviar contexto, não faça pesquisa complementar sem autorização posterior. Se autorizar a pesquisa, siga os critérios de fontes desta skill.

## Antes de começar

1. Resolva a raiz do plugin dois níveis acima desta skill.
2. Leia [references/regras-gerais.md](references/regras-gerais.md) para qualquer relatório.
3. Leia [references/modelo-meio-ambiente-2025.md](references/modelo-meio-ambiente-2025.md) para este modelo.
4. Confirme que o modelo ainda corresponde ao SHA-256 registrado na referência. Se divergir, trate-o como uma nova versão, refaça a inspeção e atualize a referência e o script antes de gerar documentos.
5. Antes de copiar ou editar o documento, pergunte obrigatoriamente, em um único bloco:
   - município;
   - estado/UF;
   - tipo do desastre ocorrido no município (por exemplo seca e estiagem, queimadas, enchentes, alagamentos, deslizamentos), que determina o enquadramento de todo o relatório;
   - ano de referência do relatório;
   - data do documento (por extenso e no formato AAAA-MM-DD);
   - secretaria responsável e órgão parceiro, apenas se diferentes do modelo (Secretaria Municipal de Meio Ambiente – SEMMA, em parceria com a Defesa Civil Municipal);
   - responsável pela assinatura e cargo, apenas se devam ser alterados;
   - imagens de cabeçalho e brasão, ou confirmação para manter as do modelo;
   - lista de localidades afetadas para o Anexo 1, se houver atualização.
6. Não deduza esses dados, não use valores do modelo (caso de Acará-PA, 2025, com foco em queimadas e estiagem) e não substitua a data ausente pela data atual. Se qualquer item obrigatório faltar, aguarde a resposta do usuário antes de iniciar a geração.
7. O modelo trata de queimadas e estiagem. Quando o tipo do desastre informado for outro, adapte o enquadramento do relatório a esse desastre em todas as seções, mantendo a estrutura, a ordem, os estilos e a quantidade de parágrafos, tabelas e seções do modelo. Não acrescente nem remova seções por causa da troca de desastre.

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
   - **Anexo 1 — localidades afetadas** — substitua a lista pelas localidades informadas pelo usuário. Preserve as duas tabelas, todas as linhas, as quatro colunas (`Nº | Localidade | Nº | Localidade`) e a numeração sequencial. Se a quantidade de localidades divergir da capacidade das tabelas do modelo, peça ao usuário que ajuste a lista; não acrescente nem remova linhas.
   - **Linha de data e bloco de assinatura** — `<Município>-<UF>, <data por extenso>.`, cargo, `<Município>-<UF>.` e ano. Só altere nome e cargo se o usuário fornecer.
   - **Referências** — atualize a estatística municipal, a URL de previsão do tempo do município, a URL do IBGE Cidades do município e as datas de acesso, conferindo cada endereço em fonte oficial.
6. Ajuste os títulos e as legendas dos anexos ao tipo do desastre informado. Não altere `Anexo 2` e `Anexo 3` nem qualquer outra seção fotográfica no fluxo padrão; só substitua fotografias se o usuário fornecer os arquivos e autorizar, preservando dimensões, proporção, âncora e posição.
7. Não altere nenhuma outra parte do documento, inclusive órgão emissor, numeração de figuras, cabeçalhos, rodapés, logos, campo de número de página, seções ou paginação, salvo pedido explícito do usuário.
8. Não invente fatos novos. Não mude números, valores, quantidades, ações, datas secundárias ou bases legais sem dados e pedido explícitos do usuário.
9. Preserve integralmente a estilização do template: estilos `Ttulo1`, `Ttulo2`, `Corpodetexto` e `TableParagraph`, fontes, tamanhos, cores, negritos, alinhamentos, espaçamentos, margens, quebras, seções, ancoragens e posições de imagens.
10. Faça substituições dentro das execuções (`runs`) e células existentes, reproduzindo suas propriedades. Não reconstrua o documento e não substitua `paragraph.text` ou `cell.text` de forma a apagar a formatação interna.
11. Antes da entrega, confira que apenas as alterações autorizadas foram realizadas e que nenhuma menção a queimadas ou estiagem sobrou quando o desastre informado for outro. Renderize todas as páginas para inspeção visual quando o ambiente permitir; se não permitir, conclua as verificações estruturais disponíveis e informe a limitação.
12. Confirme que o arquivo original da pasta `template/` permanece byte a byte inalterado.

## Saída

- Entregue sempre um arquivo `.docx` final dentro da pasta mensal correta, com a estilização padrão do template preservada.
- O nome sugerido é `RELATORIO TECNICO MEIO AMBIENTE - <DESASTRE> - <MUNICIPIO> - <AAAA-MM-DD>.docx`.
- Nunca sobrescreva uma saída existente sem autorização explícita. Diferencie revisões com sufixos como `- RASCUNHO`, `- REVISAO 01` ou `- FINAL`.
- Não deixe arquivos de inspeção, PDFs ou imagens de QA dentro de `outputs/`.
