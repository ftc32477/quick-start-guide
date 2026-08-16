# 프로그래밍

## 1. 기본 자료

다음은 프로그래밍에서 추가로 필요한 자료입니다.

### 애플리케이션

- Git
- Visual Studio Code
- Android Studio

---

## 2. 환경 설정

다음은 본격적으로 시작하기 전에 설정해야 할 작업 환경입니다. 안내에 따라 진행하고, 궁금한 점은 관리자에게 문의하세요.

### 웹 브라우저

북마크에 추가로 저장해야 할 웹사이트는 다음과 같습니다.

| 이름 | 주소 |
|------|------|
| Programming Resources | https://www.firstinspires.org/resources/library/ftc/programming-resources |
| REV Robotics Documentation | https://docs.revrobotics.com/duo-control/hello-robot-java/welcome |
| Pedro Pathing | https://pedropathing.com/ |
| Robot Dashboard | http://192.168.43.1:8080/ |

### Git

Git은 우리 팀이 사용하는 프로그램 파일 버전 관리 도구입니다. Android Studio에는 Git이 내장되어 있지 않으므로 설치하고 설정해야 하며, 다음 두 가지 방법 중 하나를 선택하면 됩니다.

**방법 1(Android Studio에서 Git 다운로드 및 설치):**

1. Android Studio를 열고 설정 페이지로 들어갑니다. Windows/Linux는 File → Settings, macOS는 Android Studio → Settings(또는 Preferences)
2. 왼쪽 메뉴에서 Version Control을 펼치고 Git 클릭
3. Git이 감지되지 않으면 인터페이스에 다운로드 입구가 표시됩니다. 클릭해 다운로드하고 설치하면 됩니다
4. 설치 완료 후 Path to Git executable에서 Git 프로그램 경로를 확인하고(Windows는 git.exe), Test를 클릭해 Successful이 표시되면 Apply와 OK를 눌러 저장합니다

**방법 2(Git을 먼저 별도 설치한 뒤 Android Studio에서 경로 설정):**

