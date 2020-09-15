# Manuscript Template Repository

Welcome to the template repository for building scientific manuscripts in markdown with version control. This repository contains an example layout, template files and general-purpose scripts to automate many of the steps in structuring and organising a manuscript folder, generating figures and creating/editing text documents.

## Basic layout

- [scripts](scripts/)
  - Utility script for [collecting data and analyses](scripts/data_collection.py) repositories from existing github directories
  - Utility scripts for generating [figure panels](scripts/figure_panels.py), [layouts](scripts/figure_layouts.py) and [exporting to png](scripts/figure_to_text.py) files for use in the text drafting process
  - [pandoc commands](scripts/pandoc_commands.md) contains various terminal commands to assist with converting ```.md``` to ```.docx```
  - Also contains a template script for [initialising the subfolders](scripts/initialise_subfolders.py) that do not necessarily need to be tracked by git (although these currently have placeholders to make them visibile in the template repository)
- [text](text/)
  - Contains current markdown and docx version of the manuscript, labelled as current version number
  - When incrementing version, markdown file is renamed (with no other changes) prior to exporting the docx version that will be transfered to the [collaborators edits](collaborators_edits/) folder.
  - [reference.docx](text/reference.docx) is the template document for pandoc export and SHOULD NOT BE RENAMED. Any changes to the internal styles of this document dictate the final export version from pandoc.
- [figures](figures/)
  - Will contain folders (F1_name) where individual figure panels (panel_#.svg) are collected. Panels should be collected using the [figure_panels](scripts/figure_panels.py) script. 
  - Optionally, the figure layouts for each figure (figure_#.svg) can be created using the [figure_layouts](scripts/figure_layouts.py) script.
- [data_and_analyses](data_and_analyses/)
  - Will contain each experimental repository that will contribute analyses for the figures. Repositories are initialised into this folder using the [data_collection](scripts/data_collection.py) script.
  - Also contains [resources](data_and_analysis/resources/) folder for any databases/additional resources that pertain to the analyses are stored. Note that these analyses are not tracked via version control, however the [resources index](data_and_analysis/resources/resources.md) file is to ensure a record of the relevant resources.
- [collaborators_edits](collaborators_edits/)
  - contains all ```.docx``` versions of the manuscript labelled with manuscript shortname and version identifier
  - also contains [version index](collaborators_edits/version_index.md) which lists all versions that have been created, and who interacts with these versions (i.e. when they are sent to and returned from collaborators) 
- [resources](resources/)
  - Contains any additional references or useful info for use during the text drafting process. Note that these resources are not tracked via version control, however the [resources index](resources/resources.md) file is to ensure a record of the relevant resources.
- [archive](archive/)
  - recycling folder for anything deemed no longer relevant. Note that the folder is not tracked via git, although any files originally tracked by git and moved into this folder will continue to be tracked.
- [manuscript_README](manuscript_README.md) file is to be renamed as README.md to overwrite this file when creating a new repository, and tracks draft status
- [markdownlint.json](markdownlint.json) specifies linting rule to be ignored when drafting text in markdown
- [.gitignore](.gitignore) standard gitignore format
- [README.md](README.md) this explainer file, which should be removed and replaced with manuscript-tracking README

## Before you start

Using this format makes the following assumptions:

1. The experimental analyses to be included in the manuscript have their own independent github repositories, and will continue to be tracked via their own git repositories using a "manuscript" branch for development from within the data_and_analyses folder.
2. Only changes to the manuscript components are tracked via this repository, such as text and figures
3. Text drafts will be compiled in markdown, and exported to ```.docx``` format.

Using the complete functionality requires the following dependencies:

- [Inkscape](https://inkscape.org/) - free vector graphics editor
- [Pandoc](https://pandoc.org/)
- 
- Microsoft Office (specifically Word for editing the reference document)

In addition, the general workflow underlying this repository was conceived to integrate with [VSCode](https://code.visualstudio.com/) and you may find some of the following extensions useful:

- vscode-pandoc
- Pandoc Markdown Preview
- Markdown Table Prettifier
- Excel to Markdown table
- Code Spell Checker
- Zotero citation picker
- Pandoc Citer

## Initial Setup

To get started, clone this repository using GitHub's 'use template' option. The following initial cleanup steps are recommended:

- remove the ```.txt``` placeholder files: [archive](archive\archive.txt), [for_powerpoint_outlines](figures\outlines\for_powerpoint_outlines.txt) and [for_svg_fig_pieces](figures\utilities\for_svg_fig_pieces.txt)
- Remove this README.md file, and relabel [manuscript_README.md](manuscript_README.md) as ```README.md```
- Update the details of the new README.md file, including the manuscript running title and any additional information
- Update the name of the [template markdown](text/shortname_v#.#.md) file ```shortname_v#.#.md``` with the manuscript's running title


## General Workflow

### Data collection

You are now ready to begin constructing the [data_and_analysis](data_and_analysis/) folder using the [data_collection](scripts/data_collection.py) script. 

### Figure creation, including export to png

- 

### Text drafts, including figure captions and referencing

- 

### Export to docx and versioning

- 

## Additional Information

- inserting changes from collaborators
- 

## Disclaimer

*This template repository was designed for personal use and is provided as-is. Whilst I endeavour to keep it up-to-date and respond to issues raised here,  I can provide no guarantee of the completeness, accuracy, reliability, suitability or availability of the information, services and software contained here for your use case.*
