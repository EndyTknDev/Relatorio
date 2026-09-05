---
name: relatorio-saude-estiagem
description: Gera relatórios técnicos e planos municipais de resposta em saúde para seca e estiagem no formato DOCX, usando o template RELATORIO DA SAÚDE ESTIAGEM.docx e preservando sua estilização. Use somente para relatórios de saúde baseados nesse modelo; não use para pareceres clínicos individuais.
---

# Relatório de Saúde — Estiagem

Use `template/RELATORIO DA SAÚDE ESTIAGEM.docx` como autoridade de estrutura e aparência. Nunca edite diretamente qualquer arquivo da pasta `template/`.

## Regras obrigatórias compartilhadas

1. Preserve integralmente toda a estrutura e toda a estilização do template durante a cópia, o preenchimento, a substituição de imagens e a verificação. Não acrescente, remova, duplique, reorganize ou reconstrua seções, páginas, parágrafos, tabelas, linhas, células, cabeçalhos, rodapés, quebras, campos, imagens ou espaços reservados. Preserve estilos, fontes, tamanhos, cores, destaques, alinhamentos, recuos, espaçamentos, margens, bordas, paginação, ancoragens, dimensões e posições. Faça somente substituições localizadas nos elementos existentes. Se os dados não couberem na estrutura disponível, peça ao usuário que os ajuste; não altere a estrutura.
2. Antes de solicitar os dados, verifique se mensagens anteriores da conversa já contêm inputs relacionados a este documento. Se houver, não os reutilize silenciosamente: pergunte se o usuário deseja reaproveitá-los e apresente todos os valores candidatos no formato `Campo: valor`. Aguarde a confirmação e depois solicite apenas os dados ausentes ou substituições desejadas.
3. Antes de qualquer pesquisa externa, pergunte se o usuário prefere enviar o contexto, os dados e as fontes ou se autoriza o agente a pesquisar as informações. Apresente claramente as duas possibilidades e aguarde a escolha. Se o usuário enviar contexto, não faça pesquisa complementar sem autorização posterior. Se autorizar a pesquisa, siga os critérios de fontes desta skill.

## Preparação obrigatória

1. Resolva a raiz do plugin dois níveis acima desta skill.
2. Leia [references/modelo-saude-estiagem.md](references/modelo-saude-estiagem.md) para localizar os campos, tabelas e imagens.
3. Leia [references/regras-tecnicas-saude.md](references/regras-tecnicas-saude.md) antes de pesquisar ou redigir conteúdo de saúde.
4. Confirme que o SHA-256 do template corresponde ao registrado na referência. Se divergir, interrompa a geração e refaça a inspeção antes de atualizar a skill.
5. Antes de pesquisar, copiar ou editar o documento, solicite em um único bloco:
   - município, estado e UF;
   - data do relatório e período da estiagem;
   - número/ano do ofício, órgão emissor e destinatário;
   - nome oficial da Secretaria Municipal de Saúde, sigla e responsável pela assinatura;
   - situação observada, localidades e grupos populacionais afetados;
   - indicadores epidemiológicos disponíveis, período, fonte e distinção entre casos observados e riscos projetados;
   - objetivos, ações já executadas e ações previstas;
   - rede assistencial e retaguarda: unidades, códigos CNES, hospital de referência, leitos, UTI, equipamentos, equipes e fluxo de transporte, somente quando confirmados;
   - orçamento total e categorias de despesa;
   - listas aprovadas de medicamentos injetáveis, medicamentos orais/tópicos, soluções e materiais, incluindo apresentação, unidade e quantidade;
   - dados agregados de atendimento por unidade e os dois meses de comparação;
   - mapa e três fotografias, com local, data, fonte/autoria e contexto para as legendas;
   - três imagens institucionais do cabeçalho e endereço, CEP e e-mail do rodapé, ou confirmação para manter os elementos do modelo.
