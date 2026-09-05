---
name: parecer-tecnico-defesa-civil
description: Gera pareceres técnicos da Defesa Civil em DOCX para fundamentar decretos de situação de emergência ou estado de calamidade, usando o modelo oficial preservado e adaptando os dados do município, do desastre, dos danos e das ações. Use somente para pareceres baseados no template PARECER_TECNICO_DEFESA_CIVIL.docx.
---

# Parecer Técnico da Defesa Civil

Use `template/PARECER_TECNICO_DEFESA_CIVIL.docx` como autoridade de estrutura e aparência. Nunca edite o arquivo da pasta `template/` diretamente.

## Regras padrão obrigatórias

Antes de qualquer ação, leia e aplique integralmente [as regras padrão do plugin](../../rules/regras-padrao.md). As regras específicas abaixo complementam esse arquivo e não dispensam nenhuma de suas exigências.

## Antes de gerar

1. Resolva a raiz do plugin dois níveis acima desta pasta.
2. Leia [references/modelo-parecer-tecnico.md](references/modelo-parecer-tecnico.md).
3. Confirme o SHA-256 do template. Se ele não corresponder ao valor registrado na referência, pare e faça nova inspeção antes de gerar qualquer saída.
4. Solicite os dados em blocos curtos e sucessivos, seguindo as opções selecionáveis das regras padrão. Aguarde a resposta de cada bloco antes de apresentar o seguinte:
   1. **Identificação:** município e estado/UF; secretaria responsável; assunto.
   2. **Tipo do desastre:** ofereça primeiro `Estiagem ou seca`, `Inundação, enchente ou alagamento` e `Incêndio florestal ou queimada`, sempre com a opção livre para escrever. Mencione no enunciado que também são recorrentes ou relevantes no Amazonas/Manaus e no Pará: chuvas intensas, enxurradas, erosão de margem fluvial (`terras caídas`), deslizamento ou movimento de massa, vendaval e baixa umidade. Se o usuário escolher a opção livre, aceite qualquer tipologia e confirme a redação antes de continuar.
   3. **Decreto e enquadramento:** número e data do decreto; código COBRADE.
   4. **Data do documento:** calcule as opções no fuso `America/Manaus` e ofereça `Hoje — <DD/MM/AAAA>`, `Ontem — <DD/MM/AAAA>` e `Último dia útil — <DD/MM/AAAA>`, além da opção livre para outra data e hora. Nunca grave literalmente `Hoje`, `Ontem` ou `Último dia útil` no documento; use a data absoluta selecionada pelo usuário.
   5. **Identidade institucional:** imagens de cabeçalho ou a alternativa permitida pelas regras padrão; responsável pela assinatura, cargo e portaria, somente se devam ser alterados.
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
   - prejuízos e aquisições, com descrição, quantidade ou extensão quando aplicável e valor individual, usando obrigatoriamente o formato definido na seção seguinte;
   - ações realizadas, equipes e instituições mobilizadas;
   - recursos materiais empregados, valores já gastos e apoio ainda necessário.
4. Não use números, custos, datas, localidades, ações ou consequências do template para preencher lacunas.

## Formato obrigatório de prejuízos e aquisições

Sempre peça os prejuízos e as aquisições em um bloco próprio. Ofereça as opções selecionáveis `Escrever ou colar a lista`, `Informar item por item` e `Não se aplica ao caso`, além da opção livre para escrever. Solicite uma ocorrência por linha, iniciada por hífen, com descrição objetiva e valor em reais.

Use estes padrões:

- Prejuízo: `-Prejuízos com <descrição, quantidade ou extensão> - R$ <valor>;`
- Aquisição: `-Aquisição de <quantidade, unidade e item> R$ <valor>.`

Durante a solicitação, apresente sempre o exemplo abaixo como orientação exclusivamente de formato. Deixe claro que os dados são ilustrativos e não podem ser reutilizados no parecer real:

```text
-Prejuízos com perda de produção agrícola familiar em 1.100 hectares produtivos já destruídos - R$ 2.550.000,00;
-Prejuízos ambientais - R$ 550.000,00;
-Prejuízos na criação de animais - R$ 680.000,00;
-Prejuízo com falta de água potável - R$ 1.250.000,00.
-Aquisição de 20.000 litros de gasolina R$ 170.000,00.
-Aquisição de 15.000 litros de diesel R$ 120.000,00.
-Aquisição de água mineral R$ 3.500.000,00.
-Aquisição de cestas de alimentos R$ 5.000.000,00.
```

Preserve os valores informados pelo usuário e normalize apenas ortografia, pontuação e apresentação monetária. Se uma linha não trouxer valor, unidade ou quantidade necessária, peça confirmação em vez de calcular, estimar ou completar o dado. Não trate o exemplo como fonte factual nem some os valores sem solicitação.

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
3. Verifique estruturalmente que não foram adicionados ou removidos parágrafos, tabelas, linhas, células, seções ou imagens.
4. Compare visualmente todas as páginas do modelo e da saída, seguindo a seção 6 das regras padrão. Sem renderização e inspeção completas, a saída permanece rascunho e não pode ser entregue como final validado.
5. Entregue apenas o DOCX final; não coloque arquivos de inspeção em `outputs/`.
