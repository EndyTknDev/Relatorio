---
name: relatorio-saude-estiagem
description: Gera relatórios técnicos e planos municipais de resposta em saúde no formato DOCX, usando o template RELATORIO DA SAÚDE ESTIAGEM.docx, preservando sua estilização e adaptando o título e o conteúdo à situação de saúde informada (estiagem ou outra emergência sanitária). Use somente para relatórios de saúde baseados nesse modelo; não use para pareceres clínicos individuais.
---

# Relatório de Saúde — Estiagem

Use `template/RELATORIO DA SAÚDE ESTIAGEM.docx` como autoridade de estrutura e aparência. Nunca edite diretamente qualquer arquivo da pasta `template/`.

## Regras obrigatórias compartilhadas

1. Preserve integralmente toda a estrutura e toda a estilização do template durante a cópia, o preenchimento, a substituição de imagens e a verificação. Não acrescente, remova, duplique, reorganize ou reconstrua seções, páginas, parágrafos, tabelas, linhas, células, cabeçalhos, rodapés, quebras, campos, imagens ou espaços reservados. Preserve estilos, fontes, tamanhos, cores, destaques, alinhamentos, recuos, espaçamentos, margens, bordas, paginação, ancoragens, dimensões e posições. Faça somente substituições localizadas nos elementos existentes. Se os dados não couberem na estrutura disponível, peça ao usuário que os ajuste; não altere a estrutura.
2. Antes de solicitar os dados, verifique se mensagens anteriores da conversa já contêm inputs relacionados a este documento. Se houver, não os reutilize silenciosamente: pergunte se o usuário deseja reaproveitá-los e apresente todos os valores candidatos no formato `Campo: valor`. Aguarde a confirmação e depois solicite apenas os dados ausentes ou substituições desejadas.
3. Antes de qualquer pesquisa externa, pergunte se o usuário prefere enviar o contexto, os dados e as fontes ou se autoriza o agente a pesquisar as informações. Apresente claramente as duas possibilidades e aguarde a escolha. Se o usuário enviar contexto, não faça pesquisa complementar sem autorização posterior. Se autorizar a pesquisa, siga os critérios de fontes desta skill.
4. Toda imagem exigida do usuário (cabeçalho, brasão, mapas, fotografias, capturas de tela) só admite duas respostas seguras: um arquivo fornecido para substituir a mídia existente, preservando quadro, dimensões, proporção e ancoragem; ou, quando a skill permitir, confirmação explícita para manter a mídia já presente na cópia. Se o usuário pedir para não usar nenhuma imagem nesse espaço — inclusive quando a skill não permitir manter a mídia do modelo por ela identificar outro município ou órgão —, não exclua o elemento gráfico, o quadro ou a seção para simular um espaço vazio. Explique a limitação, ofereça como única alternativa segura substituir o conteúdo da mídia por uma imagem neutra em branco do mesmo formato e proporção, sem texto, marca ou identidade de terceiros, e só prossiga depois que o usuário confirmar essa alternativa.

## Preparação obrigatória

1. Resolva a raiz do plugin dois níveis acima desta skill.
2. Leia [references/modelo-saude-estiagem.md](references/modelo-saude-estiagem.md) para localizar os campos, tabelas e imagens. Esta versão do modelo não tem mais anexo fotográfico.
3. Leia [references/regras-tecnicas-saude.md](references/regras-tecnicas-saude.md) antes de pesquisar ou redigir conteúdo de saúde.
4. Confirme que o SHA-256 do template corresponde ao registrado na referência. Se divergir, interrompa a geração e refaça a inspeção antes de atualizar a skill.
5. Peça os dados em blocos sucessivos — não solicite tudo de uma vez. Aguarde a resposta de cada bloco antes de abrir o próximo:
   1. **Identificação geral:** município, estado e UF; data do relatório; período da estiagem (ou da situação de saúde em questão); número/ano do ofício; órgão emissor (nome oficial da Secretaria Municipal de Saúde e sigla); destinatário.
   2. **Situação, indicadores e objetivos** (depois do bloco 1): situação observada; localidades e grupos populacionais afetados; indicadores epidemiológicos disponíveis — sempre com período, fonte e se são casos observados ou risco projetado. Dê exemplos ao usuário para deixar claro o que informar, como: "42 casos de diarreia aguda notificados na UBS Centro entre 01/09 e 20/09/2026, conforme boletim da vigilância epidemiológica municipal" ou "risco elevado de dengue projetado pela Sala de Situação estadual para outubro/2026"; objetivos do plano; ações já executadas e ações previstas.
   3. **Rede assistencial e demais dados institucionais** (depois do bloco 2): rede assistencial e retaguarda — unidades, códigos CNES, hospital de referência, leitos, UTI, equipamentos, equipes e fluxo de transporte, somente quando confirmados; responsável pela assinatura e cargo.
   4. **Orçamento e medicamentos** (depois do bloco 3): orçamento total e categorias de despesa; listas aprovadas de medicamentos injetáveis, orais/tópicos, soluções e materiais, com apresentação, unidade e quantidade. Aceite essa relação também como planilha `.xlsx` anexada, com colunas equivalentes a item, descrição, unidade e quantidade — a mesma estrutura das tabelas do modelo.
   5. **Identidade visual e contato** (somente depois que os quatro blocos acima estiverem completos, com ou sem marcadores `[NECESSÁRIO INFORMAÇÃO]` confirmados): três imagens institucionais do cabeçalho; endereço, CEP e e-mail do rodapé. Se o usuário não puder fornecer alguma dessas informações agora, não altere a estrutura nem o conteúdo do cabeçalho ou do rodapé — mantenha os elementos atuais da cópia e informe claramente que essa parte precisará ser editada manualmente no documento final antes do envio.
