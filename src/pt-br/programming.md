# Programação

## 1. Requisitos básicos

Os itens a seguir são requisitos complementares de Programação.

### Aplicativos

- Git
- Visual Studio Code
- Android Studio

---

## 2. Configuração do ambiente

O ambiente de trabalho abaixo deve ser configurado antes do início oficial. Siga as instruções; em caso de dúvidas, consulte um administrador.

### Navegador de internet

Salve também os seguintes sites nos favoritos:

| Nome | Endereço |
|------|------|
| Programming Resources | https://www.firstinspires.org/resources/library/ftc/programming-resources |
| REV Robotics Documentation | https://docs.revrobotics.com/duo-control/hello-robot-java/welcome |
| Pedro Pathing | https://pedropathing.com/ |
| Robot Dashboard | http://192.168.43.1:8080/ |

### Git

O Git é a ferramenta de controle de versão dos arquivos de programa adotada pela nossa equipe. O Android Studio não vem com o Git, então é preciso instalá-lo e configurá-lo; escolha uma das duas formas a seguir.

**Forma 1 (baixar e instalar o Git dentro do Android Studio):**

1. Abra o Android Studio e entre nas configurações: no Windows/Linux, File → Settings; no macOS, Android Studio → Settings (ou Preferences)
2. No menu à esquerda, expanda Version Control e clique em Git
3. Se o Git não for detectado, a tela oferece um link de download; clique para baixar e instalar
4. Depois de instalar, confirme o caminho do Git em Path to Git executable (no Windows, `git.exe`) e clique em Test; quando aparecer Successful, clique em Apply e OK

**Forma 2 (instalar o Git separadamente e configurar o caminho no Android Studio):**

