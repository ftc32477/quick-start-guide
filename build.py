#!/usr/bin/env python3
"""
FTC 32477 Origin 快速入门指南 — 多语言 Markdown → HTML 构建工具

用法:
    python3 build.py                      # 构建所有语言版本
    python3 build.py --watch              # 监听文件变化并自动构建
    python3 build.py --channel dev        # 显式指定构建通道（dev 显示 preview 版本并加 noindex）
    python3 build.py --channel release    # release 通道（默认非 dev 分支）

构建通道判定：--channel 参数 > GITHUB_REF_NAME（CI 检出为 detached HEAD）> 本地 git 分支。

目录结构:
    src/{zh-hans,zh-hant,en-us,fr,es,ko}/  — 各语言 Markdown 源文件（在此编辑内容）
    images/                 — 图片资源（自动复制到 dist/images/）
    fonts/                  — PDF 字体子集（网页版不使用）
    dist/                   — 生成的 HTML 网站（根门户 + 各语言子目录）
"""

import os
import re
import sys
import time
import shutil
import hashlib
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
DIST_DIR = os.path.join(BASE_DIR, "dist")

# 内容页清单（page_key 为所有语言共用；各语言主页 index.html 由 render_lang_homepage 生成，不在其中）
PAGE_KEYS = [
    "preface",
    "member",
    "modeling",
    "build",
    "programming",
    "outreach",
    "afterword",
]

# 各语言配置
LANGUAGES = {
    "zh-hans": {
        "label": "简体中文",
        "lang_label": "语言",
        "menu_label": "菜单",
        "back_home_label": "返回主页",
        "back_portal_label": "返回门户",
        "sort_label": "排序",
        "dev_badge_label": "开发预览版",
        "brand": "快速入门指南",
        "site_title": "FTC 32477 Origin 快速入门指南",
        "pages": {
            "index":       "主页",
            "preface":     "前言",
            "member":      "队员须知",
            "modeling":    "建模设计",
            "build":       "结构建造",
            "programming": "程序设计",
            "outreach":    "外部联络",
            "afterword":   "后记",
        },
    },
    "zh-hant": {
        "label": "繁體中文",
        "lang_label": "語言",
        "menu_label": "選單",
        "back_home_label": "返回首頁",
        "back_portal_label": "返回入口",
        "sort_label": "排序",
        "dev_badge_label": "開發預覽版",
        "brand": "快速入門指南",
        "site_title": "FTC 32477 Origin 快速入門指南",
        "pages": {
            "index":       "首頁",
            "preface":     "前言",
            "member":      "隊員須知",
            "modeling":    "建模設計",
            "build":       "結構建造",
            "programming": "程式設計",
            "outreach":    "外部聯絡",
            "afterword":   "後記",
        },
    },
    "en-us": {
        "label": "English (US)",
        "lang_label": "Language",
        "menu_label": "Menu",
        "back_home_label": "Back to home",
        "back_portal_label": "Back to portal",
        "sort_label": "Sort",
        "dev_badge_label": "Dev Preview",
        "brand": "Quick Start Guide",
        "site_title": "FTC 32477 Origin Quick Start Guide",
        "pages": {
            "index":       "Home",
            "preface":     "Preface",
            "member":      "Team Essentials",
            "modeling":    "Modeling &amp; Design",
            "build":       "Hardware &amp; Build",
            "programming": "Programming",
            "outreach":    "Outreach &amp; PR",
            "afterword":   "Afterword",
        },
    },
    "fr": {
        "label": "Français",
        "lang_label": "Langue",
        "menu_label": "Menu",
        "back_home_label": "Retour à l'accueil",
        "back_portal_label": "Retour au portail",
        "sort_label": "Trier",
        "dev_badge_label": "Aperçu développement",
        "brand": "Guide de démarrage rapide",
        "site_title": "Guide de démarrage rapide FTC 32477 Origin",
        "pages": {
            "index":       "Accueil",
            "preface":     "Préface",
            "member":      "Essentiels de l'équipe",
            "modeling":    "Modélisation &amp; Conception",
            "build":       "Matériel &amp; Construction",
            "programming": "Programmation",
            "outreach":    "Sensibilisation &amp; Relations publiques",
            "afterword":   "Postface",
        },
    },
    "es": {
        "label": "Español",
        "lang_label": "Idioma",
        "menu_label": "Menú",
        "back_home_label": "Volver al inicio",
        "back_portal_label": "Volver al portal",
        "sort_label": "Ordenar",
        "dev_badge_label": "Vista previa de desarrollo",
        "brand": "Guía de inicio rápido",
        "site_title": "Guía de inicio rápido de FTC 32477 Origin",
        "pages": {
            "index":       "Inicio",
            "preface":     "Prefacio",
            "member":      "Esenciales del equipo",
            "modeling":    "Modelado y diseño",
            "build":       "Hardware y construcción",
            "programming": "Programación",
            "outreach":    "Divulgación y relaciones públicas",
            "afterword":   "Epílogo",
        },
    },
    "ko": {
        "label": "한국어",
        "lang_label": "언어",
        "menu_label": "메뉴",
        "back_home_label": "홈으로 돌아가기",
        "back_portal_label": "포털로 돌아가기",
        "sort_label": "정렬",
        "dev_badge_label": "개발 미리보기",
        "brand": "빠른 시작 가이드",
        "site_title": "FTC 32477 Origin 빠른 시작 가이드",
        "pages": {
            "index":       "홈",
            "preface":     "머리말",
            "member":      "팀원 필수사항",
            "modeling":    "모델링 및 설계",
            "build":       "하드웨어 및 제작",
            "programming": "프로그래밍",
            "outreach":    "아웃리치 및 대외 홍보",
            "afterword":   "후기",
        },
    },
    "pt-br": {
        "label": "Português (BR)",
        "lang_label": "Idioma",
        "menu_label": "Menu",
        "back_home_label": "Voltar ao início",
        "back_portal_label": "Voltar ao portal",
        "sort_label": "Ordenar",
        "dev_badge_label": "Prévia de desenvolvimento",
        "brand": "Guia de início rápido",
        "site_title": "Guia de início rápido do FTC 32477 Origin",
        "pages": {
            "index":       "Início",
            "preface":     "Prefácio",
            "member":      "Essenciais da equipe",
            "modeling":    "Modelagem e design",
            "build":       "Hardware e construção",
            "programming": "Programação",
            "outreach":    "Divulgação e relações públicas",
            "afterword":   "Posfácio",
        },
    },
}

DEFAULT_LANG = "zh-hans"

# 社交分享 og:image 使用线上绝对地址（GitHub Pages 部署路径）
OG_IMAGE = "https://ftc32477.github.io/docs/images/basic/team_logo.png"


def meta_tags(title, description):
    """SEO 描述与社交分享 meta（og:/twitter:，含绝对地址 og:image）。"""
    t = title.replace('"', "&quot;")
    d = description.replace('"', "&quot;")
    return (
        f'<meta name="description" content="{d}">\n'
        f'<meta property="og:type" content="website">\n'
        f'<meta property="og:title" content="{t}">\n'
        f'<meta property="og:description" content="{d}">\n'
        f'<meta property="og:image" content="{OG_IMAGE}">\n'
        f'<meta name="twitter:card" content="summary">\n'
        f'<meta name="twitter:title" content="{t}">\n'
        f'<meta name="twitter:description" content="{d}">\n'
        f'<meta name="twitter:image" content="{OG_IMAGE}">'
    )

# PDF 下载链接指向的 GitHub Release（发版时更新 RELEASE_TAG，并同步 VERSIONS 顶部条目与 PDF 文件名）
RELEASE_BASE = "https://github.com/ftc32477/quick-start-guide/releases/download"
RELEASE_TAG = "v1.3.3"

