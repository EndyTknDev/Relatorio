# Modelo: relatório técnico de agricultura — estiagem 2025

## Referência preservada

- Caminho na raiz do plugin: `template/RELATORIO_AGRICULTURA_ESTIAGEM_-_2025.docx`.
- SHA-256: `752D715DBA725A84F4A5FE898D43E4092AA704D600F871D940D6EF78F00C70F0`.
- Tamanho observado: `107.585` bytes.
- Caso do modelo: Acará, Pará (PA), ano agrícola 2025, documento datado de 17 de novembro de 2025.
- O arquivo é somente leitura. Toda geração começa por uma cópia.
- Esta é uma nova versão do modelo (o relatório fotográfico — mapa e as 16 fotografias — foi removido pelo responsável pela skill). O hash, o tamanho e toda esta referência foram atualizados a partir dela; se o hash divergir novamente no futuro, trate como mais uma nova versão e repita a inspeção.

## Estrutura e aparência

- 3 seções, todas retrato: 1 contínua e 2 com quebra para nova página (era 19 seções antes da remoção do relatório fotográfico).
- 34 parágrafos no corpo (era 294) e nenhuma tabela.
- **Nenhuma imagem no corpo do documento.** O relatório fotográfico (mapa + 16 fotografias) foi removido; o modelo agora é somente texto, além da identidade visual do cabeçalho e rodapé.
- 5 arquivos de mídia, todos usados no cabeçalho/rodapé (identidade visual institucional). 1 parte de cabeçalho e 3 partes de rodapé (`even`, `default`/ímpar e `first`); confirme com o usuário se essa distinção de página par/ímpar/primeira é intencional.
- Estilos em uso: `Heading 1` (5 ocorrências) e `Body Text` (22), com identificadores internos em inglês nesta versão. Formatação direta é usada ao longo do documento; não a normalize.
- Rodapé com endereço (`Rod. PA 252, km 01, Cacoal, Acará - Pará`), CEP e e-mail (`semact_acara@outlook...`).
- O arquivo carrega um rótulo de confidencialidade do Microsoft Purview (`docMetadata/LabelInfo.xml`) que imprime o texto "Classified - Confidential" nos rodapés — o mesmo padrão observado em outros templates deste plugin. Esse texto não é conteúdo do relatório; não o trate como campo a preencher nem o remova por conta própria.
- Não foi encontrado destaque de cor (highlight/shading) nesta versão do documento nem comentários internos de autoria (o pacote não contém `comments.xml`). Se uma versão futura reintroduzir comentários ou destaques, trate como nova inspeção antes de aplicar as orientações abaixo.

## Ordem de conteúdo

1. Título, Assunto, Referência, Justificativa (caracterização do município, efeitos sobre pastagens/lavouras, relação com incêndios) e quatro linhas de prejuízos.
2. Diagnóstico.
3. Conclusão.
4. Encerramento, data e assinatura.

**Não existe mais relatório fotográfico** (mapa de focos/eventos e as 16 fotografias que ocupavam páginas próprias). Não peça nem insira essas evidências por padrão; se o usuário pedir explicitamente para reintroduzi-las, trate como uma inserção nova a negociar (posição, tamanho, legenda), deixando claro que isso altera a estrutura do modelo atual.

## Mapa de substituições textuais

Localize cada bloco pelo título ou pelo texto de abertura, na ordem acima, e não por número de parágrafo fixo — a remoção do relatório fotográfico reindexou todo o documento em relação a versões anteriores desta referência.

- **Título:** nome oficial e sigla da secretaria; preserve caixa, alinhamento e estilo.
- **Assunto:** mês ou período, ano agrícola e município.
- **Referência:** município e estado. O enquadramento de estiagem, o COBRADE `1.4.1.1.0` e as Portarias nº 260/2022 e nº 3.646/2022 permanecem no fluxo padrão.
- **Justificativa:** caracterização do município, efeitos sobre pastagens e lavouras, relação com incêndios e as quatro linhas físicas de prejuízo (perda de produção agrícola familiar, prejuízos ambientais, prejuízos na criação de animais, prejuízo com falta de água potável). Preserve os quatro parágrafos; se a quantidade de categorias informada pelo usuário for diferente, peça que ele ajuste ou agrupe os dados para caber nessa estrutura — não acrescente nem remova parágrafos.
- **Diagnóstico:** período e abrangência da estiagem, danos, riscos ligados à água, perdas pecuárias e efeitos nas atividades agrícolas e na renda familiar.
- **Conclusão:** síntese técnica dos impactos e medidas emergenciais/recomendações.
- **Encerramento e data:** município, UF e data por extenso.
- **Assinatura:** nome, cargo e ato de nomeação.
- **Cabeçalho e rodapé:** nomes institucionais, imagens e contatos somente quando fornecidos ou autorizados; caso contrário, preserve os do modelo.

## Orientações incorporadas de inspeções anteriores

Estas orientações vinham originalmente de comentários de autoria do modelo, hoje ausentes do pacote; permanecem válidas como guia editorial:

- O Assunto deve indicar o mês ou período, e não apenas o ano.
- O trecho de enquadramento do desastre na Referência deve ser mantido no fluxo padrão.
- A caracterização da Justificativa deve usar dados verificados do município solicitado.
- O Diagnóstico e a Conclusão devem ser redigidos de forma original e específica ao município, sem copiar a redação de Acará.
- Os valores de prejuízo vêm do usuário; não devem ser produzidos por pesquisa genérica nem estimados pelo agente.

## Gates de fidelidade

- O hash do modelo permanece `752D715DBA725A84F4A5FE898D43E4092AA704D600F871D940D6EF78F00C70F0`.
- A saída mantém 3 seções, 34 parágrafos e nenhuma tabela, salvo mudança estrutural expressamente autorizada.
- Nenhuma imagem de corpo (mapa/fotografia) é esperada por padrão nesta versão; a identidade visual do cabeçalho/rodapé permanece como no modelo, salvo substituição fornecida e autorizada pelo usuário.
- Não há texto cortado, sobreposição, deformação ou página vazia indevida.
- Não permanece dado factual, contato, assinatura ou identidade institucional de Acará-PA quando o relatório for de outro município, exceto item cuja manutenção tenha sido expressamente autorizada.
