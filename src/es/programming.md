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

**Traducción al chino:**

1. Abra [Android Studio Chinese Language Pack](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases)
2. Descargue el paquete de idioma más reciente (archivo .jar)
3. En la lista de pestañas de la izquierda de la pantalla principal, elija «Plugins» y después «Install Plugin from Disk»
4. Elija el archivo .jar descargado y ábralo; cuando el complemento se cargue, asegúrese de que queda activado
5. En la lista de pestañas de la izquierda, elija «Customize», entre en «Language and Region», seleccione «Chinese (Simplified) 简体中文» en «Language» y «Americas» en «Region», y reinicie

**Clonar el repositorio:**

1. En la lista de pestañas de la izquierda, pulse «GitHub» y autorice con «Log In via GitHub».
2. Elija el repositorio de código de la temporada actual (p. ej., `ftc32477/FTC-32477-Decode-Program`)
3. Elija una carpeta vacía cuya ruta no vaya a cambiar y pulse «Clone»
4. Espere a que termine la descarga; puede ver el progreso en la pestaña «Build» de la barra lateral izquierda o mediante la barra de progreso de la esquina inferior derecha

> [!warning] Si tiene problemas, consulte al administrador.

### Visual Studio Code

Visual Studio Code es la herramienta de edición de código y consulta del historial que utiliza nuestro equipo.

**Proceso de instalación y configuración del entorno:**

1. Abra [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
2. Descargue la versión correspondiente e instálela
3. Abra el [complemento de traducción al chino](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans) e instálelo.

---

## 3. Presentación de las herramientas

### Android Studio

Documentación oficial: [https://developer.android.com/studio/intro?hl=zh-cn](https://developer.android.com/studio/intro?hl=zh-cn)

En este proyecto, partimos del marco de aplicaciones oficial de FTC y escribimos el programa de control del robot en Java dentro de la carpeta `TeamCode`, para invocar las distintas bibliotecas de dependencias que el robot necesita para funcionar.

Sobre los conocimientos básicos de Android Studio, consulte las páginas sencillas de la documentación oficial.

### Visual Studio Code

Documentación oficial: [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

Dado que la lógica de manejo de Visual Studio Code es similar a la de Android Studio, y que en este proyecto se usa con menos frecuencia, para las guías de interfaz consulte la parte de Android Studio; no se repite aquí.

### Robot Dashboard

- Conéctese a la red wifi «`32477-RC`». Contraseña wifi: pregunte al administrador u obténgala a través del Driver Hub.
- La dirección es: [http://192.168.43.1:8080/](http://192.168.43.1:8080/)
- Es la página web del módulo wifi integrado del Control Hub (nombre oficial: Robot Controller Console, es decir, la consola del controlador del robot), que ofrece un panel gráfico de administración del Control Hub.

Sobre los conocimientos básicos de Robot Dashboard, consulte las páginas sencillas de la documentación oficial.

---

## 4. Flujo de trabajo

El trabajo central del grupo de Programación se divide en tres partes:

- **Programa autónomo**: la lógica de control de la fase autónoma (Auto) de la temporada
- **Programa manual**: la lógica de manejo de la fase de control por mando (TeleOp)
- **Configuración de sensores**: la configuración de los distintos sensores y del sistema de visión

### La depuración es el núcleo

> [!info] La verdadera dificultad del desarrollo de programas está en la depuración. Rutas autónomas, manejo manual, parámetros PID, configuración de visión: la mayoría de los sensores disponen de paquetes ya hechos que pueden reutilizarse directamente; lo que de verdad hay que hacer es «ajustar».

La depuración atraviesa todo el proceso de desarrollo:

1. **Análisis de requisitos**: clarificar las reglas y las tareas de la temporada actual
2. **Diseño de la arquitectura**: diseñar la arquitectura general del programa y la división en módulos
3. **Escritura de código**: escribir el código Java en Android Studio
4. **Control de versiones**: gestionar las versiones del código con Git
5. **Depuración**: ajustar las rutas autónomas, el manejo manual, los parámetros PID y la configuración de visión
6. **Pruebas y verificación**: verificar el funcionamiento del programa en el robot
7. **Revisión de código**: revisar y fusionar el código mediante GitHub
8. **Despliegue y publicación**: desplegar la versión final en el Robot Controller
