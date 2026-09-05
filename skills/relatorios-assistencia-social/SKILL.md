---
name: relatorios-assistencia-social
description: Gera relatórios DOCX de assistência social sobre seca e estiagem a partir do modelo preservado, adaptando município, estado, data, Situação geral, Diagnóstico Preliminar e Conclusão sem alterar a estilização. Use quando o usuário pedir um relatório baseado nesse template; não use para outros tipos de documento.
---

# Relatórios de Assistência Social

Use os modelos da pasta `template/` como autoridade de estrutura e aparência. Nunca edite um arquivo dessa pasta diretamente.

## Regras obrigatórias compartilhadas

1. Preserve integralmente toda a estrutura e toda a estilização do template durante a cópia, o preenchimento, a substituição de imagens e a verificação. Não acrescente, remova, duplique, reorganize ou reconstrua seções, páginas, parágrafos, tabelas, linhas, células, cabeçalhos, rodapés, quebras, campos, imagens ou espaços reservados. Preserve estilos, fontes, tamanhos, cores, destaques, alinhamentos, recuos, espaçamentos, margens, bordas, paginação, ancoragens, dimensões e posições. Faça somente substituições localizadas nos elementos existentes. Se os dados não couberem na estrutura disponível, peça ao usuário que os ajuste; não altere a estrutura.
2. Antes de solicitar os dados, verifique se mensagens anteriores da conversa já contêm inputs relacionados a este documento. Se houver, não os reutilize silenciosamente: pergunte se o usuário deseja reaproveitá-los e apresente todos os valores candidatos no formato `Campo: valor`. Aguarde a confirmação e depois solicite apenas os dados ausentes ou substituições desejadas.
3. Antes de qualquer pesquisa externa, pergunte se o usuário prefere enviar o contexto, os dados e as fontes ou se autoriza o agente a pesquisar as informações. Apresente claramente as duas possibilidades e aguarde a escolha. Se o usuário enviar contexto, não faça pesquisa complementar sem autorização posterior. Se autorizar a pesquisa, siga os critérios de fontes desta skill.
4. Toda imagem exigida do usuário (cabeçalho, brasão, mapas, fotografias, capturas de tela) só admite duas respostas seguras: um arquivo fornecido para substituir a mídia existente, preservando quadro, dimensões, proporção e ancoragem; ou, quando a skill permitir, confirmação explícita para manter a mídia já presente na cópia. Se o usuário pedir para não usar nenhuma imagem nesse espaço — inclusive quando a skill não permitir manter a mídia do modelo por ela identificar outro município ou órgão —, não exclua o elemento gráfico, o quadro ou a seção para simular um espaço vazio. Explique a limitação, ofereça como única alternativa segura substituir o conteúdo da mídia por uma imagem neutra em branco do mesmo formato e proporção, sem texto, marca ou identidade de terceiros, e só prossiga depois que o usuário confirmar essa alternativa.

## Antes de começar

1. Resolva a raiz do plugin dois níveis acima desta skill.
2. Leia [references/regras-gerais.md](references/regras-gerais.md) para qualquer relatório.
3. Para o modelo `RELATORIO ASSISTÊNCIA SOCIAL SECA E ESTIAGEM 2025.docx`, leia também [references/modelo-seca-estiagem-2025.md](references/modelo-seca-estiagem-2025.md). Esta versão não tem mais relatório fotográfico no final do documento.
4. Confirme que o modelo ainda corresponde ao hash registrado na referência. Se divergir, trate-o como uma nova versão e faça outra inspeção antes de gerar documentos.
5. Antes de copiar ou editar o documento, pergunte obrigatoriamente, em um único bloco:
   - município;
   - estado;
   - data do relatório.
6. Para qualquer um desses três campos que o usuário confirmar que não pode fornecer agora, substitua o dado pelo texto literal `[NECESSÁRIO INFORMAÇÃO]`, sem inventar nem completar por suposição. Confirme essa substituição com o usuário antes de prosseguir e liste, na entrega, os campos marcados dessa forma.
7. Não deduza esses três dados, não use valores do modelo e não substitua a data ausente pela data atual. Se qualquer item estiver faltando e sem confirmação de placeholder, aguarde a resposta do usuário antes de iniciar a geração.

## Fluxo de trabalho

1. Use a data informada para criar o destino `outputs/<Mês> <Ano>/`, com o mês em português e inicial maiúscula. Use `scripts/criar_saida.py` para preparar uma cópia do modelo quando possível.
2. Trabalhe somente na cópia de saída.
3. Substitua município, estado e data em todas as ocorrências pertinentes do relatório.
4. Adapte somente estes blocos textuais, preservando a estrutura, o tom institucional e a extensão aproximada do modelo:
   - `Situação Geral`;
   - `Diagnóstico Preliminar`;
   - `Conclusão`.
5. Em `Situação Geral`, contextualize o município e o estado informados usando redação semelhante à do modelo.
6. Em `Diagnóstico Preliminar`, adapte a redação à localidade informada e mantenha a função técnica da seção conforme o modelo.
7. Em `Conclusão`, adapte a síntese e as recomendações à localidade informada, mantendo a lógica do modelo.
8. Não altere nenhuma outra parte do documento, inclusive assinatura, assunto, interessado, secretaria, cabeçalhos, rodapés, logos, seções ou paginação, salvo se o usuário pedir explicitamente uma dessas alterações. O modelo não tem mais fotografias por padrão; se o usuário pedir para inserir alguma, trate como inserção nova a negociar (posição, tamanho, legenda), deixando claro que isso altera a estrutura do modelo atual.
9. Não invente fatos novos. Não mude números, valores, quantidades, ações, datas secundárias ou bases legais sem dados e pedido explícitos do usuário.
10. Preserve integralmente a estilização do template: fontes, tamanhos, cores, negritos, alinhamentos, espaçamentos, margens, quebras, estilos, ancoragens e posições.
11. Antes da entrega, confira que apenas as alterações autorizadas foram realizadas. Renderize todas as páginas para inspeção visual quando o ambiente permitir; se não permitir, conclua as verificações estruturais disponíveis e informe a limitação.
12. Confirme novamente que o arquivo original da pasta `template/` permanece byte a byte inalterado.

## Saída

- Entregue sempre um arquivo `.docx` final dentro da pasta mensal correta, com a estilização padrão do template preservada.
- Nunca sobrescreva uma saída existente sem autorização explícita.
- Não deixe arquivos de inspeção, PDFs ou imagens de QA dentro de `outputs/`.
