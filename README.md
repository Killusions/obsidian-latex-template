# Project Title

## General

This is a project made from the `obsidian-latex-template`.

It of a [scientific report](./deliverables/ScientificReport/scientific_report.pdf) and its [source](./deliverables/ScientificReport/scientific_report.md).

The project uses Markdown (and LaTeX) and yarn v1 (Node.js) as a task runner.

It uses Obsidian (Markdown) for [documentation](./Overview.md) and planning, it can also be viewed with any other markdown viewer (including GitHub/GitLab).

To open this project in Obsidian, open the root folder of this repository as a Vault, all plugins and settings should already be set up.

For Node.js dependency management it uses [yarn v1](https://classic.yarnpkg.com/lang/en/), please first install Node.js with npm.

To install yarn, run `npm install --global yarn`.

To then set up this project simply type `yarn`.

To see available commands, check out the `scripts` section of the `package.json` and run them using `yarn <command>`.

To install LaTex and Pandoc for building the documentation, run `yarn pdf:prepare` (may trigger large downloads).

To build the PDF, run `yarn pdf:export` (may take a while).

To format, use `yarn format`.

To store images and the PDF, it uses [Git LFS](https://git-lfs.com/) to not bloat project storage, make sure to install it first.

## Authors and acknowledgment

This template is downstream from a project done by the following students:

- [Linus Schlumberger](https://github.com/Killusions)
- [Lukas Stöckli](https://github.com/Valairaa)
- [Yutaro Sigrist](https://github.com/yusigrist)
