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
page-margin: 2.5cm
---

# Header

## Subheader

### Tables with images need to have a header (like this one) right before (can have an empty header), they also need a table header:

_Images should also be using the path `./images/<file>` to be converted correctly._

| **Before DQA pipeline**   |                           |                           |
| ------------------------- | ------------------------- | ------------------------- |
| ![](./images/example.png) | ![](./images/example.png) | ![](./images/example.png) |
| **After DQA pipeline**    |                           |                           |
| ![](./images/example.png) | ![](./example.png)        | ![](./images/example.png) |

Links to sections should be in kebab-case, like `[link](#tables-with-images...)`.

You may also use inline LaTeX for formulas or tables.

$$
\begin{aligned}
&\text{Table 1. Example table.}^{1} \\[6pt]
&\begin{array}{lccc}
\hline
\text{Type}
  & \text{Metric 1}
  & \text{Metric 2}
\\\hline
\text{Experiment 1}     & 0.55 & 0.56 \\
\text{Experiment 2} & 0.87 & 0.86 \\
\hline
\end{array} \\[6pt]
&^{1}\!\text{ Additional information.}
\end{aligned}
$$

## Unnumbered header {-}

This section has an unnumbered header

### {-}

This section has an empty header, should be one higher than the table of contents (toc) level.

<div style="page-break-after: always; visibility: hidden;">\pagebreak</div>

# Bibliography {-}
