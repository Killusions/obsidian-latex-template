# Project Title

## General

This is a project made from the `dspro_template`.

It consists of a codebase, a [scientific report](./deliverables/ScientificReport/scientific_report.pdf) ([source](./deliverables/ScientificReport/scientific_report.md)).

The project uses Markdown (and LaTeX), Python and Node.js with Typescript.

It uses Obsidian (Markdown) for [documentation](./Overview.md) and planning, it can also be viewed with any other markdown viewer (including GitHub/GitLab).

For Python dependency management it uses [poetry](https://python-poetry.org/).

To set it up do `poetry install`, to add dependencies use `poetry add`.

To run commands use `poetry shell` to spawn a subshell.

Select the `venv` after running `poetry install` for Jupyter Notebooks.

For Node.js dependency management it uses [yarn v1](https://classic.yarnpkg.com/lang/en/).

To set it up simply type `yarn`.

To see available commands, check out the `scripts` section of the `package.json` and run them using `yarn <command>`.

All project relevant commands are handled via yarn, including formatting our Python, Typescript, and Markdown files and generating our report from our Markdown source.

## Collecting data

Simply run `yarn scrape:prepare`, then `yarn scrape:ui` (for local testing), `yarn scrape` or `scrape:deploy` (for multiple parallel instances).

## Authors and acknowledgment

The whole project was done by the following students:

- [Linus Schlumberger](https://github.com/Killusions)
- [Lukas Stöckli](https://github.com/Valairaa)
- [Yutaro Sigrist](https://github.com/yusigrist)
