# Programación

## 1. Información básica

A continuación se indican los materiales adicionales que requiere Programación.

### Aplicaciones

- Git
- Visual Studio Code
- Android Studio

---

## 2. Configuración del entorno

A continuación se describe el entorno de trabajo que hay que configurar antes de empezar. Siga las instrucciones y consulte al administrador si tiene dudas.

### Navegador web

Sitios web adicionales que hay que añadir a marcadores:

| Nombre | Dirección |
|------|------|
| Programming Resources | https://www.firstinspires.org/resources/library/ftc/programming-resources |
| REV Robotics Documentation | https://docs.revrobotics.com/duo-control/hello-robot-java/welcome |
| Pedro Pathing | https://pedropathing.com/ |
| Robot Dashboard | http://192.168.43.1:8080/ |

### Git

Git es la herramienta de control de versiones de los archivos de programa que utiliza nuestro equipo. Android Studio no trae Git incorporado, por lo que hay que instalarlo y configurarlo; elija uno de los dos métodos siguientes.

**Método 1 (descargar e instalar Git desde Android Studio):**

1. Abra Android Studio y entre en los ajustes: en Windows/Linux, File → Settings; en macOS, Android Studio → Settings (o Preferences)
2. En el menú de la izquierda, despliegue Version Control y pulse Git
3. Si no se detecta Git, la interfaz ofrece un acceso de descarga; púlselo, descárguelo e instálelo
4. Tras la instalación, confirme la ruta del ejecutable de Git en Path to Git executable (git.exe en Windows); pulse Test y, cuando muestre Successful, pulse Apply y OK para guardar

**Método 2 (instalar primero Git por separado y configurar la ruta después en Android Studio):**