# 历史版本数据（发版时在最前追加一条；status："released" 正式发布 / "preview" 开发中，仅 dev 分支预览站显示）
# name / changes 均按各语言提供；date 为 ISO 格式，页面按语言本地化展示
VERSIONS = [
    {
        "tag": "v1.3.3",
        "date": "2026-10-03",
        "status": "released",
        "name": {
            "zh-hans": "2026年9月第1版·第3次修订",
            "zh-hant": "2026年9月第1版·第3次修訂",
            "en-us": "September 2026, 1st Edition · Revision 3",
            "fr": "Septembre 2026, 1re édition · révision 3",
            "es": "1.ª edición, septiembre de 2026 · revisión 3",
            "ko": "2026년 9월 제1판 · 3차 개정",
        },
        "changes": {
            "zh-hans": [
                "后记两张合照下新增合影名单（按上排/下排从左至右标注姓名），六语言同步。",
                "README 重构：文首新增阅读导航与按任务直达表，并新增「配图规范」章节（尺寸、去 EXIF、截图去敏、图片组、合照规范）。",
                "dev 预览站新增可见「开发预览版」标识（打印时自动隐藏）。",
                "PDF 页面尺寸统一为精确 A4（595.276×841.89pt），构建时自动归一化，不缩放内容。",
            ],
            "zh-hant": [
                "後記兩張合照下新增合影名單（按上排/下排由左至右標註姓名），六語言同步。",
                "README 重構：文首新增閱讀導覽與按任務直達表，並新增「配圖規範」章節（尺寸、去除 EXIF、截圖去敏、圖片組、合照規範）。",
                "dev 預覽站新增可見「開發預覽版」標識（列印時自動隱藏）。",
                "PDF 頁面尺寸統一為精確 A4（595.276×841.89pt），建置時自動歸一化，不縮放內容。",
            ],
            "en-us": [
                "Added photo rosters under both group photos in the afterword (top/bottom rows, left to right), synchronized across all six languages.",
                "README restructured: added a top-of-file reading guide with task-based links, plus an \"Image Guidelines\" section (sizes, EXIF removal, screenshot hygiene, image rows, group-photo rules).",
                "The dev preview site now shows a visible \"Dev Preview\" badge (hidden automatically when printing).",
                "Unified all PDF page sizes to exact A4 (595.276×841.89 pt) during build, without scaling content.",
            ],
            "fr": [
                "Ajout de la liste nominative sous les deux photos de groupe de la postface (rangées supérieure/inférieure, de gauche à droite), synchronisée dans les six langues.",
                "README restructuré : guide de lecture en tête avec liens par tâche, et nouvelle section « Règles pour les images » (dimensions, suppression des EXIF, hygiène des captures d'écran, groupes d'images, photos de groupe).",
                "Le site de prévisualisation dev affiche désormais un badge « Aperçu développement » (masqué automatiquement à l'impression).",
                "Toutes les pages PDF sont désormais au format A4 exact (595,276 × 841,89 pt) lors du build, sans mise à l'échelle du contenu.",
            ],
            "es": [
                "Añadidas las listas de nombres bajo las dos fotos de grupo del epílogo (filas superior/inferior, de izquierda a derecha), sincronizadas en los seis idiomas.",
                "README reestructurado: guía de lectura al inicio con enlaces por tarea y nueva sección «Reglas para las imágenes» (tamaños, eliminación de EXIF, higiene de capturas, grupos de imágenes, fotos de grupo).",
                "El sitio de vista previa dev ahora muestra una etiqueta visible «Vista previa de desarrollo» (se oculta al imprimir).",
                "Todas las páginas del PDF se unifican al A4 exacto (595,276 × 841,89 pt) durante la compilación, sin escalar el contenido.",
            ],
            "ko": [
                "후기의 단체 사진 두 장 아래에 촬영 명단(윗줄/아랫줄 왼쪽부터)을 추가하고 6개 언어에 동기화했습니다.",
                "README 개편: 문서 상단에 읽기 안내와 작업별 바로가기를 추가하고, 「이미지 규칙」 절(크기, EXIF 제거, 스크린샷 위생, 이미지 그룹, 단체 사진 규칙)을 신설했습니다.",
                "dev 미리보기 사이트에 눈에 보이는 「개발 미리보기」 배지를 추가했습니다(인쇄 시 자동 숨김).",
                "PDF 모든 페이지 크기를 정확한 A4(595.276×841.89pt)로 통일했으며 내용은 축소하지 않습니다.",
            ],
        },
        "pdfs": {
            "zh-hans": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.3-zh-hans.pdf",
            "zh-hant": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.3-zh-hant.pdf",
            "en-us": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.3-en-us.pdf",
            "fr": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.3-fr.pdf",
            "es": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.3-es.pdf",
            "ko": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.3-ko.pdf",
        },
    },
    {
        "tag": "v1.3.2",
        "date": "2026-10-03",
        "status": "released",
        "name": {
            "zh-hans": "2026年9月第1版·第2次修订",
            "zh-hant": "2026年9月第1版·第2次修訂",
            "en-us": "September 2026, 1st Edition · Revision 2",
            "fr": "Septembre 2026, 1re édition · révision 2",
            "es": "1.ª edición, septiembre de 2026 · revisión 2",
            "ko": "2026년 9월 제1판 · 2차 개정",
        },
        "changes": {
            "zh-hans": [
                "修正英文版 LocalSend 下载链接（原 /en/download 失效），并为西班牙语、韩语版补回遗漏的「队伍自建局域网」信息框。",
                "法语、西班牙语、韩语版外部文档链接改用对应语言页面（LocalSend、Bambu Studio、GitHub Docs、Android Studio）；统一简中版案例顺序与西/韩语术语标注。",
                "工程与站点：CI 部署前先构建校验并加并发保护；修复 dev 通道在 CI 中的判定；dev 站 noindex、正式站 canonical/hreflang；发布仓库清理历史 PDF 并新增根入口、robots、404 与 sitemap。",
                "PDF：新增章/节书签大纲与文档元数据；统一全书页面尺寸；提升版权页法律声明对比度；局域网地址补充访问范围说明。",
            ],
            "zh-hant": [
                "修正英文版 LocalSend 下載連結（原 /en/download 失效），並為西班牙語、韓語版補回遺漏的「隊伍自建區域網路」資訊框。",
                "法語、西班牙語、韓語版外部文件連結改用對應語言頁面（LocalSend、Bambu Studio、GitHub Docs、Android Studio）；統一簡中版案例順序與西/韓語術語標註。",
                "工程與站點：CI 部署前先建置校驗並加並行保護；修復 dev 通道在 CI 中的判定；dev 站 noindex、正式站 canonical/hreflang；發布倉庫清理歷史 PDF 並新增根入口、robots、404 與 sitemap。",
                "PDF：新增章/節書籤大綱與文件中介資料；統一全書頁面尺寸；提升版權頁法律聲明對比度；區域網址補充存取範圍說明。",
            ],
            "en-us": [
                "Fixed the English LocalSend download link (the old /en/download path is dead) and restored the missing \"team LAN / campus gateway\" info box in the Spanish and Korean editions.",
                "French, Spanish and Korean editions now link to the matching language pages for LocalSend, Bambu Studio, GitHub Docs and Android Studio; aligned case ordering and terminology annotations.",
                "Engineering & site: CI now rebuilds and verifies before deploying, with concurrency protection; fixed dev-channel detection in CI; the dev site is noindex while production gains canonical/hreflang; cleaned historical PDFs from the pages repository and added a root entry, robots, 404 and sitemap.",
                "PDF: added chapter/section outlines and document metadata, unified page sizes, improved copyright-page legal contrast, and clarified the LAN-only address.",
            ],
            "fr": [
                "Correction du lien de téléchargement LocalSend en anglais (l'ancien chemin /en/download est mort) et rétablissement de l'encadré « réseau local de l'équipe » manquant dans les éditions espagnole et coréenne.",
                "Les éditions française, espagnole et coréenne renvoient désormais vers les pages en langue correspondante pour LocalSend, Bambu Studio, GitHub Docs et Android Studio ; ordre des cas et annotations terminologiques harmonisés.",
                "Ingénierie et site : la CI reconstruit et vérifie avant de déployer, avec protection contre les exécutions concurrentes ; détection du canal dev corrigée ; site dev en noindex, site de production avec canonical/hreflang ; nettoyage des PDF historiques du dépôt de publication et ajout d'une entrée racine, robots, 404 et sitemap.",
                "PDF : ajout des signets de chapitres/sections et des métadonnées, unification des formats de page, amélioration du contraste de la mention légale et précision sur l'accès au réseau local.",
            ],
            "es": [
                "Corregido el enlace de descarga de LocalSend en la edición inglesa (la antigua ruta /en/download no funciona) y restaurado el cuadro informativo «LAN del equipo» que faltaba en las ediciones española y coreana.",
                "Las ediciones francesa, española y coreana ahora enlazan a las páginas en su idioma para LocalSend, Bambu Studio, GitHub Docs y Android Studio; se alinearon el orden de los casos y las anotaciones terminológicas.",
                "Ingeniería y sitio: la CI ahora recompila y verifica antes de desplegar, con protección de concurrencia; corregida la detección del canal dev; sitio dev con noindex y producción con canonical/hreflang; limpieza de los PDF históricos del repositorio de publicación y añadidos entrada raíz, robots, 404 y sitemap.",
                "PDF: añadidos marcadores de capítulo/sección y metadatos del documento, tamaños de página unificados, mejor contraste de la mención legal y aclaración sobre el acceso a la red local.",
            ],
            "ko": [
                "영어판 LocalSend 다운로드 링크를 수정하고(기존 /en/download 경로 만료), 스페인어·한국어판에서 누락된 「팀 자체 구축 LAN」 안내 상자를 복원했습니다.",
                "프랑스어·스페인어·한국어판의 외부 문서 링크를 해당 언어 페이지로 변경했으며(LocalSend, Bambu Studio, GitHub Docs, Android Studio), 사례 순서와 용어 표기를 통일했습니다.",
                "엔지니어링·사이트: CI가 배포 전에 재빌드·검증하고 동시 실행을 방지하도록 했으며, CI의 dev 채널 판정을 수정했습니다. dev 사이트는 noindex, 정식 사이트는 canonical/hreflang을 적용했고, 배포 저장소의 과거 PDF를 정리하고 루트 진입 페이지·robots·404·sitemap을 추가했습니다.",
                "PDF: 장/절 북마크와 문서 메타데이터를 추가하고 페이지 크기를 통일했으며, 판권면 법적 고지의 대비를 개선하고 LAN 주소의 접속 범위를 명시했습니다.",
            ],
        },
        "pdfs": {
            "zh-hans": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.2-zh-hans.pdf",
            "zh-hant": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.2-zh-hant.pdf",
            "en-us": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.2-en-us.pdf",
            "fr": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.2-fr.pdf",
            "es": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.2-es.pdf",
            "ko": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.2-ko.pdf",
        },
    },
    {
        "tag": "v1.3.1",
        "date": "2026-10-03",
        "status": "released",
        "name": {
            "zh-hans": "2026年9月第1版·第1次修订",
            "zh-hant": "2026年9月第1版·第1次修訂",
            "en-us": "September 2026, 1st Edition · Revision 1",
            "fr": "Septembre 2026, 1re édition · révision 1",
            "es": "1.ª edición, septiembre de 2026 · revisión 1",
            "ko": "2026년 9월 제1판 · 1차 개정",
        },
        "changes": {
            "zh-hans": [
                "PDF 排版字体全面升级：正文改用思源宋体、标题改用思源黑体、引文/图注/前言改用霞鹜文楷，西文与数字优先使用 Times New Roman（缺失时 Tinos）。",
                "页眉与页脚改由构建脚本统一盖印字体子集，跨平台字形一致。",
                "字体按实际用字裁成子集随仓库提供（约 10MB），离线构建、无需安装字体；构建时自动校验用字覆盖。",
                "中文排版由大量 Type3 碎片字体改为规范 Type0 嵌入子集：文字可搜索复制，PDF 体积约减半。网页版不受影响。",
            ],
            "zh-hant": [
                "PDF 排版字體全面升級：正文改用思源宋體、標題改用思源黑體、引文/圖註/前言改用霞鶩文楷，西文與數字優先使用 Times New Roman（缺失時 Tinos）。",
                "頁眉與頁腳改由建置腳本統一蓋印字體子集，跨平台字形一致。",
                "字體按實際用字裁成子集隨倉庫提供（約 10MB），離線建置、無需安裝字體；建置時自動校驗用字覆蓋。",
                "中文排版由大量 Type3 碎片字體改為規範 Type0 嵌入子集：文字可搜尋複製，PDF 體積約減半。網頁版不受影響。",
            ],
            "en-us": [
                "PDF typography overhaul: body text in Source Han Serif, headings in Source Han Sans, quotations/captions/preface in LXGW WenKai (Kai), and Latin text and figures in Times New Roman (Tinos as fallback).",
                "Headers and footers are now stamped by the build script using embedded font subsets, for consistent glyphs across platforms.",
                "Fonts are subset to the characters actually used and shipped with the repository (about 10 MB): offline builds with no font installation, plus automatic character-coverage checks at build time.",
                "CJK text now uses proper embedded Type0 subsets instead of many fragmented Type3 fonts: text is searchable and copyable, and PDF size is roughly halved. The website is unaffected.",
            ],
            "fr": [
                "Refonte typographique des PDF : texte courant en Source Han Serif, titres en Source Han Sans, citations/légendes/préface en LXGW WenKai (kai), et texte latin et chiffres en Times New Roman (Tinos en secours).",
                "Les en-têtes et pieds de page sont désormais imprimés par le script de build à partir de sous-ensembles de polices embarqués, pour des glyphes identiques sur toutes les plateformes.",
                "Les polices sont réduites aux caractères réellement utilisés et fournies avec le dépôt (environ 10 Mo) : builds hors ligne sans installation de polices, avec contrôle automatique de la couverture des caractères.",
                "Les textes CJK utilisent désormais de véritables sous-ensembles Type0 embarqués au lieu de nombreux fragments Type3 : texte recherchable et copiable, taille des PDF environ divisée par deux. Le site web n'est pas affecté.",
            ],
            "es": [
                "Renovación tipográfica de los PDF: cuerpo en Source Han Serif, títulos en Source Han Sans, citas/pies de foto/prefacio en LXGW WenKai (kai) y texto latino y cifras en Times New Roman (Tinos como reserva).",
                "Los encabezados y pies de página ahora los estampa el script de compilación con subconjuntos de fuentes incrustados, para obtener glifos idénticos en todas las plataformas.",
                "Las fuentes se recortan a los caracteres realmente usados y se incluyen en el repositorio (unos 10 MB): compilación sin conexión y sin instalar fuentes, con verificación automática de cobertura de caracteres.",
                "El texto CJK ahora usa subconjuntos Type0 incrustados en lugar de numerosos fragmentos Type3: el texto se puede buscar y copiar, y el tamaño de los PDF se reduce a la mitad. El sitio web no se ve afectado.",
            ],
            "ko": [
                "PDF 타이포그래피 전면 개편: 본문은 본명조(思源宋體), 제목은 본고딕(思源黑體), 인용/그림 설명/머리말은 샤오우웬카이(霞鶩文楷), 라틴 문자와 숫자는 Times New Roman(없으면 Tinos)을 사용합니다.",
                "머리글과 바닥글을 빌드 스크립트가 내장 글꼴 서브셋으로 통일하여 인쇄하며, 플랫폼에 관계없이 동일한 글리프를 보장합니다.",
                "글꼴은 실제 사용된 글자만 잘라 서브셋으로 저장소에 포함(약 10MB)되므로 오프라인 빌드가 가능하고 글꼴 설치가 필요 없으며, 빌드 시 글자 커버리지를 자동 검증합니다.",
                "한중일 텍스트는 수많은 Type3 조각 글꼴 대신 규격 Type0 내장 서브셋을 사용하여 검색·복사가 가능하고 PDF 용량이 약 절반으로 줄었습니다. 웹 버전은 영향을 받지 않습니다.",
            ],
        },
        "pdfs": {
            "zh-hans": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.1-zh-hans.pdf",
            "zh-hant": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.1-zh-hant.pdf",
            "en-us": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.1-en-us.pdf",
            "fr": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.1-fr.pdf",
            "es": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.1-es.pdf",
            "ko": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.1-ko.pdf",
        },
    },
    {
        "tag": "v1.3.0",
        "date": "2026-09-09",
        "status": "released",
        "name": {
            "zh-hans": "2026年9月第1版",
            "zh-hant": "2026年9月第1版",
            "en-us": "September 2026, 1st Edition",
            "fr": "Septembre 2026, 1re édition",
            "es": "1.ª edición, septiembre de 2026",
            "ko": "2026년 9월 제1판",
        },
        "changes": {
            "zh-hans": [
                "队员须知新增「赛季与活动安排」章节：赛季时间线与赛事规则须知（仅限 Xbox 360 手柄、磁悬浮禁令、参赛年龄 12–18 岁），并细化队伍局域网说明。",
                "程序设计新增「AI 辅助编程」小节（配合 AI Agent 等工具）与 Driver 手柄操作说明。",
                "外部联络补充工程笔记定位、经费说明与「启发奖与赛事得分」（竞技第一 40 分、启发奖第一 60 分），并补充强队定制车案例。",
                "结构建造补充官方器材采购平替策略；建模设计补充建模文件共享经验。",
            ],
            "zh-hant": [
                "隊員須知新增「賽季與活動安排」章節：賽季時間線與賽事規則須知（僅限 Xbox 360 手把、磁浮禁令、參賽年齡 12–18 歲），並細化隊伍區域網路說明。",
                "程式設計新增「AI 輔助程式設計」小節（配合 AI Agent 等工具）與 Driver 手把操作說明。",
                "外部聯絡補充工程筆記定位、經費說明與「啟發獎與賽事得分」（競技第一 40 分、啟發獎第一 60 分），並補充強隊訂製車案例。",
                "結構建造補充官方器材採購平替策略；建模設計補充建模檔案共享經驗。",
            ],
            "en-us": [
                "Team Essentials: added a \"Season & Schedule\" section (season timeline and rules notes — Xbox 360 controller only, magnetic levitation ban, age range 12–18) and refined the team LAN description.",
                "Programming: added an \"AI-Assisted Programming\" section (using AI Agent tools) and a Driver/controller note.",
                "Outreach & PR: clarified the engineering notebook's role, added funding notes and an \"Inspire Award & Scoring\" section (40 points for competition first place vs 60 for the Inspire Award), and added a case of strong teams with fully custom vehicles.",
                "Hardware & Build: added the procurement substitution strategy for official parts; Modeling & Design: added experience on sharing CAD files between teams.",
            ],
            "fr": [
                "Essentiels de l'équipe : ajout d'une section « Saison et emploi du temps » (calendrier de la saison et règles — manette Xbox 360 uniquement, interdiction de la sustentation magnétique, tranche d'âge 12–18 ans) et précisions sur le réseau local de l'équipe.",
                "Programmation : ajout d'une section « Programmation assistée par IA » (avec des outils d'agent IA) et d'une note sur le pilotage (Driver).",
                "Sensibilisation & Relations publiques : clarification du rôle du cahier d'ingénierie, ajout de notes sur le financement et d'une section « Prix Inspire et notation » (40 points pour la première place compétitive contre 60 pour le prix Inspire), et ajout d'un cas d'équipes fortes aux robots entièrement personnalisés.",
                "Matériel & Construction : ajout de la stratégie de substitution pour l'achat de pièces officielles ; Modélisation & Conception : ajout d'une expérience sur le partage des fichiers CAO entre équipes.",
            ],
            "es": [
                "Esenciales del equipo: añadida la sección «Temporada y horarios» (calendario de la temporada y notas sobre las reglas — solo mando Xbox 360, prohibición de la levitación magnética, rango de edad 12–18) y precisada la descripción de la LAN del equipo.",
                "Programación: añadida la sección «Programación asistida por IA» (con herramientas de agente de IA) y una nota sobre el pilotaje (Driver).",
                "Divulgación y relaciones públicas: aclarado el papel del cuaderno de ingeniería, añadidas notas de financiación y la sección «Premio Inspire y puntuación» (40 puntos para el primer puesto competitivo frente a 60 del Premio Inspire), y añadido un caso de equipos fuertes con robots totalmente personalizados.",
                "Hardware y construcción: añadida la estrategia de sustitución para la compra de piezas oficiales; Modelado y diseño: añadida una experiencia sobre el intercambio de archivos CAD entre equipos.",
            ],
            "ko": [
                "팀원 필수사항: 「시즌과 활동 일정」 장 추가(시즌 일정과 규칙 — Xbox 360 컨트롤러만 허용, 자기 부상 금지, 참가 연령 12~18세) 및 팀 LAN 설명 보강.",
                "프로그래밍: 「AI 활용 프로그래밍」 절 추가(AI Agent 등 도구 활용) 및 Driver 컨트롤러 조종 안내 추가.",
                "아웃리치 및 대외 홍보: 엔지니어링 노트의 역할 명확화, 경비 안내와 「Inspire 어워드와 점수」 절 추가(경기 1위 40점 대 Inspire 어워드 1위 60점), 완전 맞춤형 로봇을 만드는 강팀 사례 추가.",
                "하드웨어 및 제작: 공식 부품 구매 대체 전략 추가; 모델링 및 설계: 팀 간 CAD 파일 공유 경험 추가.",
            ],
        },
        "pdfs": {
            "zh-hans": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.0-zh-hans.pdf",
            "zh-hant": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.0-zh-hant.pdf",
            "en-us": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.0-en-us.pdf",
            "fr": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.0-fr.pdf",
            "es": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.0-es.pdf",
            "ko": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.3.0-ko.pdf",
        },
    },
    {
        "tag": "v1.2.2",
        "date": "2026-08-17",
        "status": "released",
        "name": {
            "zh-hans": "2026年8月第3版·第2次修订",
            "zh-hant": "2026年8月第3版·第2次修訂",
            "en-us": "August 2026, 3rd Edition, 2nd Revision",
            "fr": "Août 2026, 3e édition, 2e révision",
            "es": "3.ª edición, agosto de 2026, 2.ª revisión",
            "ko": "2026년 8월 제3판 · 2차 개정",
        },
        "changes": {
            "zh-hans": [
                "繁体中文版「结构体/装配体」术语统一为繁体字形（結構體/裝配體）。",
                "历史版本页说明补充：早期版本仅含发布时已有的语言。",
                "PDF 封面/封底版本信息改为两行排版并加大行距，封底右对齐。",
                "工程化更新：版次信息全面数据驱动（侧边栏页脚、主页最新版本、PDF 封面日期自动取自 VERSIONS）；新增 check-dist CI 校验与 release.sh 半自动发版脚本；Release 说明归档至 release-notes/；全站新增 SEO 社交分享 meta 与本地化无障碍标签；--watch 扩展监听 images/ 与 build.py。",
            ],
            "zh-hant": [
                "繁體中文版「结构体/装配体」術語統一為繁體字形（結構體/裝配體）。",
                "歷史版本頁說明補充：早期版本僅含發布時已有的語言。",
                "PDF 封面/封底版本資訊改為兩行排版並加大行距，封底右對齊。",
                "工程化更新：版次資訊全面資料驅動（側邊欄頁尾、首頁最新版本、PDF 封面日期自動取自 VERSIONS）；新增 check-dist CI 校驗與 release.sh 半自動發版腳本；Release 說明歸檔至 release-notes/；全站新增 SEO 社交分享 meta 與本地化無障礙標籤；--watch 擴展監聽 images/ 與 build.py。",
            ],
            "en-us": [
                "Traditional Chinese edition: the Onshape terms 「结构体/装配体」 are now written in traditional characters (結構體/裝配體).",
                "Version history page: clarified that earlier versions include only the languages available at their release.",
                "PDF cover and back cover: version information is now set on two lines with increased line spacing, and the back cover lines are right-aligned.",
                "Engineering updates: edition data is now fully data-driven from VERSIONS (sidebar footer, homepage latest version, PDF cover date); added a check-dist CI workflow and a semi-automated release script (release.sh); Release notes are archived in release-notes/; all pages now include SEO/social-sharing meta tags and localized accessibility labels; --watch now monitors images/ and build.py as well.",
            ],
            "fr": [
                "Édition chinoise traditionnelle : les termes Onshape « 结构体/装配体 » sont désormais écrits en caractères traditionnels (結構體/裝配體).",
                "Page d'historique des versions : précision que les versions antérieures ne contiennent que les langues disponibles à leur publication.",
                "Couverture et quatrième de couverture du PDF : les informations de version sont désormais sur deux lignes avec un interligne accru, et les lignes de la quatrième de couverture sont alignées à droite.",
                "Améliorations techniques : les informations d'édition sont désormais entièrement dérivées des VERSIONS (pied de page latéral, dernière version de la page d'accueil, date de couverture du PDF) ; ajout d'un workflow CI check-dist et d'un script de publication semi-automatisé (release.sh) ; les notes de version sont archivées dans release-notes/ ; toutes les pages incluent désormais des balises meta SEO/partage social et des étiquettes d'accessibilité localisées ; --watch surveille également images/ et build.py.",
            ],
            "es": [
                "Edición en chino tradicional: los términos de Onshape «结构体/装配体» se escriben ahora en caracteres tradicionales (結構體/裝配體).",
                "Página de historial de versiones: se aclara que las versiones anteriores incluyen solo los idiomas disponibles en su publicación.",
                "Cubierta y contraportada del PDF: la información de versión se muestra ahora en dos líneas con mayor interlineado, y las líneas de la contraportada están alineadas a la derecha.",
                "Mejoras de ingeniería: los datos de edición se derivan ahora por completo de VERSIONS (pie de página lateral, versión más reciente de la página de inicio, fecha de la cubierta del PDF); se añade un workflow CI check-dist y un script de publicación semiautomatizado (release.sh); las notas de versión se archivan en release-notes/; todas las páginas incluyen ahora metaetiquetas SEO/para compartir en redes y etiquetas de accesibilidad localizadas; --watch también supervisa images/ y build.py.",
            ],
            "ko": [
                "중국어 번체판: Onshape 용어 「结构体/装配体」를 번체자(結構體/裝配體)로 통일했습니다.",
                "버전 기록 페이지: 초기 버전에는 출시 당시 제공되던 언어만 포함된다는 설명을 추가했습니다.",
                "PDF 표지/뒷표지: 버전 정보를 두 줄로 배치하고 줄 간격을 넓혔으며, 뒷표지는 오른쪽 정렬했습니다.",
                "엔지니어링 개선: 판본 정보를 VERSIONS에서 완전히 데이터 구동(사이드바 푸터, 홈 최신 버전, PDF 표지 날짜)하고, check-dist CI 워크플로와 반자동 발매 스크립트(release.sh)를 추가했으며, Release 설명을 release-notes/에 보관합니다. 모든 페이지에 SEO/소셜 공유 meta 태그와 현지화된 접근성 라벨을 추가했고, --watch가 images/와 build.py도 감시합니다.",
            ],
        },
        "pdfs": {
            "zh-hans": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-zh-hans.pdf",
            "zh-hant": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-zh-hant.pdf",
            "en-us": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-en-us.pdf",
            "fr": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-fr.pdf",
            "es": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-es.pdf",
            "ko": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.2-ko.pdf",
        },
    },
    {
        "tag": "v1.2.1",
        "date": "2026-08-16",
        "status": "released",
        "name": {
            "zh-hans": "2026年8月第3版·第1次修订",
            "zh-hant": "2026年8月第3版·第1次修訂",
            "en-us": "August 2026, 3rd Edition, 1st Revision",
            "fr": "Août 2026, 3e édition, 1re révision",
            "es": "3.ª edición, agosto de 2026, 1.ª revisión",
            "ko": "2026년 8월 제3판 · 1차 개정",
        },
        "changes": {
            "zh-hans": [
                "繁体中文版人名附注简体原名（如 付修齊（付修齐）），繁简同形者不加注。",
                "简体/繁体中文版中外来译名附注来源语言原名（如 结构体（Part Studio）、构建（Build））；全语言标注规范写入 README。",
                "门户韩语语言卡片上沿配色与西班牙语一致（#ffb953）。",
            ],
            "zh-hant": [
                "繁體中文版人名附註簡體原名（如 付修齊（付修齐）），繁簡同形者不加註。",
                "簡體/繁體中文版中外來譯名附註來源語言原名（如 结构体（Part Studio）、建置（Build））；全語言標註規範寫入 README。",
                "入口韓語語言卡片上沿配色與西班牙語一致（#ffb953）。",
            ],
            "en-us": [
                "Traditional Chinese edition: person names now carry their Simplified Chinese originals (e.g., 付修齊（付修齐）); names identical across both scripts are not annotated.",
                "Simplified and Traditional Chinese editions: translated terms of foreign origin now carry their source-language names (e.g., 结构体（Part Studio）, 构建（Build）); the annotation convention for all languages is documented in the project README.",
                "Portal: the Korean language card accent color now matches the Spanish card (#ffb953).",
            ],
            "fr": [
                "Édition chinoise traditionnelle : les noms de personnes portent désormais leur version en chinois simplifié (ex. 付修齊（付修齐）) ; les noms identiques dans les deux écritures ne sont pas annotés.",
                "Éditions chinoises simplifiée et traditionnelle : les termes traduits d'origine étrangère portent désormais leur nom dans la langue source (ex. 结构体（Part Studio）, 构建（Build）) ; la convention d'annotation pour toutes les langues est documentée dans le README du projet.",
                "Portail : la couleur d'accent de la carte de langue coréenne correspond désormais à celle de la carte espagnole (#ffb953).",
            ],
            "es": [
                "Edición en chino tradicional: los nombres de personas llevan ahora su versión en chino simplificado (p. ej., 付修齊（付修齐）); los nombres idénticos en ambas escrituras no se anotan.",
                "Ediciones en chino simplificado y tradicional: los términos traducidos de origen extranjero llevan ahora su nombre en el idioma de origen (p. ej., 结构体（Part Studio）, 构建（Build）); la convención de anotación para todos los idiomas está documentada en el README del proyecto.",
                "Portal: el color de acento de la tarjeta de idioma coreano coincide ahora con el de la tarjeta española (#ffb953).",
            ],
            "ko": [
                "중국어 번체판: 인명에 간체 원명을 병기하고(예: 付修齊（付修齐）), 번간체 동형인 이름은 병기하지 않습니다.",
                "중국어 간체/번체판: 외국어에서 번역된 용어에 출처 언어 원명을 병기합니다(예: 结构体（Part Studio）, 构建（Build）). 모든 언어의 표기 규칙을 README에 문서화했습니다.",
                "포털: 한국어 언어 카드 상단 색상을 스페인어 카드와 동일하게 변경했습니다(#ffb953).",
            ],
        },
        "pdfs": {
            "zh-hans": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.1-zh-hans.pdf",
            "zh-hant": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.1-zh-hant.pdf",
            "en-us": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.1-en-us.pdf",
            "fr": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.1-fr.pdf",
            "es": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.1-es.pdf",
            "ko": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.1-ko.pdf",
        },
    },
    {
        "tag": "v1.2.0",
        "date": "2026-08-16",
        "status": "released",
        "name": {
            "zh-hans": "2026年8月第3版",
            "zh-hant": "2026年8月第3版",
            "en-us": "August 2026, 3rd Edition",
            "fr": "Août 2026, 3e édition",
            "es": "3.ª edición, agosto de 2026",
            "ko": "2026년 8월 제3판",
        },
        "changes": {
            "zh-hans": [
                "新增韩语（한국어）版本：七章全文与网站页面（语言主页、历史版本页）同步提供韩语译本，并发布韩语 PDF。",
                "全部语言版本统一人名与专有名词标注规范：真实人名附注汉字原名（如 Fu Xiuqi (付修齐)，韩语版用汉字读音加注，如 부수제(付修齐)），平台与专有物名附注来源语言原名（如 KIRIN (麒麟)、Bilibili (哔哩哔哩)）。",
                "本版为 2026年8月第3版。",
            ],
            "zh-hant": [
                "新增韓語（한국어）版本：七章全文與網站頁面（語言首頁、歷史版本頁）同步提供韓語譯本，並發布韓語 PDF。",
                "全部語言版本統一人名與專有名詞標註規範：真實人名附註漢字原名（如 Fu Xiuqi (付修齊)，韓語版用漢字讀音加註，如 부수제(付修齊)），平台與專有物名附註來源語言原名（如 KIRIN (麒麟)、Bilibili (嗶哩嗶哩)）。",
                "本版為 2026年8月第3版。",
            ],
            "en-us": [
                "Added a Korean (한국어) edition: full translations of all seven chapters and the website pages (language homepage, version history), with a Korean PDF included.",
                "Standardized name annotations across all language editions: real person names now carry their original Chinese characters (e.g., Fu Xiuqi (付修齐); in Korean, names are given in their Korean hanja readings, e.g., 부수제(付修齐)), and proper nouns such as platforms carry their source-language names (e.g., KIRIN (麒麟), Bilibili (哔哩哔哩)).",
                "This release is the August 2026, 3rd Edition.",
            ],
            "fr": [
                "Ajout d'une édition coréenne (한국어) : traduction complète des sept chapitres et des pages du site (page d'accueil, historique des versions), avec un PDF coréen inclus.",
                "Harmonisation des annotations de noms dans toutes les éditions linguistiques : les noms de personnes portent désormais leurs caractères chinois d'origine (ex. Fu Xiuqi (付修齐) ; en coréen, les noms sont donnés dans leur lecture hanja, ex. 부수제(付修齐)), et les noms propres tels que les plateformes portent leur nom dans la langue source (ex. KIRIN (麒麟), Bilibili (哔哩哔哩)).",
                "Cette version est la 3e édition d'août 2026.",
            ],
            "es": [
                "Se ha añadido la edición en coreano (한국어): traducción completa de los siete capítulos y de las páginas del sitio (página de inicio, historial de versiones), con un PDF en coreano incluido.",
                "Se han unificado las anotaciones de nombres en todas las ediciones lingüísticas: los nombres de personas reales llevan ahora sus caracteres chinos originales (p. ej., Fu Xiuqi (付修齐); en coreano se usa la lectura hanja, p. ej., 부수제(付修齐)), y los nombres propios como las plataformas llevan su nombre en el idioma de origen (p. ej., KIRIN (麒麟), Bilibili (哔哩哔哩)).",
                "Esta versión es la 3.ª edición de agosto de 2026.",
            ],
            "ko": [
                "한국어(한국어) 버전 추가: 7개 장 전체 번역과 웹사이트 페이지(언어 홈, 버전 기록)의 한국어 번역을 제공하며 한국어 PDF를 함께 발표합니다.",
                "모든 언어 버전에서 인명 및 고유명사 표기 규칙 통일: 실존 인명에는 한자 원명을 병기하고(예: Fu Xiuqi (付修齐); 한국어판은 한자 독음으로 표기, 예: 부수제(付修齐)), 플랫폼 등 고유명사에는 출처 언어 원명을 병기합니다(예: KIRIN (麒麟), Bilibili (哔哩哔哩)).",
                "이번 버전은 2026년 8월 제3판입니다.",
            ],
        },
        "pdfs": {
            "zh-hans": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.0-zh-hans.pdf",
            "zh-hant": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.0-zh-hant.pdf",
            "en-us": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.0-en-us.pdf",
            "fr": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.0-fr.pdf",
            "es": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.0-es.pdf",
            "ko": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.2.0-ko.pdf",
        },
    },
    {
        "tag": "v1.1.0",
        "date": "2026-08-15",
        "status": "released",
        "name": {
            "zh-hans": "2026年8月第2版",
            "zh-hant": "2026年8月第2版",
            "en-us": "August 2026, 2nd Edition",
            "fr": "Août 2026, 2e édition",
            "es": "2.ª edición, agosto de 2026",
            "ko": "2026년 8월 제2판",
        },
        "changes": {
            "zh-hans": [
                "新增西班牙语（Español）版本：七章全文与网站页面（语言主页、历史版本页）同步提供西班牙语译本，并发布西班牙语 PDF。",
                "门户语言选择卡片上沿配色更新：简体/繁體中文为 #a61615，English (US)/Français 为 #d85d23，新增的西班牙语卡片为 #ffb953。",
                "本版为 2026年8月第2版，正式发布。",
            ],
            "zh-hant": [
                "新增西班牙語（Español）版本：七章全文與網站頁面（語言首頁、歷史版本頁）同步提供西班牙語譯本，並發布西班牙語 PDF。",
                "入口語言選擇卡片上沿配色更新：簡體/繁體中文為 #a61615，English (US)/Français 為 #d85d23，新增的西班牙語卡片為 #ffb953。",
                "本版為 2026年8月第2版，正式發布。",
            ],
            "en-us": [
                "Added a Spanish (Español) edition: full translations of all seven chapters and the website pages (language homepage, version history), with a Spanish PDF included.",
                "Updated the portal language card accent colors: #a61615 for Simplified/Traditional Chinese, #d85d23 for English (US)/Français, and #ffb953 for the new Spanish card.",
                "This release is the August 2026, 2nd Edition.",
            ],
            "fr": [
                "Ajout d'une édition espagnole (Español) : traduction complète des sept chapitres et des pages du site (page d'accueil, historique des versions), avec un PDF espagnol inclus.",
                "Mise à jour des couleurs d'accent des cartes de langue du portail : #a61615 pour le chinois simplifié/traditionnel, #d85d23 pour English (US)/Français et #ffb953 pour la nouvelle carte espagnole.",
                "Cette version est la 2e édition d'août 2026.",
            ],
            "es": [
                "Se ha añadido la edición en español (Español): traducción completa de los siete capítulos y de las páginas del sitio (página de inicio, historial de versiones), con un PDF en español incluido.",
                "Se han actualizado los colores de acento de las tarjetas de idioma del portal: #a61615 para el chino simplificado/tradicional, #d85d23 para English (US)/Français y #ffb953 para la nueva tarjeta en español.",
                "Esta versión es la 2.ª edición de agosto de 2026.",
            ],
            "ko": [
                "스페인어(Español) 버전 추가: 7개 장 전체 번역과 웹사이트 페이지(언어 홈, 버전 기록)의 스페인어 번역을 제공하며 스페인어 PDF를 함께 발표합니다.",
                "포털 언어 선택 카드 상단 색상 업데이트: 중국어 간체/번체는 #a61615, English (US)/Français는 #d85d23, 새 스페인어 카드는 #ffb953.",
                "이번 버전은 2026년 8월 제2판입니다.",
            ],
        },
        "pdfs": {
            "zh-hans": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.1.0-zh-hans.pdf",
            "zh-hant": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.1.0-zh-hant.pdf",
            "en-us": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.1.0-en-us.pdf",
            "fr": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.1.0-fr.pdf",
            "es": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.1.0-es.pdf",
        },
    },
    {
        "tag": "v1.0.0",
        "date": "2026-08-14",
        "status": "released",
        "name": {
            "zh-hans": "2026年8月第1版",
            "zh-hant": "2026年8月第1版",
            "en-us": "August 2026, 1st Edition",
            "fr": "Août 2026, 1re édition",
            "es": "1.ª edición, agosto de 2026",
            "ko": "2026년 8월 제1판",
        },
        "changes": {
            "zh-hans": [
                "首次出版，收录前言、队员须知、建模设计、结构建造、程序设计、外部联络、后记共七章。",
                "提供简体中文、繁體中文、English (US)、Français 四种语言版本。",
                "合并版 PDF 含封面、目录、正文与封底，页码连续编排，目录可跳转。",
            ],
            "zh-hant": [
                "首次出版，收錄前言、隊員須知、建模設計、結構建造、程式設計、外部聯絡、後記共七章。",
                "提供簡體中文、繁體中文、English (US)、Français 四種語言版本。",
                "合併版 PDF 含封面、目錄、正文與封底，頁碼連續編排，目錄可跳轉。",
            ],
            "en-us": [
                "First publication, containing seven chapters: Preface, Team Essentials, Modeling & Design, Hardware & Build, Programming, Outreach & PR, and Afterword.",
                "Available in four language editions: Simplified Chinese, Traditional Chinese, English (US), and Français.",
                "The merged PDF comprises a cover, a table of contents, the main text, and a back cover, with continuous page numbering and navigable table-of-contents links.",
            ],
            "fr": [
                "Première publication, comprenant sept chapitres : Préface, Essentiels de l'équipe, Modélisation & Conception, Matériel & Construction, Programmation, Sensibilisation & Relations publiques et Postface.",
                "Disponible en quatre versions linguistiques : chinois simplifié, chinois traditionnel, English (US) et Français.",
                "Le PDF fusionné comprend une couverture, une table des matières, le texte principal et une quatrième de couverture, avec une pagination continue et une table des matières navigable.",
            ],
            "es": [
                "Primera publicación, que incluye siete capítulos: Prefacio, Esenciales del equipo, Modelado y diseño, Hardware y construcción, Programación, Divulgación y relaciones públicas y Epílogo.",
                "Disponible en cuatro ediciones lingüísticas: chino simplificado, chino tradicional, English (US) y Français.",
                "El PDF combinado incluye cubierta, índice, texto principal y contraportada, con numeración de páginas continua e índice navegable.",
            ],
            "ko": [
                "첫 출판. 머리말, 팀원 필수사항, 모델링 및 설계, 하드웨어 및 제작, 프로그래밍, 아웃리치 및 대외 홍보, 후기 총 7개 장을 수록했습니다.",
                "중국어 간체, 중국어 번체, English (US), Français 4개 언어 버전을 제공합니다.",
                "병합 PDF에는 표지, 목차, 본문과 뒷표지가 포함되며, 페이지 번호가 연속으로 매겨지고 목차에서 바로 이동할 수 있습니다.",
            ],
        },
        "pdfs": {
            "zh-hans": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.0.0-zh-hans.pdf",
            "zh-hant": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.0.0-zh-hant.pdf",
            "en-us": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.0.0-en-us.pdf",
            "fr": "FTC-Team-32477-Origin-Quick-Start-Guide-v1.0.0-fr.pdf",
        },
    },
]


