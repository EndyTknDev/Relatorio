# Regras padrão das skills de relatórios

Leia e aplique estas regras integralmente sempre que uma skill deste plugin for usada. As regras específicas de cada skill complementam este arquivo e definem os campos, fontes, substituições e verificações próprias de cada modelo.

As exigências de fidelidade e verificação da seção 6 prevalecem sobre permissões antigas das skills para entregar sem inspeção visual ou improvisar imagens. Instruções explícitas do usuário prevalecem. Divergências entre o pacote real e sua documentação devem ser resolvidas antes da edição afetada.

## 1. Preservação do template

Preserve integralmente toda a estrutura e toda a estilização do template durante a cópia, o preenchimento, a inserção de imagens e a verificação. Os templates desta versão são intencionalmente livres de imagens e de relações de mídia; os parágrafos, quebras, seções e demais propriedades que definiam a localização dos antigos slots foram mantidos. Não acrescente, remova, duplique, reorganize ou reconstrua seções, páginas, parágrafos, tabelas, linhas, células, cabeçalhos, rodapés, quebras, campos ou espaços reservados. Preserve estilos, fontes, tamanhos, cores, destaques, alinhamentos, recuos, espaçamentos, margens, bordas e paginação. Faça somente alterações localizadas. Se os dados não couberem na estrutura disponível, peça ao usuário que os ajuste; não altere a estrutura.

## 2. Dados presentes na conversa

Primeiro, leia os inputs e anexos enviados pelo usuário junto ao comando inicial da skill. Aproveite diretamente os dados fornecidos explicitamente para o relatório atual, sem pedir que sejam repetidos ou confirmar sua reutilização. Se todos os inputs necessários já estiverem presentes e claros, prossiga com a execução sem perguntar como o usuário prefere informar os dados.

Somente se ainda faltarem inputs, pergunte: `Como você prefere informar os dados restantes?`, com as opções selecionáveis `Aos poucos, em etapas` e `Todos de uma vez`, sempre permitindo uma resposta escrita. Aguarde a escolha antes de solicitar apenas os dados ausentes. Se o usuário já tiver indicado essa preferência para o relatório atual, aplique-a sem perguntar novamente. Esclareça somente as ambiguidades que impeçam a execução.

- `Aos poucos, em etapas`: solicite um pequeno bloco de campos relacionados por vez e aguarde a resposta antes de apresentar o próximo.
- `Todos de uma vez`: envie em uma única solicitação todos os inputs ainda necessários, organizados por assunto, incluindo exemplos de preenchimento, arquivos necessários e escolhas aplicáveis. Depois, pergunte apenas sobre lacunas, ambiguidades ou campos que dependam das respostas recebidas.

A preferência escolhida prevalece sobre instruções específicas das skills que determinem um único bloco ou blocos sucessivos. Preserve em ambos os modos os campos obrigatórios, as opções selecionáveis e a resposta escrita; não repita dados já fornecidos nem presuma autorizações ainda não concedidas.

Antes de solicitar os dados, verifique se mensagens anteriores da conversa já contêm entradas relacionadas ao documento. Se houver, não as reutilize silenciosamente: pergunte se o usuário deseja reaproveitá-las e apresente todos os valores candidatos no formato `Campo: valor`. Aguarde a confirmação e depois solicite apenas os dados ausentes ou as substituições desejadas.

Sempre que precisar pedir informações, use a interface de seleção disponível e faça perguntas curtas, com duas ou três opções objetivas por vez. Toda pergunta deve permitir uma resposta escrita: mantenha a opção livre `Outra opção — escrever resposta` ou o campo equivalente oferecido pela interface. Para dados naturalmente abertos, como descrição de danos, localidades ou listas de itens, inclua uma opção visível como `Escrever ou colar os dados`.

Se não houver interface de seleção, apresente as alternativas como lista numerada e encerre com `Outra opção — escreva sua resposta`. Não transforme uma ausência de dados em autorização para inventar informações. Quando houver muitas alternativas, mostre primeiro as três mais prováveis e mencione no enunciado as demais possibilidades relevantes, que poderão ser informadas pela opção escrita.

