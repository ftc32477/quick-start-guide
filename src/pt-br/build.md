# Hardware e construção

## 1. Requisitos básicos

Os itens a seguir são requisitos complementares de Hardware e construção.

### Aplicativos

- Bambu Studio
- RD Works V8

### Contas online

- E-mail (recomendamos @gmail.com ou @outlook.com)
- Bambu Studio — [https://bambulab.cn/](https://bambulab.cn/)
- Onshape — [https://www.onshape.com/](https://www.onshape.com/)
- CycleZLab — [https://www.cyclezlab.com/](https://www.cyclezlab.com/)

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

### Bambu Studio

O Bambu Studio é a solução de impressão 3D adotada pela nossa equipe.

**Registro:**

1. Abra [https://bambulab.cn/](https://bambulab.cn/), clique no canto superior direito e registre uma conta com número de celular ou outro método.

**Instalação e configuração do ambiente:**

1. Abra [https://bambulab.cn/en/download/studio](https://bambulab.cn/en/download/studio)
2. Escolha a versão adequada, baixe e instale.

**Atenção:**

- No Windows, você pode alterar o diretório de instalação, desde que o caminho termine em `..\Bambu Studio\`. Ao concluir a instalação, marque as opções "abrir arquivos .3mf com o Bambu Studio", "abrir arquivos .stl com o Bambu Studio" e "abrir arquivos .step/.stp com o Bambu Studio".
- No macOS, basta arrastar o `BambuStudio.app` para a pasta Aplicativos.
- Abra o Bambu Studio. Na tela de login, escolha "China continental". Em impressoras, selecione pelo menos a **Bambu Lab P1S** e a **Bambu Lab P2S**; materiais podem ficar na configuração padrão. Marque "Instalar plugin de rede do Bambu".
- Faça login na conta Bambu com número de celular ou outro método.

### RD Works V8

> [!danger] **Atenção:** instalar este programa no macOS não é nada recomendado; seria necessário usar uma máquina virtual como Parallels Desktop, VMware Fusion ou CrossOver.

O RD Works V8 é o software que acompanha a cortadora a laser adotada pela nossa equipe.

**Instalação e configuração do ambiente:**

1. Obtenha o instalador `RDWorksV8Setup.exe` com um administrador ou com o professor orientador, abra-o e clique em "Install".
2. Você pode marcar "posicionar manualmente o caminho de instalação" para alterar o local.
3. Conecte o computador à cortadora a laser e clique em "Instalar driver USB".
4. Mantenha as demais opções padrão.

---

## 3. Introdução a ferramentas e materiais

### Ferramentas comuns

> [!danger] Antes de usar qualquer ferramenta manual, verifique se ela está em bom estado (por exemplo, se o cabo está solto ou se a mandíbula está lascada) e use luvas de proteção ou óculos de proteção quando necessário.

> [!info] Aqui listamos apenas as ferramentas mais usadas. As demais serão reunidas no apêndice "Lista de ferramentas", que será ampliado continuamente.

#### Chave Allen (sextavada)

Ferramenta em L ou T de seção hexagonal, usada para girar parafusos com sextavado interno. Ao usar, insira completamente a ponta curta ou longa no encaixe hexagonal do parafuso: girar no sentido horário aperta; no sentido anti-horário, solta. Chaves com cabo em T costumam ser usadas para dar mais alavanca ou trabalhar em furos profundos.

> [!info] Nossos tamanhos mais usados são M3 e M4; mantenha sempre os dois por perto.

#### Soquete

Ferramenta cilíndrica de aperto com interior hexagonal, capaz de envolver porcas ou cabeças de parafuso. Ao usar, encaixe o soquete na vertical sobre a porca e gire com o cabo. A vantagem é a grande área de contato, que reduz o deslizamento, e a facilidade de trabalhar em espaços apertados onde uma chave comum não gira.

#### Chave inglesa

Chave universal com abertura ajustável dentro de um intervalo, adequada para porcas hexagonais de diferentes tamanhos. Ao usar, gire a rosca sem fim para ajustar a abertura até ela encostar nos lados opostos da porca. Além disso, garanta que a mandíbula fixa receba o esforço principal — a força deve ser aplicada na direção da mandíbula fixa — para evitar que a chave quebre ou escorregue.

#### Alicate de bico chato

Ferramenta de preensão com bico achatado, geralmente com dentes finos internos para aumentar o atrito. Ao usar, serve para dobrar chapas metálicas finas, segurar peças pequenas ou dar apoio durante a montagem.

#### Alicate de bico fino

Alicate de bico longo e cônico, ideal para espaços estreitos. Ao usar, costuma segurar peças pequenas, dobrar fios finos ou retirar objetos presos em circuitos e estruturas densas. A base do bico geralmente tem lâmina de corte, podendo ser usado também como alicate de corte.

#### Alicate decapador

Ferramenta específica para remover o isolamento dos fios sem ferir o condutor metálico. Ao usar, escolha o entalhe correspondente à espessura do fio, encaixe o fio no entalhe, aperte o cabo, gire levemente e puxe para fora para desencapar.

#### Martelo de unha

Ferramenta para golpear objetos e movê-los ou deformá-los. Uma face é plana, para bater, e a outra tem formato em V, para arrancar pregos. Ao usar, segure a extremidade do cabo para obter o máximo de torque. Ao bater, mantenha a face plana paralela à superfície do alvo para evitar escorregões laterais.

#### Trena

Fita métrica metálica flexível com mola de recolhimento, usada para medir distâncias maiores ou dimensões não lineares. Ao usar, puxe a fita e prenda o gancho na borda do objeto ou apoie-o em uma superfície de referência. Leia as marcações e, ao terminar, pressione a trava ou deixe a fita recolher sozinha. Observe que o gancho tem uma pequena folga; isso compensa a espessura do gancho para que as medições internas e externas sejam consistentes.

#### Paquímetro

As partes principais do paquímetro são a escala principal A e a escala móvel (vernier) B, que desliza sobre ela.

- **Princípio**: o paquímetro usa a diferença fixa entre a menor divisão da escala principal (1 mm) e a da escala móvel para aumentar a precisão. Os mais comuns têm 10, 20 ou 50 divisões.
- **Leitura**: primeiro leia a escala principal, conforme a posição do zero da escala móvel; depois veja qual linha da escala móvel coincide com uma linha da escala principal; combine as duas leituras para obter o comprimento medido.
- **Uso**: quando as duas garras de medição externa (ou interna) se tocam, o zero da escala móvel coincide com o zero da escala principal. Prenda (ou encaixe) o objeto entre as garras e combine as leituras da escala principal e da móvel para obter o comprimento do objeto.

#### Micrômetro

No micrômetro, a bigorna A e a escala fixa B ficam presas à estrutura C; o tambor móvel E, o catraca D e o parafuso de ajuste fino D' ficam ligados ao fuso F, que se move por uma rosca de precisão dentro de B.

- **Princípio**: quando o tambor D dá uma volta completa, o fuso F avança ou recua um passo da rosca na direção do eixo. O passo da escala fixa B do micrômetro é 0,5 mm, e o tambor E tem 50 divisões iguais; assim, cada divisão do tambor corresponde a 0,01 mm de avanço ou recuo do fuso F. O micrômetro mede com precisão de 0,01 mm.
- **Leitura**: primeiro leia a escala B, observando se a marca de meio milímetro ficou visível; depois leia a escala E, em que cada divisão vale 0,01 mm. Combine as leituras de B e E para obter o comprimento medido.
- **Uso**: primeiro encoste F em A, alinhando a borda esquerda de E com o zero de B; prenda o objeto entre F e A, gire D e, quando F estiver perto do objeto, pare de usar D e passe para D'; ao ouvir o som de "clique", pare e faça a leitura.

### Materiais comuns

#### Materiais gerais

Itens que podem ser comprados em qualquer canal:

- Parafusos e porcas diversos
- Colunas sextavadas
- Polias de correia dentada
- Rolamentos

> [!warning] Eixos não entram nos materiais gerais: as especificações de eixo são bem específicas, então compre conforme a necessidade real de cada projeto.

#### Materiais específicos

Perfis específicos oficiais da REV e da goBILDA.

#### Características dos materiais

| Marca | Características |
|------|------|
| **REV** | Mais antiga, porém essencial. Os três módulos de controle eletrônico (Driver Hub, Control Hub e Expansion Hub) usam principalmente produtos REV. As peças estruturais incluem perfis de alumínio variados (uso relativamente menor), úteis para pequenos batentes e para fixar estruturas com deslocamentos fora do padrão. Os perfis usam principalmente parafusos Allen M3 de cabeça cilíndrica, eixos REX de 6 mm, engrenagens e correntes; o motor de eixo transversal 72:1 e o motor 40:1 são os mais úteis e usados. |
| **goBILDA** | Vigas em C, vigas quadradas ou vigas finas, eixos REX de 8 mm, conectores padronizados de vários tipos e excelente compatibilidade de fixação. Usa principalmente parafusos M4 (oficialmente de 10 mm) e motores da linha 5203. Ideal para kits com transmissão direta do motor. |

**Detalhes do fornecedor REV:**

- **Módulos de controle eletrônico**: os três módulos Driver Hub, Controller Hub (ou seja, Control Hub) e Expansion Hub são principalmente produtos REV.
- **Peças estruturais**: predominam os perfis de alumínio; hoje são menos usados, mas servem para pequenos batentes e para fixar estruturas com deslocamentos fora do padrão.
- **Parafusos especiais**: os perfis REV usam parafusos Allen M3 de cabeça cilíndrica; esse parafuso fica preso dentro do perfil de alumínio e praticamente só os perfis REV o utilizam.
- **Especificação de eixo**: a REV usa eixos REX de 6 mm, uma medida exclusiva da marca.
- **Motores**: a REV oferece o motor de eixo transversal 72:1 (nome oficial Core Hex, saída transversal a 90°, sem eixo de saída próprio) e o motor padrão 40:1 (nome oficial HD Hex). O motor transversal 72:1 permite soluções de montagem especiais, mas seu projeto estrutural é antigo e, no ambiente atual, é difícil encontrar com o que combiná-lo.
- **Engrenagens e correntes**: a REV também fornece, mas normalmente damos preferência aos produtos goBILDA.

**Detalhes do fornecedor goBILDA:**

- **Vigas em C**: há os modelos quadrado e fino. A viga quadrada serve para estruturas grandes, como o chassi; a fina, para ligações de maior vão.
- **Conectores**: oferece conectores padronizados de todos os tipos, com alto grau de padronização e ótima compatibilidade com os próprios materiais e com os da REV.
- **Parafusos**: usa principalmente M4; o parafuso oficial é o M4 de 10 mm com cabeça cilíndrica.
- **Especificação de eixo**: eixos REX de 8 mm.
- **Motores**: a linha 5203 é a mais usada e serve bem para transmissão direta padrão. Pela resistência do eixo REX de 8 mm e pela forma de montagem dos motores, a goBILDA é o kit mais adequado para transmissão direta do motor.

#### Filamentos de impressão 3D

| Tipo | Temperatura de impressão (aprox.) | Descrição |
|------|------|------|
| PLA | 220 °C | Filamento plástico básico padrão |
| PETG-CF | 240+ °C | Filamento plástico com fibra de carbono |

Compre filamentos oficiais da Bambu Lab (拓竹) ou da SUNLU (三绿), de qualidade relativamente estável.

**Contração:**

- Em geral, o PLA não exige preocupação com contração.
- Ao imprimir buchas de eixo, pode ocorrer contração de cerca de 5% no diâmetro, que deve ser medida conforme o formato impresso.
- A contração do PETG-CF varia bastante com tempo, temperatura e lote; antes de usar, recomendamos imprimir uma peça simples de teste no formato do componente para medir a contração.

#### Materiais de corte a laser

| Material | Características | Uso |
|------|------|------|
| Placa de acrílico | Resistência relativamente alta | Chapas de carga em grandes vãos |
| Placa de PP | Bastante tenaz | Peças de proteção; exigem mais pontos de fixação e suportam impacto direto |
| Placa de madeira | Custo relativamente baixo | Empena com facilidade; usar em casos especiais |

> [!info] As propriedades dos materiais ficam registradas aqui de forma fixa. Os parâmetros de processo do corte a laser, como potência e velocidade, ficam em um apêndice atualizado continuamente.

#### Cabos

**Cabos de alimentação:**

- Cabo bateria–Hub (conforme o projeto, a bateria pode ligar direto no Control Hub ou no Expansion Hub)
- Cabo Con–EXP
- Interruptor com cabo próprio
- Cabos de alimentação dos motores: nos motores goBILDA, o conector de alimentação não é compatível com o Hub; é preciso cortar o conector original e refazer a ponta usando terminais.

**Cabos de dados (cabo do encoder do motor):**

- Na goBILDA, o conector e a ordem dos fios são diferentes dos do Hub (o fio amarelo e o branco são invertidos); atenção especial ao montar.
- Cabos de sensores I2C: sem exigências especiais.
- Cabos de dados Con e EXP.
- Extensores de servo: atenção à orientação.

**Cabos de dados do computador principal:**

- Hub para computador: o Control Hub usa cabo USB-A para USB-C; o Expansion Hub usa cabo mini USB.
- Outros: cabos adaptadores USB-A para USB-C, USB-A para mini USB, USB-C para mini USB etc.
- Cabo de rede (pode ser usado como conexão auxiliar; não é obrigatório).
- Cabo de dados do controle (USB-A para micro USB).

**Infraestrutura (tratada como consumível):**

- Wi-Fi, câmeras de monitoramento, cabos de rede, réguas de tomada e outros itens de infraestrutura são geridos como consumíveis; reponha em tempo.

---

## 4. Fluxo de trabalho

1. **Compra de peças**
   - Os fornecedores oficiais de equipamentos do FTC ficam no exterior, com prazo longo e preço alto; para materiais não urgentes, é possível buscar alternativas em plataformas nacionais, equilibrando custo e velocidade de entrega
2. **Fabricação de peças próprias**
   - Produção de peças por impressão 3D
   - Corte a laser de chapas
3. **Montagem do hardware**
4. **Conexão dos cabos**
5. **Escrita da Robot Configuration** (em conjunto com Programação)
6. **Conexão entre Driver Station e Robot Controller** (em conjunto com Programação)

### Montagem do hardware

#### Ordem de montagem

> [!warning] Na montagem manual comum, costuma-se fazer o chassi primeiro e ir somando por cima. Em um robô de competição temos os desenhos de modelagem, e essa ordem pode causar muito retrabalho por causa de peças que ficam encobertas.

- A ordem deve ser ajustada conforme as relações de oclusão: **instale primeiro as peças que ficam escondidas atrás de motores, módulos de controle etc.**, e depois as peças que os cobrem.
- Por exemplo: confirme que todas as peças ao redor do motor já foram instaladas e só então instale o motor.

#### Cuidados no uso das peças

- Em peças presas ao eixo, evite os modelos com parafuso de fixação (set screw): ele danifica o eixo.
- Não aperte demais os parafusos.
- Outras regras de uso de peças serão acrescentadas continuamente.

#### Espaço reservado para manutenção

- Não tenha preguiça na hora de montar: não esconda parafusos e porcas em lugares difíceis de alcançar.
- O princípio é "fácil de consertar" — se, para reparar o robô, for preciso desmontá-lo inteiro, a competição não pode continuar.

#### Proteção contra estática

- Em tempo seco, a estática aparece com facilidade e causa perda de conexão do robô e leituras imprecisas dos sensores.
- Medidas de proteção: instale um fio de aterramento no robô para descarregar a estática no chão; envolva sensores como a IMU com papel-alumínio para proteção.

#### Organização dos cabos

- Estruturas retráteis com trilhos devem usar espaguete (tubo de proteção) nos fios, para que eles não fiquem soltos, travem o trilho ou até se rompam.
- A organização dos cabos é o trabalho mais técnico da montagem; leve a sério.

### Conexão dos cabos

#### Conexão entre Control Hub e Expansion Hub

- **Alimentação**: conector macho no fêmea.
- **Dados**: use as portas RS-485 com cabos de 3 vias. Cada lado tem 2 portas RS-485; basta escolher uma de cada lado, sem necessidade de correspondência fixa.

> [!warning] Os conectores oficiais têm encaixe à prova de erro — mas o encaixe à prova de erro não protege contra insistência. Se não entrar, confira a orientação do conector; nunca force.

#### Conexão entre Driver Station e Robot Controller

A parte de rede, tanto na estrutura quanto no programa, pode reaproveitar diretamente o conteúdo da seção de Programação.

#### Escrita da Robot Configuration

O arquivo de configuração é conteúdo conjunto de estrutura e programação; veja a seção de Programação.

---

## 5. Primeiros passos na construção

### Instalar e configurar o Bambu Studio

Baixe, instale e avance; escolha o local de instalação, e a pasta é criada automaticamente.

**Observações:**

- Marque todas as caixas de seleção
- Ao abrir, siga o guia de registro e escolha China continental
- Selecione apenas as impressoras P1S e P2S
- Mantenha os materiais padrão mais usados
- Instale o plugin de rede
- Faça login no canto superior esquerdo (número de celular ou terceiros)

### Exportar o arquivo de modelagem do Onshape

1. Abra o arquivo de modelagem e selecione a peça desejada; no canto inferior esquerdo, o Onshape marca a posição dessa peça na lista de instâncias à esquerda.
2. Clique com o botão direito na peça e escolha abrir a aba correspondente à instância para entrar na área de construção da peça.
3. Clique com o botão direito sobre o número da peça, no canto inferior esquerdo, e escolha exportar.
   - Atenção: a opção de exportar só aparece depois que você obtém permissão de edição do documento.
4. Altere o formato para STEP, renomeie o arquivo conforme a necessidade e mantenha as demais opções padrão.

### Importar e posicionar no Bambu Studio

- Crie um novo projeto no Bambu Studio, clique no botão "Importar" na parte superior e importe o arquivo STEP; confirme as opções de importação padrão.
- Se a posição da peça não ficar como esperado, não selecione nenhuma peça, clique com o botão direito na mesa de impressão e escolha "organizar automaticamente" (Auto Arrange) ou "orientar automaticamente" (Auto Orient).
- Ajuste manual: selecione a peça e segure o botão esquerdo para arrastar; clique no botão de rotação para girar nos modos relativo ou absoluto.
- Diferença de operação: por padrão, o Bambu Studio funciona como o Onshape — arrastar com o botão esquerdo gira a vista e com o direito desloca; se preferir, altere o modo de operação nas configurações. Com uma peça selecionada, arrastar com o botão esquerdo move a peça diretamente.

### Configurar os parâmetros de impressão

**Escolha de impressora e filamento:**

| Impressora | Bico | Filamento |
|--------|------|------|
| P1S (bico original) | 0,4 mm | PLA Basic |
| P1S (bico trocado, dedicada a fibra de carbono) | 0,6 mm | PETG-CF |
| P2S (duas unidades) | 0,4 mm | PLA Basic |

**Escolha dos parâmetros conforme o tipo de peça:**

| Tipo | Parâmetros |
|------|------|
| Peças decorativas | Parâmetros padrão do Bambu Studio |
| Peças estruturais sem carga | Configuração usual da equipe de modelagem |
| Peças estruturais de carga | Configuração usual da equipe de modelagem (alta resistência) |

> [!info] Os parâmetros acima são as configurações usuais da nossa equipe; ajuste conforme a necessidade.

**Várias peças na mesma mesa:**

- Várias cópias da mesma peça: selecione a peça, clique com o botão direito e escolha "clonar".
- Peças diferentes: clique de novo em "Importar" e importe o arquivo.

### Conectar a impressora 3D

- Entre na aba "Dispositivo", ative o modo LAN e a impressora na rede local será detectada automaticamente (ativar o modo LAN pode desconectar a conta atual; ignore o aviso).
- Se a impressora não for encontrada: confirme primeiro se o modo LAN está ativado; se ainda não aparecer, vincule manualmente por IP + código de acesso. O IP fica na página de Wi-Fi das configurações da impressora, e o código de acesso, no avatar da conta após ativar o modo LAN.
- Depois de fatiar, confira na aba "Visualizar" e, antes de imprimir, envie a pré-visualização ao responsável atual de modelagem ou de estrutura para confirmar a configuração antes de mandar imprimir.

### Ajustes de impressão

**Impressora P2S:**

- Ative o timelapse antes de imprimir.
- O nivelamento automático da mesa é obrigatório.
- Selecione o filamento carregado e a impressora de destino.

**Impressora P1S:**

- O timelapse pode ficar desativado por padrão.
- O nivelamento automático da mesa e a calibração dinâmica de fluxo devem estar ambos em automático.

### Tratamento de falhas de impressão

- **P2S**: tem detecção de "spaghetti" (macarrão) por IA; quando ocorre o emaranhado de filamento, a máquina para a impressão sozinha e envia um aviso à conta logada. Depois de limpar o arquivo com erro, o equipamento reinicia automaticamente.
- **P1S**: não tem reconhecimento automático de spaghetti; acompanhe o estado em tempo real durante a impressão. Ao detectar o problema, pare manualmente a impressão e localize o arquivo com erro no histórico de impressões, na pasta cache à esquerda, para limpá-lo.

### Instalar e configurar o RD Works V8

**Instalação:**

1. Obtenha o instalador .exe com um administrador ou com o professor orientador e escolha Install
2. Marque a instalação manual de caminho para alterar o local
3. Mantenha as demais opções padrão
4. Depois de conectar a cortadora a laser, escolha instalar o driver USB
5. Feche e abra o software novamente