6. Para qualquer informação obrigatória dos blocos 1 a 4 que o usuário confirmar que não pode fornecer agora, substitua o campo correspondente pelo texto literal `[NECESSÁRIO INFORMAÇÃO]`, sem inventar nem completar com suposições. Confirme essa substituição com o usuário antes de prosseguir e, na entrega, liste todos os campos que ficaram marcados dessa forma.
7. Não substitua informação ausente por dados do caso de Acará-PA nem pela data atual — a única forma aceita de sinalizar um dado ausente é o marcador `[NECESSÁRIO INFORMAÇÃO]` combinado com a confirmação do usuário. Dados clínicos, orçamento, estoques, quantidades, capacidade hospitalar e atendimentos exigem confirmação da Secretaria de Saúde; pesquisa pública não substitui essa confirmação.

## Pesquisa e redação

- Consulte fontes oficiais e atuais para caracterizar riscos e orientar a resposta institucional: Ministério da Saúde, Vigidesastres, vigilância ambiental e epidemiológica, secretaria estadual e municipal de saúde, Defesa Civil e CNES.
- Use dados locais ou oficiais com período e fonte identificados. Não transforme risco potencial em ocorrência confirmada.
- O conteúdo clínico do modelo é apenas referência estrutural. Não reutilize automaticamente nomes de medicamentos ou esquemas terapêuticos como recomendação.
- Nas linhas de tratamento, redija condutas institucionais compatíveis com protocolos oficiais atuais e indique avaliação por profissional habilitado. Não produza prescrição individual.
- Não invente doenças, casos, óbitos, leitos, equipes, equipamentos, estoques, custos, unidades, CNES ou ações.
- Na entrega, forneça os links das fontes externas efetivamente usadas. Não crie uma nova seção de referências no DOCX sem solicitação expressa.

## Preenchimento do modelo

1. Normalize a data para `AAAA-MM-DD` e execute `scripts/criar_saida.py` para criar a cópia em `outputs/<Mês> <Ano>/`.
2. Trabalhe somente na cópia de saída.
3. Atualize todas as ocorrências institucionais do cabeçalho e rodapé com os dados do bloco 5. Substitua as três imagens institucionais apenas pelos arquivos fornecidos e mantenha dimensões, posição, proporção e ancoragem. Atualize o e-mail visível e os dois destinos `mailto:` juntos. Se o usuário não forneceu esses dados no bloco 5 e confirmou que fará isso depois, não altere cabeçalho, rodapé, endereço nem e-mail — mantenha os elementos da cópia como estão e reforce, na mensagem de entrega, que essa parte ainda depende de edição manual.
4. Atualize o número do ofício, órgão, município, estado, data, destinatário e assunto. Adapte o título à situação informada, pois nem sempre será estiagem: use `PLANO DE RESPOSTA À <SITUAÇÃO>` ou `PLANO DE RESPOSTA AO <SITUAÇÃO>` — conforme a concordância de gênero exigida pelo termo informado — seguido de ` – MUNICÍPIO DE <MUNICÍPIO>`. Mantenha a coerência entre o título e a situação descrita nos demais blocos (Justificativa, Impactos, etc.), adaptando as menções ao fenômeno onde for necessário para refletir a situação informada.
5. Adapte somente os blocos abaixo, preservando a função, a ordem, a quantidade de parágrafos físicos e a extensão aproximada:
   - **Justificativa:** contexto local da situação informada, áreas e populações afetadas, água, calor, fumaça, alimentos e vulnerabilidades comprovadas.
   - **Impactos na saúde:** mantenha a organização por água contaminada, doenças respiratórias, nutrição, vetores, calor e saúde mental, ajustando cada risco e conduta ao contexto e aos protocolos oficiais. Identifique claramente o que foi observado e o que é risco esperado.
   - **Objetivos:** ações educativas, preventivas, assistenciais e logísticas coerentes com o plano municipal.
   - **Estrutura de retaguarda hospitalar:** informe apenas capacidades confirmadas. Não mantenha menções a UTI, ventilação mecânica ou equipe multidisciplinar se não forem comprovadas.
   - **Capacidade de resposta e recursos necessários:** adapte as seis ações existentes sem criar compromissos não autorizados.
   - **Orçamento estimado:** use somente o total e as categorias fornecidos; confira a consistência entre total, itens e quantidades.
   - **Conclusão:** sintetize vulnerabilidades, resposta integrada e continuidade do cuidado, sem alegações clínicas ou operacionais não comprovadas.