_BACKFILL_PT_BR = {
    "v1.3.3": {
        "name": "Setembro de 2026, 1.ª edição · revisão 3",
        "changes": [
            'Listas de nomes adicionadas sob as duas fotos de grupo do posfácio (filas de cima/baixo, da esquerda para a direita), sincronizadas nos seis idiomas.',
            'README reestruturado: adicionado um guia de leitura no início do arquivo, com links por tarefa, além de uma seção de "Diretrizes de imagens" (tamanhos, remoção de EXIF, higiene de capturas de tela, grupos de imagens, regras para fotos de grupo).',
            'O site de prévia de desenvolvimento agora exibe um selo visível de "Prévia de desenvolvimento" (oculto automaticamente na impressão).',
            'Todos os tamanhos de página dos PDFs foram unificados para A4 exato (595,276×841,89 pt) na build, sem escalar o conteúdo.',
        ],
    },
    "v1.3.2": {
        "name": "Setembro de 2026, 1.ª edição · revisão 2",
        "changes": [
            'Corrigido o link de download do LocalSend na edição em inglês (o antigo caminho /en/download estava quebrado) e restaurado o quadro informativo "rede local da equipe / gateway do campus" que faltava nas edições em espanhol e coreano.',
            'As edições em francês, espanhol e coreano agora apontam para as páginas no idioma correspondente para LocalSend, Bambu Studio, documentação do GitHub e Android Studio; ordem dos casos e anotações de terminologia alinhadas.',
            'Engenharia e site: a CI agora recompila e verifica antes de implantar, com proteção contra execuções concorrentes; corrigida a detecção do canal dev na CI; o site dev recebe noindex enquanto a produção ganha canonical/hreflang; PDFs históricos removidos do repositório de publicação, com entrada raiz, robots, 404 e sitemap adicionados.',
            'PDF: adicionados sumário de capítulos/seções e metadados do documento, tamanhos de página unificados, melhor contraste do texto legal da página de créditos e esclarecimento do endereço acessível somente na rede local.',
        ],
    },
    "v1.3.1": {
        "name": "Setembro de 2026, 1.ª edição · revisão 1",
        "changes": [
            'Reformulação tipográfica dos PDFs: texto corrido em Source Han Serif, títulos em Source Han Sans, citações/legendas/prefácio em LXGW WenKai (Kai) e textos e números em latim em Times New Roman (Tinos como alternativa).',
            'Cabeçalhos e rodapés agora são carimbados pelo script de build com subconjuntos de fontes embutidos, garantindo glifos consistentes em todas as plataformas.',
            'As fontes são reduzidas aos caracteres realmente usados e distribuídas com o repositório (cerca de 10 MB): builds offline sem instalar fontes, além de verificação automática de cobertura de caracteres na build.',
            'Textos CJK agora usam subconjuntos Type0 embutidos adequados, em vez de muitas fontes Type3 fragmentadas: o texto é pesquisável e copiável, e o tamanho dos PDFs caiu cerca de metade. O site não foi afetado.',
        ],
    },
    "v1.3.0": {
        "name": "Setembro de 2026, 1.ª edição",
        "changes": [
            'Essenciais da equipe: adicionada a seção "Temporada e calendário" (linha do tempo da temporada e observações de regras — somente controle Xbox 360, proibição de levitação magnética, faixa etária de 12 a 18 anos) e refinada a descrição da rede local da equipe.',
            'Programação: adicionada a seção "Programação assistida por IA" (uso de ferramentas de agente de IA) e uma observação sobre o Driver/controle.',
            'Divulgação e relações públicas: esclarecido o papel do caderno de engenharia, adicionadas notas de financiamento e a seção "Prêmio Inspiração e pontuação" (40 pontos para o primeiro lugar na competição contra 60 do Prêmio Inspiração), além de um caso de equipes fortes com robôs totalmente personalizados.',
            'Hardware e construção: adicionada a estratégia de substituição na compra de peças oficiais; Modelagem e design: adicionada experiência sobre compartilhamento de arquivos CAD entre equipes.',
        ],
    },
    "v1.2.2": {
        "name": "Agosto de 2026, 3.ª edição, 2.ª revisão",
        "changes": [
            'Edição em chinês tradicional: os termos do Onshape 「结构体/装配体」 agora são escritos em caracteres tradicionais (結構體/裝配體).',
            'Página de histórico de versões: esclarecido que as versões anteriores incluem apenas os idiomas disponíveis na época do lançamento.',
            'Capa e contracapa dos PDFs: as informações de versão agora são dispostas em duas linhas, com espaçamento maior, e as linhas da contracapa ficam alinhadas à direita.',
            'Atualizações de engenharia: os dados de edição agora são totalmente orientados por VERSIONS (rodapé da barra lateral, versão mais recente da página inicial, data da capa do PDF); adicionados o workflow de CI check-dist e o script semiautomático de release (release.sh); as notas de versão são arquivadas em release-notes/; todas as páginas passam a incluir meta tags de SEO/compartilhamento social e rótulos de acessibilidade localizados; --watch agora também monitora images/ e build.py.',
        ],
    },
    "v1.2.1": {
        "name": "Agosto de 2026, 3.ª edição, 1.ª revisão",
        "changes": [
            'Edição em chinês tradicional: os nomes de pessoas agora trazem o original em chinês simplificado (por exemplo, 付修齊（付修齐）); nomes idênticos nos dois conjuntos de caracteres não recebem anotação.',
            'Edições em chinês simplificado e tradicional: termos traduzidos de origem estrangeira agora trazem o nome no idioma de origem (por exemplo, 结构体（Part Studio）, 构建（Build）); a convenção de anotação para todos os idiomas está documentada no README do projeto.',
            'Portal: a cor de destaque do cartão de coreano agora combina com a do cartão de espanhol (#ffb953).',
        ],
    },
    "v1.2.0": {
        "name": "Agosto de 2026, 3.ª edição",
        "changes": [
            'Adicionada a edição em coreano (한국어): tradução completa dos sete capítulos e das páginas do site (página inicial do idioma, histórico de versões), com PDF em coreano incluído.',
            'Padronizadas as anotações de nomes em todas as edições: nomes reais de pessoas agora trazem os caracteres chineses originais (por exemplo, Fu Xiuqi (付修齐); em coreano, os nomes usam a leitura em hanja, por exemplo, 부수제(付修齐)), e nomes próprios como plataformas trazem o nome no idioma de origem (por exemplo, KIRIN (麒麟), Bilibili (哔哩哔哩)).',
            'Esta versão é a 3.ª edição de agosto de 2026.',
        ],
    },
    "v1.1.0": {
        "name": "Agosto de 2026, 2.ª edição",
        "changes": [
            'Adicionada a edição em espanhol (Español): tradução completa dos sete capítulos e das páginas do site (página inicial do idioma, histórico de versões), com PDF em espanhol incluído.',
            'Atualizadas as cores de destaque dos cartões de idioma do portal: #a61615 para chinês simplificado/tradicional, #d85d23 para inglês (EUA)/francês e #ffb953 para o novo cartão de espanhol.',
            'Esta versão é a 2.ª edição de agosto de 2026.',
        ],
    },
    "v1.0.0": {
        "name": "Agosto de 2026, 1.ª edição",
        "changes": [
            'Primeira publicação, com sete capítulos: Prefácio, Essenciais da equipe, Modelagem e design, Hardware e construção, Programação, Divulgação e relações públicas e Posfácio.',
            'Disponível em quatro edições de idioma: chinês simplificado, chinês tradicional, inglês (EUA) e francês.',
            'O PDF unificado é composto por capa, sumário, texto principal e contracapa, com numeração contínua de páginas e links navegáveis no sumário.',
        ],
    },
}

for _v in VERSIONS:
    _bf = _BACKFILL_PT_BR.get(_v["tag"])
    if _bf and "pt-br" not in _v.get("name", {}):
        _v["name"]["pt-br"] = _bf["name"]
        _v["changes"]["pt-br"] = _bf["changes"]


def latest_edition(lang_key):
    """最新已发布版本的版次名（取自 VERSIONS 顶部 released 条目，数据驱动）。"""
    for v in VERSIONS:
        if v.get("status") != "preview":
            name = v.get("name", {})
            return (name.get(lang_key) or name.get("en-us")
                    or name.get("zh-hans", ""))
    return ""


# 侧边栏页脚："版次名 · 编辑组名"（版次随发版自动更新，仅编辑组名在此维护）
TEAM_LABELS = {
    "zh-hans": "编写小组",
    "zh-hant": "編寫小組",
    "en-us": "Editorial Team",
    "fr": "Équipe éditoriale",
    "es": "Equipo editorial",
    "ko": "편집팀",
    "pt-br": "Equipe editorial",
}
for _lk in LANGUAGES:
    LANGUAGES[_lk]["footer"] = f"{latest_edition(_lk)} &middot; {TEAM_LABELS[_lk]}"


