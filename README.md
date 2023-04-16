# Manuscript Template Repository

Welcome to the template repository for building scientific manusrc/utilities in markdown with version control. This repository contains an example layout, template files and general-purpose src/utilities to automate many of the steps in structuring and organising a manuscript folder, generating figures and creating/editing text documents.

## Basic layout

- [manuscript.qmd](manuscript.qmd)
  - Template markdown document with sections for a basic manuscript, including Abstract, Introduction, Methods, Results, Discussion etc.
  - This is currently setup for basic manual rendering using Pandoc, however the Quarto workflow is strongly recommended - you can add this functionality by following the directions available via the [basic](https://github.com/dezeraecox-manuscripts/basic) template

- [figures](figures/)
  - Should contain complete figure ```.svg``` and ```.png``` file, which can optionally be created using the [figure_panels](src/utilities/figure_panels.py) and [figure_layouts](src/utilities/figure_layouts.py) scripts.
  - This enables figures to be referenced in the ```.qmd``` files uing the relative path ```figures/name.png```

- [src/utilities](src/utilities/)
  - Utility script for [collecting data and analyses](src/utilities/data_collection.py) repositories from existing github directories
  - Utility src/utilities for generating [figure panels](src/utilities/figure_panels.py), [layouts](src/utilities/figure_layouts.py) and [exporting to png](src/utilities/figure_to_text.py) files for use in the text drafting process

- [data_and_analyses](data_and_analyses/)
  - Will contain each experimental repository that contribute analyses for the figures. Repositories are initialised into this folder using the [data_collection](src/utilities/data_collection.py) script.
  - Also contains any databases/additional resources that pertain to the analyses are stored. Note that these components should not be tracked via version control, however it is a good idea to keep track of the download date and version e.g. in the [resources index](data_and_analyses/resources.md).

- [submissions](submissions/)
  - Will contain all ```.docx``` versions of the manuscript labelled with manuscript shortname and version identifier
  - For edits from collaborators, these are appended with collaborators initials
  - Also contains [version index](versions/version_index.md) which lists all versions that have been created, and who interacts with these versions (i.e. when they are sent to and returned from collaborators) 
  - By default, this folder is not tracked via git to avoid exceeding the github file size limits, however the index file is. In addition, when incrementing versions in the index file, the commit will be tagged with a version identifier. 

- [resources](resources/)
  - [reference.docx](text/reference.docx) is a template document for pandoc export and SHOULD NOT BE RENAMED. Any changes to the internal styles of this document dictate the final export version from pandoc.
  - Contains any additional references or useful info for use during the text drafting process. Note that these resources are not tracked via version control.

- [archive](archive/)
  - recycling folder for anything deemed no longer relevant. Note that the folder is not tracked via git, although any files originally tracked by git and moved into this folder will continue to be tracked.

- [markdownlint.json](markdownlint.json) specifies linting rule to be ignored when drafting text in markdown

- [.gitignore](.gitignore) standard gitignore format

- [README.md](README.md) this explainer file, which should be removed and replaced with a manuscript-specific README. Some templates are provided for inspiration.

## Before you start

Using this format makes the following assumptions:

1. The experimental analyses to be included in the manuscript have their own independent github repositories, and will continue to be tracked via their own git repositories using a "manuscript" branch for development from within the data_and_analyses folder.
2. Only changes to the manuscript components are tracked via this repository, such as text and figures
3. Text drafts will be compiled in markdown, and exported to ```.docx``` or ```.pdf``` formats.

Using the complete functionality requires the following dependencies:

- [Inkscape](https://inkscape.org/) - free vector graphics editor
- [Pandoc](https://pandoc.org/)
- [Zotero](https://www.zotero.org/) with the [ZotFile](http://zotfile.com/) and [BetterBibTex](https://retorque.re/zotero-better-bibtex/) tools installed
- [Quarto](https://quarto.org/)
- Microsoft Office (specifically Word for editing the reference document)

In addition, the general workflow underlying this repository was conceived to integrate with [VSCode](https://code.visualstudio.com/) and you may find some of the following extensions useful:

- vscode-pandoc
- quarto
- Pandoc Markdown Preview
- Markdown Table Prettifier
- Excel to Markdown table
- Code Spell Checker
- [Zotero citation picker](https://marketplace.visualstudio.com/items?itemName=mblode.zotero)
- Pandoc Citer

## Initial Setup

To get started, clone this repository using GitHub's 'use template' option. The following initial cleanup steps are recommended:

- remove the ```.txt``` placeholder files: [archive](archive\archive.txt), [outlines](figures\outlines\outlines.txt)
- Remove this README.md file, and create a new README.md including the manuscript running title and any additional information specific to the manuscript itself
- Update the name of the [template markdown](manuscript.qmd) file with the manuscript's running title


## General Workflow

### Data collection

You are now ready to begin constructing the [data_and_analysis](data_and_analysis/) folder using the [data_collection](src/utilities/data_collection.py) script. 

### Figure creation, including export to png

- Once individual figure panels have been created compile them into the ```figures``` folder, optionally using the [figure_panels](src/utilities/figure_panels.py) and [figure_layouts](src/utilities/figure_layouts.py) scripts to copy and rename individual panels into subdirectories within the [figures](figures/) folder
- Once complete, figures can be bacth-exported to ```png``` using the [figure_to_text](src/utilities/figure_to_text.py) script

### Text drafting

- Complete text draft within the [manuscript.qmd](manuscript.qmd) document
- General markdown syntax can be used to add italicised, bold text etc and to delineate sections using heading styles
- In addition, latex can be used for symbols and inline math which will be converted to inline

- Examples include:
  - ^2^ superscript
  - ~2~ subscript
  - $\alpha$ or $\beta$ or β

#### Figure captions

- Figures should be generated within the ```figures``` folder, and the ```figure_to_text.py``` script used to then copy relevant the files (and convert ```.svg``` to ```.png``` as appropriate)
- The figures and associated captions can be inserted using pandoc format and relative paths to the figures folder
- In-text references to the figure can then be included which will be converted to linked references
- For more information, see [syntax guide](https://maehr.github.io/academic-pandoc-template/markdown.html))

- Example formats of interest:
  - Figure caption: ```![**title**. details.](figures/figure_1.png){#fig-shortname}```
  - Intext figure reference: ```(Fig. {@fig-short_name}panel)```
  - Supp figure caption: ```![**title**. details.](path){#fig-shortname secno=2}```

#### Referencing with Zotero and BetterBibTex

- Before inserting references, you need to generate a copy of your Zotero library (or references of interest) as a ```.json``` style bibtex file, which can be exported from Zotero using ```File``` -> ```Export library``` -> ```Better CSL JSON``` with the ```Keep updated``` option checked (this will append cite keys for newly-added documents to your library automatically)
- Citations can then be included inline in plain text using the citation picker e.g. [@cox2020]
- When converting to ```.docx```, a custom filter will then generate live citation fields using the style stipulated in the header yml in the draft text (default is currently set to Cell style, additional CSL styles can be found [here](https://www.zotero.org/styles)).
- The BetterBibTEx custom pandoc filter ```zotero.lua``` is included in the text folder by default. If you need a fresh download, it can be found [here](https://retorque.re/zotero-better-bibtex/exporting/zotero.lua).

#### Continuous preview using VSCode

- As mentioned above, this workflow is designed to use VSCode, and in particular it provides the ability to preview rendered versions of the output live in the editor
- When getting started with the vscode-pandoc extensions, open the user settings and under ```Pandoc Options``` add the ```reference.docx``` from the resources folder to the Docx Opt String, which will render test output using the template file
- Under ```Pandoc Markdown Preview```, add the following options to the ```Extra Pandoc Arguements``` field: ```--filter pandoc-fignos --bibliography=zotero.json --lua-filter=zotero.lua```
- Now, to live-preview the markdown document inside the editor ```Ctrl+Shift+R```, or to preview the exported document  ```Ctrl+K, P``` and choose format of interest

### Export to docx and versioning

- When ready to generate a version for collaborators/submission:
    1. Add version information to pandoc code commented at the end of the ```.md``` file
    2. Complete the version index with updated version information
    3. Commit the version index and manuscript with the version tag in the commit
    4. Open new terminal and complete pandoc export using the updated command, placing the exported doc version into the [versions](versions/) folder
    5. Make any final updates to the ```.docx``` version of the manuscript in the versions folder (simple cosmetic updates are often necessary at this stage)
- Version is now ready to share with collaborators/submit as necessary

## Additional Information

- Inserting changes from collaborators who use track changes in ```.docx``` format remains a sticking point in this workflow - the reverse conversion from ```.docx``` to markdown is imperfect and the individual word-level changes given by track changes are difficult to implement. 
- For now, the simplest solution has been to copy individual chunks of edited text into the ```.md``` version, to preserve the citation entries.
- You can find more information on tagging git commits [here](https://git-scm.com/book/en/v2/Git-Basics-Tagging).

## Disclaimer

*This template repository was designed for personal use and is provided as-is. Whilst I endeavour to keep it up-to-date and respond to issues raised here,  I can provide no guarantee of the completeness, accuracy, reliability, suitability or availability of the information, services and software contained here for your use case.*
