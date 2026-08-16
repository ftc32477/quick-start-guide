# Modelado y diseño

## 1. Información básica

A continuación se indican los materiales adicionales que requiere Modelado y diseño.

### Aplicaciones

- Navegador web (Chrome, Edge o Safari)
- LocalSend
- Biblioteca de piezas FTC de Onshape — [https://ftconshape.com/](https://ftconshape.com/) (mantenida por FIRST y PTC; puede solicitar el acceso a la carpeta compartida enviando un correo a FIRST@ptc.com)
- Complemento de la biblioteca de piezas FTC Insert Tool — [https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba](https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba) (instalar desde la tienda de aplicaciones de Onshape: Subscribe → Get for Free)

### Cuentas en línea

- CycleZLab — [https://www.cyclezlab.com/](https://www.cyclezlab.com/) (gratuito; hay que solicitar la adhesión)

---

## 2. Configuración del entorno

A continuación se describe el entorno de trabajo que hay que configurar antes de empezar. Siga las instrucciones y consulte al administrador si tiene dudas.

### Navegador web

Sitios web adicionales que hay que añadir a marcadores:

| Nombre | Dirección |
|------|------|
| goBILDA | https://www.gobilda.com/ |
| REV Robotics | https://www.revrobotics.com/ |
| CycleZLab | https://www.cyclezlab.com/ |
| Onshape Education | https://www.onshape.com/en/education/ |

### Registro de la cuenta de Onshape

Onshape es la plataforma de modelado en la nube que utiliza nuestro equipo. Frente a programas de modelado industriales como SolidWorks, Onshape apenas consume recursos, facilita el uso compartido del proyecto entre dispositivos, es fácil de aprender y cuenta con soporte oficial de FIRST: con todas sus funciones, resulta ideal para aprender modelado CAD y desarrollar proyectos.

**Proceso de registro:**

1. Abra [https://www.onshape.com/en/education/](https://www.onshape.com/en/education/) y registre una cuenta del plan educativo
2. Rellene el nombre (First name), los apellidos (Last name) y el correo electrónico

> [!warning] No utilice buzones nacionales chinos como QQ: es probable que no reciba el código de verificación. Se recomienda @gmail.com o @outlook.com.

3. En la siguiente pantalla, seleccione el rol «Student», el tipo de centro «Grade School / K-12 (Ages <18)» y la fecha de nacimiento; cuando termine, pulse «Next»
4. Rellene la siguiente información por orden:
   - Nombre del centro: BEIJING NATIONAL DAY EXPERIMENTAL SCHOOL
   - Sitio web del centro: [https://sysyzx.bjhdedu.cn/](https://sysyzx.bjhdedu.cn/)
   - Año previsto de graduación
   - Motivo del registro: I am a member of FTC Team 32477, and I registered this account to use the team's modeling tools. (si no sabe qué escribir, use esta frase)
   - Marque la aceptación de los tres términos y condiciones inferiores y complete el registro
5. Compruebe el correo de confirmación en su buzón

> [!info] Tras registrarse, facilite su cuenta al administrador para que le añada a la carpeta compartida del equipo.

**Problemas frecuentes:**

- En el último paso aparece un error de reCAPTCHA: el servicio de verificación humana no responde. Pruebe a cambiar de entorno de red y asegúrese de poder conectar con el servicio reCAPTCHA.
- No llega el código de verificación al correo: si pasan más de 3 minutos, pruebe con otro buzón (Outlook o Gmail; no use QQ).

### Configuración del entorno de Onshape

1. Entre en el espacio de trabajo, pulse el icono de la cuenta en la esquina superior derecha y elija la primera opción del menú desplegable, «Mi cuenta»
2. Elija la tercera opción del menú de la derecha, «Preferencias»; cambie la primera opción de idioma a «简体中文» y pulse Guardar
3. En el mismo menú, cambie la opción de unidades inferior a sistema métrico (en el entorno de trabajo del equipo la longitud se usa en milímetros por defecto)

> [!info] Los cambios anteriores solo se aplican a los documentos creados después del cambio; las unidades de los documentos antiguos no se ven afectadas.

4. Ajuste su perfil personal según sus preferencias

### Complementos de Onshape

Gracias a su naturaleza en la nube, Onshape dispone de un rico catálogo de complementos compartidos, disponibles en la tienda de aplicaciones de Onshape, en sitios web de terceros y mediante el uso compartido entre usuarios.

Entre los complementos que utiliza habitualmente el equipo (solo como ejemplos):

- **Biblioteca de piezas FTC de Onshape** (fundamental; véase «1. Información básica»)
- **Lighten** (función personalizada para aligerar la estructura de las piezas)
- **Spur gear** (función personalizada generadora de engranajes)
- **HTD Pulley Generator** (derivado de otros documentos; generador de poleas de correa síncrona)

---

## 3. Puntos clave del modelado y diseño

### Diseño y ensamblaje de piezas

Al modelar en 3D con Onshape, preste especial atención a los siguientes puntos:

- **Precisión dimensional**: asegúrese de que todas las dimensiones del modelo coinciden con las piezas reales
- **Relaciones de ensamblaje**: defina correctamente las relaciones de montaje entre piezas (Mate y Mate Connector)
- **Verificación de interferencias**: realice una comprobación de interferencias una vez terminado el ensamblaje
- **Nomenclatura de las piezas**: nombre las piezas y los conjuntos siguiendo la convención unificada

### Documentos del proyecto y espacio de trabajo

Al trabajar en proyectos del equipo, cree los documentos en la carpeta compartida del equipo para que los demás miembros puedan acceder a ellos. Si aún no se ha unido, pida al administrador que le añada a la carpeta compartida del equipo.

1. En el menú izquierdo del espacio de trabajo personal, elija «Compartido conmigo», abra la carpeta «32477» y ya podrá crear documentos nuevos o abrir los creados por el equipo (cada documento es un proyecto)
2. Para crear un proyecto nuevo: pulse el botón azul de creación en la esquina superior izquierda de la página, elija «Documento» y espere a que se cree y se abra

Al entrar en el espacio de trabajo, verá las pestañas «Part Studio» y «Assembly» en la parte inferior (pulse el signo + a la derecha de la pestaña para crear uno nuevo):

- **Part Studio**: zona de modelado de piezas individuales (corresponde al boceto y la pieza del flujo CAD); las piezas se crean mediante restricciones de boceto
- **Assembly**: zona de montaje de las piezas creadas en «Part Studio» o de piezas disponibles en la biblioteca (corresponde al ensamblaje del flujo CAD)

En un documento se pueden crear tantos «Assembly» y «Part Studio» como se desee. Para facilitar la modificación y la gestión, tenga en cuenta: en un Part Studio conviene crear una sola pieza; ensamble el robot por estructuras y únalas al final en un conjunto general.

### Flujo básico de modelado

Como manual de iniciación, aquí solo se presentan las operaciones y el flujo de trabajo más básicos de Onshape.

#### Dibujo de bocetos

Cree un boceto nuevo en «Part Studio», elija un plano de referencia y dibuje el contorno con las herramientas de boceto (línea, rectángulo, círculo...); después, fije la forma mediante cotas y restricciones geométricas (horizontal, vertical, tangente...). Conviene que el boceto esté totalmente restringido para que las operaciones posteriores sean fiables.

#### Creación de piezas

Una vez terminado el boceto, convierta el contorno bidimensional en un sólido tridimensional con herramientas como extrusión, revolución o barrido, y perfeccione la pieza con operaciones de taladro, chaflán y redondeo. Todas las operaciones se registran por orden en la lista de operaciones y pueden revertirse y modificarse en cualquier momento.

#### Ensamblaje de piezas

Inserte en «Assembly» las piezas creadas en «Part Studio» o piezas disponibles de la biblioteca, y conéctelas según sus relaciones de montaje con Mate y Mate Connector. Tras el ensamblaje, compruebe que el movimiento es fluido y que no hay interferencias.

#### Uso de las herramientas

Onshape ofrece herramientas de análisis como medición, sección y propiedades de masa, con las que puede comprobar dimensiones y peso en cualquier momento durante el modelado; el menú contextual ofrece además operaciones rápidas como ocultar, aislar y renombrar.

### Resistencia del modelo y experiencia de diseño

La resistencia de las piezas impresas en 3D depende del material y de la estructura. A continuación se indican los conceptos de diseño estructural más utilizados:

- **Piezas estructurales centrales** (vigas, paneles estructurales): imprima preferiblemente con PETG-CF (los parámetros figuran en el capítulo «Hardware y construcción»); espesor no inferior a 4 mm
- **Piezas guía** (rieles de bolas, topes estructurales): puede usarse PLA; espesor de pared no inferior a 2 mm
- **Piezas decorativas de protección** (paneles laterales): espesor de pared no inferior a 1,5 mm
- Para tableros o estructuras frágiles como el metacrilato, evite en lo posible los agujeros densos (separación entre agujeros inferior a 3 mm); la anchura de las zonas de unión sometidas a esfuerzo entre estructuras no debe ser inferior a 7 mm
- Evite en lo posible los ángulos vivos y redondéelos con chaflanes para prevenir la rotura por concentración de tensiones

> [!info] Los datos anteriores son solo orientativos; los parámetros reales deben optimizarse mediante la validación con piezas físicas.

### Ideas de modelado y referencia de calendario

- Al concebir el diseño del robot, divida las tareas del juego en elementos pequeños, diseñe por separado la estructura de cada uno y combínelos después
- Antes de modelar formalmente, consulte la opinión de otros miembros y diseñe en función de la estrategia de puntuación del equipo
- Tras completar el modelado del robot, piense en el proceso real de montaje: para estructuras difíciles de instalar, como los tornillos interiores, reserve de antemano canales de instalación y espacio para el cableado
- Considere un diseño modular que facilite la reparación y la optimización posteriores
- En la versión final, procure un diseño integrado y reduzca las estructuras pequeñas innecesarias para aumentar la resistencia y la ligereza del conjunto

**Referencia de calendario:**

- En cuanto a los plazos, el primer diseño puede ser tosco, pero debe terminarse y fabricarse cuanto antes para dejar tiempo a la depuración del programa y a los entrenamientos del Driver, y para probar la estructura real e iterar; antes de la fase de clasificación, un robot completo apto para competir debe haber pasado al menos 3 iteraciones (referencia)
- Siga de cerca la actividad de los equipos extranjeros: la comunidad FTC organiza actividades como «Robot in 30 Hours Reveal | FTC», en las que los equipos participantes pueden compartir sus soluciones de la nueva temporada en cualquier momento; también puede consultar las soluciones de los equipos de FRC, VEX y otras competiciones

### Recursos de aprendizaje de Onshape

Como plataforma de modelado profesional, Onshape cuenta con recursos oficiales de aprendizaje completos: [https://learn.onshape.com/](https://learn.onshape.com/); también hay muchos tutoriales en plataformas de vídeo como Bilibili (哔哩哔哩) o YouTube.

- Dada la similitud del flujo de trabajo entre programas CAD (boceto, pieza, ensamblaje), los tutoriales de SolidWorks, Autodesk Fusion y otros programas también tienen valor didáctico y ayudan a desarrollar la percepción espacial de las piezas y la familiaridad con el flujo de modelado
- Recuerde siempre que la práctica es más importante que la teoría: busque modelos en Bilibili (哔哩哔哩) para practicar, intente primero modelarlos por su cuenta y consulte el tutorial solo si de verdad no le sale; en la vida cotidiana también puede observar y reflexionar sobre las ideas de modelado de estructuras pequeñas
- En la FTC conviene estudiar las buenas soluciones de otros equipos: la mayoría de los equipos punteros tienen su propio sitio web y publican sus soluciones en abierto; puede buscar el número del equipo FTC en YouTube o Google para encontrar su sitio oficial; también puede consultar los modelos de otros equipos en CycleZLab y sitios similares

> [!info] Si tiene dudas, consulte a los veteranos del modelado o busque directamente en Internet.

### Bibliotecas de piezas habituales en FTC

Proveedores de piezas y plataformas de recursos habituales en FTC:

- **goBILDA**: ofrece piezas estructurales FTC completas
- **REV Robotics**: ofrece módulos de control electrónico y piezas estructurales
- **CycleZLab**: plataforma de la comunidad FIRST Robotics (archivo de CAD, código y diarios de construcción)

### Convenciones de diseño

- Utilice el sistema métrico (mm)
- Todas las piezas impresas en 3D deben reservar holguras adecuadas (se recomienda 0,2–0,3 mm)
- Formatos de exportación: archivos STEP para mecanizado, STL para impresión 3D y 3MF para laminado e impresión
