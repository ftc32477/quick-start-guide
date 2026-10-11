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

**중국어 언어 팩 설치(선택 사항):**

1. [Android Studio Chinese Language Pack](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases) 열기
2. 최신 언어 확장 패키지(.jar 파일) 다운로드
3. 메인 페이지 왼쪽 탭 목록에서 "Plugins"를 선택하고 "Install Plugin from Disk" 선택
4. 다운로드한 .jar 파일을 선택해 열고, 플러그인이 로드되면 활성화 상태인지 확인
5. 왼쪽 탭 목록에서 "Customize"를 선택하고 "Language and Region"에 들어가 "Language"를 "Chinese (Simplified) 简体中文"으로, "Region"을 "Americas"로 선택한 뒤 재시작

**저장소 클론:**

1. 왼쪽 탭 목록에서 "GitHub" 클릭, "Log In via GitHub"로 인증합니다.
2. 현재 시즌에 해당하는 프로그램 저장소를 선택합니다(시즌마다 별도로 만들며, 이름은 `FTC-32477-<시즌>-Program` 형식입니다. 새 시즌 저장소가 만들어지기 전에는 관리자에게 먼저 확인하세요)
3. 경로가 바뀌지 않을 빈 폴더를 선택하고 "Clone" 클릭
4. 파일 다운로드가 끝날 때까지 기다립니다. 왼쪽 사이드바의 "Build" 탭이나 창 오른쪽 아래의 진행 표시줄에서 진행 상황을 볼 수 있습니다

> [!warning] 문제가 있으면 관리자에게 문의하세요.

### Visual Studio Code

Visual Studio Code는 우리 팀이 사용하는 코드 편집 및 이력 확인 도구입니다.

**소프트웨어 설치 및 환경 설정 절차:**

1. [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download) 열기
2. 해당 버전을 다운로드하고 설치하면 됩니다
3. 중국어 인터페이스가 필요하면 [VS Code 중국어 언어 팩](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans)을 설치합니다.

---

## 3. 도구 소개

### Android Studio

