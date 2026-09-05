# Modelo — Relatório Fotográfico

## Identificação do arquivo

- Caminho relativo: `template/RELATORIO FOTOGRÁFICO.docx`.
- SHA-256 esperado: `43E7D8B999BB7810842C75EB7577872116FA9E025494EBEB85B67B29718EE0D5`.
- Extensão obrigatória da saída: `.docx`.

O nome contém acento Unicode e pode ser normalizado de formas diferentes pelo sistema operacional. Localize o modelo pelo hash, não apenas pelo nome literal.

## Estrutura preservada

- 16 páginas A4 em orientação retrato.
- 136 parágrafos no corpo, nenhuma tabela e três seções.
- Dois logotipos no cabeçalho.
- Capa com identificação do estado, município e prefeitura; título `RELATÓRIO FOTOGRÁFICO`; subtítulo do desastre/tema, município/UF e ano.
- Estilos utilizados: `Heading 1`, `Normal` e `Body Text`.

## Ordem dos slots fotográficos

Use a ordem recebida como a ordem das figuras. Não reorganize com base no conteúdo visual sem autorização do usuário.

## Padrão de legenda

Crie uma legenda por fotografia. O texto deve ser breve, descritivo e institucional, por exemplo:

`Figura 01 — Trecho de curso d'água com nível reduzido e margens expostas. Local: Comunidade Exemplo. Data: 20/08/2026. Fonte: Defesa Civil Municipal.`

O exemplo mostra apenas a forma. Nunca reaproveite seus dados em uma saída real.

- Use observação visual apenas para a descrição objetiva.
- Use local, data e fonte/autoria somente quando forem informados.
- Não atribua causa, desastre, dano, intensidade, espécie ou localização apenas pela aparência da imagem.
- Não identifique pessoas sem informação confirmada.
- Omita campos ausentes e mantenha a pontuação natural.

## Preservação visual e técnica

- Preserve as três seções, a geometria das páginas, os quadros, as quebras e a composição do cabeçalho.
- Preserve tamanho, posição, alinhamento e proporção dos objetos de imagem. Use contenção proporcional; não estique fotografias.
- Reaproveite os parágrafos próximos às imagens para as legendas. Algumas páginas do modelo têm uma legenda compartilhada ou espaços vazios; ajuste apenas os `runs` necessários para obter uma legenda individual por fotografia sem redesenhar a página.
- Não faça substituições amplas por `paragraph.text`, pois isso elimina a formatação dos `runs` e pode remover desenhos.
- Não deixe na saída fotografias, legendas, município ou logotipos do caso de Acará-PA, salvo manutenção expressamente autorizada pelo usuário.

## Controle de capacidade

- Quantidade inferior: pedir a escolha entre manter posições vazias, compactar ou remover páginas antes de alterar a estrutura.
- Quantidade superior: pedir a escolha entre segundo volume ou expansão do padrão.
- Nunca preencher espaços duplicando fotografias ou mantendo imagens do modelo.