6. Atualize as tabelas de medicamentos, soluções e materiais somente com relações formalmente fornecidas ou confirmadas pela gestão de saúde/farmácia, inclusive quando vierem como planilha `.xlsx` anexada. Preserve em todas elas a estrutura de quatro colunas `ITEM | DESCRIÇÃO DOS PRODUTOS | UND | QTD`; a quantidade de linhas — e, quando necessário, a quantidade de tabelas/páginas dessa seção — acompanha o tamanho da relação fornecida. Não trunque itens nem force o conteúdo do usuário a caber nas linhas do modelo para preservar a paginação original; avise o usuário se a mudança de tamanho alterar visivelmente a paginação.
7. Não trate as listas de Acará como seleção clínica padrão. Não calcule consumo, dosagem, estoque ou quantidade com base apenas em população ou em pesquisa genérica.
8. Não inclua mapa nem fotografias por padrão — o anexo fotográfico foi removido desta versão do modelo. Se o usuário pedir explicitamente para incluir mapa e/ou fotografias, trate como uma inserção nova a negociar com ele (posição, tamanho e legenda no formato `Figura <n> — <descrição objetiva>. Local: <local>. Data: <DD/MM/AAAA>. Fonte: <autoria/órgão>.`, sem inventar campos ausentes) e informe que essa adição altera a estrutura do modelo padrão.
9. Antes de preencher a seção `ANEXO — PLANILHA DE ATENDIMENTO NAS UNIDADES`, se os dados agregados de atendimento ainda não tiverem sido fornecidos, pergunte ao usuário se ele possui essa tabela. Informe a estrutura de colunas esperada (`UF | IBGE | Município | Unidade de Saúde - CNES | Tipo Unidade | Desc Unidade | <mês/ano 1> | <mês/ano 2>`) para orientar o envio. Se o usuário pedir para excluir essa seção, remova a tabela e o título/subtítulo do anexo, mantendo apenas o parágrafo de encerramento ("Na certeza de contar com a vossa compreensão...") e o espaço reservado para a assinatura. Se os dados forem fornecidos, atualize a tabela com UF, código IBGE, município, unidade, CNES, tipo, descrição e os dois meses de comparação informados. Use apenas dados agregados e não inclua nomes ou informações de pacientes.
10. Atualize o encerramento e a assinatura somente com nome, cargo e demais dados fornecidos. Não mantenha identidade ou contatos de Acará em relatório de outro município.
11. Preserve estilos, fontes, tamanhos, negritos, sublinhados, alinhamentos, espaçamentos, margens, bordas das tabelas, cabeçalhos, rodapés, quebras, seções e posicionamento de imagens.
12. Faça substituições locais em `runs`, células, relações e mídias existentes. Não reconstrua o documento e não substitua `paragraph.text` ou `cell.text` de forma a apagar a formatação interna.
13. Faça apenas o que foi solicitado. Não acrescente seções, páginas, listas, indicadores ou recomendações não autorizadas.

## Verificação e entrega

- Confirme que o template original permanece com o mesmo SHA-256.
- Preserve 16 seções, 155 parágrafos de nível superior, 8 tabelas e 3 imagens no cabeçalho, salvo alteração autorizada (inclusão de anexo fotográfico ou exclusão da planilha de atendimento, por exemplo). Nenhuma imagem de corpo é esperada por padrão nesta versão.
- Confirme que as tabelas de medicamentos, soluções e materiais correspondem às listas aprovadas — inclusive quando vieram por planilha `.xlsx` — e que a tabela de atendimento, quando mantida, corresponde aos dados agregados fornecidos; a quantidade de linhas de cada tabela acompanha os dados recebidos.
- Verifique que não há dados residuais de Acará-PA, inclusive imagens, CNES, unidades, meses, contatos, orçamento ou capacidades hospitalares.
- Confirme que toda alegação epidemiológica informa período e fonte e que risco potencial não aparece como caso confirmado.
- Confirme que todo campo marcado como `[NECESSÁRIO INFORMAÇÃO]` foi de fato confirmado com o usuário e está listado na mensagem de entrega, e que nenhum outro campo obrigatório ficou vazio ou com dado inventado.
- Renderize e inspecione todas as páginas geradas. Corrija texto cortado, sobreposição, tabela quebrada, imagem deformada ou página vazia indevida.
- Entregue sempre um único `.docx` com a estilização padrão do template em `outputs/<Mês> <Ano>/`.
- Nome sugerido: `RELATORIO SAUDE - <SITUAÇÃO> - <MUNICIPIO> - <AAAA-MM-DD>.docx`.
- Nunca sobrescreva uma saída existente sem autorização explícita. Use sufixo de revisão quando necessário.
- Não deixe PDFs ou imagens de verificação dentro de `outputs/`.