## 3. Autorização para pesquisa externa

Antes de qualquer pesquisa externa, pergunte se o usuário prefere enviar o contexto, os dados e as fontes ou se autoriza o agente a pesquisar as informações. Apresente claramente as duas possibilidades e aguarde a escolha. Se o usuário enviar o contexto, não faça pesquisa complementar sem autorização posterior. Se autorizar a pesquisa, siga os critérios de fontes da skill utilizada.

## 4. Imagens e slots vazios

Valide esta descrição no pacote real antes de copiar: inventarie mídias, relações de imagem e desenhos no corpo, cabeçalhos e rodapés. Se houver imagens apesar da declaração de ausência, ou faltar a referência de posições exigida abaixo, interrompa a edição das imagens e informe a inconsistência. Não remova, substitua por branco nem reconstrua o cabeçalho para contornar o problema. Não presuma que o slot é opcional. Preserve o original e resolva a versão do modelo ou a autorização específica para a alteração.

**O texto do cabeçalho é independente das imagens e deve ser sempre preservado.** Se o usuário não enviar ou não autorizar imagens de cabeçalho, mantenha integralmente os textos, caixas de texto, campos e respectivas formatações do cabeçalho. A ausência de brasão, logomarca ou fotografia nunca autoriza apagar, esvaziar, ocultar ou substituir o texto institucional. Altere esse texto somente quando houver dados confirmados para o novo caso e a própria skill autorizar seu preenchimento; nesse caso, substitua apenas os valores variáveis e preserve os rótulos, a estrutura e a formatação.

Os templates não contêm imagens para manter ou substituir. Quando uma saída exigir cabeçalho, brasão, mapa, fotografia, captura de tela ou outra imagem, leia `references/especificacoes-imagens-removidas.md` da skill. Recrie somente os slots necessários conforme a tabela: parte e parágrafo, tipo (`inline`, `anchor` ou VML), tamanho do quadro, posição horizontal e vertical e ajuste do texto. Não tente deduzir esses parâmetros pela aparência de um novo arquivo.

Use apenas imagem fornecida pelo usuário ou obtida de fonte verificável com autorização. Nunca restaure a mídia removida, use identidade de outro município ou trate fotografia de outro local como evidência. Se uma imagem obrigatória não for fornecida, pare e solicite o arquivo; não invente, não gere imagem neutra e não use retângulo branco para simular preenchimento. Se o slot for opcional e o usuário não quiser imagem, deixe-o vazio sem remover seu parágrafo, quebra, seção ou propriedades.

Depois da inserção, renderize todas as páginas e verifique posição, dimensões, proporção, recorte, legenda, margens e sobreposição. Antes de qualquer inserção, o template e sua cópia inicial devem conter zero arquivos em `word/media`, zero relações do tipo `image` e zero elementos `a:blip` ou `v:imagedata`.

## 5. Desempenho, bloqueios e limite de tentativas

Antes de iniciar a geração, verifique uma única vez por ambiente se Python e LibreOffice estão instalados e acessíveis pelo PATH. No Windows, resolva `python`, `python3` ou `py` e `soffice` com `Get-Command` e valide os executáveis com uma consulta de versão de até 15 segundos. Um alias da Microsoft Store ou um comando que não execute não comprova uma instalação funcional. Reutilize os caminhos já validados durante a execução.

Se algum comando não estiver disponível, faça uma única busca direcionada nas instalações conhecidas: pastas do Python em `%LOCALAPPDATA%\Programs\Python` e `Program Files`, runtime Python fornecido pelo ambiente do Codex quando disponível, e pastas `LibreOffice\program` em `Program Files` e `Program Files (x86)`. Consulte também o PATH persistente do usuário, pois o processo atual pode estar usando uma versão antiga. Não faça varredura recursiva de todo o disco nem conclua que o programa está ausente apenas por não estar no PATH.