6. Não substitua informação ausente por dados do caso de Acará-PA nem pela data atual. Dados clínicos, orçamento, estoques, quantidades, capacidade hospitalar e atendimentos exigem confirmação da Secretaria de Saúde; pesquisa pública não substitui essa confirmação.

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
3. Atualize todas as ocorrências institucionais do cabeçalho e rodapé. Substitua as três imagens institucionais apenas pelos arquivos fornecidos e mantenha dimensões, posição, proporção e ancoragem. Atualize o e-mail visível e os dois destinos `mailto:` juntos.
4. Atualize o número do ofício, órgão, município, estado, data, destinatário, assunto e o título `PLANO DE RESPOSTA À ESTIAGEM – MUNICÍPIO DE <MUNICÍPIO>`.
5. Adapte somente os blocos abaixo, preservando a função, a ordem, a quantidade de parágrafos físicos e a extensão aproximada:
   - **Justificativa:** contexto local da estiagem, áreas e populações afetadas, água, calor, fumaça, alimentos e vulnerabilidades comprovadas.
   - **Impactos da estiagem na saúde:** mantenha a organização por água contaminada, doenças respiratórias, nutrição, vetores, calor e saúde mental, ajustando cada risco e conduta ao contexto e aos protocolos oficiais. Identifique claramente o que foi observado e o que é risco esperado.
   - **Objetivos:** ações educativas, preventivas, assistenciais e logísticas coerentes com o plano municipal.
   - **Estrutura de retaguarda hospitalar:** informe apenas capacidades confirmadas. Não mantenha menções a UTI, ventilação mecânica ou equipe multidisciplinar se não forem comprovadas.
   - **Capacidade de resposta e recursos necessários:** adapte as seis ações existentes sem criar compromissos não autorizados.
   - **Orçamento estimado:** use somente o total e as categorias fornecidos; confira a consistência entre total, itens e quantidades.
   - **Conclusão:** sintetize vulnerabilidades, resposta integrada e continuidade do cuidado, sem alegações clínicas ou operacionais não comprovadas.
6. Atualize as tabelas 0 a 6 somente com relações de medicamentos, soluções e materiais formalmente fornecidas ou confirmadas pela gestão de saúde/farmácia. Preserve as quatro colunas `ITEM | DESCRIÇÃO DOS PRODUTOS | UND | QTD` e todas as linhas existentes. Se a quantidade de itens não couber, peça ao usuário que ajuste ou agrupe a relação; não altere a estrutura.
7. Não trate as listas de Acará como seleção clínica padrão. Não calcule consumo, dosagem, estoque ou quantidade com base apenas em população ou em pesquisa genérica.
8. No anexo fotográfico, mantenha um mapa e três fotografias nos quatro slots existentes. Substitua somente por evidências do município informado ou por fonte verificável autorizada.
9. Para as três fotografias, use os parágrafos vazios de quebra de seção indicados na referência e acrescente a legenda `Figura <n> — <descrição objetiva>. Local: <local>. Data: <DD/MM/AAAA>. Fonte: <autoria/órgão>.` Não invente campos ausentes. O mapa deve conter título, período e fonte na própria arte ou em legenda compatível.
10. Atualize a tabela 7 com UF, código IBGE, município, unidade, CNES, tipo, descrição e os dois meses de atendimento fornecidos. Use apenas dados agregados e não inclua nomes ou informações de pacientes.
11. Atualize o encerramento e a assinatura somente com nome, cargo e demais dados fornecidos. Não mantenha identidade ou contatos de Acará em relatório de outro município.
12. Preserve estilos, fontes, tamanhos, negritos, sublinhados, alinhamentos, espaçamentos, margens, bordas das tabelas, cabeçalhos, rodapés, quebras, seções e posicionamento de imagens.
13. Faça substituições locais em `runs`, células, relações e mídias existentes. Não reconstrua o documento e não substitua `paragraph.text` ou `cell.text` de forma a apagar a formatação interna.
14. Faça apenas o que foi solicitado. Não acrescente seções, páginas, listas, indicadores ou recomendações não autorizadas.

## Verificação e entrega

- Confirme que o template original permanece com o mesmo SHA-256.
- Preserve 19 páginas, 21 seções, 172 parágrafos de nível superior, 8 tabelas, 3 imagens no cabeçalho e 4 imagens no corpo.
- Confirme que as tabelas 0–6 correspondem às listas aprovadas e que a tabela 7 corresponde aos dados agregados fornecidos.
- Verifique que não há dados residuais de Acará-PA, inclusive imagens, CNES, unidades, meses, contatos, orçamento ou capacidades hospitalares.
- Confirme que toda alegação epidemiológica informa período e fonte e que risco potencial não aparece como caso confirmado.
- Confirme que as três fotografias possuem legendas coerentes e que o mapa identifica título, período e fonte.
- Renderize e inspecione todas as páginas. Corrija texto cortado, sobreposição, tabela quebrada, imagem deformada, legenda deslocada ou página vazia indevida.
- Entregue sempre um único `.docx` com a estilização padrão do template em `outputs/<Mês> <Ano>/`.
- Nome sugerido: `RELATORIO SAUDE - ESTIAGEM - <MUNICIPIO> - <AAAA-MM-DD>.docx`.
- Nunca sobrescreva uma saída existente sem autorização explícita. Use sufixo de revisão quando necessário.
- Não deixe PDFs ou imagens de verificação dentro de `outputs/`.