공식 문서: [https://developer.android.com/studio/intro?hl=ko](https://developer.android.com/studio/intro?hl=ko)

이 프로젝트는 FTC 공식 애플리케이션 프레임워크를 기반으로, `TeamCode` 폴더에서 Java로 로봇 제어 프로그램을 작성하고 실행에 필요한 의존성 라이브러리를 호출합니다.

Android Studio에서 알아야 할 기본 지식은 공식 문서의 간단한 페이지 안내를 참고하세요.

### Visual Studio Code

공식 문서: [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

Visual Studio Code는 Android Studio와 조작 로직이 비슷하고 사용 빈도가 낮으므로, 인터페이스 조작은 Android Studio 부분을 참고하세요.

### Robot Dashboard

- Wi-Fi 네트워크 '`32477-RC`'에 연결합니다. Wi-Fi 비밀번호: 관리자에게 문의하거나 Driver Hub를 통해 확인합니다.
- 주소: [http://192.168.43.1:8080/](http://192.168.43.1:8080/) (로봇 로컬 네트워크에서만 접속 가능)
- Control Hub에 내장된 Wi-Fi 모듈의 웹 페이지(공식 명칭 Robot Controller Console, 즉 로봇 컨트롤러 콘솔)로, Control Hub를 관리하는 그래픽 백엔드를 제공합니다.

Robot Dashboard에서 알아야 할 기본 지식은 공식 문서의 간단한 페이지 안내를 참고하세요.

---

## 4. 작업 흐름

프로그래밍 팀의 핵심 업무는 세 부분으로 나뉩니다.

- **자율 프로그램**: 시즌 자율 단계(Auto)의 제어 로직
- **수동 프로그램**: 원격 조종 단계(TeleOp)의 조작 로직
- **센서 설정**: 각종 센서와 비전 시스템의 설정

> [!info] 컨트롤러 조종(Driver): 참가 로봇은 Xbox 컨트롤러로 조종하며, 공식적으로 Xbox 360 모델만 허용됩니다. Driver는 팀 내 선발로 정해지며, 컨트롤러 조작에 익숙한 사람이 더 유리합니다.

### 디버깅이 핵심

> [!info] 프로그램 개발의 어려움은 주로 디버깅에 있습니다. 자율 경로, 수동 조작, PID 매개변수, 비전 설정 등은 대부분 이미 재사용할 수 있는 기성 패키지가 있으므로, 작업의 중점은 매개변수 조정과 검증입니다.

디버깅은 개발 프로세스 전반을 관통합니다.

1. **요구 분석**: 현재 시즌의 규칙과 과제 요구를 명확히 합니다
2. **아키텍처 설계**: 프로그램 전체 아키텍처와 모듈 분할을 설계합니다
3. **코드 작성**: Android Studio에서 Java 코드를 작성합니다
4. **버전 관리**: Git으로 코드 버전을 관리합니다
5. **디버깅**: 자율 경로, 수동 조작, PID 매개변수, 비전 설정을 튜닝합니다
6. **테스트 검증**: 로봇에서 프로그램 기능을 검증합니다
7. **코드 리뷰**: GitHub로 코드 리뷰와 병합을 진행합니다
8. **배포 발표**: 최종 버전을 Robot Controller에 배포합니다


### AI 활용 프로그래밍

> [!info] 프로그램 개발에는 AI Agent 등의 도구를 활용해 보조받을 수 있습니다. 핵심 능력은 **AI가 생성한 코드를 읽고, 수정 방향을 정하고, 디버깅 방법을 익히는 것**이며, 모든 코드를 처음부터 직접 작성할 필요는 없습니다.

- 프로그래밍 언어의 핵심 논리(for 반복문, while 반복문 등)는 언어마다 공통이며 문법만 다릅니다. C++ 기초가 있는 학생은 Java 개발에 빠르게 적응할 수 있습니다

---

## 5. GitHub 협업 기초

> [!info] 이 절은 GitHub 사용에 필요한 최소한의 내용을 다룹니다: 저장소 보기, 파일 다운로드, 피드백 제출, 내용 수정, 협업 참여, 오픈소스 프로젝트 검색. 자세한 설명은 문서 끝의 공식 문서 안내를 참고하세요. 인터페이스 버튼은 대부분 영어이므로 본문에서도 영어로 표기합니다.

### GitHub란 무엇인가

GitHub는 Git 기반의 **코드 호스팅 및 협업 플랫폼**입니다. 코드는 클라우드(저장소)에 저장되며 전체 수정 이력(커밋)이 보존되고, 여러 사람이 같은 프로젝트에서 협업할 수 있습니다(브랜치, 끌어오기 요청). 이 밖에도 이슈, 자동화(Actions), 웹사이트 호스팅(Pages) 등의 도구를 제공합니다.

우리 팀이 GitHub를 사용하는 주요 목적:

- **시즌 프로그램 보관**: 시즌마다 공개 저장소를 하나씩 만들고(공식 SDK 템플릿에서 포크), 시즌 종료 후에는 읽기 전용으로 보관합니다. 새 시즌 저장소가 만들어지면 이 절의 표에 추가합니다.
- **《빠른 시작 가이드》 유지 관리**: 소스 파일과 빌드 스크립트를 공개 저장소 `ftc32477/quick-start-guide`에 보관합니다.
- **팀 사이트 게시**: 사이트 게시 저장소는 `ftc32477/ftc32477.github.io`이며, 각 섹션은 각자의 소스 저장소에서 GitHub Actions로 빌드된 후 해당 하위 경로로 푸시됩니다(이 가이드 → `/docs/`). 루트 경로는 현재 `/docs/`로 리디렉션됩니다. 앞으로 각종 자료는 각각 소스 저장소를 만들어 해당 하위 경로로 푸시할 예정입니다.
- **오픈소스 프로젝트 검색**: 범용 엔지니어링 도구와 FTC 커뮤니티가 공유하는 코드 및 해법을 검색합니다.

**계정과 조직**: 본인 계정을 사용하며(가입 절차는 《팀원 필수사항》 참고), 관리자가 조직 `ftc32477`에 초대합니다. 저장소는 조직 소유이며, 작업 권한은 관리자가 역할별로 부여합니다:

| 역할 | 할 수 있는 일(요약) |
|------|------|
| 읽기(Read) | 프로젝트 보기와 토론 |
| 심사(Triage) | 이슈와 끌어오기 요청 관리, 단 코드 작성 불가 |
| 쓰기(Write) | 저장소에 내용 푸시 |
| 유지 관리(Maintain) | 저장소 관리, 단 민감하거나 파괴적인 작업 불가 |
| 관리(Admin) | 전체 권한, 저장소 삭제 등 포함 |

> [!warning] 쓰기 권한이 없으면 변경 사항을 끌어오기 요청으로 제출하거나 유지 관리자에게 처리를 맡깁니다. 권한이 확실하지 않으면 읽기 전용으로 작업하고, 권한 제한을 탐색하거나 우회하지 마세요.

### 용어 빠른 참조

| 용어 | 의미(한 줄) |
|------|----------------|
| 저장소(Repository) | 프로젝트 파일과 전체 이력 기록을 보관하는 위치 |
| 커밋(Commit) | 설명이 붙은 한 번의 수정 스냅샷이며, 이력을 구성함 |
| 브랜치(Branch) | 저장소 안의 병렬 개발 라인이며, 변경 사항이 먼저 적용되는 곳 |
| 클론(Clone) | 저장소를 로컬 컴퓨터로 완전히 다운로드하는 것 |
| 포크(Fork) | 남의 저장소를 내 계정으로 복사하는 것이며, 변경 사항이 원본 저장소에 영향을 주지 않음 |
| 끌어오기 요청(Pull Request, PR) | 특정 브랜치의 변경 사항을 검토하고 병합해 달라고 요청하는 방식이며, 협업의 핵심 |
| 이슈(Issue) | 질문, 오류 보고, 제안을 위한 토론 글 |
| 릴리스(Release) | 버전 번호를 붙인 공식 배포이며, 다운로드 파일(가이드 PDF 등)을 첨부 |
| 별표(Star) | 즐겨찾기와 좋아요 기능이며, 프로젝트 인기도 판단에도 사용 |
| 감시(Watch) | 저장소 활동 알림을 구독 |
| Actions | GitHub의 자동화 파이프라인(이 프로젝트에서는 사이트 빌드와 게시에 사용) |
| Pages | GitHub의 정적 웹사이트 호스팅(이 프로젝트의 사이트가 이곳에서 게시됨) |
| README | 저장소 첫 화면의 설명 문서이며, 가장 먼저 읽어야 함 |

### 팀 저장소 지도

| 저장소 | 설명 | 수정 방법 |
|------|------|----------|
| `quick-start-guide` | 가이드 소스 파일, 빌드 스크립트와 사이트 산출물(공개) | 끌어오기 요청 제출 또는 유지 관리자 처리 |
| `ftc32477.github.io` | 팀 사이트 게시 저장소(공개), 내용은 각 소스 저장소에서 자동 푸시 | 직접 수정 금지 |
| `.github` | 조직 홈페이지 자료(조직 소개 등, 공개) | 끌어오기 요청 제출 또는 유지 관리자 처리 |
| `FTC-32477-<시즌>-Program` | 시즌 프로그램 저장소(공개): 시즌마다 따로 만들고, 지난 시즌은 읽기 전용으로 보관, 새 시즌 저장소가 만들어지면 구체적인 이름을 추가 | 프로그램 팀 내부 분담에 따름 |

> [!danger] **게시 저장소 금지 구역**: `ftc32477.github.io`의 모든 내용은 각 소스 저장소에서 GitHub Actions를 통해 자동으로 푸시됩니다. 직접 수정하면 다음 푸시 때 덮어써집니다. 이 저장소나 생성된 내용에서 편집, 커밋, 삭제를 하지 마세요. 사이트 문제는 항상 해당 소스 저장소에서 처리합니다(이 가이드는 `quick-start-guide`).

### 보기와 다운로드

1. 조직 홈페이지 [https://github.com/ftc32477](https://github.com/ftc32477)를 열고, Repositories 목록에서 저장소에 들어갑니다
2. 먼저 저장소 첫 화면의 **README**를 읽습니다(프로젝트 용도, 사용 방법). 오른쪽 About 영역에 소개와 홈페이지 링크가 있습니다
3. 상단 탭(권한에 따라 표시 여부가 결정됩니다):
   - **Code**: 파일 목록과 커밋 이력
   - **Issues**: 문제와 제안
   - **Pull requests**: 검토 대기 중인 변경 사항
   - **Actions**: 자동 빌드와 게시 기록
   - **Releases**: 정식 버전과 다운로드 파일
4. 저장소 전체 다운로드: Code → **Download ZIP**
5. 가이드 PDF 다운로드: **Releases**에 들어가 버전을 선택하고, Assets에서 해당 언어를 다운로드합니다
6. 이력 보기: Code 페이지의 **Commits** 목록 → 개별 커밋을 클릭해 구체적인 변경 사항(diff)을 확인합니다

### 문제 보고(Issue)

장애가 발생하거나 문서에 오류가 있거나 제안할 사항이 있으면 Issue로 보고합니다:

1. 대상 저장소의 **Issues** 탭을 열고, 같은 문제가 이미 있는지 먼저 검색합니다
2. **New issue**를 클릭하고, 한 문장 제목으로 문제를 설명합니다
3. 본문에 **무엇이 발생했는지**, **기대한 결과**, **재현 방법**(단계), 관련 스크린샷(개인 정보는 먼저 제거)을 명확히 작성합니다
4. 제출 후 답변을 확인합니다. 문제가 해결되면 유지 관리자가 닫습니다

> [!info] 가이드의 고정 피드백 창구: [https://github.com/ftc32477/quick-start-guide/issues](https://github.com/ftc32477/quick-start-guide/issues)

### 웹에서 수정(편집 → PR 제출)

쓰기 권한이 없으면 GitHub가 웹에서의 변경 사항을 자동으로 "포크(Fork) + 끌어오기 요청(PR)"으로 만듭니다:

1. 로그인 후 수정할 파일을 엽니다(예: 가이드 `src/zh-hans/` 아래의 `.md` 문서)
2. 파일 오른쪽 위의 연필 아이콘 **Edit this file**을 클릭합니다
3. 쓰기 권한이 없으면 페이지에서 포크를 자동으로 만들겠다고 안내하며, 동의하면 됩니다
4. 내용을 수정하고 **Commit changes**에 명확한 설명을 한 문장 작성합니다
5. **Create a new branch for this commit and start a pull request**를 선택하고, 브랜치 이름은 `fix/typo-member`처럼 지정합니다
6. 열린 PR 양식에서 수정 내용과 이유를 설명하고 **Create pull request**를 클릭합니다
7. 유지 관리자의 검토를 기다립니다. 의견이 있으면 그에 따라 계속 수정하며, 병합되면 변경 사항이 반영됩니다

> [!warning] PR 하나에는 한 가지 일만 제출합니다. 익숙하지 않은 파일(빌드 스크립트, 생성 산출물 등)은 수정하지 마세요. 게시 저장소에는 어떤 변경도 제출하지 마세요.

### 로컬 협업

로컬에서 저장소를 클론해 개발하는 것이 가장 일반적인 방식입니다. 전제 조건은 컴퓨터에 Git이 설치되어 있는 것입니다("2. 환경 설정" 참고). 자주 쓰는 명령은 다음과 같습니다:

```bash
# 저장소를 로컬로 클론
git clone https://github.com/ftc32477/quick-start-guide.git
cd quick-start-guide

# 작업 시작 전 최신 변경 사항 가져오기
git pull

# 이번 작업용 새 브랜치 만들기
git switch -c feat/my-feature

# 파일 수정 후: 상태 확인, 스테이징, 커밋
git status
git add <파일>
git commit -m "이번 수정 설명"

# 브랜치를 GitHub로 푸시
git push -u origin feat/my-feature
```

푸시한 후 GitHub에서 해당 브랜치의 Pull Request를 만들어 검토와 병합을 기다립니다. Android Studio와 Visual Studio Code는 동등한 그래픽 작업을 제공하므로("2. 환경 설정" 참고), 인터페이스에서 같은 단계를 수행할 수 있습니다.

> [!warning] 세 가지 규칙: **먼저 pull한 후 작업**; **커밋 하나에는 한 가지 일만 하고 설명을 명확히 작성**; **자기 브랜치에 푸시하고 main에 직접 푸시하지 않기**.

**포크와 업스트림 동기화(외부 프로젝트에 참여할 때)**: 포크한 저장소는 자동으로 업데이트되지 않습니다. 먼저 원본 저장소를 업스트림으로 추가해야 합니다: `git remote add upstream <원본 저장소 주소>`, 그다음 `git fetch upstream`과 병합으로 동기화합니다(자세한 내용은 공식 문서 "포크 동기화" 절 참고).

### 오픈소스 커뮤니티(검색, 평가, 기여)

**검색**(검색창은 한정자를 지원하며 조합해 사용할 수 있습니다):

- `topic:ftc`, `topic:first-tech-challenge`, `topic:ftc-robot`: FTC 커뮤니티 프로젝트의 통합 진입점
- `ftc language:Java sort:updated`: 최근에도 유지 관리되고 있는 Java 프로젝트
- `"FIRST Tech Challenge" in:readme`: README에서 FTC를 언급한 프로젝트

FTC에서 자주 쓰는 오픈소스 자료(모두 GitHub에서 찾을 수 있습니다):

| 프로젝트 | 용도 |
|------|------|
| FIRST-Tech-Challenge/FtcRobotController | FTC 공식 SDK와 예제 |
| FTCLib/FTCLib | FTC에서 자주 쓰는 도구 라이브러리 |
| acmerobotics/road-runner | 동작 계획과 경로 추종 |
| Pedro-Pathing/PedroPathing | 경로 계획 |
| acmerobotics/ftc-dashboard | 디버깅 대시보드 |
| OpenFTC/EasyOpenCV | 비전 처리 |
| the-orange-alliance, ftc-scout/ftc-scout | 대회 데이터와 통계 |

**저장소의 사용 가능 여부 평가(다섯 가지 확인)**: 최근 커밋 시각(유지 관리 여부), README와 문서 품질, 라이선스(License), Issues 활동도, Releases 정식 버전 유무.

**라이선스 요약**(남의 코드나 자료를 사용하기 전에 반드시 확인):

| 라이선스 | 한 줄 설명 |
|--------|------------|
| MIT | 가장 관대함: 저작권 표시만 유지하면 자유롭게 사용 가능 |
| Apache-2.0 | 마찬가지로 관대하며, 특허 허여와 변경 사항 표시 요구 사항이 있음 |
| GPL-3.0 | 전파성 있음: 이를 기반으로 한 2차 저작물도 오픈소스로 공개해야 함 |
| 라이선스 없음 | 기본적으로 "모든 권리 보유"이므로 **직접 복사해 사용할 수 없으며**, 먼저 저자에게 연락해야 함 |

**기여 참여**: 먼저 프로젝트 루트의 `CONTRIBUTING.md`(기여 가이드)와 행동 강령을 읽습니다. 확실하지 않은 변경은 먼저 Issue를 열어 논의합니다. 자잘한 수정은 위의 "편집 → PR 제출" 절차로 제출합니다.

> [!warning] 보안: 출처를 알 수 없는 스크립트나 실행 파일을 실행하지 마세요. API Key, 비밀번호, Token을 Issue나 저장소에 올리지 마세요. `curl | bash`류의 설치 명령에 주의하세요.

### 위험한 작업 경고

> [!danger] 다음 작업은 되돌릴 수 없는 손실을 초래할 수 있으므로 일반 팀원은 절대 실행하지 마세요. 반드시 필요한 경우에는 먼저 관리자의 확인을 받으세요.
>
> - 게시 저장소 `ftc32477.github.io` 직접 수정(덮어써지고 정식 사이트가 훼손됩니다)
> - `git push --force`: 원격 이력을 강제로 덮어써 팀원의 커밋이 사라질 수 있습니다
> - `git reset --hard`: 로컬의 미푸시 변경 사항을 버리며 되찾기 어렵습니다
> - 브랜치 삭제, 저장소 삭제, 저장소의 공개 여부, 이름, 소유권 변경
> - 저장소에 키, 비밀번호, Token 제출(한 번 공개되면 삭제해도 이력에 남으므로 즉시 폐기하고 재발급해야 합니다)
> - Issue, PR 또는 공개 저장소에 내부 자료와 개인 정보(이메일, 주소, 스크린샷 속 개인 정보) 게시
> - 출처를 알 수 없는 코드 실행 또는 병합

> [!info] 계정 보안: 다른 사람과 계정을 공유하지 마세요. GitHub는 코드 기여에 참여하는 계정에 2단계 인증(2FA)을 의무화하고 있으므로 안내에 따라 활성화하세요. 개인용 액세스 토큰(Token)은 최소 권한으로 만들고 절대 코드나 저장소에 기록하지 마세요.

### 연습 목록

1. 조직 홈페이지를 열고 `quick-start-guide` 저장소에 들어가 README를 보고 이 프로젝트가 무엇을 하는지 말해 봅니다
2. Releases에서 아무 언어로 된 가이드 PDF를 다운로드합니다
3. 커밋 이력에서 가장 최근 수정을 찾고 무엇을 바꿨는지 말해 봅니다
4. Issues에서 "PDF"를 검색해 관련 문제가 있는지 확인합니다
5. "편집 → PR 제출" 절차에 따라 오타 하나를 수정하고 끌어오기 요청을 제출합니다

### 공식 문서 안내

더 깊이 있는 사용법이 필요하면 다음 공식 문서를 필요에 따라 참고하세요:

- GitHub 빠른 시작: [https://docs.github.com/ko/get-started/quickstart](https://docs.github.com/ko/get-started/quickstart)
- 코드 작성과 저장(브랜치/커밋/PR): [https://docs.github.com/ko/get-started/start-your-journey/writing-and-storing-your-code](https://docs.github.com/ko/get-started/start-your-journey/writing-and-storing-your-code)
- Git 치트시트: [https://docs.github.com/ko/get-started/git-basics/git-cheatsheet](https://docs.github.com/ko/get-started/git-basics/git-cheatsheet)
- 검색 구문: [https://docs.github.com/ko/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax](https://docs.github.com/ko/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax)
- GitHub 조직의 저장소 역할: [https://docs.github.com/ko/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization](https://docs.github.com/ko/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization)
- 대화형 과정(영어): [https://skills.github.com/](https://skills.github.com/)

> [!info] 확실하지 않은 작업은 먼저 관리자에게 문의하거나 Issues에 질문하세요.