Ao encontrar uma instalação funcional e estável fora do PATH, configure o PATH do usuário adicionando somente a pasta do executável validado, preservando todas as entradas existentes, sua ordem e sem duplicatas. Respeite as permissões do ambiente e solicite a aprovação técnica exigida para essa gravação. Não sobrescreva o PATH inteiro com uma lista parcial, não altere o PATH do sistema e não adicione caminhos temporários ou versionados do cache do Codex ao PATH permanente. Para um runtime fornecido pelo Codex, use seu caminho absoluto na execução. Se o PATH já contiver a pasta, não grave novamente. Use o executável pelo caminho absoluto na sessão atual e informe que novos processos reconhecerão a alteração após reabrir o aplicativo. Valide a configuração uma única vez depois da mudança.

Se não encontrar uma instalação funcional de Python ou LibreOffice, informe qual programa está ausente e que deve ser instalado e disponibilizado no PATH para viabilizar o fluxo padrão e melhorar o desempenho operacional, evitando buscas e tentativas repetidas. Não prometa aceleração da conversão apenas por alterar o PATH. Não instale programas automaticamente sem solicitação do usuário. Interrompa a etapa dependente até a instalação; um Python funcional fornecido pelo ambiente pode atender à execução sem exigir outra instalação. Essa verificação conta como o diagnóstico direcionado permitido abaixo, sem iniciar uma nova sequência de buscas após a falha.

Antes de copiar, editar, substituir ou renderizar um arquivo, confirme que ele pode ser aberto com o acesso necessário. A existência isolada de um arquivo temporário `~$` não comprova bloqueio; valide o acesso ao DOCX de destino. Se o arquivo estiver aberto no Word, bloqueado por outro processo ou retornar `PermissionError`/erro de compartilhamento, interrompa imediatamente a execução e peça ao usuário que feche o arquivo para continuar. Não tente sobrescrever, renomear, criar uma versão alternativa, iniciar o renderizador ou repetir comandos enquanto o bloqueio persistir. Depois que o usuário confirmar o fechamento, verifique o acesso uma única vez e retome do ponto interrompido.

Reutilize os resultados de inspeções, hashes e inventários enquanto o arquivo não mudar. Agrupe verificações independentes em uma única etapa e não reabra nem reinspecione repetidamente o mesmo pacote OOXML sem uma alteração intermediária que justifique nova análise.

Faça as alterações solicitadas em um lote coerente, execute uma verificação estrutural após esse lote e renderize uma única vez a versão resultante. Faça nova renderização somente quando uma correção real tiver sido aplicada ao documento depois da inspeção anterior.

Use o LibreOffice configurado como renderizador padrão. Não tente automatizar o Microsoft Word como conversor alternativo, salvo pedido explícito do usuário. Se o LibreOffice não estiver disponível ou a renderização falhar por problema do ambiente, execute no máximo um diagnóstico direcionado, informe o bloqueio e pare; não encadeie conversores alternativos nem repita comandos equivalentes.

Toda conversão ou renderização deve ter limite de tempo explícito de até 120 segundos. Se o processo exceder esse limite, encerre apenas o processo iniciado para essa tentativa, informe em que etapa ocorreu a interrupção e aguarde orientação do usuário. Uma repetição automática só é permitida quando a causa tiver sido identificada e corrigida; nunca repita o mesmo comando sem mudança concreta nas condições de execução.

## 6. Fidelidade efetiva do texto e validação visual obrigatória

Estas regras se aplicam a todas as sete skills e aos respectivos scripts de geração.

### Antes de editar

- Valide hash, acesso, estrutura e inventário real do modelo, incluindo cabeçalhos, rodapés, campos, caixas de texto e imagens. Um hash correto não resolve instruções contraditórias sobre esse arquivo.
- Registre os campos editáveis e a formatação de cada trecho: rótulo, valor, texto corrido e destaques. Registre também o espaço disponível, quebras e distribuição das tabelas nas páginas.
- Resolva uma única vez o LibreOffice: caminho absoluto informado pelo usuário, variável `RELATORIO_SOFFICE`, PATH e instalações conhecidas da seção 5. Valide a versão com timeout e reutilize o caminho absoluto para modelo e saída. Não dependa de uma instalação empacotada quando o usuário disponibilizou uma instalação local. Caminho ausente no PATH não significa programa ausente. Não altere o PATH persistente se usar o executável por caminho absoluto já resolver a tarefa.
- Verifique acentos no XML decodificado em UTF-8. Caracteres mal exibidos no terminal não comprovam corrupção do DOCX. Não reescreva títulos ou textos estáticos com base apenas na exibição do console.

