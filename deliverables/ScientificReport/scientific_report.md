---
title: Scientific Report
subtitle: "Team name: Example Team"
author:
  - Linus Schlumberger
  - Lukas Stöckli
  - Yutaro Sigrist
keywords:
  - Ai
  - Deep Learning
date: 17-01-2025
toc: true
toc-depth: 2
toc-own-page: true
toc-title: "Table of Contents"
bibliography: ./deliverables/ScientificReport/references/references.bib
csl: ./deliverables/ScientificReport/.assets/apa.csl
lang: en
titlepage: true
titlepage-rule-color: "360049"
titlepage-rule-height: 1
titlepage-background: ./deliverables/ScientificReport/.assets/background5.pdf
linkcolor: "link"
urlcolor: "link"
linestretch: 1.2
fontsize: 10pt
header-includes:
  - |
    \RedeclareSectionCommand[
      beforeskip=0.1em,
      afterskip=0.3em
    ]{section}

    \RedeclareSectionCommand[
      beforeskip=0.05em,
      afterskip=0.2em
    ]{subsection}

    \RedeclareSectionCommand[
      beforeskip=0.01em,
      afterskip=0.1em
    ]{subsubsection}

    \RedeclareSectionCommand[
      beforeskip=0.0em,
      afterskip=0.05em
    ]{paragraph}

    \definecolor{link}{HTML}{0096FF}
abstract-own-page: true
abstract: |
  TODO: Insert abstract here.
---

##### Tables with images need to have a header (like this one) right before (can have an empty header), they also need a table header:

| **Before DQA pipeline**   |                           |                           |
| ------------------------- | ------------------------- | ------------------------- |
| ![](./images/example.png) | ![](./images/example.png) | ![](./images/example.png) |
| **After DQA pipeline**    |                           |                           |
| ![](./images/example.png) | ![](./example.png)        | ![](./images/example.png) |

#### Bibliography
