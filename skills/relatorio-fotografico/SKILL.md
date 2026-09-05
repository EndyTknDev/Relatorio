---
name: relatorio-fotografico
description: Gera relatórios fotográficos em DOCX a partir do modelo oficial, inserindo as imagens fornecidas e criando automaticamente uma legenda objetiva para cada fotografia sem alterar a estilização. Use somente para documentos baseados no template RELATORIO FOTOGRÁFICO.docx.
---

# Relatório Fotográfico

Use `template/RELATORIO FOTOGRÁFICO.docx` como autoridade de estrutura e aparência. Nunca edite diretamente qualquer arquivo da pasta `template/`.

## Regras padrão obrigatórias

Antes de qualquer ação, leia e aplique integralmente [as regras padrão do plugin](../../rules/regras-padrao.md). As regras específicas abaixo complementam esse arquivo e não dispensam nenhuma de suas exigências.

## Antes de começar

1. Resolva a raiz do plugin dois níveis acima desta skill.
2. Leia [references/modelo-relatorio-fotografico.md](references/modelo-relatorio-fotografico.md).
3. Confirme que o SHA-256 do modelo corresponde ao valor registrado na referência. Se divergir, interrompa a geração, trate o arquivo como uma nova versão e refaça a inspeção antes de atualizar esta skill.
4. Antes de copiar, editar ou gerar o documento, peça em um único bloco somente os dados ainda não informados:
   - município;
   - estado e UF;
   - data do relatório em `DD/MM/AAAA` ou `AAAA-MM-DD`;
   - desastre ou tema do relatório;
   - imagem esquerda e imagem direita do cabeçalho, ou confirmação expressa para manter as imagens existentes;
   - arquivos das fotografias, na ordem em que devem aparecer, até o limite padrão de 28 imagens;
   - opcionalmente, local, data, fonte/autoria e contexto de cada fotografia.
5. As fotografias são entradas obrigatórias. Não use as fotografias do modelo como conteúdo de uma nova saída.
6. Se o usuário já tiver fornecido algum dado na mensagem atual, não o peça novamente. Para dados encontrados em mensagens anteriores, siga a confirmação de reutilização das regras compartilhadas.

## Legendas automáticas

- Inspecione visualmente cada fotografia fornecida e gere automaticamente uma legenda curta, objetiva e institucional.
- Descreva apenas o que é visível ou foi informado pelo usuário. Não invente local, data, autoria, espécie, causa, intensidade, prejuízo ou identidade de pessoas.
- Quando os metadados estiverem disponíveis, use `Figura <n> — <descrição objetiva>. Local: <local>. Data: <DD/MM/AAAA>. Fonte: <autoria/órgão>.`
- Omita os campos não informados. Não escreva “não informado” na legenda.
- Numere as figuras na ordem dos arquivos recebidos e mantenha correspondência individual entre fotografia, legenda e posição no documento.
- Não peça ao usuário que escreva as legendas. Peça esclarecimento somente quando a imagem for ambígua e uma interpretação não verificável for indispensável.

## Fluxo de trabalho

1. Converta a data para `AAAA-MM-DD` e use `scripts/criar_saida.py` para criar uma cópia em `outputs/<Mês> <Ano>/`, com o mês em português e inicial maiúscula.
2. Trabalhe somente na cópia de saída.
3. Atualize na capa e no cabeçalho apenas município, estado/UF, data/ano, desastre/tema e identificação institucional fornecida pelo usuário.
4. Substitua as imagens do cabeçalho apenas pelos arquivos fornecidos. Preserve posição, proporção, ancoragem e alinhamento.
5. Insira as fotografias na ordem recebida, substituindo as mídias existentes e mantendo os quadros e a proporção de cada imagem.
6. Insira uma legenda automática para cada fotografia nos parágrafos de legenda existentes ou nos espaços imediatamente associados, preservando a estilização visual do modelo.
7. Se houver menos de 28 imagens, não duplique arquivos, não conserve fotos antigas e não remova páginas nem posições. Peça ao usuário as imagens faltantes para preencher os 28 espaços existentes.
8. Se houver mais de 28 imagens, peça ao usuário que selecione as 28 que integrarão o documento. Não expanda o padrão nem crie um segundo volume nesta execução.
9. Não gere, retoque ou altere o conteúdo das fotografias sem pedido explícito.
10. Não altere estilos, fontes, tamanhos, cores, alinhamentos, margens, cabeçalhos, rodapés, quebras ou seções. Faça substituições locais em `runs`, relacionamentos e mídias existentes; não reconstrua o documento e não use substituição integral de `paragraph.text`.
11. Faça apenas o que foi solicitado. Não acrescente pesquisa, texto técnico, seções ou elementos gráficos não pedidos.

## Verificação e entrega

- Confirme que o modelo original mantém o mesmo SHA-256 antes e depois.
- Confirme que nenhum dado, fotografia ou legenda de Acará-PA permaneceu indevidamente na saída.
- Confira a ordem das imagens e a correspondência de todas as legendas.
- Confirme que nenhuma legenda apresenta como fato um dado que não foi fornecido ou que não esteja claramente visível.
- Renderize e inspecione todas as páginas. Corrija texto cortado, sobreposição, imagem deformada, legenda separada da fotografia ou página vazia indevida.
- Entregue sempre um único arquivo `.docx`, com a estilização padrão do template, na pasta mensal correta.
- O nome sugerido é `RELATORIO FOTOGRAFICO - <TEMA> - <MUNICIPIO> - <AAAA-MM-DD>.docx`.
- Nunca sobrescreva uma saída existente sem autorização explícita. Use um sufixo de revisão quando necessário.
- Não deixe PDFs, imagens de inspeção ou outros temporários dentro de `outputs/`.
