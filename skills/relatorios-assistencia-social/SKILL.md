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

## Antes de começar

1. Resolva a raiz do plugin dois níveis acima desta skill.
2. Leia [references/regras-gerais.md](references/regras-gerais.md) para qualquer relatório.
3. Para o modelo `RELATORIO ASSISTÊNCIA SOCIAL SECA E ESTIAGEM 2025.docx`, leia também [references/modelo-seca-estiagem-2025.md](references/modelo-seca-estiagem-2025.md).
4. Confirme que o modelo ainda corresponde ao hash registrado na referência. Se divergir, trate-o como uma nova versão e faça outra inspeção antes de gerar documentos.
5. Antes de copiar ou editar o documento, pergunte obrigatoriamente:
   - município;
   - estado;
   - data do relatório.
6. Não deduza esses três dados, não use valores do modelo e não substitua a data ausente pela data atual. Se qualquer item estiver faltando, aguarde a resposta do usuário antes de iniciar a geração.

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
8. Não altere nenhuma outra parte do documento, inclusive fotografias, assinatura, assunto, interessado, secretaria, cabeçalhos, rodapés, logos, seções ou paginação, salvo se o usuário pedir explicitamente uma dessas alterações.
9. Não invente fatos novos. Não mude números, valores, quantidades, ações, datas secundárias ou bases legais sem dados e pedido explícitos do usuário.
10. Preserve integralmente a estilização do template: fontes, tamanhos, cores, negritos, alinhamentos, espaçamentos, margens, quebras, estilos, ancoragens e posições.
11. Antes da entrega, confira que apenas as alterações autorizadas foram realizadas. Renderize todas as páginas para inspeção visual quando o ambiente permitir; se não permitir, conclua as verificações estruturais disponíveis e informe a limitação.
12. Confirme novamente que o arquivo original da pasta `template/` permanece byte a byte inalterado.

## Saída

- Entregue sempre um arquivo `.docx` final dentro da pasta mensal correta, com a estilização padrão do template preservada.
- Nunca sobrescreva uma saída existente sem autorização explícita.
- Não deixe arquivos de inspeção, PDFs ou imagens de QA dentro de `outputs/`.
