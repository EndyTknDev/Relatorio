# Regras gerais do relatório de agricultura — estiagem

## Integridade do modelo

- Trate todos os arquivos de `template/` como somente leitura.
- Gere a saída a partir de uma cópia e registre o SHA-256 do modelo antes e depois.
- Se o hash do modelo mudar, não tente adaptar automaticamente: refaça a inspeção e atualize a referência e o script.
- Não use o arquivo de saída como novo template.

## Organização das saídas

- Salve em `outputs/<Mês> <Ano>/`, por exemplo `outputs/Novembro 2025/`.
- A data documental fornecida pelo usuário determina a pasta; não use a data atual como substituta.
- Use mês em português, com inicial maiúscula e sem número prefixado.
- Não sobrescreva arquivos existentes. Use sufixos como `- RASCUNHO`, `- REVISAO 01` ou `- FINAL` somente quando necessário.
- Não deixe arquivos temporários, PDFs de renderização ou imagens de QA dentro de `outputs/`.

## Conteúdo e linguagem

- Use português brasileiro formal, claro e institucional.
- Preserve a grafia oficial de municípios, órgãos, comunidades, culturas, programas e atos normativos.
- Escreva siglas por extenso na primeira ocorrência, seguida da sigla entre parênteses, quando isso couber no texto existente.
- Separe fatos observados, dados oficiais, estimativas declaradas, ações executadas e recomendações.
- Não transfira dados do caso de Acará-PA para outro município.
- Não invente quantitativos, valores, totais, percentuais, datas, coordenadas, comunidades, produtores, famílias, culturas atingidas, rebanhos, ocorrências, responsáveis ou bases legais.
- Confira a soma dos prejuízos apenas quando todas as parcelas tiverem sido fornecidas. Identifique explicitamente qualquer estimativa informada pelo usuário.
- Dados territoriais, demográficos e produtivos pesquisados devem ter fonte oficial e ano de referência. Não misture anos sem explicação.
- Verifique atos normativos em fonte oficial antes de alterar a redação jurídica do modelo.
- Não adicione seções, anexos, quadros ou listas sem solicitação expressa.

## Evidências e privacidade

- O modelo não tem mais relatório fotográfico por padrão (mapa e as 16 fotografias foram removidos). Não peça nem insira essas evidências no fluxo padrão.
- Se o usuário pedir explicitamente para reintroduzir mapa e/ou fotografias, trate como uma inserção nova a negociar (posição, tamanho, legenda), usando somente imagens fornecidas pelo usuário ou obtidas de fonte verificável com autorização e condições de uso compatíveis, e deixando claro que isso altera a estrutura do modelo atual.
- Não use fotografia de outro município como se fosse evidência local. Não altere o conteúdo de uma evidência para simular dano, data, localização, coordenadas ou intensidade.
- Toda fotografia inserida deve receber legenda compatível com seu conteúdo. Informe local, data e fonte/autoria apenas quando comprovados.
- Não identifique pessoas vulneráveis, propriedades privadas ou coordenadas sensíveis sem necessidade administrativa e autorização.

## Fidelidade visual

- Preserve fontes, tamanhos, cores, realces (quando presentes), negritos, sublinhados, alinhamentos, recuos, espaçamentos, margens, tamanho de página, cabeçalhos, rodapés, logos, quebras e seções.
- Preserve os estilos `Heading 1`, `Body Text` e `Normal` e a formatação direta de cada execução.
- Edite texto dentro dos `runs` existentes. Não atribua texto ao parágrafo inteiro de modo que elimine sua formatação ou seus desenhos.
- Ao substituir mídias, mantenha relações, dimensões, proporção, âncora, posição e ordem de empilhamento.
- Não reconstrua o DOCX do zero e não aplique melhorias visuais não solicitadas.

## Checklist de entrega

- Modelo original com hash inalterado.
- Saída na pasta de mês e ano correta, sem sobrescrever outro arquivo.
- Município, UF, período, ano, data e secretaria consistentes em todo o documento.
- Justificativa, prejuízos, Diagnóstico e Conclusão adaptados somente com dados autorizados ou verificados.
- Valores conferidos contra o input do usuário.
- Identidade institucional, contatos e assinatura correspondem ao município do relatório; nenhum mapa ou fotografia foi adicionado sem pedido explícito.
- Se o pacote contiver comentários internos de autoria (esta versão não contém), remova-os da cópia final sem alterar texto visível apenas para isso.
- Todas as páginas geradas renderizadas e visualmente revisadas (a versão atual tem 3 seções; confirme o número exato de páginas por renderização).
- Arquivo final entregue em `.docx` com a aparência do template preservada.

