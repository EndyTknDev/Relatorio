# Regras gerais dos relatórios

## Integridade dos modelos

- Arquivos em `template/` são somente leitura e constituem a fonte oficial de estrutura e aparência.
- Todo novo relatório começa como uma cópia em `outputs/<Mês> <Ano>/`.
- Registre e compare o SHA-256 do modelo antes e depois do trabalho.
- Uma alteração intencional do modelo exige nova versão, nova inspeção e atualização da referência correspondente.

## Organização das saídas

- O padrão de pasta é `outputs/<Mês> <Ano>/`, por exemplo `outputs/Agosto 2026/`.
- O mês deve ser escrito em português, com inicial maiúscula e sem número prefixado.
- A data informada pelo usuário determina a pasta. Não inicie o trabalho e não use a data atual enquanto município, estado e data do relatório não tiverem sido fornecidos.
- O nome sugerido é `RELATORIO ASSISTENCIA SOCIAL - <ASSUNTO> - <MUNICIPIO> - <AAAA-MM-DD>.docx`.
- Não sobrescreva arquivos existentes. Diferencie revisões com sufixos como `- RASCUNHO`, `- REVISAO 01` ou `- FINAL`, conforme o estágio informado pelo usuário.

## Conteúdo e linguagem

- Antes de criar a cópia de trabalho, pergunte município, estado e data do relatório. Os três campos são obrigatórios.
- Para qualquer um desses três campos que o usuário confirmar que não pode fornecer agora, use o marcador literal `[NECESSÁRIO INFORMAÇÃO]` no lugar do dado, sem inventar nem completar por suposição. Confirme essa substituição com o usuário antes de prosseguir e liste, na entrega, os campos marcados dessa forma.
- Faça apenas o que o usuário pedir. Para o fluxo padrão deste modelo, limite as mudanças a município, estado, data, Situação Geral, Diagnóstico Preliminar e Conclusão.
- Use português brasileiro formal, claro, objetivo e institucional.
- Separe fato observado, estimativa, avaliação técnica, ação executada e recomendação.
- Preserve a grafia oficial de órgãos, municípios, programas e comunidades.
- Escreva siglas por extenso na primeira ocorrência, seguida da sigla entre parênteses.
- Mantenha datas, quantidades e valores consistentes em todo o documento. Quando o padrão do modelo exigir número por extenso, confira a equivalência.
- Não invente pessoas atingidas, prejuízos, ações, custos, locais, datas, equipes, fotografias ou fundamentos legais. Não altere dados factuais do modelo sem input e pedido explícito.
- Leis, decretos e outros atos normativos devem ser verificados em fonte oficial quando forem incluídos ou atualizados.

## Privacidade e evidências

- Inclua somente dados pessoais necessários à finalidade administrativa do relatório.
- Não exponha documentos pessoais, endereços completos, prontuários ou informações sensíveis sem necessidade e autorização.
- O modelo não tem mais fotografias por padrão (o relatório fotográfico do final foi removido). Não insira fotografias no fluxo padrão; faça isso somente se o usuário pedir explicitamente e fornecer os arquivos, tratando como inserção nova.
- Quando houver legenda, identifique local, data e contexto sem expor pessoas vulneráveis desnecessariamente.

## Fidelidade e qualidade

- Preserve integralmente o sistema visual do modelo: fontes, tamanhos, cores, destaques, alinhamentos, espaçamentos, tamanho e orientação de página, margens, cabeçalhos, rodapés, logos, estilos, quebras, seções e posicionamento de imagens.
- Não normalize estilos antigos, converta títulos, reconstrua o documento ou aplique melhorias visuais. A estilização do template não deve ser modificada.
- Evite mudanças em partes internas não relacionadas ao conteúdo solicitado.
- Revise todas as páginas renderizadas, especialmente as imagens de identidade visual do cabeçalho, as quebras de seção e os rodapés.
- Confirme que não existem texto cortado, sobreposição, imagens deformadas, páginas vazias indevidas ou conteúdo residual do caso usado como modelo.
- Se a renderização não estiver disponível, execute auditorias estruturais e informe que a inspeção visual ficou pendente.

## Checklist de entrega

- O modelo original continua com o mesmo hash.
- A saída está na pasta de mês e ano correspondente à data documental.
- Município, estado, data e os três blocos autorizados foram adaptados.
- Nenhuma parte fora do escopo solicitado foi modificada.
- Números, datas, nomes e bases legais foram conferidos.
- Nenhuma fotografia ou anexo foi adicionado sem pedido explícito do usuário.
- Todo campo marcado como `[NECESSÁRIO INFORMAÇÃO]` foi confirmado com o usuário e está listado na entrega.
- Cabeçalhos, rodapés, logos, seções e paginação foram preservados.
- A saída não sobrescreveu outro arquivo.