# 面向未来的"语言数量"短语：随 LANGUAGES 语言数自动取词，历史发版记录不改
LANG_COUNT_PHRASES = {
    "zh-hans": {6: "六种语言", 7: "七种语言", 8: "八种语言"},
    "zh-hant": {6: "六種語言", 7: "七種語言", 8: "八種語言"},
    "en-us": {6: "six languages", 7: "seven languages", 8: "eight languages"},
    "fr": {6: "six langues", 7: "sept langues", 8: "huit langues"},
    "es": {6: "seis idiomas", 7: "siete idiomas", 8: "ocho idiomas"},
    "ko": {6: "6개 언어", 7: "7개 언어", 8: "8개 언어"},
    "pt-br": {6: "seis idiomas", 7: "sete idiomas", 8: "oito idiomas"},
}


def lang_count_phrase(lang_key):
    """当前语言总数对应的短语（如 七种语言 / seven languages）。"""
    total = len(LANGUAGES)
    return LANG_COUNT_PHRASES[lang_key].get(total, str(total))


# 站点基础地址（release 通道）；dev 通道页面加 noindex 不参与收录
SITE_BASE_URL = "https://ftc32477.github.io/docs"

_CHANNEL = None


def set_channel(value):
    """显式指定构建通道（dev / release），优先于环境变量与 git 分支。"""
    global _CHANNEL
    _CHANNEL = value


def _on_dev_branch():
    """当前构建是否为 dev 通道。

    优先级：--channel 参数 > GITHUB_REF_NAME（CI 检出为 detached HEAD，
    git 分支名不可用）> 本地 git 分支。dev 构建时历史页显示 preview 版本，
    且所有页面注入 noindex。
    """
    if _CHANNEL in ("dev", "release"):
        return _CHANNEL == "dev"
    ref = os.environ.get("GITHUB_REF_NAME", "").strip()
    if ref:
        return ref == "dev"
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            stderr=subprocess.DEVNULL, cwd=BASE_DIR,
        )
        return out.decode("utf-8", "ignore").strip() == "dev"
    except Exception:
        return False


def _release_month_label():
    """门户页脚用：最新版本的发布年月（如 2026年10月）。"""
    m = re.match(r"(\d{4})-(\d{2})", VERSIONS[0].get("date", ""))
    return f"{m.group(1)}年{int(m.group(2))}月" if m else ""


_BARE_AMP_RE = re.compile(
    r"&(?![a-zA-Z][a-zA-Z0-9]{1,31};|#\d+;|#x[0-9a-fA-F]+;)"
)


def escape_bare_amp(html):
    """转义非实体的裸 &（保留 &amp; / &#...; 等既有实体）。"""
    return _BARE_AMP_RE.sub("&amp;", html)


def seo_links(lang_key=None, page_key=None):
    """canonical 与 hreflang 链接；dev 通道改为 noindex 不收录。"""
    if _on_dev_branch():
        return '<meta name="robots" content="noindex,nofollow">'
    if lang_key is None:
        url = f"{SITE_BASE_URL}/index.html"
        links = [
            f'<link rel="alternate" hreflang="{lk}" href="{SITE_BASE_URL}/{lk}/index.html">'
            for lk in LANGUAGES
        ]
    else:
        page = f"{page_key}.html" if page_key else "index.html"
        url = f"{SITE_BASE_URL}/{lang_key}/{page}"
        links = [
            f'<link rel="alternate" hreflang="{lk}" href="{SITE_BASE_URL}/{lk}/{page}">'
            for lk in LANGUAGES
        ]
        links.append(
            f'<link rel="alternate" hreflang="x-default" href="{SITE_BASE_URL}/en-us/{page}">'
        )
    return f'<link rel="canonical" href="{url}">\n' + "\n".join(links)


def favicon_links(prefix="../images/basic/"):
    """补充 32px 与 apple-touch-icon PNG 变体。"""
    return (
        f'<link rel="icon" type="image/png" sizes="32x32" '
        f'href="{prefix}icon_team_logo_32.png">\n'
        f'<link rel="apple-touch-icon" sizes="180x180" '
        f'href="{prefix}apple-touch-icon.png">'
    )


def dev_badge(lang_key=None):
    """dev 通道的可见预览标识（仅 dev 构建输出；打印时隐藏）。"""
    if not _on_dev_branch():
        return ""
    if lang_key:
        label = LANGUAGES[lang_key].get("dev_badge_label", "开发预览版")
    else:
        label = LANGUAGES["zh-hans"]["dev_badge_label"]
    return f'<div class="dev-badge" role="note">{label}</div>'



def visible_versions():
    """历史页展示的版本：正式构建只显示已发布版本，dev 构建额外显示 preview。"""
    if _on_dev_branch():
        return VERSIONS
    return [v for v in VERSIONS if v.get("status") != "preview"]


# ============================================================
#  MARKDOWN → HTML 转换器
# ============================================================

def parse_markdown(text):
    """
    将 Markdown 文本转换为 HTML。

    返回 (html, headings)，其中 headings 为 h2/h3 标题列表，
    每项为 {"level": int, "id": str, "text": str}，供侧边栏二级目录使用。
    """
    lines = text.split("\n")
    out = []
    headings = []
    used_ids = {}
    i = 0

    def flush_paragraph(buf):
        if buf:
            content = "\n".join(buf)
            out.append(f"<p>{inline_parse(content)}</p>")
            buf.clear()

    para_buf = []
    pending_ol_start = 0  # 被引用块打断的有序列表的下一项编号（跨块续号）

    while i < len(lines):
        line = lines[i]

        # 代码块
        if line.strip().startswith("```"):
            flush_paragraph(para_buf)
            pending_ol_start = 0
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            code_html = escape_html("\n".join(code_lines))
            out.append(f"<pre><code>{code_html}</code></pre>")
            continue

        # 图片 ![](url)（连续多张自动合并为横向排布）
        img_match = re.match(r"^!\[(.*?)\]\((.*?)\)\s*$", line.strip())
        if img_match:
            flush_paragraph(para_buf)
            pending_ol_start = 0
            imgs = []
            while i < len(lines):
                m = re.match(r"^!\[(.*?)\]\((.*?)\)\s*$", lines[i].strip())
                if not m:
                    break
                alt = m.group(1)
                src = m.group(2)
                caption = f'<figcaption>{escape_html(alt)}</figcaption>' if alt else ""
                imgs.append(
                    f'<figure class="img-fig">'
                    f'<img src="{src}" alt="{escape_html(alt)}" loading="lazy">{caption}</figure>'
                )
                i += 1
            if len(imgs) > 1:
                out.append('<div class="img-row">' + "".join(imgs) + "</div>")
            else:
                out.append('<div class="img-row img-row-single">' + "".join(imgs) + "</div>")
            continue

        # 表格
        if "|" in line and line.strip().startswith("|"):
            flush_paragraph(para_buf)
            pending_ol_start = 0
            table_lines = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1

            if len(table_lines) >= 2:
                out.append(render_table(table_lines))
            else:
                for tl in table_lines:
                    out.append(f"<p>{inline_parse(tl.strip())}</p>")
            continue

        # 水平线
        if re.match(r"^[-*_]{3,}\s*$", line.strip()):
            flush_paragraph(para_buf)
            pending_ol_start = 0
            out.append("<hr>")
            i += 1
            continue

        # 标题
        heading_match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading_match:
            flush_paragraph(para_buf)
            pending_ol_start = 0
            level = len(heading_match.group(1))
            content = heading_match.group(2).strip()
            content = re.sub(r"\s+#+\s*$", "", content)
            if level in (2, 3):
                plain = plain_text(content)
                hid = slugify(plain)
                if hid in used_ids:
                    used_ids[hid] += 1
                    hid = f"{hid}-{used_ids[hid]}"
                else:
                    used_ids[hid] = 0
                headings.append({"level": level, "id": hid, "text": plain})
                out.append(f'<h{level} id="{hid}">{inline_parse(content)}</h{level}>')
            else:
                out.append(f"<h{level}>{inline_parse(content)}</h{level}>")
            i += 1
            continue

        # 无序列表
        ul_match = re.match(r"^(\s*)[-*+]\s+(.+)$", line)
        if ul_match:
            flush_paragraph(para_buf)
            pending_ol_start = 0
            list_html, i, _ = parse_list(lines, i, len(ul_match.group(1)), ordered=False)
            out.append(list_html)
            continue

        # 有序列表（引用块打断后可通过 start 属性续号）
        ol_match = re.match(r"^(\s*)\d+\.\s+(.+)$", line)
        if ol_match:
            flush_paragraph(para_buf)
            list_html, i, item_count = parse_list(
                lines, i, len(ol_match.group(1)), ordered=True
            )
            if pending_ol_start:
                list_html = list_html.replace(
                    "<ol>", f'<ol start="{pending_ol_start}">', 1
                )
            pending_ol_start = item_count + 1
            out.append(list_html)
            continue

        # 引用（支持第一行 [!info] / [!warning] / [!danger] 类型标记）
        blockquote_match = re.match(r"^>\s?(.*)$", line)
        if blockquote_match:
            flush_paragraph(para_buf)
            bq_lines = []
            bq_class = None
            while i < len(lines):
                m = re.match(r"^>\s?(.*)$", lines[i])
                if not m:
                    break
                if bq_class is None:
                    tm = re.match(r"^\[!(info|warning|danger)\]\s?(.*)$", m.group(1))
                    if tm:
                        bq_class = tm.group(1)
                        if tm.group(2):
                            bq_lines.append(tm.group(2))
                    else:
                        bq_lines.append(m.group(1))
                else:
                    bq_lines.append(m.group(1))
                i += 1
            bq_content = inline_parse(" ".join(bq_lines))
            cls = f' class="bq-{bq_class}"' if bq_class else ""
            out.append(f"<blockquote{cls}>{bq_content}</blockquote>")
            continue

        # 右对齐行（--> 前缀，如落款）
        right_match = re.match(r"^-->\s?(.+)$", line)
        if right_match:
            flush_paragraph(para_buf)
            pending_ol_start = 0
            out.append(
                f'<p class="align-right">{inline_parse(right_match.group(1).strip())}</p>'
            )
            i += 1
            continue

        # 空行 → 段落边界
        if line.strip() == "":
            flush_paragraph(para_buf)
            i += 1
            continue

        # 普通文本行
        pending_ol_start = 0
        para_buf.append(line)
        i += 1

    flush_paragraph(para_buf)
    return escape_bare_amp("\n".join(out)), headings


