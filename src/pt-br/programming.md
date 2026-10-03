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
2. Escolha o repositório de código da temporada atual (por exemplo, `ftc32477/FTC-32477-Decode-Program`)
3. Escolha uma pasta vazia, em um caminho que não vai mudar, e clique em "Clone"
4. Aguarde a conclusão do download; acompanhe pelo cartão "Build" na barra lateral esquerda ou pela barra de progresso no canto inferior direito

> [!warning] Em caso de problemas, consulte um administrador.

### Visual Studio Code

O Visual Studio Code é a ferramenta adotada pela nossa equipe para edição de código e consulta de histórico.

**Instalação e configuração do ambiente:**

1. Abra [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. Baixe a versão correspondente e instale
3. Para traduzir a interface, instale o [pacote de idioma português (Brasil)](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-pt-BR).

---

## 3. Introdução às ferramentas

### Android Studio

Documentação oficial: [https://developer.android.com/studio/intro?hl=pt-br](https://developer.android.com/studio/intro?hl=pt-br)

Neste projeto, usamos a estrutura de aplicativo oficial do FTC e escrevemos, na pasta `TeamCode`, o programa de controle do robô em Java, chamando as bibliotecas de que o robô precisa para funcionar.

Para os conhecimentos básicos necessários no Android Studio, consulte os guias introdutórios da documentação oficial.

### Visual Studio Code

Documentação oficial: [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

Como a lógica de operação do Visual Studio Code é parecida com a do Android Studio, e o primeiro é usado com menos frequência neste projeto, consulte a seção do Android Studio para orientações de interface; não repetimos os detalhes aqui.

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

> [!info] Operação do controle (Driver): o robô é operado com um controle de Xbox, e oficialmente apenas o modelo Xbox 360 é permitido; o Driver é escolhido internamente pelo critério "quem manda bem, joga", e alunos que se dão bem em jogos com controle levam vantagem natural.

### A depuração é o ponto central

> [!info] A verdadeira dificuldade do desenvolvimento está na depuração. Caminhos autônomos, operação manual, parâmetros de PID, configuração de visão — a maioria dos sensores tem pacotes prontos que podem ser reutilizados; o que você realmente faz é "ajustar".

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

> [!info] Hoje programar não é tão difícil: é possível usar ferramentas como agentes de IA como apoio. A capacidade central é **entender o código gerado pela IA, definir a direção das mudanças e dominar a depuração** — não é preciso escrever todo o código do zero.

- A lógica central das linguagens de programação (como laços `for` e `while`) é universal, mudando apenas a sintaxe; quem tem base em C++ se adapta rápido ao desenvolvimento em Java