1. Visite el sitio oficial de Git [https://git-scm.com/downloads](https://git-scm.com/downloads) y descargue el instalador adecuado para su sistema (Windows / macOS / Linux)
2. Ejecute el instalador y complete la instalación con las opciones predeterminadas pulsando Next
3. Abra Android Studio y vaya a Ajustes → Version Control → Git
4. En Path to Git executable, introduzca o seleccione la ruta del ejecutable de Git (se detecta automáticamente si la variable de entorno está configurada)
5. Pulse Test; cuando muestre Successful, pulse Apply y OK para guardar

Si necesita activar el control de versiones en el proyecto actual: pulse en el menú superior VCS → Enable Version Control Integration..., elija Git y pulse OK.

### Android Studio

Android Studio es la herramienta de escritura de programas que utiliza nuestro equipo.

**Proceso de instalación y configuración del entorno:**

1. Abra [https://developer.android.com/studio](https://developer.android.com/studio)
2. Pulse «Download Android Studio», descargue la versión correspondiente e instálela.

**A tener en cuenta al instalar en Windows:**

- Marque las dos casillas
- Elija una ruta con espacio suficiente y que no vaya a cambiar

**Inicialización:**

- Elija el modo «Standard»
- Al aceptar el acuerdo, marque «Accept»
- Deje el resto tal cual y pulse «Next»

**Instalación del paquete de idioma chino (opcional):**

1. Abra [Android Studio Chinese Language Pack](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases)
2. Descargue el paquete de idioma más reciente (archivo .jar)
3. En la lista de pestañas de la izquierda de la pantalla principal, elija «Plugins» y después «Install Plugin from Disk»
4. Elija el archivo .jar descargado y ábralo; cuando el complemento se cargue, asegúrese de que queda activado
5. En la lista de pestañas de la izquierda, elija «Customize», entre en «Language and Region», seleccione «Chinese (Simplified) 简体中文» en «Language» y «Americas» en «Region», y reinicie

**Clonar el repositorio:**

1. En la lista de pestañas de la izquierda, pulse «GitHub» y autorice con «Log In via GitHub».
2. Elija el repositorio de programa correspondiente a la temporada actual (cada temporada se crea uno independiente; el nombre tiene el formato `FTC-32477-<temporada>-Program`; antes de crear el repositorio de la nueva temporada, confirme con el administrador)
3. Elija una carpeta vacía cuya ruta no vaya a cambiar y pulse «Clone»
4. Espere a que termine la descarga; puede ver el progreso en la pestaña «Build» de la barra lateral izquierda o mediante la barra de progreso de la esquina inferior derecha

> [!warning] Si tiene problemas, consulte al administrador.

### Visual Studio Code

Visual Studio Code es la herramienta de edición de código y consulta del historial que utiliza nuestro equipo.

**Proceso de instalación y configuración del entorno:**

1. Abra [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. Descargue la versión correspondiente e instálela
3. Si necesita la interfaz en chino, instale el [paquete de idioma chino de VS Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans).

---

## 3. Presentación de las herramientas

### Android Studio

Documentación oficial: [https://developer.android.com/studio/intro?hl=es](https://developer.android.com/studio/intro?hl=es)

Este proyecto se basa en el marco de aplicaciones oficial de FTC: se escribe el programa de control del robot en Java dentro de la carpeta `TeamCode` y se invocan las bibliotecas de dependencias necesarias para su funcionamiento.

Sobre los conocimientos básicos de Android Studio, consulte las páginas sencillas de la documentación oficial.

### Visual Studio Code

Documentación oficial: [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

La lógica de manejo de Visual Studio Code es similar a la de Android Studio y su frecuencia de uso es menor; para las operaciones de interfaz, consulte la parte de Android Studio.

### Robot Dashboard

- Conéctese a la red wifi «`32477-RC`». Contraseña wifi: pregunte al administrador u obténgala a través del Driver Hub.
- La dirección es: [http://192.168.43.1:8080/](http://192.168.43.1:8080/) (solo accesible desde la red local del robot)
- Es la página web del módulo wifi integrado del Control Hub (nombre oficial: Robot Controller Console, es decir, la consola del controlador del robot), que ofrece un panel gráfico de administración del Control Hub.

Sobre los conocimientos básicos de Robot Dashboard, consulte las páginas sencillas de la documentación oficial.

---

## 4. Flujo de trabajo

El trabajo central del grupo de Programación se divide en tres partes:

- **Programa autónomo**: la lógica de control de la fase autónoma (Auto) de la temporada
- **Programa manual**: la lógica de manejo de la fase de control por mando (TeleOp)
- **Configuración de sensores**: la configuración de los distintos sensores y del sistema de visión

> [!info] Pilotaje (Driver): el robot de competición se pilota con un mando Xbox; oficialmente solo se permite el modelo Xbox 360. Los pilotos se seleccionan dentro del equipo; quienes están familiarizados con el manejo del mando tienen más ventaja.

### La depuración es el núcleo

> [!info] La dificultad del desarrollo de programas está principalmente en la depuración. Rutas autónomas, manejo manual, parámetros PID, configuración de visión, etc.: en la mayoría de los casos ya hay paquetes disponibles que pueden reutilizarse; el trabajo se centra en el ajuste y la verificación de los parámetros.

La depuración atraviesa todo el proceso de desarrollo:

1. **Análisis de requisitos**: clarificar las reglas y las tareas de la temporada actual
2. **Diseño de la arquitectura**: diseñar la arquitectura general del programa y la división en módulos
3. **Escritura de código**: escribir el código Java en Android Studio
4. **Control de versiones**: gestionar las versiones del código con Git
5. **Depuración**: ajustar las rutas autónomas, el manejo manual, los parámetros PID y la configuración de visión
6. **Pruebas y verificación**: verificar el funcionamiento del programa en el robot
7. **Revisión de código**: revisar y fusionar el código mediante GitHub
8. **Despliegue y publicación**: desplegar la versión final en el Robot Controller


### Programación asistida por IA

> [!info] El desarrollo de programas puede apoyarse en herramientas como AI Agent. La capacidad clave es **entender el código generado por la IA, definir con claridad qué hay que modificar y dominar los métodos de depuración**; no es necesario escribir todo el código desde cero.

- La lógica básica de la programación (bucles for, bucles while, etc.) es universal entre lenguajes; solo cambia la sintaxis. Quienes tienen base en C++ se adaptan rápidamente a Java.

---

## 5. Fundamentos de colaboración en GitHub

> [!info] Esta sección cubre el contenido mínimo necesario para usar GitHub: consultar repositorios, descargar archivos, enviar comentarios, modificar contenido, colaborar y buscar proyectos de código abierto. La explicación completa está en el apartado de documentación oficial al final de la sección. Los botones de la interfaz están principalmente en inglés; en el texto se citan tal cual aparecen.

### Qué es GitHub

GitHub es una **plataforma de alojamiento de código y colaboración** basada en Git: el código se almacena en la nube (repositorio) y conserva el historial completo de modificaciones (confirmaciones); varias personas pueden colaborar en un mismo proyecto (ramas, solicitudes de incorporación de cambios), y además incorpora herramientas complementarias como incidencias, automatización (Actions) y alojamiento de sitios web (Pages).

Principales usos de GitHub en nuestro equipo:

- **Almacenar los programas de temporada**: cada temporada se crea un repositorio público independiente (a partir de la plantilla del SDK oficial) y, al terminar la temporada, se archiva como de solo lectura; cuando se cree el repositorio de la nueva temporada, se añadirá a la tabla de esta sección.
- **Mantener la «Guía de inicio rápido»**: los archivos fuente y los scripts de compilación están en el repositorio público `ftc32477/quick-start-guide`.
- **Publicar el sitio del equipo**: el repositorio de publicación del sitio es `ftc32477/ftc32477.github.io`; cada sección se compila desde su repositorio de origen con GitHub Actions y se envía a su subruta correspondiente (esta guía → `/docs/`); la ruta raíz redirige actualmente a `/docs/`. En el futuro, los distintos recursos contarán cada uno con su repositorio de origen y se enviarán a sus respectivas subrutas.
- **Buscar proyectos de código abierto**: localizar herramientas de ingeniería generales y el código y las soluciones que comparte la comunidad de FTC.

**Cuenta y organización**: utilice su propia cuenta (el proceso de registro se explica en «Esenciales del equipo») y espere a que el administrador le invite a unirse a la organización `ftc32477`. Los repositorios pertenecen a la organización; el administrador asigna los permisos de operación por rol:

| Rol | Qué puede hacer (resumen) |
|------|------|
| Lectura (Read) | Ver y discutir proyectos |
| Clasificación (Triage) | Gestionar incidencias y solicitudes de incorporación de cambios, pero no escribir código |
| Escritura (Write) | Enviar contenido al repositorio |
| Mantenimiento (Maintain) | Administrar el repositorio, pero sin realizar operaciones sensibles o destructivas |
| Administración (Admin) | Permisos totales, incluidas operaciones como eliminar repositorios |

> [!warning] Si no tiene permiso de escritura, envíe los cambios mediante una solicitud de incorporación de cambios o pida a los mantenedores que los apliquen; si no está seguro de sus permisos, actúe en modo de solo lectura y no intente explorar ni eludir las restricciones de permisos.

### Glosario rápido

| Término | Significado (una frase) |
|------|----------------|
| Repositorio (Repository) | Lugar donde se almacenan los archivos del proyecto y su historial completo |
| Confirmación (Commit) | Instantánea de una modificación con su descripción, que forma parte del historial |
| Rama (Branch) | Línea de desarrollo paralela dentro de un repositorio; los cambios se aplican primero en ella |
| Clon (Clone) | Descarga completa del repositorio al ordenador local |
| Bifurcación (Fork) | Copia de un repositorio ajeno en la propia cuenta; los cambios no afectan al repositorio original |
| Solicitud de incorporación de cambios (Pull Request, PR) | Mecanismo para solicitar la revisión y la fusión de los cambios de una rama; el núcleo de la colaboración |
| Incidencia (Issue) | Hilo de discusión para preguntas, errores y sugerencias |
| Lanzamiento (Release) | Publicación oficial con un número de versión y archivos descargables (como el PDF de la guía) |
| Estrella (Star) | Marcar como favorito y mostrar apoyo; también sirve para medir la popularidad de un proyecto |
| Observar (Watch) | Suscribirse a las notificaciones de actividad del repositorio |
| Actions | La automatización de flujos de trabajo de GitHub (en este proyecto se usa para compilar y publicar el sitio) |
| Pages | El alojamiento de sitios web estáticos de GitHub (el sitio de este proyecto se publica con él) |
| README | El documento de presentación de la página principal del repositorio; debe leerse en primer lugar |

### Mapa de repositorios del equipo

| Repositorio | Descripción | Cómo modificarlo |
|------|------|----------|
| `quick-start-guide` | Archivos fuente de la guía, scripts de compilación y artefactos del sitio (público) | Enviar una solicitud de incorporación de cambios o pedir a los mantenedores que apliquen los cambios |
| `ftc32477.github.io` | Repositorio de publicación del sitio del equipo (público); su contenido lo envían automáticamente los repositorios de origen | No modificar directamente |
| `.github` | Materiales de la página de la organización, como su descripción (público) | Enviar una solicitud de incorporación de cambios o pedir a los mantenedores que apliquen los cambios |
| `FTC-32477-<temporada>-Program` | Repositorio del programa de temporada (público): se crea uno independiente por temporada y los antiguos se archivan como de solo lectura; cuando se cree el de la nueva temporada, se añadirá su nombre concreto | Según el reparto interno del grupo de Programación |

> [!danger] **Zona prohibida del repositorio de publicación**: todo el contenido de `ftc32477.github.io` proviene de sus respectivos repositorios de origen y lo envía automáticamente GitHub Actions; cualquier modificación directa se sobrescribirá en el siguiente envío. No haga clic en editar, confirmar ni eliminar en ese repositorio ni en ningún contenido generado. Los problemas del sitio se tratan siempre en el repositorio de origen correspondiente (para esta guía, `quick-start-guide`).

### Consulta y descarga

1. Abra la página de la organización [https://github.com/ftc32477](https://github.com/ftc32477) y entre en un repositorio desde la lista Repositories
2. Lea primero el **README** de la página principal del repositorio (para qué sirve el proyecto y cómo se usa); en la zona About de la derecha están la descripción y el enlace a la página del proyecto
3. Pestañas superiores (su visibilidad depende de los permisos):
   - **Code**: lista de archivos e historial de confirmaciones
   - **Issues**: problemas y sugerencias
   - **Pull requests**: cambios pendientes de revisión
   - **Actions**: registros de compilación y publicación automáticas
   - **Releases**: lanzamientos oficiales y archivos descargables
4. Para descargar el repositorio completo: Code → **Download ZIP**
5. Para descargar el PDF de la guía: entre en **Releases**, elija la versión y descargue de Assets el archivo del idioma correspondiente
6. Para consultar el historial: lista **Commits** de la página Code → entre en una confirmación concreta para ver los cambios detallados (diff)

### Reportar problemas (Issue)

Cuando encuentre un fallo, un error en la documentación o tenga una sugerencia, use una incidencia para comunicarlo:

1. Abra la pestaña **Issues** del repositorio correspondiente y busque primero si ya existe el mismo problema
2. Pulse **New issue** y describa el problema con un título de una sola frase
3. En el cuerpo del mensaje, indique con claridad: **qué ha ocurrido**, **qué resultado esperaba**, **cómo reproducirlo** (pasos) y capturas de pantalla relevantes (elimine antes la información personal)
4. Tras enviarla, esté atento a las respuestas; una vez resuelto el problema, los mantenedores lo cerrarán

> [!info] Canal fijo para enviar comentarios sobre la guía: [https://github.com/ftc32477/quick-start-guide/issues](https://github.com/ftc32477/quick-start-guide/issues)

### Modificación desde la web (editar → enviar una PR)

Sin permiso de escritura, GitHub convierte automáticamente los cambios hechos en la web en «bifurcación (Fork) + solicitud de incorporación de cambios (PR)»:

1. Inicie sesión y abra el archivo que desea modificar (por ejemplo, un `.md` de `src/es/` de la guía)
2. Pulse el icono del lápiz de la esquina superior derecha del archivo: **Edit this file**
3. Si no tiene permiso de escritura, la página le indicará que se creará una bifurcación automáticamente; acepte
4. Haga la modificación y, en **Commit changes**, escriba una descripción clara en una sola frase
5. Elija **Create a new branch for this commit and start a pull request**, con un nombre de rama como `fix/typo-member`
6. En el formulario de PR que se abre, explique qué modifica y por qué, y pulse **Create pull request**
7. Espere la revisión de los mantenedores; si hay comentarios, siga modificando según lo indicado; una vez fusionado, los cambios surtirán efecto

> [!warning] Una PR debe contener un solo asunto; no modifique archivos que no conozca (scripts de compilación, artefactos generados, etc.); no envíe ningún cambio al repositorio de publicación.

### Colaboración local

La forma más habitual de trabajar es clonar el repositorio en local. Se requiere tener Git instalado en el ordenador (véase «2. Configuración del entorno»). Los comandos de uso frecuente son los siguientes:

```bash
# Clonar el repositorio en local
git clone https://github.com/ftc32477/quick-start-guide.git
cd quick-start-guide

# Antes de empezar, obtenga los últimos cambios
git pull

# Cree una rama para este trabajo
git switch -c feat/my-feature

# Tras modificar archivos: ver estado, preparar y confirmar
git status
git add <archivo>
git commit -m "descripción de este cambio"

# Subir la rama a GitHub
git push -u origin feat/my-feature
```

Después de subir la rama, cree en GitHub una solicitud de incorporación de cambios para esa rama y espere su revisión y fusión. Android Studio y Visual Studio Code ofrecen operaciones gráficas equivalentes (véase «2. Configuración del entorno»); los mismos pasos pueden realizarse desde la interfaz.

> [!warning] Tres normas: **haga pull antes de empezar**; **una confirmación, un solo asunto y con una descripción clara**; **suba los cambios a su propia rama, no directamente a main**.

**Sincronización de la bifurcación con el repositorio ascendente (al participar en proyectos externos)**: las bifurcaciones no se actualizan automáticamente. Primero añada el repositorio original como ascendente con `git remote add upstream <dirección del repositorio original>` y después sincronice con `git fetch upstream` y la operación de fusión correspondiente (consulte la sección «Sincronizar una bifurcación» de la documentación oficial).

### Comunidad de código abierto (búsqueda, evaluación y contribución)

**Búsqueda** (el cuadro de búsqueda admite calificadores, que pueden combinarse):

- `topic:ftc`, `topic:first-tech-challenge`, `topic:ftc-robot`: punto de entrada general a los proyectos de la comunidad de FTC
- `ftc language:Java sort:updated`: proyectos de Java que siguen recibiendo mantenimiento
- `"FIRST Tech Challenge" in:readme`: proyectos cuyo README menciona FTC

Recursos de código abierto de uso frecuente en FTC (todos disponibles en GitHub):

| Proyecto | Uso |
|------|------|
| FIRST-Tech-Challenge/FtcRobotController | SDK oficial de FTC y ejemplos |
| FTCLib/FTCLib | Biblioteca de utilidades de uso frecuente en FTC |
| acmerobotics/road-runner | Planificación de movimientos y seguimiento de trayectorias |
| Pedro-Pathing/PedroPathing | Planificación de trayectorias |
| acmerobotics/ftc-dashboard | Panel de depuración |
| OpenFTC/EasyOpenCV | Procesamiento de visión |
| the-orange-alliance, ftc-scout/ftc-scout | Datos y estadísticas de competiciones |

**Cómo evaluar si un repositorio es utilizable (cinco puntos)**: fecha de la última confirmación (si sigue recibiendo mantenimiento), calidad del README y de la documentación, licencia (License), actividad en Issues y si Releases tiene lanzamientos oficiales.

**Resumen de licencias** (consúltelo antes de usar código o materiales ajenos):

| Licencia | Explicación en una frase |
|--------|------------|
| MIT | La más permisiva: basta con conservar el aviso de derechos de autor para usarla libremente |
| Apache-2.0 | Igualmente permisiva; además concede licencia de patentes y exige declarar los cambios |
| GPL-3.0 | Con efecto copyleft: las obras derivadas basadas en ella también deben publicarse como código abierto |
| Sin licencia | Por defecto, «todos los derechos reservados»: **no** se puede copiar ni usar directamente; hay que contactar antes con el autor |

**Cómo contribuir**: lea primero el `CONTRIBUTING.md` (guía de contribución) y el código de conducta de la raíz del proyecto; si tiene dudas sobre un cambio, abra primero una incidencia para discutirlo; para correcciones menores, siga el proceso «editar → enviar una PR» descrito más arriba.

> [!warning] Seguridad: no ejecute scripts ni archivos ejecutables de origen desconocido; no publique claves de API, contraseñas ni tokens en una incidencia o en un repositorio; desconfíe de comandos de instalación del tipo `curl | bash`.

### Advertencia sobre operaciones peligrosas

> [!danger] Las siguientes operaciones pueden causar pérdidas irreversibles y ningún miembro debe realizarlas; si es realmente necesario, confirme antes con el administrador.
>
> - Modificar directamente el repositorio de publicación `ftc32477.github.io` (se sobrescribirá y contaminará el sitio oficial)
> - `git push --force`: sobrescribe a la fuerza el historial remoto y puede hacer desaparecer confirmaciones de otros compañeros
> - `git reset --hard`: descarta los cambios locales no subidos y es difícil recuperarlos
> - Eliminar ramas o repositorios, o cambiar la visibilidad, el nombre o la titularidad de un repositorio
> - Enviar al repositorio claves, contraseñas o tokens (una vez públicos, permanecen en el historial aunque se eliminen; hay que revocarlos y regenerarlos de inmediato)
> - Publicar material interno o información personal (correo, dirección, datos personales en capturas) en una incidencia, una PR o un repositorio público
> - Ejecutar o fusionar código de origen desconocido

> [!info] Seguridad de la cuenta: no comparta su cuenta con otras personas; GitHub está exigiendo la autenticación en dos fases (2FA) a las cuentas que contribuyen con código, actívela según las indicaciones; cree los tokens de acceso personal con los permisos mínimos y no los escriba nunca en el código ni en un repositorio.

### Lista de ejercicios

1. Abra la página de la organización, entre en el repositorio `quick-start-guide` y explique con el README para qué sirve este proyecto
2. Descargue de Releases el PDF de la guía en cualquier idioma
3. Encuentre en el historial de confirmaciones la última modificación y diga qué cambió
4. Busque «PDF» en Issues y compruebe si hay alguna pregunta relacionada
5. Corrija una errata siguiendo el proceso «editar → enviar una PR» y envíe una solicitud de incorporación de cambios

### Acceso a la documentación oficial

Para un uso más avanzado, consulte estos documentos oficiales según sus necesidades:

- Inicio rápido de GitHub: [https://docs.github.com/es/get-started/quickstart](https://docs.github.com/es/get-started/quickstart)
- Escribir y guardar código (ramas/confirmaciones/PR): [https://docs.github.com/es/get-started/start-your-journey/writing-and-storing-your-code](https://docs.github.com/es/get-started/start-your-journey/writing-and-storing-your-code)
- Hoja de referencia de Git: [https://docs.github.com/es/get-started/git-basics/git-cheatsheet](https://docs.github.com/es/get-started/git-basics/git-cheatsheet)
- Sintaxis de búsqueda: [https://docs.github.com/es/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax](https://docs.github.com/es/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax)
- Roles de repositorio de una organización de GitHub: [https://docs.github.com/es/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization](https://docs.github.com/es/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization)
- Curso interactivo (en inglés): [https://skills.github.com/](https://skills.github.com/)

> [!info] Ante cualquier operación dudosa, consulte primero al administrador o pregunte en Issues.