def plain_text(md_text):
    """去除行内 Markdown 标记，返回纯文本（用于目录显示）。"""
    text = re.sub(r"!\[(.*?)\]\((.*?)\)", r"\1", md_text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_`]", "", text)
    return text.strip()


def slugify(text):
    """生成标题锚点 ID：保留中英文数字，其余字符去除。"""
    slug = re.sub(r"[^\w\u4e00-\u9fff-]", "", text, flags=re.UNICODE)
    return slug or "section"


def parse_list(lines, i, indent, ordered):
    """
    递归解析列表（支持嵌套）。

    lines[i] 是列表的第一项，其缩进为 indent。
    返回 (html, next_index)。
    """
    tag = "ol" if ordered else "ul"
    items = []

    while i < len(lines):
        line = lines[i]
        m = re.match(r"^(\s*)(\d+\.|[+\-*])\s+(.+)$", line)
        if not m:
            break
        cur_indent = len(m.group(1))
        if cur_indent < indent or cur_indent > indent:
            break

        content = inline_parse(m.group(3).strip())
        items.append({"content": content, "sub": ""})
        i += 1

        # 检查紧邻的嵌套子列表
        while i < len(lines):
            sub = re.match(r"^(\s*)(\d+\.|[+\-*])\s+(.+)$", lines[i])
            if sub and len(sub.group(1)) > cur_indent:
                sub_html, i, _ = parse_list(
                    lines, i, len(sub.group(1)),
                    ordered=sub.group(2).rstrip(".").isdigit()
                )
                items[-1]["sub"] += sub_html
                continue
            break

    html = f"<{tag}>"
    for item in items:
        html += f"<li>{item['content']}{item['sub']}</li>"
    html += f"</{tag}>"
    return html, i, len(items)


def inline_parse(text):
    """解析行内元素。"""
    # 图片（行内）
    text = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1" loading="lazy">', text)
    # 链接
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    # 粗斜体
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    # 粗体
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # 斜体
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    # 行内代码
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def escape_html(text):
    """转义 HTML 特殊字符。"""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_table(lines):
    """渲染 Markdown 表格。"""
    def split_cells(l):
        return [c.strip() for c in l.strip().strip("|").split("|")]

    header = split_cells(lines[0])
    alignments = []
    if len(lines) >= 2 and re.match(r"^[\|\s\-:]+$", lines[1]):
        align_row = split_cells(lines[1])
        for cell in align_row:
            if cell.startswith(":") and cell.endswith(":"):
                alignments.append("center")
            elif cell.endswith(":"):
                alignments.append("right")
            else:
                alignments.append("left")
        body_start = 2
    else:
        body_start = 1
        alignments = ["left"] * len(header)

    thead = "<thead><tr>" + "".join(
        f'<th style="text-align:{alignments[j] if j < len(alignments) else "left"}">{inline_parse(h)}</th>'
        for j, h in enumerate(header)
    ) + "</tr></thead>"

    tbody_rows = []
    for row_line in lines[body_start:]:
        cells = split_cells(row_line)
        tbody_rows.append(
            "<tr>" + "".join(
                f'<td style="text-align:{alignments[j] if j < len(alignments) else "left"}">{inline_parse(c)}</td>'
                for j, c in enumerate(cells)
            ) + "</tr>"
        )
    tbody = "<tbody>" + "".join(tbody_rows) + "</tbody>"

    return f'<div class="table-wrap"><table>{thead}{tbody}</table></div>'


# ============================================================
#  HTML 公共样式
# ============================================================

CSS = r"""
:root {
  --red: #d32f2f;
  --dark: #1a1a2e;
  --slate: #16213e;
  --card: #ffffff;
  --text: #2c2c2c;
  --muted: #666;
  --border: #e0e0e0;
  --radius: 10px;
  --sidebar-w: 260px;
  --topbar-h: 52px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei","Noto Sans SC",sans-serif;
  color:var(--text);background:#f8f9fa;line-height:1.8;min-height:100vh
}

/* ====== TOP BAR (mobile) ====== */
.topbar{
  display:none;position:fixed;top:0;left:0;right:0;height:var(--topbar-h);
  background:var(--dark);color:#fff;z-index:200;align-items:center;
  padding:0 12px;gap:8px
}
.topbar .brand{
  font-weight:700;font-size:14px;flex:1;min-width:0;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap
}
.topbar .brand a{
  color:#fff;text-decoration:none;cursor:pointer
}
.topbar .brand a:hover{opacity:.85}
.lang-select{
  background:rgba(255,255,255,.1);color:#fff;border:1px solid rgba(255,255,255,.25);
  border-radius:6px;font-size:13px;padding:6px 26px 6px 10px;max-width:150px;
  appearance:none;-webkit-appearance:none;cursor:pointer;
  background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23aaa'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 8px center
}
.lang-select option{color:#2c2c2c;background:#fff}
.topbar .menu-btn{
  background:none;border:none;color:#fff;font-size:24px;cursor:pointer;
  width:40px;height:40px;flex-shrink:0;display:flex;align-items:center;
  justify-content:center;border-radius:6px;line-height:1
}
.topbar .menu-btn:hover{background:rgba(255,255,255,.1)}

/* ====== SIDEBAR ====== */
nav.sidebar{
  position:fixed;top:0;left:0;bottom:0;width:var(--sidebar-w);
  background:var(--dark);color:#ccc;overflow-y:auto;z-index:100;
  display:flex;flex-direction:column;transition:transform .28s ease;
}
nav.sidebar::-webkit-scrollbar{width:4px}
nav.sidebar::-webkit-scrollbar-thumb{background:#444;border-radius:2px}
.sidebar-header{padding:24px 20px 14px;border-bottom:1px solid rgba(255,255,255,.08);text-align:center}
.sidebar-header .home-link{
  display:block;text-decoration:none;border-radius:8px;
  padding:4px 0;transition:background .18s
}
.sidebar-header .home-link:hover{background:rgba(255,255,255,.06)}
.sidebar-header .home-link:hover .sub{color:#fff}
.sidebar-header .logo{font-size:22px;font-weight:700;color:#fff;line-height:1.3}
.sidebar-header .sub{font-size:12px;color:#f44336;margin-top:4px;letter-spacing:1px}
/* 语言切换：侧边栏下拉选项栏（节省空间给目录） */
.lang-select-sidebar{
  margin:12px 14px 0;width:calc(100% - 28px);box-sizing:border-box;
  background:rgba(255,255,255,.1);color:#fff;
  border:1px solid rgba(255,255,255,.25);border-radius:8px;
  font-size:13px;padding:7px 26px 7px 10px;
  appearance:none;-webkit-appearance:none;cursor:pointer;
  background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23aaa'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 8px center
}
.lang-select-sidebar option{color:#2c2c2c;background:#fff}
.sidebar-nav{flex:1;padding:12px 0}
.sidebar-nav a{
  display:block;padding:10px 22px;color:#aaa;text-decoration:none;
  font-size:14px;border-left:3px solid transparent;transition:all .18s
}
.sidebar-nav a:hover{color:#fff;background:rgba(255,255,255,.04)}
.sidebar-nav a.active{color:#fff;background:rgba(244,67,54,.15);border-left-color:#f44336}
/* 二级目录：仅当前页面显示 */
.sidebar-nav a.sub-link{
  padding:5px 22px 5px 34px;font-size:12.5px;color:#8a8a8a;border-left-color:transparent
}
.sidebar-nav a.sub-link:hover{color:#fff}
.sidebar-nav a.sub-link.sub-3{padding-left:46px;font-size:12px;color:#777}
/* 侧边栏队徽 */
.side-logo{
  display:block;width:64px;height:64px;margin:0 auto 10px;
  border-radius:14px;object-fit:cover
}
/* 顶栏队徽（移动端） */
.topbar-logo{width:22px;height:22px;border-radius:5px;flex-shrink:0}
.sidebar-footer{padding:16px 20px;font-size:11px;color:#555;border-top:1px solid rgba(255,255,255,.08);text-align:center}

/* ====== OVERLAY (mobile) ====== */
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:99}

/* ====== MAIN CONTENT ====== */
/*
 * 响应式宽度策略：
 *   宽屏：内容固定 900px 宽（含 padding），居中于侧边栏右侧
 *   中屏：随宽度缩小，左右留白逐渐收窄直至消失
 *   窄屏（<768px）：侧边栏折叠，内容全宽
 *
 * 兼容性说明：部分 Chrome 版本对嵌套在自定义属性中的
 * min()/max()/clamp()（含 vw 单位）存在布局计算 bug（宽度会算成 0，
 * 正文空白而侧边栏正常）。因此此处只用普通 calc + max-width 封顶，
 * 并为 min()/max()/clamp() 提供级联回退声明。
 */
main{
  box-sizing:content-box;
  --pad: 40px;                                        /* 回退：clamp 不支持时 */
  --pad: clamp(12px, 4vw, 48px);
  padding: 40px var(--pad);
  /* 宽度：随视口收缩，上限 900px（含 padding，即内容宽 900-2*pad） */
  width: calc(100vw - var(--sidebar-w) - 2 * var(--pad));
  max-width: calc(900px - 2 * var(--pad));
  /* 左外边距：回退为紧贴侧边栏，支持 max() 时在宽屏居中 */
  margin-left: var(--sidebar-w);
  margin-left: calc(var(--sidebar-w) + max(0px, (100vw - var(--sidebar-w) - 900px) / 2));
  margin-right: auto;
}

/* Hero */
.hero{
  background:linear-gradient(135deg,var(--dark) 0%,var(--slate) 100%);color:#fff;
  border-radius:var(--radius);padding:44px 40px;margin-bottom:36px;
  position:relative;overflow:hidden
}
.hero::after{
  content:'';position:absolute;right:-40px;bottom:-40px;
  width:200px;height:200px;background:var(--red);opacity:.18;border-radius:50%
}
.hero h1{font-size:28px;font-weight:700;position:relative;z-index:1}
.hero .subtitle{font-size:14px;margin-top:10px;opacity:.8;position:relative;z-index:1}
.hero .badge{
  display:inline-block;background:var(--red);padding:4px 14px;
  border-radius:20px;font-size:12px;font-weight:600;margin-bottom:12px;
  position:relative;z-index:1
}

/* Sections */
section{margin-bottom:40px}
section h2{font-size:22px;font-weight:700;padding-bottom:10px;margin-bottom:20px;border-bottom:2px solid var(--red);color:var(--dark)}
section h3{font-size:17px;font-weight:600;margin:28px 0 10px;color:var(--slate)}
section h4,.card h4{font-size:15px;font-weight:600;margin:18px 0 8px}
.card{background:var(--card);border-radius:var(--radius);padding:24px 28px;box-shadow:0 1px 4px rgba(0,0,0,.04);margin-bottom:16px}
p{margin-bottom:10px}
a{color:#1565c0;text-decoration:none;overflow-wrap:anywhere}
a:hover{text-decoration:underline}
ul,ol{padding-left:22px;margin-bottom:12px}
li{margin-bottom:4px}
code{background:#f0f0f0;padding:2px 6px;border-radius:4px;font-size:13px;font-family:"SF Mono","Fira Code",monospace}
pre{background:#1a1a2e;color:#e0e0e0;padding:16px 20px;border-radius:var(--radius);overflow-x:auto;margin-bottom:14px;font-size:13px;line-height:1.6}
pre code{background:none;padding:0;color:inherit}
blockquote{
  border-left:4px solid var(--red);background:#fef5f5;padding:12px 18px;
  margin:14px 0;border-radius:0 var(--radius) var(--radius) 0;font-size:14px;color:#8b0000
}
/* 类型化引用块：[!info] 蓝 / [!warning] 黄 / [!danger] 红（仅颜色区分，无标签） */
blockquote.bq-info{border-left-color:#1565c0;background:#eaf3fb;color:#0d3c66}
blockquote.bq-warning{border-left-color:#f9a825;background:#fff8e1;color:#6d4c00}
blockquote.bq-danger{border-left-color:#d32f2f;background:#fef5f5;color:#8b0000}
hr{border:none;border-top:1px solid var(--border);margin:24px 0}
img{max-width:100%;border-radius:var(--radius);margin:12px 0}
/* 锚点跳转留白（避免被固定顶栏遮挡） */
h2,h3{scroll-margin-top:16px}

/* 图片排布：多图横向，窄屏自动纵向 */
.img-row{
  display:flex;flex-wrap:wrap;gap:14px;margin:14px 0
}
.img-row .img-fig{
  flex:1 1 40%;min-width:0;margin:0
}
.img-row .img-fig img{
  width:100%;margin:0;border-radius:var(--radius)
}
.img-row figcaption{
  text-align:center;font-size:12px;color:var(--muted);margin-top:6px
}
.img-row-single .img-fig{flex-basis:100%}
@media(max-width:600px){
  .img-row{flex-direction:column;gap:12px}
  h2,h3{scroll-margin-top:64px}
}

/* Table */
.table-wrap{overflow-x:auto;margin-bottom:14px}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{border:1px solid var(--border);padding:10px 14px;text-align:left}
th{background:var(--dark);color:#fff;font-weight:600}
tr:nth-child(even){background:#fafafa}

/* ====== RESPONSIVE ====== */

/* Narrow: collapse sidebar */
@media(max-width:768px){
  .topbar{display:flex}
  nav.sidebar{
    transform:translateX(-100%);
    top:var(--topbar-h);z-index:101;
    width:280px;                        /* 回退：min() 不支持时 */
    width:min(280px,84vw)
  }
  nav.sidebar.open{transform:translateX(0)}
  .overlay.show{display:block}
  main{
    margin-left:0;margin-top:var(--topbar-h);
    width: calc(100vw - 2 * var(--pad));
    max-width: none;
  }
  .hero{padding:28px 20px}
  .hero h1{font-size:22px}
  .card{padding:16px 18px}
  section h2{font-size:19px}
  section h3{font-size:16px}
  .table-wrap{margin-left:-18px;margin-right:-18px;width:calc(100% + 36px)}
}

/* Very narrow screens */
@media(max-width:420px){
  .topbar .brand{font-size:13px}
  .lang-select{max-width:132px;font-size:12px;padding:5px 22px 5px 8px}
  main{--pad: 12px}
  .card{padding:14px 14px}
  .hero{padding:22px 16px}
  .hero h1{font-size:20px}
}

/* dev 预览标识（仅 dev 通道构建时输出；打印隐藏） */
.dev-badge{
  position:fixed;right:14px;bottom:14px;z-index:400;
  background:#d32f2f;color:#fff;padding:6px 14px;border-radius:999px;
  font-size:12px;font-weight:600;box-shadow:0 2px 8px rgba(0,0,0,.25);opacity:.92
}
@media print{.dev-badge{display:none!important}}
/* ====== PRINT (PDF 导出) ====== */
/*
 * 注意：Chrome 打印视口宽度可能低于 768px，导致移动端媒体查询规则
 * 泄漏到打印渲染。因此必须在打印样式中显式覆盖所有相关属性。
 */
@media print{
  html,body{display:block !important;width:100% !important;max-width:100% !important;overflow:visible !important}
  nav.sidebar,.topbar,.overlay{display:none !important}
  body{background:#fff}
  main{
    display:block !important;box-sizing:border-box !important;
    margin:0 !important;padding:0 !important;
    width:100% !important;max-width:100% !important;
  }
  .card{box-shadow:none;border:1px solid var(--border);padding:24px 28px}
  .hero{background:#fff;color:var(--text);border:1px solid var(--border);padding:32px 28px}
  .hero h1{color:var(--dark);font-size:28px}
  section h2{font-size:22px}
  section h3{font-size:17px}
  .hero .badge{background:var(--red);color:#fff}
  a{color:inherit;overflow-wrap:anywhere !important}
  /* 表格打印适配：覆盖移动端负边距泄漏，强制约束在页面宽度内 */
  .table-wrap{
    overflow:visible !important;
    margin:0 !important;
    width:100% !important;
    max-width:100% !important;
  }
  table{
    width:100% !important;max-width:100% !important;
    table-layout:fixed;font-size:12px
  }
  th,td{padding:6px 8px;word-break:normal;overflow-wrap:break-word}
  tr{page-break-inside:avoid}
  .img-row{flex-wrap:nowrap}
  .img-fig{page-break-inside:avoid}
  .img-row .img-fig{flex:1 1 0}
  /* 中文版段落首行缩进 2 字符（英文版按英文规范不缩进） */
  html[lang="zh-hans"] main p,html[lang="zh-hant"] main p{text-indent:2em}
  .align-right{text-align:right}
  /* 标题间距：一级标题前空约两行，二级标题前空约一行 */
  h1{margin:3.2em 0 1em}
  h2{margin:2em 0 .8em}
  h3{margin:1.2em 0 .5em}
}
"""


# ============================================================
#  页面生成
# ============================================================

def render_page(page_key, html_body, lang_key, headings=None):
    """将 HTML 正文包装进完整页面模板。"""
    lang = LANGUAGES[lang_key]
    headings = headings or []
    desc = LANG_HOME_TEXTS[lang_key].get("meta_desc", lang["site_title"])
    first_para = re.search(r"<p>(.*?)</p>", html_body, re.S)
    if first_para:
        plain = re.sub(r"<[^>]+>", "", first_para.group(1)).strip()
        if plain:
            desc = plain[:120]

    # 侧边栏导航（主页 + 当前语言的页面标题 + 当前页的二级目录）
    nav_items = [f'<a href="index.html">{lang["pages"]["index"]}</a>']
    for key in PAGE_KEYS:
        cls = ' class="active"' if key == page_key else ""
        title = lang["pages"][key]
        nav_items.append(f'<a href="{key}.html"{cls}>{title}</a>')
        if key == page_key:
            for h in headings:
                sub_cls = "sub-link" + (" sub-3" if h["level"] == 3 else "")
                nav_items.append(
                    f'<a class="{sub_cls}" href="#{h["id"]}">{escape_html(h["text"])}</a>'
                )
    nav_html = "\n".join(nav_items)

    # 语言切换：侧边栏下拉选项栏（节省空间给目录）
    sidebar_options = []
    for lk, lc in LANGUAGES.items():
        sel = " selected" if lk == lang_key else ""
        sidebar_options.append(
            f'<option value="../{lk}/{page_key}.html"{sel}>{lc["label"]}</option>'
        )
    sidebar_select_html = "".join(sidebar_options)

    # 语言切换：移动端顶栏下拉选项栏
    select_options = []
    for lk, lc in LANGUAGES.items():
        sel = " selected" if lk == lang_key else ""
        select_options.append(
            f'<option value="../{lk}/{page_key}.html"{sel}>{lc["label"]}</option>'
        )
    select_html = "".join(select_options)

    page_title = lang["pages"][page_key]
    site_title = lang["site_title"]

    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}\uff5c{site_title}</title>
{meta_tags(page_title + "｜" + site_title, desc)}
{seo_links(lang_key, page_key)}
<link rel="icon" href="../images/basic/icon_team_logo.ico" type="image/x-icon">
<link rel="shortcut icon" href="../images/basic/icon_team_logo.ico" type="image/x-icon">
{favicon_links()}
<style>{CSS}</style>
</head>
<body>

<div class="topbar">
  <img class="topbar-logo" src="../images/basic/team_logo_small.png" alt="32477 Origin">
  <span class="brand"><a href="../index.html" title="{lang['back_home_label']}">{site_title}</a></span>
  <select class="lang-select" id="langSelect" aria-label="{lang['lang_label']}">
{select_html}
  </select>
  <button class="menu-btn" id="menuBtn" aria-label="{lang['menu_label']}" aria-controls="sidebar" aria-expanded="false">\u2630</button>
</div>
<div class="overlay" id="overlay"></div>

<nav class="sidebar" id="sidebar">
  <div class="sidebar-header">
    <a class="home-link" href="../index.html" title="{lang['back_home_label']}">
      <img class="side-logo" src="../images/basic/team_logo_small.png" alt="32477 Origin Team Logo">
      <div class="logo">FTC 32477<br>Origin</div>
      <div class="sub">{lang["brand"]}</div>
    </a>
    <select class="lang-select-sidebar" id="langSelectSide" aria-label="{lang['lang_label']}">
{sidebar_select_html}
    </select>
  </div>
  <div class="sidebar-nav">
{nav_html}
  </div>
  <div class="sidebar-footer">{lang["footer"]}</div>
</nav>

<main>
{html_body}
</main>

<script>
(function(){{
  var sb=document.getElementById("sidebar");
  var ol=document.getElementById("overlay");
  var btn=document.getElementById("menuBtn");
  function open(){{sb.classList.add("open");ol.classList.add("show");btn.setAttribute("aria-expanded","true")}}
  function close(){{sb.classList.remove("open");ol.classList.remove("show");btn.setAttribute("aria-expanded","false")}}
  btn.addEventListener("click",function(){{sb.classList.contains("open")?close():open()}});
  ol.addEventListener("click",close);
  var ls=document.getElementById("langSelect");
  if(ls){{ls.addEventListener("change",function(){{window.location.href=ls.value}})}};
  var lss=document.getElementById("langSelectSide");
  if(lss){{lss.addEventListener("change",function(){{window.location.href=lss.value}})}};
}})();
</script>
{dev_badge(lang_key)}
</body>
</html>"""


# ============================================================
#  主页（语言选择落地页）
# ============================================================

PORTAL_CSS = r"""
:root {
  --red: #d32f2f;
  --dark: #1a1a2e;
  --slate: #16213e;
  --card: #ffffff;
  --text: #2c2c2c;
  --muted: #666;
  --border: #e0e0e0;
  --radius: 12px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei","Noto Sans SC",sans-serif;
  color:var(--text);background:#f8f9fa;line-height:1.8;min-height:100vh
}

/* Hero */
.hero{
  background:linear-gradient(135deg,var(--dark) 0%,var(--slate) 100%);
  color:#fff;text-align:center;padding:72px 32px 64px;position:relative;overflow:hidden
}
.hero::before{
  content:'';position:absolute;left:-80px;top:-80px;width:260px;height:260px;
  background:var(--red);opacity:.12;border-radius:50%
}
.hero::after{
  content:'';position:absolute;right:-60px;bottom:-60px;width:220px;height:220px;
  background:var(--red);opacity:.15;border-radius:50%
}
.hero .badge{
  display:inline-block;background:var(--red);padding:5px 16px;border-radius:20px;
  font-size:12px;font-weight:600;letter-spacing:1px;margin-bottom:16px;
  position:relative;z-index:1
}
.hero .hero-logo{
  width:96px;height:96px;border-radius:20px;margin:0 auto 18px;
  display:block;position:relative;z-index:1;box-shadow:0 4px 16px rgba(0,0,0,.25)
}
.hero h1{font-size:34px;font-weight:700;position:relative;z-index:1;line-height:1.35}
.hero .subtitle{font-size:15px;margin-top:12px;opacity:.85;position:relative;z-index:1}

/* Container */
.container{max-width:860px;margin:0 auto;padding:40px 20px 64px}
section{margin-bottom:44px}
section>h2{
  font-size:21px;font-weight:700;margin-bottom:18px;color:var(--dark);
  padding-bottom:10px;border-bottom:2px solid var(--red)
}
/* 中英文内容同字号同深度，以示平等 */
section>h2 .en{font-size:inherit;color:inherit;font-weight:inherit;margin-left:10px}

/* Language cards */
.lang-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
.lang-card{
  background:var(--card);border-radius:var(--radius);padding:28px 24px;
  box-shadow:0 2px 8px rgba(0,0,0,.05);display:flex;flex-direction:column;
  transition:transform .18s,box-shadow .18s;border-top:3px solid transparent;
  text-decoration:none;color:inherit
}
.lang-card:hover{transform:translateY(-3px);box-shadow:0 8px 20px rgba(0,0,0,.09)}
.lang-card.zh-hans{border-top-color:#a61615}
.lang-card.zh-hant{border-top-color:#a61615}
.lang-card.en-us{border-top-color:#d85d23}
.lang-card.fr{border-top-color:#d85d23}
.lang-card.es{border-top-color:#ffb953}
/* dev 预览标识（仅 dev 通道构建时输出；打印隐藏） */
.dev-badge{
  position:fixed;right:14px;bottom:14px;z-index:400;
  background:#d32f2f;color:#fff;padding:6px 14px;border-radius:999px;
  font-size:12px;font-weight:600;box-shadow:0 2px 8px rgba(0,0,0,.25);opacity:.92
}
@media print{.dev-badge{display:none!important}}
.lang-card.ko{border-top-color:#ffb953}
.lang-card.pt-br{border-top-color:#1b7f4b}
.lang-card h3{font-size:18px;font-weight:700;margin-bottom:4px}
.lang-card .lang-name{font-size:13px;color:var(--muted);margin-bottom:12px}

/* Footer */
footer{
  text-align:center;padding:32px 20px;color:var(--muted);font-size:12px;
  border-top:1px solid var(--border)
}
/* 底部法律声明：中英文同字号同深度，以示平等 */
footer .legal{margin-top:20px;font-size:11px;color:#666;line-height:1.8;padding:0 12px}
footer .legal p{margin:0 0 8px}
footer .legal p:last-child{margin-bottom:0}

@media(max-width:600px){
  .hero{padding:48px 20px 44px}
  .hero h1{font-size:24px}
  .hero .subtitle{font-size:14px}
  .container{padding:28px 16px 48px}
  section>h2{font-size:19px}
  .lang-grid{grid-template-columns:1fr}
}

/* Very narrow screens */
@media(max-width:380px){
  .hero{padding:40px 14px 36px}
  .hero h1{font-size:21px}
  .hero .badge{font-size:11px}
  .container{padding:22px 12px 40px}
  .lang-card{padding:20px 16px}
}
"""


def render_portal():
    """生成根门户页（语言选择，仿 wikipedia.org 风格）。"""
    portal_desc = ("FTC 32477 Origin \u5feb\u901f\u5165\u95e8\u6307\u5357\u591a\u8bed\u8a00\u95e8\u6237\uff1a\u7b80\u4f53\u4e2d\u6587 / \u7e41\u9ad4\u4e2d\u6587 / English (US) / Fran\u00e7ais / Espa\u00f1ol / \ud55c\uad6d\uc5b4 / Portugu\u00eas (BR)\u3002Multilingual portal of the FTC 32477 Origin Quick Start Guide.")
    portal_langs = [
        ("zh-hans", "\u7b80\u4f53\u4e2d\u6587", "Simplified Chinese"),
        ("zh-hant", "\u7e41\u9ad4\u4e2d\u6587", "Traditional Chinese"),
        ("en-us", "English (US)", "English \u00b7 United States"),
        ("fr", "Fran\u00e7ais", "French \u00b7 France"),
        ("es", "Espa\u00f1ol", "Spanish \u00b7 Spain"),
        ("ko", "\ud55c\uad6d\uc5b4", "Korean \u00b7 Korea"),
        ("pt-br", "Portugu\u00eas (BR)", "Portuguese \u00b7 Brazil"),
    ]
    cards_html = "\n".join(
        f'<a class="lang-card {lk}" href="{lk}/index.html">'
        f'<h3>{native}</h3><div class="lang-name">{sub}</div></a>'
        for lk, native, sub in portal_langs
    )

    portal_date = _release_month_label()
    return f"""<!DOCTYPE html>
<html lang="zh-hans">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FTC 32477 Origin \u5feb\u901f\u5165\u95e8\u6307\u5357 | Quick Start Guide</title>
{meta_tags("FTC 32477 Origin \u5feb\u901f\u5165\u95e8\u6307\u5357 | Quick Start Guide", portal_desc)}
{seo_links()}
<link rel="icon" href="images/basic/icon_team_logo.ico" type="image/x-icon">
<link rel="shortcut icon" href="images/basic/icon_team_logo.ico" type="image/x-icon">
{favicon_links(prefix="images/basic/")}
<style>{PORTAL_CSS}</style>
</head>
<body>

<div class="hero">
  <img class="hero-logo" src="images/basic/team_logo_small.png" alt="32477 Origin Team Logo">
  <div class="badge">TEAM 32477 ORIGIN</div>
  <h1>FIRST\u00ae Tech Challenge<br>\u5feb\u901f\u5165\u95e8\u6307\u5357</h1>
  <div class="subtitle">Quick Start Guide \u00b7 \u62d2\u7edd\u91cd\u590d\u9020\u8f6e\u5b50 \u00b7 Refuse to Reinvent the Wheel</div>
</div>

<div class="container">
  <section id="languages">
    <h2>\u9009\u62e9\u8bed\u8a00 <span class="en">Choose Your Language</span></h2>
    <div class="lang-grid">
{cards_html}
    </div>
  </section>
</div>

<footer>
  32477 Origin 快速入门指南编写小组 · Editorial Team · {portal_date}
  <div class="legal">
    <p>Legal Notice: This guide is an independent product of FTC Team 32477 Origin. Our team is not affiliated with, endorsed by, or sponsored by FIRST\u00ae (For Inspiration and Recognition of Science and Technology). FIRST\u00ae, FIRST\u00ae Robotics Competition, FRC\u00ae, FIRST\u00ae Tech Challenge, and FTC\u00ae are registered trademarks of FIRST. The designs, code, and resources shared in this guide are primarily provided by our team members and may also incorporate open-source materials and contributions from others; they do not represent official FIRST materials.</p>
    <p>\u6cd5\u5f8b\u58f0\u660e\uff1a\u672c\u6307\u5357\u662f FTC 32477 Origin \u961f\u4f0d\u7684\u72ec\u7acb\u4ea7\u54c1\u3002\u672c\u961f\u4f0d\u4e0e FIRST\u00ae\uff08For Inspiration and Recognition of Science and Technology\uff09\u65e0\u96b6\u5c5e\u3001\u80cc\u4e66\u6216\u8d5e\u52a9\u5173\u7cfb\u3002FIRST\u00ae\u3001FIRST\u00ae Robotics Competition\u3001FRC\u00ae\u3001FIRST\u00ae Tech Challenge \u53ca FTC\u00ae \u5747\u4e3a FIRST \u7684\u6ce8\u518c\u5546\u6807\u3002\u672c\u6307\u5357\u4e2d\u5206\u4eab\u7684\u8bbe\u8ba1\u3001\u4ee3\u7801\u4e0e\u8d44\u6e90\u4ee5\u961f\u4f0d\u6210\u5458\u63d0\u4f9b\u7684\u5185\u5bb9\u4e3a\u4e3b\uff0c\u4ea6\u53ef\u80fd\u5305\u542b\u7ecf\u6574\u7406\u5408\u5e76\u7684\u5f00\u6e90\u6750\u6599\u4e0e\u5176\u4ed6\u8d21\u732e\u8005\u7684\u6210\u679c\uff0c\u4e0d\u4ee3\u8868 FIRST \u5b98\u65b9\u6750\u6599\u3002</p>
  </div>
</footer>

{dev_badge()}
</body>
</html>"""


# 各语言主页文案
LANG_HOME_TEXTS = {
    "zh-hans": {
        "hero_title": "FIRST\u00ae Tech Challenge<br>32477 Origin<br>\u5feb\u901f\u5165\u95e8\u6307\u5357",
        "slogan": "\u62d2\u7edd\u91cd\u590d\u9020\u8f6e\u5b50",
        "meta_desc": f"FTC 32477 Origin \u5feb\u901f\u5165\u95e8\u6307\u5357\u2014\u2014\u62d2\u7edd\u91cd\u590d\u9020\u8f6e\u5b50\u3002\u9762\u5411\u65b0\u8001\u961f\u5458\u7684\u4e03\u7ae0\u5b8c\u6574\u6307\u5357\uff1a\u961f\u5458\u987b\u77e5\u3001\u5efa\u6a21\u8bbe\u8ba1\u3001\u7ed3\u6784\u5efa\u9020\u3001\u7a0b\u5e8f\u8bbe\u8ba1\u3001\u5916\u90e8\u8054\u7edc\u4e0e\u540e\u8bb0\uff0c\u63d0\u4f9b{lang_count_phrase('zh-hans')}\u7248\u672c\u4e0e\u53ef\u6253\u5370 PDF\u3002",
        "about_title": "\u9879\u76ee\u6982\u51b5",
        "about": [
            ("\u961f\u4f0d", "FTC Team 32477 Origin"),
            ("\u5b66\u6821", "\u4e2d\u56fd\u5317\u4eac\u5e02\u6d77\u6dc0\u533a \u00b7 \u5317\u4eac\u5341\u4e00\u5b9e\u9a8c\u4e2d\u5b66"),
            ("\u5730\u5740", "\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u592a\u5e73\u8def8\u53f7 \u00b7 \u90ae\u653f\u7f16\u7801 100039"),
            ("\u6700\u65b0\u7248\u672c", latest_edition("zh-hans")),
        ],
        "download_title": "\u4e0b\u8f7d",
        "download_desc": "\u4e0b\u8f7d\u7684\u662f\u79bb\u7ebf\u7248\u672c\uff1a\u65e0\u9700\u8054\u7f51\u5373\u53ef\u9605\u8bfb\uff0c\u4e5f\u53ef\u81ea\u884c\u6253\u5370\u6216\u5206\u4eab\u5b58\u6863\u3002",
        "download_btn": "\u2193 \u4e0b\u8f7d PDF",
        "chapters_title": "\u5185\u5bb9\u7ed3\u6784",
        "versions_desc": f"\u67e5\u770b\u5404\u7248\u672c\u7684\u53d1\u5e03\u65f6\u95f4\u4e0e\u4e3b\u8981\u6539\u52a8\uff0c\u5e76\u4e0b\u8f7d{lang_count_phrase('zh-hans')} PDF\u3002",
        "versions_btn": "\u67e5\u770b\u5386\u53f2\u7248\u672c \u2192",
        "legal": "\u6cd5\u5f8b\u58f0\u660e\uff1a\u672c\u6307\u5357\u662f FTC 32477 Origin \u961f\u4f0d\u7684\u72ec\u7acb\u4ea7\u54c1\u3002\u672c\u961f\u4f0d\u4e0e FIRST\u00ae\uff08For Inspiration and Recognition of Science and Technology\uff09\u65e0\u96b6\u5c5e\u3001\u80cc\u4e66\u6216\u8d5e\u52a9\u5173\u7cfb\u3002FIRST\u00ae\u3001FIRST\u00ae Robotics Competition\u3001FRC\u00ae\u3001FIRST\u00ae Tech Challenge \u53ca FTC\u00ae \u5747\u4e3a FIRST \u7684\u6ce8\u518c\u5546\u6807\u3002\u672c\u6307\u5357\u4e2d\u5206\u4eab\u7684\u8bbe\u8ba1\u3001\u4ee3\u7801\u4e0e\u8d44\u6e90\u4ee5\u961f\u4f0d\u6210\u5458\u63d0\u4f9b\u7684\u5185\u5bb9\u4e3a\u4e3b\uff0c\u4ea6\u53ef\u80fd\u5305\u542b\u7ecf\u6574\u7406\u5408\u5e76\u7684\u5f00\u6e90\u6750\u6599\u4e0e\u5176\u4ed6\u8d21\u732e\u8005\u7684\u6210\u679c\uff0c\u4e0d\u4ee3\u8868 FIRST \u5b98\u65b9\u6750\u6599\u3002",
    },
    "zh-hant": {
        "hero_title": "FIRST\u00ae Tech Challenge<br>32477 Origin<br>\u5feb\u901f\u5165\u9580\u6307\u5357",
        "slogan": "\u62d2\u7d55\u91cd\u8907\u9020\u8f2a\u5b50",
        "meta_desc": f"FTC 32477 Origin \u5feb\u901f\u5165\u9580\u6307\u5357\u2014\u2014\u62d2\u7d55\u91cd\u8907\u9020\u8f2a\u5b50\u3002\u9762\u5411\u65b0\u8001\u968a\u54e1\u7684\u4e03\u7ae0\u5b8c\u6574\u6307\u5357\uff1a\u968a\u54e1\u9808\u77e5\u3001\u5efa\u6a21\u8a2d\u8a08\u3001\u7d50\u69cb\u5efa\u9020\u3001\u7a0b\u5f0f\u8a2d\u8a08\u3001\u5916\u90e8\u806f\u7d61\u8207\u5f8c\u8a18\uff0c\u63d0\u4f9b{lang_count_phrase('zh-hant')}\u7248\u672c\u8207\u53ef\u5217\u5370 PDF\u3002",
        "about_title": "\u5c08\u6848\u6982\u6cc1",
        "about": [
            ("\u968a\u4f0d", "FTC Team 32477 Origin"),
            ("\u5b78\u6821", "\u4e2d\u570b\u5317\u4eac\u5e02\u6d77\u6dc0\u5340 \u00b7 \u5317\u4eac\u5341\u4e00\u5be6\u9a57\u4e2d\u5b78"),
            ("\u5730\u5740", "\u5317\u4eac\u5e02\u6d77\u6dc0\u5340\u592a\u5e73\u8def8\u865f \u00b7 \u90f5\u905e\u5340\u865f 100039"),
            ("\u6700\u65b0\u7248\u672c", latest_edition("zh-hant")),
        ],
        "download_title": "\u4e0b\u8f09",
        "download_desc": "\u4e0b\u8f09\u7684\u662f\u96e2\u7dda\u7248\u672c\uff1a\u7121\u9700\u9023\u7dda\u5373\u53ef\u95b1\u8b80\uff0c\u4e5f\u53ef\u81ea\u884c\u5217\u5370\u6216\u5206\u4eab\u5b58\u6a94\u3002",
        "download_btn": "\u2193 \u4e0b\u8f09 PDF",
        "chapters_title": "\u5167\u5bb9\u7d50\u69cb",
        "versions_desc": f"\u67e5\u770b\u5404\u7248\u672c\u7684\u767c\u5e03\u6642\u9593\u8207\u4e3b\u8981\u6539\u52d5\uff0c\u4e26\u4e0b\u8f09{lang_count_phrase('zh-hant')} PDF\u3002",
        "versions_btn": "\u67e5\u770b\u6b77\u53f2\u7248\u672c \u2192",
        "legal": "\u6cd5\u5f8b\u8072\u660e\uff1a\u672c\u6307\u5357\u662f FTC 32477 Origin \u968a\u4f0d\u7684\u7368\u7acb\u7522\u54c1\u3002\u672c\u968a\u4f0d\u8207 FIRST\u00ae\uff08For Inspiration and Recognition of Science and Technology\uff09\u7121\u96b8\u5c6c\u3001\u80cc\u66f8\u6216\u8d0a\u52a9\u95dc\u4fc2\u3002FIRST\u00ae\u3001FIRST\u00ae Robotics Competition\u3001FRC\u00ae\u3001FIRST\u00ae Tech Challenge \u53ca FTC\u00ae \u5747\u70ba FIRST \u7684\u8a3b\u518a\u5546\u6a19\u3002\u672c\u6307\u5357\u4e2d\u5206\u4eab\u7684\u8a2d\u8a08\u3001\u7a0b\u5f0f\u78bc\u8207\u8cc7\u6e90\u4ee5\u968a\u4f0d\u6210\u54e1\u63d0\u4f9b\u7684\u5167\u5bb9\u70ba\u4e3b\uff0c\u4ea6\u53ef\u80fd\u5305\u542b\u7d93\u6574\u7406\u5408\u4f75\u7684\u958b\u6e90\u6750\u6599\u8207\u5176\u4ed6\u8ca2\u737b\u8005\u7684\u6210\u679c\uff0c\u4e0d\u4ee3\u8868 FIRST \u5b98\u65b9\u6750\u6599\u3002",
    },
    "en-us": {
        "hero_title": "FIRST\u00ae Tech Challenge<br>32477 Origin<br>Quick Start Guide",
        "slogan": "Refuse to Reinvent the Wheel",
        "meta_desc": f"The FTC 32477 Origin Quick Start Guide \u2014 Refuse to Reinvent the Wheel. A complete seven-chapter guide for new and returning team members, available in {lang_count_phrase('en-us')} with printable PDFs.",
        "about_title": "About Us",
        "about": [
            ("Team", "FTC Team 32477 Origin"),
            ("School", "Beijing National Day Experimental School, Haidian District, Beijing, China"),
            ("Address", "No. 8 Taiping Road, Haidian District, Beijing 100039, China"),
            ("Latest Version", latest_edition("en-us")),
        ],
        "download_title": "Download",
        "download_desc": "Download the offline edition: read it without an internet connection, print it, or share and archive it.",
        "download_btn": "\u2193 Download PDF",
        "chapters_title": "Table of Contents",
        "versions_desc": f"See what changed in each release and download its PDFs in {lang_count_phrase('en-us')}.",
        "versions_btn": "View Version History \u2192",
        "legal": "Legal Notice: This guide is an independent product of FTC Team 32477 Origin. Our team is not affiliated with, endorsed by, or sponsored by FIRST\u00ae (For Inspiration and Recognition of Science and Technology). FIRST\u00ae, FIRST\u00ae Robotics Competition, FRC\u00ae, FIRST\u00ae Tech Challenge, and FTC\u00ae are registered trademarks of FIRST. The designs, code, and resources shared in this guide are primarily provided by our team members and may also incorporate open-source materials and contributions from others; they do not represent official FIRST materials.",
    },
    "fr": {
        "hero_title": "FIRST\u00ae Tech Challenge<br>32477 Origin<br>Guide de d\u00e9marrage rapide",
        "slogan": "Refuser de r\u00e9inventer la roue",
        "meta_desc": f"Le Guide de d\u00e9marrage rapide FTC 32477 Origin \u2014 Refuser de r\u00e9inventer la roue. Un guide complet en sept chapitres pour les membres de l'\u00e9quipe, disponible en {lang_count_phrase('fr')} avec des PDF imprimables.",
        "about_title": "\u00c0 propos",
        "about": [
            ("\u00c9quipe", "FTC Team 32477 Origin"),
            ("\u00c9cole", "Beijing National Day Experimental School, district de Haidian, P\u00e9kin, Chine"),
            ("Adresse", "N\u00b0 8 Taiping Road, district de Haidian, P\u00e9kin 100039, Chine"),
            ("Derni\u00e8re version", latest_edition("fr")),
        ],
        "download_title": "T\u00e9l\u00e9charger",
        "download_desc": "T\u00e9l\u00e9chargez l'\u00e9dition hors ligne : lisez-la sans connexion Internet, imprimez-la ou partagez-la et archivez-la.",
        "download_btn": "\u2193 T\u00e9l\u00e9charger le PDF",
        "chapters_title": "Table des mati\u00e8res",
        "versions_desc": f"Dates de publication et principaux changements de chaque version, avec t\u00e9l\u00e9chargement des PDF en {lang_count_phrase('fr')}.",
        "versions_btn": "Voir l'historique des versions \u2192",
        "legal": "Mention l\u00e9gale : ce guide est un produit ind\u00e9pendant de la FTC Team 32477 Origin. Notre \u00e9quipe n'est ni affili\u00e9e \u00e0 FIRST\u00ae (For Inspiration and Recognition of Science and Technology), ni approuv\u00e9e ni sponsoris\u00e9e par celui-ci. FIRST\u00ae, FIRST\u00ae Robotics Competition, FRC\u00ae, FIRST\u00ae Tech Challenge et FTC\u00ae sont des marques d\u00e9pos\u00e9es de FIRST. Les designs, le code et les ressources partag\u00e9s dans ce guide sont principalement fournis par les membres de notre \u00e9quipe et peuvent \u00e9galement int\u00e9grer des mat\u00e9riaux open source et les contributions d'autres personnes ; ils ne constituent pas des documents officiels de FIRST.",
    },
    "es": {
        "hero_title": "FIRST\u00ae Tech Challenge<br>32477 Origin<br>Gu\u00eda de inicio r\u00e1pido",
        "slogan": "Negarse a reinventar la rueda",
        "meta_desc": f"La Gu\u00eda de inicio r\u00e1pido de FTC 32477 Origin \u2014 Negarse a reinventar la rueda. Una gu\u00eda completa de siete cap\u00edtulos para los miembros del equipo, disponible en {lang_count_phrase('es')} con PDF imprimibles.",
        "about_title": "Acerca de",
        "about": [
            ("Equipo", "FTC Team 32477 Origin"),
            ("Escuela", "Beijing National Day Experimental School, distrito de Haidian, Pek\u00edn, China"),
            ("Direcci\u00f3n", "N.\u00ba 8 Taiping Road, distrito de Haidian, Pek\u00edn 100039, China"),
            ("\u00daltima versi\u00f3n", latest_edition("es")),
        ],
        "download_title": "Descargar",
        "download_desc": "Descargue la edici\u00f3n sin conexi\u00f3n: l\u00e9ala sin conexi\u00f3n a Internet, impr\u00edmala o comp\u00e1rtala y arch\u00edvela.",
        "download_btn": "\u2193 Descargar PDF",
        "chapters_title": "\u00cdndice de contenidos",
        "versions_desc": f"Consulte las fechas de publicaci\u00f3n y los principales cambios de cada versi\u00f3n, y descargue los PDF en {lang_count_phrase('es')}.",
        "versions_btn": "Ver historial de versiones \u2192",
        "legal": "Aviso legal: esta gu\u00eda es un producto independiente del equipo FTC 32477 Origin. Nuestro equipo no est\u00e1 afiliado a FIRST\u00ae (For Inspiration and Recognition of Science and Technology), ni cuenta con su respaldo ni su patrocinio. FIRST\u00ae, FIRST\u00ae Robotics Competition, FRC\u00ae, FIRST\u00ae Tech Challenge y FTC\u00ae son marcas registradas de FIRST. Los dise\u00f1os, el c\u00f3digo y los recursos compartidos en esta gu\u00eda provienen principalmente de los miembros del equipo y pueden incluir tambi\u00e9n materiales de c\u00f3digo abierto y aportaciones de otras personas, debidamente organizados e integrados; no constituyen material oficial de FIRST.",
    },
    "ko": {
        "hero_title": "FIRST\u00ae Tech Challenge<br>32477 Origin<br>\ube60\ub978 \uc2dc\uc791 \uac00\uc774\ub4dc",
        "slogan": "\ubc14\ud034\ub97c \ub2e4\uc2dc \ubc1c\uba85\ud558\uc9c0 \uc54a\uae30",
        "meta_desc": f"FTC 32477 Origin \ube60\ub978 \uc2dc\uc791 \uac00\uc774\ub4dc \u2014 \ubc14\ud034\ub97c \ub2e4\uc2dc \ubc1c\uba85\ud558\uc9c0 \uc54a\uae30. \uc2e0\uc785\uacfc \ubca0\ud14c\ub791\uc744 \uc704\ud55c 7\uac1c \uc7a5\uc73c\ub85c \uad6c\uc131\ub41c \uc644\uc804\ud55c \uac00\uc774\ub4dc\ub85c, {lang_count_phrase('ko')} \ubc84\uc804\uacfc \uc778\uc1c4 \uac00\ub2a5\ud55c PDF\ub97c \uc81c\uacf5\ud569\ub2c8\ub2e4.",
        "about_title": "\ud504\ub85c\uc81d\ud2b8 \uc18c\uac1c",
        "about": [
            ("\ud300", "FTC Team 32477 Origin"),
            ("\ud559\uad50", "Beijing National Day Experimental School, \uc911\uad6d \ubca0\uc774\uc9d5\uc2dc \ud558\uc774\ub518\uad6c"),
            ("\uc8fc\uc18c", "\uc911\uad6d \ubca0\uc774\uc9d5\uc2dc \ud558\uc774\ub518\uad6c \ud0c0\uc774\ud551\ub85c 8\ubc88\uc9c0, \uc6b0\ud3b8\ubc88\ud638 100039"),
            ("\ucd5c\uc2e0 \ubc84\uc804", latest_edition("ko")),
        ],
        "download_title": "\ub2e4\uc6b4\ub85c\ub4dc",
        "download_desc": "\uc624\ud504\ub77c\uc778 \ubc84\uc804\uc744 \ub2e4\uc6b4\ub85c\ub4dc\ud558\uc138\uc694. \uc778\ud130\ub137 \uc5c6\uc774 \uc77d\uace0, \uc778\uc1c4\ud558\uac70\ub098 \uacf5\uc720\u00b7\ubcf4\uad00\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4.",
        "download_btn": "\u2193 PDF \ub2e4\uc6b4\ub85c\ub4dc",
        "chapters_title": "\ubaa9\ucc28",
        "versions_desc": f"\uac01 \ubc84\uc804\uc758 \ucd9c\uc2dc \ub0a0\uc9dc\uc640 \uc8fc\uc694 \ubcc0\uacbd \uc0ac\ud56d\uc744 \ud655\uc778\ud558\uace0 {lang_count_phrase('ko')} PDF\ub97c \ub2e4\uc6b4\ub85c\ub4dc\ud558\uc138\uc694.",
        "versions_btn": "\ubc84\uc804 \uae30\ub85d \ubcf4\uae30 \u2192",
        "legal": "\ubc95\uc801 \uace0\uc9c0: \uc774 \uac00\uc774\ub4dc\ub294 FTC 32477 Origin \ud300\uc758 \ub3c5\ub9bd \uc81c\uc791\ubb3c\uc785\ub2c8\ub2e4. \ubcf8 \ud300\uc740 FIRST\u00ae(For Inspiration and Recognition of Science and Technology)\uc640 \uc18c\uc18d, \ud6c4\uc6d0 \ub610\ub294 \uc2a4\ud3f0\uc11c \uad00\uacc4\uac00 \uc5c6\uc2b5\ub2c8\ub2e4. FIRST\u00ae, FIRST\u00ae Robotics Competition, FRC\u00ae, FIRST\u00ae Tech Challenge \ubc0f FTC\u00ae\ub294 FIRST\uc758 \ub4f1\ub85d \uc0c1\ud45c\uc785\ub2c8\ub2e4. \uc774 \uac00\uc774\ub4dc\uc5d0 \uacf5\uc720\ub41c \uc124\uacc4, \ucf54\ub4dc\uc640 \uc790\uc6d0\uc740 \ud300\uc6d0\uc774 \uc81c\uacf5\ud55c \ub0b4\uc6a9\uc744 \uc704\uc8fc\ub85c \ud558\uba70, \uc815\ub9ac\u00b7\ud1b5\ud569\ub41c \uc624\ud508\uc18c\uc2a4 \uc790\ub8cc\uc640 \ub2e4\ub978 \uae30\uc5ec\uc790\uc758 \uc131\uacfc\ub97c \ud3ec\ud568\ud560 \uc218 \uc788\uc73c\uba70, FIRST \uacf5\uc2dd \uc790\ub8cc\ub97c \ub300\ud45c\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.",
    },
    "pt-br": {
        "hero_title": "FIRST® Tech Challenge<br>32477 Origin<br>Guia de início rápido",
        "slogan": "Recusar reinventar a roda",
        "meta_desc": f"O Guia de início rápido do FTC 32477 Origin — Recuse reinventar a roda. Um guia completo em sete capítulos para novos membros e veteranos da equipe, disponível em {lang_count_phrase('pt-br')} com PDFs para impressão.",
        "about_title": "Sobre o projeto",
        "about": [
            ("Equipe", "FTC Team 32477 Origin"),
            ("Escola", "Beijing National Day Experimental School, Distrito de Haidian, Pequim, China"),
            ("Endereço", "N.º 8 Taiping Road, Distrito de Haidian, Pequim 100039, China"),
            ("Última versão", latest_edition("pt-br")),
        ],
        "download_title": "Download",
        "download_desc": "Baixe a edição offline: leia sem conexão com a internet, imprima ou compartilhe e arquive.",
        "download_btn": "↓ Baixar PDF",
        "chapters_title": "Sumário",
        "versions_desc": f"Veja as datas de publicação e as principais mudanças de cada versão e baixe os PDFs em {lang_count_phrase('pt-br')}.",
        "versions_btn": "Ver histórico de versões →",
        "legal": "Aviso legal: este guia é um produto independente da equipe FTC 32477 Origin. Nossa equipe não é afiliada, endossada ou patrocinada pela FIRST® (For Inspiration and Recognition of Science and Technology). FIRST®, FIRST® Robotics Competition, FRC®, FIRST® Tech Challenge e FTC® são marcas registradas da FIRST. Os designs, códigos e recursos compartilhados neste guia são fornecidos principalmente pelos membros da equipe e também podem incorporar materiais de código aberto e contribuições de terceiros; não representam materiais oficiais da FIRST.",
    },
}


LANG_HOME_CSS = r"""
/* ====== 语言主页 ====== */
.lh-page{max-width:760px;margin:0 auto}
.lh-hero{background:linear-gradient(135deg,var(--dark) 0%,var(--slate) 100%);color:#fff;text-align:center;padding:40px 24px 36px;border-radius:12px;margin-bottom:26px}
.lh-logo{width:72px;height:72px;border-radius:16px;display:block;margin:0 auto 12px;box-shadow:0 4px 16px rgba(0,0,0,.25)}
.lh-badge{display:inline-block;background:var(--red);padding:4px 14px;border-radius:16px;font-size:11px;font-weight:600;letter-spacing:1px;margin-bottom:12px}
.lh-hero h1{font-size:24px;line-height:1.4;font-weight:700}
.lh-slogan{font-size:13px;opacity:.85;margin-top:8px}
.lh-page section{margin-bottom:30px}
.lh-page section h2{font-size:19px;font-weight:700;margin-bottom:14px;color:#2c2c2c;padding-bottom:8px;border-bottom:2px solid var(--red)}
.lh-about{background:#fff;border:1px solid #e0e0e0;border-radius:12px;padding:6px 22px;box-shadow:0 1px 4px rgba(0,0,0,.04)}
.lh-line{display:flex;align-items:baseline;gap:14px;padding:12px 0;border-bottom:1px solid #f0f0f0;font-size:14.5px;margin:0}
.lh-line:last-child{border-bottom:none}
.lh-tag{font-size:12px;color:#666;min-width:72px;flex-shrink:0;background:#f0f0f0;padding:2px 10px;border-radius:12px;text-align:center}
.lh-text{font-weight:500}
.lh-pdf{display:inline-block;background:var(--dark);color:#fff;border-radius:8px;padding:10px 22px;font-size:14px;font-weight:600;text-decoration:none}
.lh-pdf:hover{background:var(--slate)}
.lh-download-desc{color:#666;font-size:14px;margin-bottom:12px}
.lh-note{color:#999;font-size:13px}
.lh-chapters{margin:0;padding:0;list-style:none}
.lh-chapters li{display:flex;align-items:center;gap:14px;background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:10px 16px;margin-bottom:8px;font-size:14px}
.lh-chapters .num{width:26px;height:26px;border-radius:50%;background:var(--red);color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0}
.lh-chapters a{color:#2c2c2c;text-decoration:none;font-weight:600}
.lh-chapters a:hover{color:var(--red)}
.lh-versions-desc{color:#666;font-size:14px;margin-bottom:12px}
.lh-btn{display:inline-block;background:var(--dark);color:#fff;border-radius:8px;padding:10px 22px;font-size:14px;font-weight:600;text-decoration:none}
.lh-btn:hover{background:var(--slate)}
.lh-legal{color:#666;font-size:11px;line-height:1.8;margin-top:8px}
/* dev 预览标识（仅 dev 通道构建时输出；打印隐藏） */
.dev-badge{
  position:fixed;right:14px;bottom:14px;z-index:400;
  background:#d32f2f;color:#fff;padding:6px 14px;border-radius:999px;
  font-size:12px;font-weight:600;box-shadow:0 2px 8px rgba(0,0,0,.25);opacity:.92
}
@media print{.dev-badge{display:none!important}}
@media print{.topbar,.sidebar,.overlay{display:none!important}}
"""


def render_lang_homepage(lang_key):
    """生成某语言的本地化主页（复用指南页外壳：侧边栏/顶栏/语言切换）。"""
    lang = LANGUAGES[lang_key]
    t = LANG_HOME_TEXTS[lang_key]

    nav_items = [f'<a href="index.html" class="active">{lang["pages"]["index"]}</a>']
    for key in PAGE_KEYS:
        nav_items.append(f'<a href="{key}.html">{lang["pages"][key]}</a>')
    nav_html = "\n".join(nav_items)

    select_options = "".join(
        f'<option value="../{lk}/index.html"{" selected" if lk == lang_key else ""}>'
        f'{lc["label"]}</option>'
        for lk, lc in LANGUAGES.items()
    )

    about_lines = "".join(
        f'<p class="lh-line"><span class="lh-tag">{label}</span>'
        f'<span class="lh-text">{value}</span></p>'
        for label, value in t["about"]
    )

    chapter_items = "".join(
        f'<li><span class="num">{i}</span><a href="{key}.html">{lang["pages"][key]}</a></li>'
        for i, key in enumerate(PAGE_KEYS, start=1)
    )

    released = [v for v in VERSIONS if v.get("status") != "preview"]
    if released:
        pdf_filename = released[0].get("pdfs", {}).get(lang_key)
        if pdf_filename:
            pdf_block = (
                f'<a class="lh-pdf" href="{RELEASE_BASE}/{released[0]["tag"]}/{pdf_filename}" '
                f'target="_blank" rel="noopener">{t["download_btn"]}</a>'
            )
        else:
            pdf_block = f'<p class="lh-note">{VERSIONS_TEXTS[lang_key]["pdf_note"]}</p>'
    else:
        pdf_block = f'<p class="lh-note">{VERSIONS_TEXTS[lang_key]["pdf_note"]}</p>'

    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{lang["site_title"]}</title>
{meta_tags(lang["site_title"], t["meta_desc"])}
{seo_links(lang_key)}
<link rel="icon" href="../images/basic/icon_team_logo.ico" type="image/x-icon">
<link rel="shortcut icon" href="../images/basic/icon_team_logo.ico" type="image/x-icon">
{favicon_links()}
<style>{CSS}
{LANG_HOME_CSS}</style>
</head>
<body>

<div class="topbar">
  <img class="topbar-logo" src="../images/basic/team_logo_small.png" alt="32477 Origin">
  <span class="brand"><a href="../index.html" title="{lang['back_portal_label']}">{lang["site_title"]}</a></span>
  <select class="lang-select" id="langSelect" aria-label="{lang['lang_label']}">
{select_options}
  </select>
  <button class="menu-btn" id="menuBtn" aria-label="{lang['menu_label']}" aria-controls="sidebar" aria-expanded="false">\u2630</button>
</div>
<div class="overlay" id="overlay"></div>

<nav class="sidebar" id="sidebar">
  <div class="sidebar-header">
    <a class="home-link" href="../index.html" title="{lang['back_portal_label']}">
      <img class="side-logo" src="../images/basic/team_logo_small.png" alt="32477 Origin Team Logo">
      <div class="logo">FTC 32477<br>Origin</div>
      <div class="sub">{lang["brand"]}</div>
    </a>
    <select class="lang-select-sidebar" id="langSelectSide" aria-label="{lang['lang_label']}">
{select_options}
    </select>
  </div>
  <div class="sidebar-nav">
{nav_html}
  </div>
  <div class="sidebar-footer">{lang["footer"]}</div>
</nav>

<main>
  <div class="lh-page">
    <div class="lh-hero">
      <img class="lh-logo" src="../images/basic/team_logo_small.png" alt="32477 Origin Team Logo">
      <div class="lh-badge">TEAM 32477 ORIGIN</div>
      <h1>{t["hero_title"]}</h1>
      <div class="lh-slogan">{t["slogan"]}</div>
    </div>
    <section id="about">
      <h2>{t["about_title"]}</h2>
      <div class="lh-about">
{about_lines}
      </div>
    </section>
    <section id="download">
      <h2>{t["download_title"]}</h2>
      <p class="lh-download-desc">{t["download_desc"]}</p>
      {pdf_block}
    </section>
    <section id="chapters">
      <h2>{t["chapters_title"]}</h2>
      <ol class="lh-chapters">
{chapter_items}
      </ol>
    </section>
    <section id="versions">
      <h2>{VERSIONS_TEXTS[lang_key]["page_title"]}</h2>
      <p class="lh-versions-desc">{t["versions_desc"]}</p>
      <a class="lh-btn" href="versions.html">{t["versions_btn"]}</a>
    </section>
    <p class="lh-legal">{t["legal"]}</p>
  </div>
</main>

<script>
(function(){{
  var sb=document.getElementById("sidebar");
  var ol=document.getElementById("overlay");
  var btn=document.getElementById("menuBtn");
  function open(){{sb.classList.add("open");ol.classList.add("show");btn.setAttribute("aria-expanded","true")}}
  function close(){{sb.classList.remove("open");ol.classList.remove("show");btn.setAttribute("aria-expanded","false")}}
  btn.addEventListener("click",function(){{sb.classList.contains("open")?close():open()}});
  ol.addEventListener("click",close);
  var ls=document.getElementById("langSelect");
  if(ls){{ls.addEventListener("change",function(){{window.location.href=ls.value}})}};
  var lss=document.getElementById("langSelectSide");
  if(lss){{lss.addEventListener("change",function(){{window.location.href=lss.value}})}};
}})();
</script>
{dev_badge(lang_key)}
</body>
</html>"""


# ============================================================
#  历史版本页（单语言中文长页面，复用指南页外壳）
# ============================================================

VERSIONS_CSS = r"""
/* ====== 历史版本页 ====== */
.ver-page{max-width:760px;margin:0 auto}
.ver-top{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;flex-wrap:wrap}
.ver-top h1{font-size:28px;color:#2c2c2c}
.ver-sort{display:inline-flex;border:1px solid #e0e0e0;border-radius:8px;overflow:hidden;background:#fff}
.ver-sort-btn{background:#fff;border:none;padding:6px 14px;font-size:13px;cursor:pointer;color:#666}
.ver-sort-btn.active{background:#1a1a2e;color:#fff}
.ver-intro{color:#666;margin:10px 0 22px;font-size:14px}
.ver-list{display:flex;flex-direction:column;gap:16px}
.ver-list.reversed{flex-direction:column-reverse}
.ver-card{background:#fff;border:1px solid #e0e0e0;border-radius:12px;padding:22px 24px;box-shadow:0 1px 4px rgba(0,0,0,.04);scroll-margin-top:24px}
.ver-head{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.ver-tag{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-weight:700;font-size:16px;color:#1a1a2e}
.ver-name{color:#666;font-size:14px}
.ver-badge{font-size:11px;font-weight:600;padding:2px 10px;border-radius:12px}
.ver-badge.latest{background:#d32f2f;color:#fff}
.ver-badge.preview{background:#f9a825;color:#fff}
.ver-date{color:#999;font-size:12.5px;margin-top:6px}
.ver-changes{margin:12px 0 0;padding-left:20px;color:#2c2c2c;font-size:14px;line-height:1.8}
.ver-changes li{margin:2px 0}
.ver-pdfs{margin-top:14px;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.ver-pdf-label{color:#999;font-size:13px}
.ver-pdf-btn{background:#f0f0f0;color:#2c2c2c;border:1px solid #e0e0e0;border-radius:8px;padding:6px 12px;font-size:13px;font-weight:600;text-decoration:none}
.ver-pdf-btn:hover{background:#e4e4e4}
.ver-pdf-note{color:#999;font-size:13px;margin-top:12px}
#verNav{display:flex;flex-direction:column}
#verNav.reversed{flex-direction:column-reverse}
.sidebar-nav a.ver-link{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px}
/* dev 预览标识（仅 dev 通道构建时输出；打印隐藏） */
.dev-badge{
  position:fixed;right:14px;bottom:14px;z-index:400;
  background:#d32f2f;color:#fff;padding:6px 14px;border-radius:999px;
  font-size:12px;font-weight:600;box-shadow:0 2px 8px rgba(0,0,0,.25);opacity:.92
}
@media print{.dev-badge{display:none!important}}
@media print{.topbar,.sidebar,.overlay,.ver-sort{display:none!important}}
"""


def format_release_date(lang_key, iso_date):
    """按语言本地化发布日期（ISO 格式）。"""
    try:
        y, m, d = (int(x) for x in iso_date.split("-"))
    except (ValueError, AttributeError):
        return iso_date
    if lang_key in ("zh-hans", "zh-hant"):
        return f"{y}\u5e74{m}\u6708{d}\u65e5"
    if lang_key == "en-us":
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        return f"{months[m - 1]} {d}, {y}"
    if lang_key == "fr":
        months = ["janvier", "f\u00e9vrier", "mars", "avril", "mai", "juin",
                  "juillet", "ao\u00fbt", "septembre", "octobre", "novembre", "d\u00e9cembre"]
        return f"{d} {months[m - 1]} {y}"
    if lang_key == "es":
        months = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                  "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return f"{d} de {months[m - 1]} de {y}"
    if lang_key == "pt-br":
        months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
                  "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        return f"{d} de {months[m - 1]} de {y}"
    if lang_key == "ko":
        return f"{y}년 {m}월 {d}일"
    return iso_date


# 历史版本页各语言文案
VERSIONS_TEXTS = {
    "zh-hans": {
        "page_title": "\u5386\u53f2\u7248\u672c",
        "intro": f"\u4ee5\u4e0b\u5217\u51fa\u5404\u7248\u672c\u7684\u53d1\u5e03\u65f6\u95f4\u4e0e\u4e3b\u8981\u6539\u52a8\uff0c\u6bcf\u4e2a\u7248\u672c\u63d0\u4f9b{lang_count_phrase('zh-hans')}\u7684 PDF \u4e0b\u8f7d\uff08\u65e9\u671f\u7248\u672c\u4ec5\u542b\u53d1\u5e03\u65f6\u5df2\u6709\u7684\u8bed\u8a00\uff09\uff0c\u4e0d\u63d0\u4f9b\u7f51\u9875\u7248\u3002",
        "sort_desc": "\u6700\u65b0\u5728\u524d",
        "sort_asc": "\u6700\u65e9\u5728\u524d",
        "pdf_label": "\u4e0b\u8f7d\uff1a",
        "status_dev": "\u72b6\u6001\uff1a\u5f00\u53d1\u4e2d\uff08\u672a\u53d1\u5e03\uff09",
        "date_prefix": "\u53d1\u5e03\u65f6\u95f4\uff1a",
        "badge_latest": "\u6700\u65b0\u7248\u672c",
        "badge_preview": "\u9884\u89c8",
        "pdf_note": "PDF \u5f85\u6b63\u5f0f\u53d1\u5e03\u540e\u63d0\u4f9b\u4e0b\u8f7d\u3002",
        "pdf_langs": {"zh-hans": "\u7b80\u4f53\u4e2d\u6587", "zh-hant": "\u7e41\u9ad4\u4e2d\u6587", "en-us": "English (US)", "fr": "Fran\u00e7ais", "es": "Espa\u00f1ol", "pt-br": "Português (BR)", "ko": "\ud55c\uad6d\uc5b4"},
    },
    "zh-hant": {
        "page_title": "\u6b77\u53f2\u7248\u672c",
        "intro": f"\u4ee5\u4e0b\u5217\u51fa\u5404\u7248\u672c\u7684\u767c\u5e03\u6642\u9593\u8207\u4e3b\u8981\u6539\u52d5\uff0c\u6bcf\u500b\u7248\u672c\u63d0\u4f9b{lang_count_phrase('zh-hant')}\u7684 PDF \u4e0b\u8f09\uff08\u65e9\u671f\u7248\u672c\u50c5\u542b\u767c\u5e03\u6642\u5df2\u6709\u7684\u8a9e\u8a00\uff09\uff0c\u4e0d\u63d0\u4f9b\u7db2\u9801\u7248\u3002",
        "sort_desc": "\u6700\u65b0\u5728\u524d",
        "sort_asc": "\u6700\u65e9\u5728\u524d",
        "pdf_label": "\u4e0b\u8f09\uff1a",
        "status_dev": "\u72c0\u614b\uff1a\u958b\u767c\u4e2d\uff08\u672a\u767c\u5e03\uff09",
        "date_prefix": "\u767c\u5e03\u6642\u9593\uff1a",
        "badge_latest": "\u6700\u65b0\u7248\u672c",
        "badge_preview": "\u9810\u89bd",
        "pdf_note": "PDF \u5f85\u6b63\u5f0f\u767c\u5e03\u5f8c\u63d0\u4f9b\u4e0b\u8f09\u3002",
        "pdf_langs": {"zh-hans": "\u7b80\u4f53\u4e2d\u6587", "zh-hant": "\u7e41\u9ad4\u4e2d\u6587", "en-us": "English (US)", "fr": "Fran\u00e7ais", "es": "Espa\u00f1ol", "pt-br": "Português (BR)", "ko": "\ud55c\uad6d\uc5b4"},
    },
    "en-us": {
        "page_title": "Version History",
        "intro": f"Release dates and key changes of each version. PDFs in {lang_count_phrase('en-us')} are provided for download (earlier versions include only the languages available at their release); no web edition is kept for past versions.",
        "sort_desc": "Newest first",
        "sort_asc": "Oldest first",
        "pdf_label": "Download:",
        "status_dev": "Status: under development (unreleased)",
        "date_prefix": "Released: ",
        "badge_latest": "Latest",
        "badge_preview": "Preview",
        "pdf_note": "PDFs will be available after the official release.",
        "pdf_langs": {"zh-hans": "\u7b80\u4f53\u4e2d\u6587", "zh-hant": "\u7e41\u9ad4\u4e2d\u6587", "en-us": "English (US)", "fr": "Fran\u00e7ais", "es": "Espa\u00f1ol", "pt-br": "Português (BR)", "ko": "\ud55c\uad6d\uc5b4"},
    },
    "fr": {
        "page_title": "Historique des versions",
        "intro": f"Dates de publication et principaux changements de chaque version. Les PDF en {lang_count_phrase('fr')} sont disponibles en t\u00e9l\u00e9chargement (les versions ant\u00e9rieures ne contiennent que les langues disponibles \u00e0 leur publication) ; aucune version web des versions pass\u00e9es n'est conserv\u00e9e.",
        "sort_desc": "Plus r\u00e9cents d'abord",
        "sort_asc": "Plus anciens d'abord",
        "pdf_label": "T\u00e9l\u00e9charger :",
        "status_dev": "Statut : en d\u00e9veloppement (non publi\u00e9e)",
        "date_prefix": "Publi\u00e9 : ",
        "badge_latest": "Derni\u00e8re version",
        "badge_preview": "Aper\u00e7u",
        "pdf_note": "Les PDF seront disponibles apr\u00e8s la publication officielle.",
        "pdf_langs": {"zh-hans": "\u7b80\u4f53\u4e2d\u6587", "zh-hant": "\u7e41\u9ad4\u4e2d\u6587", "en-us": "English (US)", "fr": "Fran\u00e7ais", "es": "Espa\u00f1ol", "pt-br": "Português (BR)", "ko": "\ud55c\uad6d\uc5b4"},
    },
    "es": {
        "page_title": "Historial de versiones",
        "intro": f"Fechas de publicaci\u00f3n y cambios principales de cada versi\u00f3n. Se ofrecen PDF en {lang_count_phrase('es')} para descargar (las versiones anteriores incluyen solo los idiomas disponibles en su publicaci\u00f3n); no se conservan ediciones web de versiones anteriores.",
        "sort_desc": "M\u00e1s recientes primero",
        "sort_asc": "M\u00e1s antiguos primero",
        "pdf_label": "Descargar:",
        "status_dev": "Estado: en desarrollo (no publicada)",
        "date_prefix": "Publicado: ",
        "badge_latest": "\u00daltima versi\u00f3n",
        "badge_preview": "Vista previa",
        "pdf_note": "Los PDF estar\u00e1n disponibles tras la publicaci\u00f3n oficial.",
        "pdf_langs": {"zh-hans": "\u7b80\u4f53\u4e2d\u6587", "zh-hant": "\u7e41\u9ad4\u4e2d\u6587", "en-us": "English (US)", "fr": "Fran\u00e7ais", "es": "Espa\u00f1ol", "pt-br": "Português (BR)", "ko": "\ud55c\uad6d\uc5b4"},
    },
    "ko": {
        "page_title": "\ubc84\uc804 \uae30\ub85d",
        "intro": f"\uac01 \ubc84\uc804\uc758 \ucd9c\uc2dc \ub0a0\uc9dc\uc640 \uc8fc\uc694 \ubcc0\uacbd \uc0ac\ud56d\uc785\ub2c8\ub2e4. {lang_count_phrase('ko')} PDF\ub97c \ub2e4\uc6b4\ub85c\ub4dc\ud560 \uc218 \uc788\uc73c\uba70(\ucd08\uae30 \ubc84\uc804\uc740 \ucd9c\uc2dc \ub2f9\uc2dc \uc81c\uacf5\ub418\ub358 \uc5b8\uc5b4\ub9cc \ud3ec\ud568), \uacfc\uac70 \ubc84\uc804\uc758 \uc6f9 \ubc84\uc804\uc740 \uc81c\uacf5\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.",
        "sort_desc": "\ucd5c\uc2e0\uc21c",
        "sort_asc": "\uc624\ub798\ub41c \uc21c",
        "pdf_label": "\ub2e4\uc6b4\ub85c\ub4dc:",
        "status_dev": "\uc0c1\ud0dc: \uac1c\ubc1c \uc911 (\ubbf8\ucd9c\uc2dc)",
        "date_prefix": "\ucd9c\uc2dc\uc77c: ",
        "badge_latest": "\ucd5c\uc2e0 \ubc84\uc804",
        "badge_preview": "\ubbf8\ub9ac\ubcf4\uae30",
        "pdf_note": "PDF\ub294 \uc815\uc2dd \ucd9c\uc2dc \ud6c4 \ub2e4\uc6b4\ub85c\ub4dc\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4.",
        "pdf_langs": {"zh-hans": "\u7b80\u4f53\u4e2d\u6587", "zh-hant": "\u7e41\u9ad4\u4e2d\u6587", "en-us": "English (US)", "fr": "Fran\u00e7ais", "es": "Espa\u00f1ol", "pt-br": "Português (BR)", "ko": "\ud55c\uad6d\uc5b4"},
    },
    "pt-br": {
        "page_title": "Histórico de versões",
        "intro": f"Datas de publicação e principais mudanças de cada versão. Há PDFs em {lang_count_phrase('pt-br')} para download (as versões anteriores incluem apenas os idiomas disponíveis na época do lançamento); não mantemos edições web de versões anteriores.",
        "sort_desc": "Mais recentes primeiro",
        "sort_asc": "Mais antigas primeiro",
        "pdf_label": "Baixar:",
        "status_dev": "Status: em desenvolvimento (não publicada)",
        "date_prefix": "Publicado em ",
        "badge_latest": "Mais recente",
        "badge_preview": "Prévia",
        "pdf_note": "Os PDFs estarão disponíveis após o lançamento oficial.",
        "pdf_langs": {"zh-hans": "简体中文", "zh-hant": "繁體中文", "en-us": "English (US)", "fr": "Français", "es": "Español", "pt-br": "Português (BR)", "ko": "한국어"},
    },
}


def render_versions_page(lang_key):
    """生成某语言的历史版本页：倒序长列表 + 正序/倒序切换 + 侧边栏版本号锚点。"""
    t = VERSIONS_TEXTS[lang_key]
    lang = LANGUAGES[lang_key]
    versions = visible_versions()

    cards = []
    nav_items = []
    for idx, v in enumerate(versions):
        is_preview = v.get("status") == "preview"
        if is_preview:
            badge = f'<span class="ver-badge preview">{t["badge_preview"]}</span>'
        elif idx == 0:
            badge = f'<span class="ver-badge latest">{t["badge_latest"]}</span>'
        else:
            badge = ""
        changes = "".join(
            f"<li>{escape_bare_amp(c)}</li>"
            for c in v.get("changes", {}).get(lang_key) or []
        )
        if is_preview:
            date_line = f'<div class="ver-date">{t["status_dev"]}</div>'
        else:
            date_line = (
                f'<div class="ver-date">{t["date_prefix"]}'
                f'{format_release_date(lang_key, v["date"])}</div>'
            )
        if is_preview:
            pdf_row = f'<p class="ver-pdf-note">{t["pdf_note"]}</p>'
        else:
            btns = []
            for lk, label in t["pdf_langs"].items():
                fname = v.get("pdfs", {}).get(lk)
                if fname:
                    btns.append(
                        f'<a class="ver-pdf-btn" href="{RELEASE_BASE}/{v["tag"]}/{fname}" '
                        f'target="_blank" rel="noopener">{label}</a>'
                    )
            pdf_row = (
                f'<div class="ver-pdfs"><span class="ver-pdf-label">{t["pdf_label"]}</span>'
                + "".join(btns)
                + "</div>"
            )
        name = (v.get("name", {}).get(lang_key)
                or v.get("name", {}).get("en-us", "")
                or v.get("name", {}).get("zh-hans", ""))
        cards.append(
            f'<article class="ver-card" id="{v["tag"]}">'
            f'<div class="ver-head"><span class="ver-tag">{v["tag"]}</span>'
            f'<span class="ver-name">{name}</span>{badge}</div>'
            f'{date_line}'
            f'<ul class="ver-changes">{changes}</ul>'
            f'{pdf_row}'
            f'</article>'
        )
        nav_items.append(f'<a class="ver-link" href="#{v["tag"]}">{v["tag"]}</a>')

    cards_html = "\n".join(cards)
    nav_html = "\n".join(nav_items)

    # 语言切换：切换到历史版本页的对应语言版本（与指南页行为一致）
    select_options = "".join(
        f'<option value="../{lk}/versions.html"{" selected" if lk == lang_key else ""}>'
        f'{lc["label"]}</option>'
        for lk, lc in LANGUAGES.items()
    )

    return f"""<!DOCTYPE html>
<html lang="{lang_key}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t["page_title"]}\uff5c{lang["site_title"]}</title>
{meta_tags(t["page_title"] + "｜" + lang["site_title"], LANG_HOME_TEXTS[lang_key]["meta_desc"])}
{seo_links(lang_key, "versions")}
<link rel="icon" href="../images/basic/icon_team_logo.ico" type="image/x-icon">
<link rel="shortcut icon" href="../images/basic/icon_team_logo.ico" type="image/x-icon">
{favicon_links()}
<style>{CSS}
{VERSIONS_CSS}</style>
</head>
<body>

<div class="topbar">
  <img class="topbar-logo" src="../images/basic/team_logo_small.png" alt="32477 Origin">
  <span class="brand"><a href="../index.html" title="{lang['back_home_label']}">{lang["site_title"]}</a></span>
  <select class="lang-select" id="langSelect" aria-label="{lang['lang_label']}">
{select_options}
  </select>
  <button class="menu-btn" id="menuBtn" aria-label="{lang['menu_label']}" aria-controls="sidebar" aria-expanded="false">\u2630</button>
</div>
<div class="overlay" id="overlay"></div>

<nav class="sidebar" id="sidebar">
  <div class="sidebar-header">
    <a class="home-link" href="../index.html" title="{lang['back_home_label']}">
      <img class="side-logo" src="../images/basic/team_logo_small.png" alt="32477 Origin Team Logo">
      <div class="logo">FTC 32477<br>Origin</div>
      <div class="sub">{t["page_title"]}</div>
    </a>
    <select class="lang-select-sidebar" id="langSelectSide" aria-label="{lang['lang_label']}">
{select_options}
    </select>
  </div>
  <div class="sidebar-nav" id="verNav">
{nav_html}
  </div>
  <div class="sidebar-footer">{lang["footer"]}</div>
</nav>

<main>
  <div class="ver-page">
    <div class="ver-top">
      <h1>{t["page_title"]}</h1>
      <div class="ver-sort" role="group" aria-label="{lang['sort_label']}">
        <button id="sortDesc" class="ver-sort-btn active" type="button">{t["sort_desc"]}</button>
        <button id="sortAsc" class="ver-sort-btn" type="button">{t["sort_asc"]}</button>
      </div>
    </div>
    <p class="ver-intro">{t["intro"]}</p>
    <div class="ver-list" id="verList">
{cards_html}
    </div>
  </div>
</main>

<script>
(function(){{
  var sb=document.getElementById("sidebar");
  var ol=document.getElementById("overlay");
  var btn=document.getElementById("menuBtn");
  function open(){{sb.classList.add("open");ol.classList.add("show");btn.setAttribute("aria-expanded","true")}}
  function close(){{sb.classList.remove("open");ol.classList.remove("show");btn.setAttribute("aria-expanded","false")}}
  btn.addEventListener("click",function(){{sb.classList.contains("open")?close():open()}});
  ol.addEventListener("click",close);
  var ls=document.getElementById("langSelect");
  if(ls){{ls.addEventListener("change",function(){{window.location.href=ls.value}})}};
  var lss=document.getElementById("langSelectSide");
  if(lss){{lss.addEventListener("change",function(){{window.location.href=lss.value}})}};
  var list=document.getElementById("verList");
  var nav=document.getElementById("verNav");
  var asc=document.getElementById("sortAsc");
  var desc=document.getElementById("sortDesc");
  function setOrder(ascending){{
    list.classList.toggle("reversed",ascending);
    nav.classList.toggle("reversed",ascending);
    asc.classList.toggle("active",ascending);
    desc.classList.toggle("active",!ascending);
  }}
  asc.addEventListener("click",function(){{setOrder(true)}});
  desc.addEventListener("click",function(){{setOrder(false)}});
}})();
</script>
{dev_badge(lang_key)}
</body>
</html>"""


# ============================================================
#  构建主流程
# ============================================================

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def build():
    """读取所有语言的 Markdown 文件并生成 HTML。"""
    print("=" * 56)
    print("  FTC 32477 Origin — 多语言快速入门指南构建工具")
    print("=" * 56)

    ensure_dir(DIST_DIR)

    total = 0
    for lang_key, lang in LANGUAGES.items():
        lang_src = os.path.join(SRC_DIR, lang_key)
        lang_dist = os.path.join(DIST_DIR, lang_key)
        ensure_dir(lang_dist)

        # 该语言的主页
        lang_home_html = render_lang_homepage(lang_key)
        with open(os.path.join(lang_dist, "index.html"), "w", encoding="utf-8") as f:
            f.write(lang_home_html)
        total += 1

        for page_key in PAGE_KEYS:
            md_path = os.path.join(lang_src, f"{page_key}.md")
            if not os.path.exists(md_path):
                print(f"  [警告] 源文件不存在: {md_path}")
                continue

            with open(md_path, "r", encoding="utf-8") as f:
                md_content = f.read()

            html_body, headings = parse_markdown(md_content)
            full_html = render_page(page_key, html_body, lang_key, headings)

            out_path = os.path.join(lang_dist, f"{page_key}.html")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(full_html)
            total += 1

        # 该语言的历史版本页
        versions_html = render_versions_page(lang_key)
        with open(os.path.join(lang_dist, "versions.html"), "w", encoding="utf-8") as f:
            f.write(versions_html)
        total += 1

        print(f"  [构建] {lang['label']} ({lang_key}) — 主页 + {len(PAGE_KEYS)} 页 + 历史版本页")

    # 生成根门户（语言选择落地页）
    portal_html = render_portal()
    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(portal_html)
    total += 1
    print("  [生成] index.html（语言门户）")

    # 复制图片目录
    dist_images = os.path.join(DIST_DIR, "images")
    if os.path.exists(dist_images):
        shutil.rmtree(dist_images)
    if os.path.exists(IMAGES_DIR):
        shutil.copytree(IMAGES_DIR, dist_images)
        img_count = sum(
            len(files)
            for _, _, files in os.walk(IMAGES_DIR)
        )
        print(f"  [复制] images/ → dist/images/ ({img_count} 个文件)")
        exif_files = []
        for root, _, files in os.walk(IMAGES_DIR):
            for name in files:
                if name.lower().endswith((".jpg", ".jpeg")):
                    path = os.path.join(root, name)
                    try:
                        with open(path, "rb") as f:
                            if b"Exif\x00\x00" in f.read(65536):
                                exif_files.append(os.path.relpath(path, BASE_DIR))
                    except Exception:
                        pass
        if exif_files:
            print("  [提示] 以下图片含 EXIF 元数据（可能含 GPS/设备信息），建议清除后重新构建：")
            for rel in exif_files:
                print(f"         {rel}")
    else:
        ensure_dir(dist_images)
        print("  [提示] images/ 目录为空，可放置图片后重新构建")

    print("-" * 56)
    print(f"  构建完成! 共生成 {total} 个 HTML 文件（根门户 + 各语言主页 + 内容页 + 历史版本页），输出目录: {shorten_path(DIST_DIR)}")
    print("=" * 56)


def shorten_path(path):
    home = os.path.expanduser("~")
    if path.startswith(home):
        return "~" + path[len(home):]
    return path


def watch():
    """监听文件变化并自动重新构建（src/*.md、images/ 与 build.py 自身）。"""
    file_hashes = {}

    def hash_file(path):
        try:
            with open(path, "rb") as f:
                return hashlib.md5(f.read()).hexdigest()
        except FileNotFoundError:
            return None

    def watched_paths():
        """(路径, 展示名) 列表：源文件、图片目录全部文件、build.py 自身。"""
        paths = []
        for lang_key in LANGUAGES:
            for page_key in PAGE_KEYS:
                p = os.path.join(SRC_DIR, lang_key, f"{page_key}.md")
                paths.append((p, f"{lang_key}/{page_key}"))
        if os.path.isdir(IMAGES_DIR):
            for root, _, files in os.walk(IMAGES_DIR):
                for fn in files:
                    p = os.path.join(root, fn)
                    paths.append((p, os.path.relpath(p, BASE_DIR)))
        paths.append((os.path.join(BASE_DIR, "build.py"), "build.py"))
        return paths

    def scan():
        changed = set()
        for path, label in watched_paths():
            h = hash_file(path)
            if h != file_hashes.get(path):
                file_hashes[path] = h
                changed.add(label)
        return changed

    for path, _ in watched_paths():
        file_hashes[path] = hash_file(path)

    build()
    print("\n  [监听] 正在监听 src/、images/ 与 build.py 的变化，按 Ctrl+C 退出...\n")

    try:
        while True:
            time.sleep(1.5)
            changed = scan()
            if changed:
                print(f"\n  检测到变化: {', '.join(sorted(changed))}")
                if "build.py" in changed:
                    print("  [提示] build.py 已变更，自动重启监听以加载新代码...\n")
                    os.execv(sys.executable, [sys.executable] + sys.argv)
                build()
                print("\n  [监听] 继续监听...\n")
    except KeyboardInterrupt:
        print("\n  已停止监听。")


if __name__ == "__main__":
    for _i, _a in enumerate(sys.argv):
        if _a == "--channel" and _i + 1 < len(sys.argv):
            set_channel(sys.argv[_i + 1])
        elif _a.startswith("--channel="):
            set_channel(_a.split("=", 1)[1])
    if "--watch" in sys.argv:
        watch()
    else:
        build()
