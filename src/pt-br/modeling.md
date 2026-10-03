# Modelagem e design

## 1. Requisitos básicos

Os itens a seguir são requisitos complementares de Modelagem e design.

### Aplicativos

- Navegador de internet (Chrome, Edge ou Safari)
- LocalSend
- Biblioteca de peças FTC do Onshape — [https://ftconshape.com/](https://ftconshape.com/) (mantida pela FIRST em parceria com a PTC; envie um e-mail para FIRST@ptc.com para entrar na pasta compartilhada)
- Plugin da biblioteca de peças FTC Insert Tool — [https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba](https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba) (instale pela Onshape App Store: Subscribe → Get for Free)

### Contas online

- CycleZLab — [https://www.cyclezlab.com/](https://www.cyclezlab.com/) (gratuito, é preciso solicitar entrada)

---

## 2. Configuração do ambiente

O ambiente de trabalho abaixo deve ser configurado antes do início oficial. Siga as instruções; em caso de dúvidas, consulte um administrador.

### Navegador de internet

Salve também os seguintes sites nos favoritos:

| Nome | Endereço |
|------|------|
| goBILDA | https://www.gobilda.com/ |
| REV Robotics | https://www.revrobotics.com/ |
| CycleZLab | https://www.cyclezlab.com/ |
| Onshape para Educação | https://www.onshape.com/en/education/ |

### Registro da conta Onshape

O Onshape é a plataforma de modelagem CAD em nuvem adotada pela nossa equipe. Em comparação com softwares industriais como o SolidWorks, o Onshape exige pouco do computador, facilita o compartilhamento de projetos entre dispositivos, é fácil de aprender e tem suporte oficial da FIRST — além de ser completo em recursos, é ideal para aprender modelagem CAD e desenvolver projetos.

**Registro:**

1. Abra [https://www.onshape.com/en/education/](https://www.onshape.com/en/education/) e cadastre uma conta educacional
2. Preencha nome (First name), sobrenome (Last name) e e-mail

> [!warning] Não use provedores de e-mail chineses, como o QQ: é provável que o código de verificação não chegue. Recomendamos @gmail.com ou @outlook.com.

3. Na tela seguinte, selecione o perfil "Student", o nível escolar "Grade School / K-12 (Ages <18)" e a data de nascimento; depois clique em avançar
4. Preencha as informações a seguir:
   - Nome da escola: BEIJING NATIONAL DAY EXPERIMENTAL SCHOOL
   - Site da escola: [https://sysyzx.bjhdedu.cn/](https://sysyzx.bjhdedu.cn/)
   - Ano previsto de formatura
   - Motivo do cadastro: I am a member of FTC Team 32477, and I registered this account to use the team's modeling tools. (use esta frase se não souber o que escrever)
   - Marque os três termos de concordância para concluir o cadastro
5. Verifique seu e-mail para confirmar o cadastro

> [!info] Após concluir o cadastro, informe sua conta a um administrador para que ele adicione você à pasta compartilhada da equipe.

**Dúvidas frequentes:**

- Erro de reCAPTCHA na última etapa: o serviço de verificação humana não respondeu. Tente trocar de rede e garanta que o serviço reCAPTCHA esteja acessível
- Código de verificação não recebido: se esperar mais de 3 minutos, tente outro e-mail (Outlook ou Gmail, não use QQ)

### Configuração de preferências do Onshape

1. Entre no espaço de trabalho, clique no ícone da conta no canto superior direito e escolha a primeira opção do menu, "Minha conta"
2. No menu à direita, escolha a terceira opção a partir do topo, "Preferências", altere a primeira opção de idioma para "Português (Brasil)" e clique em salvar
3. No mesmo menu, altere a opção de unidades para o sistema métrico (no ambiente de trabalho da equipe, o comprimento padrão é em milímetros)

> [!info] As alterações acima só valem para documentos criados depois da mudança; documentos antigos mantêm as unidades originais.

4. Ajuste seu perfil pessoal como preferir

### Plugins do Onshape

Por ser uma plataforma em nuvem, o Onshape tem um ecossistema rico de plugins compartilhados, disponíveis na Onshape App Store, em sites de terceiros e por compartilhamento direto.

Os plugins mais usados pela equipe incluem (apenas exemplos):

- **Biblioteca de peças FTC do Onshape** (essencial; veja "1. Requisitos básicos")
- **Lighten** (recurso personalizado que enxuga a estrutura para deixar a peça mais leve)
- **Spur gear** (recurso personalizado, gerador de engrenagens)
- **HTD Pulley Generator** (derivado de outro documento, gerador de polias de correia dentada)

---

## 3. Pontos essenciais da modelagem

### Projeto e montagem de peças

Ao modelar em 3D no Onshape, preste atenção especial aos pontos a seguir:

- **Precisão dimensional**: garanta que todas as dimensões do modelo correspondam às peças reais
- **Relações de montagem**: defina corretamente os encaixes entre peças (Encaixes/Mates e Conectores de Encaixe/Mate Connectors)
- **Verificação de interferência**: faça a checagem de interferências após a montagem
- **Nomenclatura de peças**: nomeie peças e montagens seguindo um padrão unificado

### Documentos de projeto e espaço de trabalho

Ao desenvolver projetos da equipe, crie os documentos na pasta compartilhada da equipe para que outros membros tenham acesso. Se você ainda não foi adicionado, fale com um administrador para entrar na pasta compartilhada.

1. No menu à esquerda da sua área de trabalho pessoal, selecione "Compartilhados comigo" e abra a pasta "32477": ali você pode criar um novo documento ou abrir um documento já criado pela equipe (um documento é um projeto)
2. Para criar um novo projeto: clique no botão azul de criação no canto superior esquerdo, escolha "Documento" e aguarde a criação e a abertura

Depois de entrar no espaço de trabalho, você verá as abas "Estúdio de Peças (Part Studio)" e "Montagem (Assembly)" na parte inferior (clique no sinal de mais ao lado das abas para criar novas):

- **Estúdio de Peças**: a área onde uma peça individual é modelada (corresponde às etapas de esboço e peça do fluxo CAD); as peças são criadas com restrições de esboço
- **Montagem**: a área onde as peças feitas no Estúdio de Peças ou peças prontas da biblioteca são unidas (corresponde à etapa de montagem do fluxo CAD)

Um documento pode conter qualquer número de Montagens e Estúdios de Peças. Para facilitar a edição e o gerenciamento: modele, se possível, apenas uma peça por Estúdio de Peças; monte o robô por subsistemas e, no final, junte tudo em uma montagem principal.

### Fluxo básico de modelagem

Como manual introdutório, aqui apresentamos apenas as operações e o fluxo mais básicos do Onshape.

#### Desenho do esboço

No Estúdio de Peças, crie um esboço, escolha um plano de referência e desenhe o contorno com ferramentas como linha, retângulo e círculo; depois fixe a forma com cotas e restrições geométricas (como horizontal, vertical e tangente). Procure deixar o esboço totalmente restringido para que as operações de recurso seguintes sejam confiáveis.

#### Criação de peças

Concluído o esboço, use ferramentas de recurso como extrusão, revolução e varredura para transformar o contorno 2D em um sólido 3D e refine a peça com furos, chanfros e arredondamentos. Todos os recursos ficam registrados em ordem na lista de recursos e podem ser retrocedidos e editados a qualquer momento.

#### Montagem de peças

Na Montagem, insira peças feitas no Estúdio de Peças ou peças prontas da biblioteca e conecte-as com Encaixes e Conectores de Encaixe conforme as relações. Depois de montar, verifique se o movimento é suave e se não há interferências.

#### Uso das ferramentas

O Onshape oferece ferramentas de análise como medição, vista de corte e propriedades de massa, permitindo conferir dimensões e peso a qualquer momento durante a modelagem; o menu de clique com o botão direito também traz atalhos como ocultar, isolar e renomear.

### Resistência do modelo e experiência de design

A resistência de peças impressas em 3D depende do material e da geometria. Estes são conceitos de design estrutural usados com frequência:

- **Peças estruturais principais** (como vigas e placas estruturais): imprima em PETG-CF sempre que possível (parâmetros no capítulo Hardware e construção), com espessura mínima de 4 mm
- **Peças de guia** (como trilhas de esferas e batentes estruturais): PLA é aceitável, com parede mínima de 2 mm
- **Peças de proteção e decoração** (como painéis laterais): parede mínima de 1,5 mm
- Para chapas ou estruturas mais frágeis, como o acrílico, evite furos muito próximos (espaçamento entre furos menor que 3 mm); nas ligações estruturais que recebem carga, a largura deve ser de pelo menos 7 mm
- Evite cantos vivos nas peças; arredonde-os com filetes para impedir que a concentração de tensão cause trincas

> [!info] Os dados acima são apenas referência; os parâmetros reais precisam ser ajustados e validados com peças físicas.

### Estratégia de design e referências de temporada

- Ao conceber o robô, divida as tarefas do desafio em itens menores, pense na estrutura de cada item separadamente e só depois combine tudo
- Antes de modelar de verdade, peça opiniões dos colegas e baseie o projeto na estratégia de pontuação da equipe
- Depois de concluir o modelo do robô inteiro, pense no processo real de montagem: para parafusos e pontos de difícil acesso, deixe canais de instalação e espaço para a passagem de cabos
- Considere projetar estruturas modulares, que facilitam reparos e otimizações posteriores
- Na versão final, prefira estruturas integradas e reduza pequenas estruturas desnecessárias, para ganhar resistência geral e leveza

**Referências de calendário:**

- No cronograma, o primeiro projeto pode ser simples, mas precisa ser concluído e construído o quanto antes, deixando tempo para depuração do programa e treino do Driver, além de testar a estrutura fisicamente para iterar e otimizar; antes dos torneios classificatórios, um robô apto a competir deve passar por pelo menos 3 iterações (referência)
- Acompanhe as equipes estrangeiras: a comunidade FTC tem eventos como "Robot in 30 Hours Reveal | FTC", e as equipes podem divulgar seus projetos da nova temporada a qualquer momento; você também pode usar como referência projetos de equipes de FRC, VEX e outras competições
- A maioria dos arquivos de modelagem de outras equipes é compartilhada publicamente, e pedir os modelos diretamente normalmente não é recusado; estude bons projetos para melhorar o seu — a experiência de equipes fortes, como a Beijing National Day School (campus principal), merece atenção especial

### Recursos de aprendizado do Onshape

Como plataforma profissional de modelagem, o Onshape tem recursos oficiais completos de aprendizado: [https://learn.onshape.com/](https://learn.onshape.com/); plataformas de vídeo como Bilibili (哔哩哔哩) e YouTube também têm muitos tutoriais.

- Como os fluxos de trabalho dos softwares CAD são parecidos (esboço, peça, montagem), tutoriais de SolidWorks, Autodesk Fusion e outros programas também têm valor de aprendizado: ajudam a desenvolver a noção espacial das peças e a familiaridade com o fluxo de modelagem
- Lembre-se de que a prática vale mais que a teoria: procure alguns modelos no Bilibili (哔哩哔哩) para reproduzir, tente modelar sozinho primeiro e só veja o tutorial se realmente travar; no dia a dia, observe e reflita sobre como modelar pequenas estruturas
- Para a competição FTC, estude bastante os bons projetos de outras equipes: a maioria das equipes fortes tem site próprio e abre seus projetos. Pesquise o número de uma equipe FTC no YouTube ou no Google para achar o site oficial, ou veja modelos de outras equipes em sites como o CycleZLab

> [!info] Em caso de dúvidas, consulte um veterano de modelagem ou pesquise na internet.

### Bibliotecas de peças comuns do FTC

Fornecedores de peças e plataformas de recursos usados com frequência no FTC:

- **goBILDA**: oferece uma linha completa de peças estruturais para FTC
- **REV Robotics**: oferece módulos de controle eletrônico e peças estruturais
- **CycleZLab**: plataforma da comunidade de robótica da FIRST (arquivo de CAD, código e registros de construção)

### Padrões de projeto

- Use unidades métricas (mm)
- Deixe folga adequada em todas as peças impressas em 3D (recomendado: 0,2–0,3 mm)
- Formatos de exportação: arquivos STEP para usinagem, STL para impressão 3D e 3MF para fatiamento e impressão