### Durante a edição

- Não atribua o novo parágrafo inteiro ao primeiro `w:t` ou `run` e esvazie os demais. Não use `paragraph.text` ou `cell.text` para reconstruir conteúdo formatado.
- Preserve os trechos de rótulo e substitua o valor nos trechos correspondentes. O texto deve continuar associado às propriedades corretas, incluindo estilos herdados, negrito, fonte, tamanho e espaçamento. Propriedades presentes em trechos vazios não comprovam preservação.
- Use `scripts/fidelidade_docx.py` como biblioteca para substituições simples com `substituir_em_trecho`. Ela recusa substituições que atravessam trechos; para conteúdo misto, mapeie explicitamente cada trecho e valide-o. Não contorne a recusa colapsando o parágrafo.
- Ajuste a redação ao espaço do campo, preservando fatos e valores. Não acrescente informações extensas em células curtas. Não reduza fonte nem altere dimensões de tabelas para fazê-las caber. Se não for possível acomodar o conteúdo autorizado, explique o conflito específico.
- Não remova cabeçalhos, desenhos, marcas ou assinaturas automaticamente. Alterações autorizadas nesses elementos precisam ser registradas e verificadas separadamente.
- A falta de arquivos de imagem não altera a obrigação de conservar o texto do cabeçalho; valide após a edição que nenhum texto institucional foi removido ou esvaziado por depender de um slot de imagem vazio.

### Depois da edição e antes de entregar

1. Execute `python scripts/fidelidade_docx.py MODELO.docx SAIDA.docx`. O verificador reprova mudanças estruturais, alterações em propriedades e perda de perfis de formatação associados a texto preenchido; sinaliza expansão acentuada dos campos. Código zero indica somente aprovação dos testes estruturais implementados, nunca aprovação visual ou equivalência completa da formatação herdada.
2. Toda reprovação exige correção ou uma exceção específica já autorizada, com comparação detalhada do elemento afetado. Não desabilite verificações globalmente. Expansões sinalizadas exigem revisão do campo no render.
3. Renderize modelo e saída com o mesmo executável, ambiente de fontes e parâmetros, em diretórios temporários distintos. Reutilize a renderização do modelo se seu hash e ambiente não mudaram. Inspecione todas as páginas de ambos, comparando posição, limites das tabelas, quebras, fontes, cabeçalhos e rodapés. Verifique formatação efetiva e legibilidade, não apenas contagens de elementos.
4. Reprove cortes, sobreposições, tabelas deslocadas, texto fora de células, mudanças inesperadas de paginação ou de identidade visual. Após uma correção real, renderize novamente a saída e repita a inspeção.
5. Se não houver renderização e inspeção de todas as páginas, a saída permanece rascunho não validado. Não a entregue como final nem afirme que a estilização foi preservada. Informe o bloqueio concreto; uma verificação estrutural não substitui a visual.
6. Confirme o hash original ao concluir e entregue apenas o DOCX aprovado. Mantenha logs e arquivos de inspeção fora de `outputs/`.

### Compatibilidade com Microsoft Word

Quando a edição usar manipulação direta de OOXML, reempacotamento ZIP ou quando houver qualquer indício de falha de abertura no Microsoft Word, normalize a cópia final antes da entrega com `python scripts/normalizar_docx_word.py SAIDA.docx --in-place`. O procedimento abre e salva uma cópia temporária pelo LibreOffice, valida o ZIP e reabre o resultado com `python-docx` antes da troca atômica. Depois da normalização, renderize e inspecione novamente todas as páginas. Nunca aplique a normalização ao template protegido.