1. Git 공식 사이트 [https://git-scm.com/downloads](https://git-scm.com/downloads)에 접속해 자신의 컴퓨터 시스템(Windows / macOS / Linux)에 맞는 설치 패키지를 다운로드합니다
2. 설치 프로그램을 실행하고 기본 옵션으로 Next를 눌러 설치를 완료합니다
3. Android Studio를 열고 설정 → Version Control → Git으로 이동합니다
4. Path to Git executable에 Git 프로그램 경로를 입력하거나 선택합니다(환경 변수가 설정되어 있으면 자동으로 감지됨)
5. Test를 클릭해 Successful이 표시되면 Apply와 OK를 눌러 저장합니다

현재 프로젝트에서 버전 관리를 활성화하려면: 상단 메뉴 VCS → Enable Version Control Integration...을 클릭하고 Git을 선택한 뒤 OK를 누릅니다.

### Android Studio

Android Studio는 우리 팀이 사용하는 프로그램 작성 도구입니다.

**소프트웨어 설치 및 환경 설정 절차:**

1. [https://developer.android.com/studio](https://developer.android.com/studio) 열기
2. "Download Android Studio"를 클릭해 해당 버전을 다운로드하고 설치합니다.

**Windows에서 설치할 때 주의할 점:**

- 두 체크박스를 모두 체크해야 합니다
- 공간이 충분하고 변경되지 않을 경로를 선택하세요

**초기화:**

- "Standard" 모드를 선택하세요
- 계약 동의 시 "Accept"를 체크하세요
- 나머지는 그대로 두고 "Next"를 선택하세요

**한글화:**

1. [Android Studio Chinese Language Pack](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases) 열기
2. 최신 언어 확장 패키지(.jar 파일) 다운로드
3. 메인 페이지 왼쪽 탭 목록에서 "Plugins"를 선택하고 "Install Plugin from Disk" 선택
4. 다운로드한 .jar 파일을 선택해 열고, 플러그인이 로드되면 활성화 상태인지 확인
5. 왼쪽 탭 목록에서 "Customize"를 선택하고 "Language and Region"에 들어가 "Language"를 "Chinese (Simplified) 简体中文"으로, "Region"을 "Americas"로 선택한 뒤 재시작

**저장소 클론:**

1. 왼쪽 탭 목록에서 "GitHub" 클릭, "Log In via GitHub"로 인증합니다.
2. 현재 시즌의 코드 저장소를 선택합니다(예: `ftc32477/FTC-32477-Decode-Program`)
3. 경로가 바뀌지 않을 빈 폴더를 선택하고 "Clone" 클릭
4. 파일 다운로드가 끝날 때까지 기다립니다. 왼쪽 사이드바의 "Build" 탭이나 창 오른쪽 아래의 진행 표시줄에서 진행 상황을 볼 수 있습니다

> [!warning] 문제가 있으면 관리자에게 문의하세요.

### Visual Studio Code

Visual Studio Code는 우리 팀이 사용하는 코드 편집 및 이력 확인 도구입니다.

**소프트웨어 설치 및 환경 설정 절차:**

1. [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download) 열기
2. 해당 버전을 다운로드하고 설치하면 됩니다
3. [한글화 플러그인](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans)을 열어 설치하면 한글화됩니다.

---

## 3. 도구 소개

### Android Studio

공식 문서: [https://developer.android.com/studio/intro?hl=zh-cn](https://developer.android.com/studio/intro?hl=zh-cn)

이 프로젝트에서는 FTC 공식 제공 애플리케이션 프레임워크를 기반으로, `TeamCode` 폴더 아래에서 Java 언어로 로봇 제어 프로그램을 작성해 로봇 구동에 필요한 각종 의존성 라이브러리를 호출합니다.

Android Studio에서 알아야 할 기본 지식은 공식 문서의 간단한 페이지 안내를 참고하세요.

### Visual Studio Code

공식 문서: [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

Visual Studio Code의 조작 로직은 Android Studio와 비슷하고, 이 프로젝트에서는 사용 빈도가 낮으므로 인터페이스 안내는 Android Studio 파트를 참고하세요. 여기서는 반복하지 않습니다.

### Robot Dashboard

- Wi-Fi 네트워크 '`32477-RC`'에 연결합니다. Wi-Fi 비밀번호: 관리자에게 문의하거나 Driver Hub를 통해 확인합니다.
- 주소: [http://192.168.43.1:8080/](http://192.168.43.1:8080/)
- Control Hub에 내장된 Wi-Fi 모듈의 웹 페이지(공식 명칭 Robot Controller Console, 즉 로봇 컨트롤러 콘솔)로, Control Hub를 관리하는 그래픽 백엔드를 제공합니다.

Robot Dashboard에서 알아야 할 기본 지식은 공식 문서의 간단한 페이지 안내를 참고하세요.

---

## 4. 작업 흐름

프로그래밍 팀의 핵심 업무는 세 부분으로 나뉩니다.

- **자율 프로그램**: 시즌 자율 단계(Auto)의 제어 로직
- **수동 프로그램**: 원격 조종 단계(TeleOp)의 조작 로직
- **센서 설정**: 각종 센서와 비전 시스템의 설정

### 디버깅이 핵심

> [!info] 프로그램 개발의 진짜 어려움은 디버깅에 있습니다. 자율 경로, 수동 조작, PID 매개변수, 비전 설정 — 대부분의 센서에는 바로 재사용할 수 있는 기성 패키지가 있습니다. 여러분이 진짜 해야 할 일은 '튜닝'입니다.

디버깅은 개발 프로세스 전반을 관통합니다.

1. **요구 분석**: 현재 시즌의 규칙과 과제 요구를 명확히 합니다
2. **아키텍처 설계**: 프로그램 전체 아키텍처와 모듈 분할을 설계합니다
3. **코드 작성**: Android Studio에서 Java 코드를 작성합니다
4. **버전 관리**: Git으로 코드 버전을 관리합니다
5. **디버깅**: 자율 경로, 수동 조작, PID 매개변수, 비전 설정을 튜닝합니다
6. **테스트 검증**: 로봇에서 프로그램 기능을 검증합니다
7. **코드 리뷰**: GitHub로 코드 리뷰와 병합을 진행합니다
8. **배포 발표**: 최종 버전을 Robot Controller에 배포합니다
