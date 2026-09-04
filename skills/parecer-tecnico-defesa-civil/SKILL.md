---
name: parecer-tecnico-defesa-civil
description: Gera pareceres técnicos da Defesa Civil em DOCX para fundamentar decretos de situação de emergência ou estado de calamidade, usando o modelo oficial preservado e adaptando os dados do município, do desastre, dos danos e das ações. Use somente para pareceres baseados no template PARECER_TECNICO_DEFESA_CIVIL.docx.
---

# Parecer Técnico da Defesa Civil

Use `template/PARECER_TECNICO_DEFESA_CIVIL.docx` como autoridade de estrutura e aparência. Nunca edite o arquivo da pasta `template/` diretamente.

## Antes de gerar

1. Resolva a raiz do plugin dois níveis acima desta pasta.
2. Leia [references/modelo-parecer-tecnico.md](references/modelo-parecer-tecnico.md).
3. Confirme o SHA-256 do template. Se ele não corresponder ao valor registrado na referência, pare e faça nova inspeção antes de gerar qualquer saída.
4. Pergunte ao usuário, em um único bloco, os seguintes dados:
   - município e estado/UF;
   - secretaria responsável;
   - assunto;
   - tipo do desastre;
   - número e data do decreto;
   - código COBRADE;
   - imagens de cabeçalho, ou confirmação para manter as imagens do modelo;
   - data e hora do documento;
   - outras informações pertinentes, inclusive responsável pela assinatura, cargo e portaria, somente se devam ser alterados.
5. Não copie nem edite o documento enquanto os dados obrigatórios estiverem faltando. Não reutilize como fatos os dados do caso de Acará presentes no template.

## Publicação e dados técnicos

1. Pesquise em fontes oficiais a publicação do decreto usando município, número e data do decreto. Registre o nome do diário oficial, número da edição e data da publicação.
2. Se não localizar uma correspondência oficial inequívoca, informe a limitação e peça ao usuário os dados da publicação. Não estime nem invente.
3. Solicite também:
   - protocolo de registro no Sistema Integrado de Informações sobre Desastres (S2ID);
   - situação de anormalidade, sugerindo `Situação de emergência` quando aplicável;
   - nível do desastre;
   - comunidades e áreas afetadas, com distâncias ou quilometragens verificáveis;
   - pessoas e famílias afetadas, perfil socioeconômico e grupos vulneráveis;
   - danos humanos, materiais, econômicos, ambientais e sanitários;
   - lista de danos materiais e respectivos custos estimados;
   - ações realizadas, equipes e instituições mobilizadas;
   - recursos materiais empregados, valores já gastos e apoio ainda necessário.
4. Não use números, custos, datas, localidades, ações ou consequências do template para preencher lacunas.

## Pesquisa de apoio

- Antes de redigir cada tópico principal, pesquise o desastre e o município na internet.
- Priorize prefeitura, Defesa Civil, órgãos ambientais, meteorológicos, hidrológicos, sanitários e diários oficiais.
- Use a pesquisa para validar e contextualizar os dados fornecidos, sem substituir o relato municipal e sem criar alegações não comprovadas.
- Não acrescente ao DOCX uma seção de referências que não exista no template, salvo pedido explícito. Apresente ao usuário, na entrega, as fontes externas efetivamente usadas.

## Geração e edição

1. Use `scripts/criar_saida.py` para copiar o template para `outputs/<Mês> <Ano>/`, considerando a data do documento. Trabalhe somente na cópia.
2. Preencha os campos do cabeçalho e das Informações Gerais com os dados confirmados.
3. Adapte somente o conteúdo necessário ao caso: Causa e Recorrência, áreas afetadas, Efeitos do Desastre, Ações Realizadas, conclusão e campos variáveis autorizados.
4. Siga a distribuição de conteúdo registrada na referência. Mantenha exatamente a quantidade de parágrafos, tabelas, linhas, células, seções e quebras do template. Quando várias responsabilidades precisarem caber em um único parágrafo físico existente, combine-as sem criar outro parágrafo.
5. Preserve o texto de assinatura do modelo, a menos que o usuário forneça substituição e peça sua alteração.
6. Substitua imagens de cabeçalho somente quando o usuário fornecer os arquivos e autorizar a troca. Preserve dimensões, posição, proporção e ancoragem. Caso contrário, mantenha as imagens originais.
7. Faça alterações localizadas, preservando propriedades de parágrafo e de execução. Não reconstrua o documento e não substitua `paragraph.text` ou `cell.text` de modo a apagar a formatação interna.

## Limites obrigatórios

- Faça apenas o que foi pedido.
- Não altere fontes, tamanhos, cores, negritos, alinhamentos, recuos, espaçamentos, margens, estilos, cabeçalhos, rodapés, logos, tabelas, paginação, quebras, seções ou posicionamento de imagens.
- Não corrija ou modernize a aparência do template.
- Não sobrescreva uma saída existente sem autorização explícita.
- Entregue sempre um arquivo `.docx` com a estilização padrão do template.

## Verificação

1. Compare o SHA-256 do template antes e depois e confirme que permaneceu idêntico.
2. Confirme que a saída contém os dados do novo caso e não conserva informações factuais de Acará, exceto elementos que o usuário tenha mandado preservar.
3. Verifique estruturalmente que não foram adicionados ou removidos parágrafos, tabelas, linhas, células, seções ou imagens fora do solicitado.
4. Renderize todas as páginas e faça inspeção visual quando o ambiente permitir. Se não for possível renderizar, conclua as verificações estruturais disponíveis e informe essa limitação.
5. Entregue apenas o DOCX final; não coloque arquivos de inspeção em `outputs/`.