1. Acesse o site oficial [https://git-scm.com/downloads](https://git-scm.com/downloads) e baixe o instalador para o seu sistema (Windows / macOS / Linux)
2. Execute o instalador e avance com Next nas opções padrão até concluir
3. Abra o Android Studio e vá em Settings → Version Control → Git
4. Em Path to Git executable, digite ou selecione o caminho do Git (se as variáveis de ambiente estiverem configuradas, ele é detectado automaticamente)
5. Clique em Test; quando aparecer Successful, clique em Apply e OK

Para ativar o controle de versão no projeto atual: clique em VCS → Enable Version Control Integration..., escolha Git e clique em OK.

### Android Studio

O Android Studio é a ferramenta de programação adotada pela nossa equipe.

**Instalação e configuração do ambiente:**

1. Abra [https://developer.android.com/studio](https://developer.android.com/studio)
2. Clique em "Download Android Studio", baixe a versão correspondente e instale.

**No Windows, atenção durante a instalação:**

- Marque as duas caixas de seleção
- Escolha um caminho com espaço suficiente e que não será alterado

**Inicialização:**

- Escolha o modo "Standard"
- Ao aceitar os termos, marque "Accept"
- Mantenha as demais opções e clique em "Next"

**Instalação do pacote de idioma em português (opcional):**

1. Abra a página do [Portuguese (Brazil) Language Pack](https://plugins.jetbrains.com/plugin/23206-portuguese-brazil-language-pack)
2. Na tela inicial, abra "Plugins" → "Marketplace", pesquise "Portuguese (Brazil) Language Pack" e instale (ou baixe o pacote e use "Install Plugin from Disk")
3. Confirme que o plugin está ativado depois de carregar
4. Se quiser escolher idioma e região manualmente, abra "Customize" → "Language and Region", defina o idioma como "Português (Brasil)" e a região como "Americas"; depois reinicie o Android Studio

**Clonar o repositório:**

1. Clique em "GitHub" na lista de abas à esquerda e use "Log in with GitHub" para autorizar.
2. Escolha o repositório de programa correspondente à temporada atual (criado separadamente a cada temporada, com nome no formato `FTC-32477-<temporada>-Program`; antes da criação do repositório da nova temporada, confirme com um administrador)
3. Escolha uma pasta vazia, em um caminho que não vai mudar, e clique em "Clone"
4. Aguarde a conclusão do download; acompanhe pelo cartão "Build" na barra lateral esquerda ou pela barra de progresso no canto inferior direito

> [!warning] Em caso de problemas, consulte um administrador.

### Visual Studio Code

O Visual Studio Code é a ferramenta adotada pela nossa equipe para edição de código e consulta de histórico.

**Instalação e configuração do ambiente:**

1. Abra [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. Baixe a versão correspondente e instale
3. Se quiser a interface em português, instale o [pacote de idioma português (Brasil)](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-pt-BR).

---

## 3. Introdução às ferramentas

### Android Studio

Documentação oficial: [https://developer.android.com/studio/intro?hl=pt-br](https://developer.android.com/studio/intro?hl=pt-br)

Este projeto baseia-se na estrutura de aplicativo oficial do FTC: o programa de controle do robô é escrito em Java na pasta `TeamCode`, chamando as bibliotecas necessárias para a execução.

Para os conhecimentos básicos necessários no Android Studio, consulte os guias introdutórios da documentação oficial.

### Visual Studio Code

Documentação oficial: [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

A lógica de operação do Visual Studio Code é semelhante à do Android Studio e seu uso é menos frequente; para as operações de interface, consulte a seção do Android Studio.

### Robot Dashboard

- Conecte-se à rede Wi-Fi "`32477-RC`". Senha do Wi-Fi: pergunte ao administrador ou obtenha pelo Driver Hub.
- Endereço: [http://192.168.43.1:8080/](http://192.168.43.1:8080/) (acessível somente na rede local do robô)
- É a página web do módulo Wi-Fi embutido no Control Hub (nome oficial: Robot Controller Console), que oferece um painel gráfico para gerenciar o Control Hub.

Para os conhecimentos básicos necessários no Robot Dashboard, consulte os guias introdutórios da documentação oficial.

---

## 4. Fluxo de trabalho

O trabalho central da equipe de programação se divide em três partes:

- **Programa autônomo**: a lógica de controle da fase autônoma da temporada (Auto)
- **Programa teleoperado**: a lógica de operação da fase controlada por controle (TeleOp)
- **Configuração de sensores**: configuração de sensores diversos e do sistema de visão

> [!info] Operação do controle (Driver): o robô é operado com um controle de Xbox, e oficialmente apenas o modelo Xbox 360 é permitido; o Driver é escolhido pela equipe, e quem tem familiaridade com o controle leva vantagem.

### A depuração é o ponto central

> [!info] A dificuldade do desenvolvimento está principalmente na depuração. Caminhos autônomos, operação manual, parâmetros de PID, configuração de visão etc.: na maioria dos casos já existem pacotes prontos que podem ser reutilizados, e o foco do trabalho é ajustar e validar parâmetros.

O trabalho de depuração atravessa todo o fluxo de desenvolvimento:

1. **Análise de requisitos**: entender as regras e as tarefas da temporada atual
2. **Arquitetura**: projetar a estrutura geral do programa e a divisão em módulos
3. **Escrita do código**: escrever o código Java no Android Studio
4. **Controle de versão**: gerenciar as versões do código com Git
5. **Depuração**: ajustar caminhos autônomos, operação manual, parâmetros de PID e configuração de visão
6. **Testes e validação**: verificar as funções do programa no robô
7. **Revisão de código**: revisar e mesclar via GitHub
8. **Implantação**: publicar a versão final no Robot Controller

### Programação assistida por IA

> [!info] O desenvolvimento de programas pode contar com o apoio de ferramentas como agentes de IA. A capacidade central é **entender o código gerado pela IA, definir a direção das mudanças e dominar os métodos de depuração** — não é preciso escrever todo o código do zero.

- A lógica central das linguagens de programação (como laços `for` e `while`) é universal, mudando apenas a sintaxe; quem tem base em C++ se adapta rápido ao desenvolvimento em Java

---

## 5. Fundamentos de colaboração no GitHub

> [!info] Esta seção cobre o mínimo necessário para usar o GitHub: visualizar repositórios, baixar arquivos, enviar feedback, modificar conteúdo, colaborar e encontrar projetos de código aberto. A explicação completa está nos links para a documentação oficial no fim da seção. A interface usa principalmente botões em inglês; no texto, os termos são indicados no formato "inglês (português)".

### O que é o GitHub

O GitHub é uma **plataforma de hospedagem de código e colaboração** baseada no Git: o código fica na nuvem (repositório) com o histórico completo de alterações (commits), várias pessoas podem colaborar no mesmo projeto (branches, pull requests) e a plataforma ainda oferece issues, automação (Actions), hospedagem de sites (Pages) e outras ferramentas.

Principais usos do GitHub na nossa equipe:

- **Armazenar os programas das temporadas**: cria-se um repositório público separado a cada temporada (criado como fork do template oficial do SDK); ao fim da temporada, o repositório é arquivado como somente leitura. Quando o repositório da nova temporada for criado, ele será acrescentado à tabela desta seção.
- **Manter o Guia de Início Rápido**: os arquivos-fonte e os scripts de build ficam no repositório público `ftc32477/quick-start-guide`.
- **Publicar o site da equipe**: o repositório de publicação do site é `ftc32477/ftc32477.github.io`; o conteúdo de cada seção é compilado pelo GitHub Actions a partir do respectivo repositório-fonte e publicado no subcaminho correspondente (este guia → `/docs/`); no momento, o caminho raiz redireciona para `/docs/`. Futuramente, cada tipo de recurso terá seu próprio repositório-fonte, com publicação no respectivo subcaminho.
- **Encontrar projetos de código aberto**: pesquisar ferramentas de engenharia em geral e códigos e soluções compartilhados pela comunidade FTC.

**Conta e organização**: use a sua própria conta (o processo de registro está em "Essenciais da equipe"); um administrador envia o convite para entrar na organização `ftc32477`. Os repositórios pertencem à organização, e as permissões de operação são atribuídas pelos administradores conforme o papel:

| Papel | O que pode fazer (resumo) |
|------|------|
| Read (leitura) | Visualizar e discutir projetos |
| Triage (triagem) | Gerenciar issues e pull requests, mas sem permissão de gravação no código |
| Write (gravação) | Enviar conteúdo para o repositório |
| Maintain (manutenção) | Gerenciar o repositório, mas sem operações sensíveis ou destrutivas |
| Admin (administrador) | Permissão total, incluindo excluir repositórios |

> [!warning] Sem permissão de gravação, envie as alterações por pull request ou deixe a cargo dos mantenedores; se não tiver certeza da sua permissão, trabalhe em modo somente leitura e não tente testar nem contornar as restrições de permissão.

### Glossário rápido

| Termo | Significado (em uma frase) |
|------|------|
| Repository (repositório) | Local onde ficam os arquivos do projeto e o histórico completo de alterações |
| Commit | Registro de um conjunto de alterações com descrição, que compõe o histórico |
| Branch (ramificação) | Linha de desenvolvimento paralela dentro do repositório; as alterações são feitas nela antes da mesclagem |
| Clone (clonagem) | Cópia completa do repositório para o computador local |
| Fork (bifurcação) | Cópia de um repositório de outra pessoa na sua conta; as alterações não afetam o repositório original |
| Pull request (PR) | Mecanismo para solicitar revisão e mesclagem das alterações de um branch; o centro da colaboração |
| Issue (problema) | Publicação de discussão para perguntas, relatos de erro e sugestões |
| Release (versão) | Versão oficial numerada, com arquivos para download (como o PDF do guia) |
| Star (estrela) | Marcação de favorito e curtida; também serve para avaliar a popularidade do projeto |
| Watch (acompanhar) | Inscrição para receber notificações de atividade do repositório |
| Actions | Pipeline de automação do GitHub (neste projeto, usado para compilar e publicar o site) |
| Pages | Hospedagem de sites estáticos do GitHub (é o que publica o site deste projeto) |
| README | Documento de apresentação na página inicial do repositório; deve ser lido primeiro |

### Mapa dos repositórios da equipe

| Repositório | Descrição | Como modificar |
|------|------|----------|
| `quick-start-guide` | Arquivos-fonte do guia, scripts de build e artefatos do site (público) | Envie um pull request ou deixe a cargo dos mantenedores |
| `ftc32477.github.io` | Repositório de publicação do site da equipe (público); o conteúdo é enviado automaticamente pelos repositórios-fonte | Não modifique diretamente |
| `.github` | Materiais da página da organização, como a descrição (público) | Envie um pull request ou deixe a cargo dos mantenedores |
| `FTC-32477-<temporada>-Program` | Repositório do programa da temporada (público): criado separadamente a cada temporada, com as temporadas antigas arquivadas como somente leitura; o nome específico será acrescentado quando o repositório da nova temporada for criado | Conforme a divisão interna da equipe de programação |

> [!danger] **Área proibida: repositório de publicação**: todo o conteúdo de `ftc32477.github.io` vem dos respectivos repositórios-fonte e é enviado automaticamente pelo GitHub Actions; alterações diretas são sobrescritas na próxima publicação. Não clique em editar, fazer commit nem excluir nada nesse repositório ou em qualquer conteúdo gerado. Qualquer problema do site deve ser tratado no repositório-fonte correspondente (para este guia, `quick-start-guide`).

### Navegação e download

1. Abra a página da organização [https://github.com/ftc32477](https://github.com/ftc32477) e entre no repositório pela lista Repositories
2. Leia primeiro o **README** na página inicial do repositório (finalidade e modo de uso do projeto); à direita, a seção About traz a descrição e o link da página inicial
3. Abas na parte superior (a visibilidade depende da sua permissão):
   - **Code**: lista de arquivos e histórico de commits
   - **Issues**: problemas e sugestões
   - **Pull requests**: alterações aguardando revisão
   - **Actions**: registros de builds e publicações automatizadas
   - **Releases**: versões oficiais e arquivos para download
4. Para baixar o repositório inteiro: Code → **Download ZIP**
5. Para baixar o PDF do guia: abra **Releases**, escolha a versão e baixe o idioma correspondente em Assets
6. Para consultar o histórico: na página Code, entre na lista **Commits** → clique em um commit para ver as alterações específicas (diff)

### Relatar problemas (Issue)

Ao encontrar falhas, erros na documentação ou tiver sugestões, envie o feedback por uma issue:

1. Abra a aba **Issues** do repositório desejado e pesquise primeiro se já existe um problema igual
2. Clique em **New issue** e resuma o problema em um título de uma frase
3. No corpo, descreva com clareza: **o que aconteceu**, **o resultado esperado**, **como reproduzir** (passos) e capturas de tela relevantes (remova antes os dados pessoais)
4. Depois de enviar, acompanhe as respostas; quando o problema for resolvido, o mantenedor o fecha

> [!info] Canal fixo para feedback do guia: [https://github.com/ftc32477/quick-start-guide/issues](https://github.com/ftc32477/quick-start-guide/issues)

### Edição pela interface web (editar → abrir PR)

Sem permissão de gravação, o GitHub converte automaticamente as alterações feitas na interface web em "fork + pull request (PR)":

1. Depois de entrar na sua conta, abra o arquivo que deseja modificar (como um `.md` em `src/pt-br/` do guia)
2. Clique no ícone de lápis **Edit this file** no canto superior direito do arquivo
3. Se você não tiver permissão de gravação, a página informará que um fork será criado automaticamente; confirme
4. Faça as alterações e escreva uma descrição clara em **Commit changes**
5. Selecione **Create a new branch for this commit and start a pull request**, com um nome de branch como `fix/typo-member`
6. No formulário de PR que abrir, explique o que foi alterado e por quê, e clique em **Create pull request**
7. Aguarde a revisão do mantenedor; se houver comentários, ajuste conforme indicado; depois da mesclagem, a alteração entra em vigor

> [!warning] Cada PR deve tratar de um único assunto; não modifique arquivos que você não conhece (scripts de build, artefatos gerados etc.); não envie alterações ao repositório de publicação.

### Colaboração local

Desenvolver com o repositório clonado localmente é a forma mais usada. O pré-requisito é ter o Git instalado no computador (ver "2. Configuração do ambiente"). Os comandos mais usados são:

```bash
# Clone o repositório para o computador local
git clone https://github.com/ftc32477/quick-start-guide.git
cd quick-start-guide

# Antes de começar, baixe as últimas alterações
git pull

# Crie um branch para este trabalho
git switch -c feat/my-feature

# Depois de alterar os arquivos: ver o status, preparar e fazer o commit
git status
git add <arquivo>
git commit -m "descrição da alteração"

# Envie o branch para o GitHub
git push -u origin feat/my-feature
```

Depois de enviar, crie um pull request para esse branch no GitHub e aguarde a revisão e a mesclagem. O Android Studio e o Visual Studio Code oferecem operações gráficas equivalentes (ver "2. Configuração do ambiente"), com as quais é possível executar os mesmos passos pela interface.

> [!warning] Três regras: **faça pull antes de começar**; **cada commit trata de um único assunto, com uma descrição clara**; **envie para o seu próprio branch, nunca diretamente para a main**.

**Fork e sincronização com o upstream (ao participar de projetos externos)**: um fork não se atualiza automaticamente. Adicione primeiro o repositório original como upstream: `git remote add upstream <URL do repositório original>` e depois sincronize com `git fetch upstream` e uma operação de merge (detalhes na seção "Sincronizar um fork" da documentação oficial).

### Comunidade de código aberto (pesquisa, avaliação e contribuição)

**Pesquisa** (a caixa de busca aceita qualificadores, que podem ser combinados):

- `topic:ftc`, `topic:first-tech-challenge`, `topic:ftc-robot`: porta de entrada geral dos projetos da comunidade FTC
- `ftc language:Java sort:updated`: projetos Java ainda mantidos recentemente
- `"FIRST Tech Challenge" in:readme`: projetos que mencionam o FTC no README

Recursos de código aberto usados com frequência no FTC (todos disponíveis no GitHub):

| Projeto | Uso |
|------|------|
| FIRST-Tech-Challenge/FtcRobotController | SDK oficial do FTC e exemplos |
| FTCLib/FTCLib | Biblioteca de utilitários comum no FTC |
| acmerobotics/road-runner | Planejamento de movimento e seguimento de trajetória |
| Pedro-Pathing/PedroPathing | Planejamento de trajetória |
| acmerobotics/ftc-dashboard | Painel de depuração |
| OpenFTC/EasyOpenCV | Processamento de visão |
| the-orange-alliance, ftc-scout/ftc-scout | Dados e estatísticas de competições |

**Como avaliar se um repositório é utilizável (cinco critérios)**: data do último commit (se ainda é mantido), qualidade do README e da documentação, licença (License), atividade nas Issues e existência de releases oficiais.

**Resumo das licenças** (leitura obrigatória antes de usar código ou materiais de terceiros):

| Licença | Explicação em uma frase |
|------|------|
| MIT | A mais permissiva: uso livre desde que o aviso de copyright seja mantido |
| Apache-2.0 | Também permissiva, com exigências adicionais de licença de patentes e aviso de alterações |
| GPL-3.0 | Exige que as obras derivadas também sejam de código aberto |
| Sem licença | Por padrão, "todos os direitos reservados": **não** é possível copiar diretamente; contate o autor primeiro |

**Como contribuir**: leia primeiro o `CONTRIBUTING.md` (guia de contribuição) e o código de conduta na raiz do projeto; para mudanças incertas, abra uma Issue para discutir; para correções pequenas, envie pelo fluxo "editar → abrir PR" descrito acima.

> [!warning] Segurança: não execute scripts ou arquivos executáveis de origem desconhecida; não envie API keys, senhas nem tokens para Issues ou repositórios; desconfie de comandos de instalação como `curl | bash`.

### Avisos sobre operações perigosas

> [!danger] As operações abaixo podem causar perdas irreversíveis; membros comuns não devem executá-las em nenhuma hipótese; se for realmente necessário, confirme antes com um administrador.

- Modificar diretamente o repositório de publicação `ftc32477.github.io` (as alterações serão sobrescritas e afetarão o site oficial)
- `git push --force`: sobrescreve o histórico remoto à força e pode fazer com que os commits dos colegas de equipe desapareçam
- `git reset --hard`: descarta alterações locais ainda não enviadas, e é difícil recuperá-las
- Excluir branches ou repositórios, ou alterar a visibilidade, o nome ou a propriedade de um repositório
- Enviar chaves, senhas ou tokens para um repositório (depois de públicos, eles permanecem no histórico mesmo se excluídos; revogue-os e recrie-os imediatamente)
- Publicar materiais internos ou informações pessoais em Issues, PRs ou repositórios públicos (e-mail, endereço, dados pessoais em capturas de tela)
- Executar ou mesclar código de origem desconhecida

> [!info] Segurança da conta: não compartilhe a sua conta; o GitHub está exigindo a ativação da verificação em duas etapas (2FA) de contas que contribuem com código, então siga as instruções para ativá-la; crie tokens de acesso pessoal (personal access tokens) com o mínimo de permissões e nunca os escreva no código nem em repositórios.

### Lista de exercícios

1. Abra a página da organização, entre no repositório `quick-start-guide` e explique, com base no README, o que o projeto faz
2. Baixe em Releases o PDF do guia em qualquer idioma
3. No histórico de commits, encontre a alteração mais recente e diga o que ela mudou
4. Pesquise "PDF" nas Issues e veja se há algum problema relacionado
5. Pelo fluxo "editar → abrir PR", corrija um erro de digitação e abra um pull request

### Links para a documentação oficial

Para usos mais avançados, consulte a documentação oficial conforme a necessidade:

- Início rápido do GitHub: [https://docs.github.com/pt/get-started/quickstart](https://docs.github.com/pt/get-started/quickstart)
- Gravar e armazenar seu código (branch/commit/PR): [https://docs.github.com/pt/get-started/start-your-journey/writing-and-storing-your-code](https://docs.github.com/pt/get-started/start-your-journey/writing-and-storing-your-code)
- Guia rápido do Git: [https://docs.github.com/pt/get-started/git-basics/git-cheatsheet](https://docs.github.com/pt/get-started/git-basics/git-cheatsheet)
- Sintaxe de pesquisa: [https://docs.github.com/pt/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax](https://docs.github.com/pt/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax)
- Funções de repositório para uma organização: [https://docs.github.com/pt/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization](https://docs.github.com/pt/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization)
- Cursos interativos (em inglês): [https://skills.github.com/](https://skills.github.com/)

> [!info] Em caso de dúvida sobre alguma operação, consulte primeiro um administrador ou pergunte nas Issues.
