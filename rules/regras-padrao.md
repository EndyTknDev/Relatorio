# Regras padrão das skills de relatórios

Leia e aplique estas regras integralmente sempre que uma skill deste plugin for usada. As regras específicas de cada skill complementam este arquivo e definem os campos, fontes, substituições e verificações próprias de cada modelo.

## 1. Preservação do template

Preserve integralmente toda a estrutura e toda a estilização do template durante a cópia, o preenchimento, a inserção de imagens e a verificação. Os templates desta versão são intencionalmente livres de imagens e de relações de mídia; os parágrafos, quebras, seções e demais propriedades que definiam a localização dos antigos slots foram mantidos. Não acrescente, remova, duplique, reorganize ou reconstrua seções, páginas, parágrafos, tabelas, linhas, células, cabeçalhos, rodapés, quebras, campos ou espaços reservados. Preserve estilos, fontes, tamanhos, cores, destaques, alinhamentos, recuos, espaçamentos, margens, bordas e paginação. Faça somente alterações localizadas. Se os dados não couberem na estrutura disponível, peça ao usuário que os ajuste; não altere a estrutura.

## 2. Dados presentes na conversa

Antes de solicitar os dados, verifique se mensagens anteriores da conversa já contêm entradas relacionadas ao documento. Se houver, não as reutilize silenciosamente: pergunte se o usuário deseja reaproveitá-las e apresente todos os valores candidatos no formato `Campo: valor`. Aguarde a confirmação e depois solicite apenas os dados ausentes ou as substituições desejadas.

## 3. Autorização para pesquisa externa

Antes de qualquer pesquisa externa, pergunte se o usuário prefere enviar o contexto, os dados e as fontes ou se autoriza o agente a pesquisar as informações. Apresente claramente as duas possibilidades e aguarde a escolha. Se o usuário enviar o contexto, não faça pesquisa complementar sem autorização posterior. Se autorizar a pesquisa, siga os critérios de fontes da skill utilizada.

## 4. Imagens e slots vazios

Os templates não contêm imagens para manter ou substituir. Quando uma saída exigir cabeçalho, brasão, mapa, fotografia, captura de tela ou outra imagem, leia `references/especificacoes-imagens-removidas.md` da skill. Recrie somente os slots necessários conforme a tabela: parte e parágrafo, tipo (`inline`, `anchor` ou VML), tamanho do quadro, posição horizontal e vertical e ajuste do texto. Não tente deduzir esses parâmetros pela aparência de um novo arquivo.

Use apenas imagem fornecida pelo usuário ou obtida de fonte verificável com autorização. Nunca restaure a mídia removida, use identidade de outro município ou trate fotografia de outro local como evidência. Se uma imagem obrigatória não for fornecida, pare e solicite o arquivo; não invente, não gere imagem neutra e não use retângulo branco para simular preenchimento. Se o slot for opcional e o usuário não quiser imagem, deixe-o vazio sem remover seu parágrafo, quebra, seção ou propriedades.

Depois da inserção, renderize todas as páginas e verifique posição, dimensões, proporção, recorte, legenda, margens e sobreposição. Antes de qualquer inserção, o template e sua cópia inicial devem conter zero arquivos em `word/media`, zero relações do tipo `image` e zero elementos `a:blip` ou `v:imagedata`.

## 5. Desempenho, bloqueios e limite de tentativas

Antes de copiar, editar, substituir ou renderizar um arquivo, confirme que ele pode ser aberto com o acesso necessário. A existência isolada de um arquivo temporário `~$` não comprova bloqueio; valide o acesso ao DOCX de destino. Se o arquivo estiver aberto no Word, bloqueado por outro processo ou retornar `PermissionError`/erro de compartilhamento, interrompa imediatamente a execução e peça ao usuário que feche o arquivo para continuar. Não tente sobrescrever, renomear, criar uma versão alternativa, iniciar o renderizador ou repetir comandos enquanto o bloqueio persistir. Depois que o usuário confirmar o fechamento, verifique o acesso uma única vez e retome do ponto interrompido.

Reutilize os resultados de inspeções, hashes e inventários enquanto o arquivo não mudar. Agrupe verificações independentes em uma única etapa e não reabra nem reinspecione repetidamente o mesmo pacote OOXML sem uma alteração intermediária que justifique nova análise.

Faça as alterações solicitadas em um lote coerente, execute uma verificação estrutural após esse lote e renderize uma única vez a versão resultante. Faça nova renderização somente quando uma correção real tiver sido aplicada ao documento depois da inspeção anterior.

Use o LibreOffice configurado como renderizador padrão. Não tente automatizar o Microsoft Word como conversor alternativo, salvo pedido explícito do usuário. Se o LibreOffice não estiver disponível ou a renderização falhar por problema do ambiente, execute no máximo um diagnóstico direcionado, informe o bloqueio e pare; não encadeie conversores alternativos nem repita comandos equivalentes.

Toda conversão ou renderização deve ter limite de tempo explícito de até 120 segundos. Se o processo exceder esse limite, encerre apenas o processo iniciado para essa tentativa, informe em que etapa ocorreu a interrupção e aguarde orientação do usuário. Uma repetição automática só é permitida quando a causa tiver sido identificada e corrigida; nunca repita o mesmo comando sem mudança concreta nas condições de execução.
