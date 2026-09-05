# Modelo: assistência social — seca e estiagem 2025

## Referência preservada

- Caminho na raiz do plugin: `template/RELATORIO ASSISTÊNCIA SOCIAL SECA E ESTIAGEM 2025.docx`. O nome pode estar armazenado em forma Unicode decomposta ou composta; localize o arquivo pelo hash, não apenas pela grafia.
- SHA-256: `A45525EFF6A3E6C095A2D55AA5082EB65CD31C7ECED0D4590EC6A25D0FB997BA`
- Tamanho observado: `62.186` bytes.
- O modelo é somente leitura. Gere relatórios exclusivamente a partir de uma cópia.
- Esta é uma nova versão do modelo (o relatório fotográfico do final do documento foi removido pelo responsável pela skill). O hash, o tamanho e toda esta referência foram atualizados a partir dela; se o hash divergir novamente no futuro, trate como mais uma nova versão e repita a inspeção.

## Estrutura apurada

- 3 seções, todas em orientação retrato: 2 contínuas e 1 com quebra para nova página.
- 33 parágrafos de nível superior (era 106 antes da remoção do relatório fotográfico).
- Nenhuma tabela.
- Nenhum campo automático do Word, nota de rodapé, nota de fim ou controle de conteúdo.
- **Nenhuma imagem no corpo do documento.** O relatório fotográfico que existia em páginas próprias ao final foi removido; o modelo agora é somente texto, além da identidade visual do cabeçalho e rodapé.
- 2 partes de cabeçalho, cada uma com 2 imagens de identidade visual. A seção 1 declara variantes de rodapé `even`, `default` (ímpar) e `first`; a seção 3 declara seu próprio cabeçalho/rodapé (`rId11`/`rId12`). Confirme com o usuário se a distinção entre página par/ímpar/primeira é intencional.
- O rodapé traz endereço ("Ao lado do Ginásio 'O Dicao'", CEP), e-mail (`semadsacara@gmail.com`) e CNPJ.
- O arquivo carrega um rótulo de confidencialidade do Microsoft Purview (`docMetadata/LabelInfo.xml`) que imprime o texto "Classified - Confidential" nos rodapés — o mesmo padrão observado em outros templates deste plugin. Esse texto não é conteúdo do relatório; não o trate como campo a preencher nem o remova por conta própria.
- Estilos em uso: `Normal`, `Body Text` e `List Paragraph` (identificadores internos em inglês nesta versão). Os títulos principais (`– IDENTIFICAÇÃO`, `– RELATÓRIO INFORMATIVO SOCIAL`) usam `List Paragraph`, não estilos `Heading`; preserve esse comportamento por fidelidade.
- Formatação direta é usada ao longo do documento; não a normalize.

## Sistema de página

- Tamanho observado: aproximadamente `8,28 × 11,94 pol.`.
- Margens esquerda e direita: `0,30 pol.`.
- Margem superior: `1,10 pol.`. Margem inferior: `0,94 pol.` na seção 1 e `1,10 pol.` na seção 3.
- A seção 1 é contínua; a seção 2 é contínua; a seção 3 inicia em nova página com cabeçalho e rodapé próprios.

## Ordem de conteúdo

1. Local e data.
2. Identificação: interessado, secretaria e assunto.
3. Título do relatório informativo social.
4. Situação geral.
5. Diagnóstico preliminar.
6. Conclusão, recomendações e providências.
7. Assinatura ou identificação da unidade responsável.

**Não existe mais relatório fotográfico** ao final do documento (era o item 8 em versões anteriores desta referência). Não peça nem insira fotografias por padrão; se o usuário pedir explicitamente para reintroduzi-las, trate como uma inserção nova a negociar (posição, tamanho, legenda), deixando claro que isso altera a estrutura do modelo atual.

## Mapa de substituições

- **Local e data:** substituir pelo município, estado e data informados pelo usuário.
- **Ocorrências geográficas:** substituir as referências pertinentes ao município e estado no corpo do relatório.
- **Situação Geral:** adaptar ao município e estado informados, mantendo redação, tom e função semelhantes aos do modelo.
- **Diagnóstico Preliminar:** adaptar ao município e estado informados, mantendo a estrutura argumentativa e técnica do modelo.
- **Conclusão:** adaptar a síntese e as recomendações ao município e estado informados, mantendo a lógica do modelo.
- **Demais conteúdos:** preservar. Não alterar interessado, secretaria, assunto, ações, números, valores, assinatura, cabeçalhos, rodapés ou logos sem pedido explícito.
- **Estilização:** preservar integralmente; faça as substituições dentro dos elementos existentes, mantendo suas propriedades de parágrafo e trecho.

## Limitações da inspeção

A inspeção visual não pôde ser concluída porque não havia conversor DOCX/PDF disponível no ambiente. Número exato de páginas e aparência exata permanecem não verificados por renderização; confirme antes de citar um total ao usuário.

## Gates de fidelidade

- Compare o hash do modelo antes e depois.
- Preserve as 3 seções e sua geometria, salvo alteração solicitada.
- Preserve cabeçalhos, rodapés, imagens institucionais e relações internas não editadas.
- Inspecione a saída inteira e confirme que município, estado e data foram atualizados nas ocorrências pertinentes.
- Confirme que somente os três blocos textuais autorizados foram modificados.
- Confirme que nenhuma propriedade visual do template foi alterada.
- Confirme que nenhuma fotografia ou anexo foi adicionado sem pedido explícito do usuário.
