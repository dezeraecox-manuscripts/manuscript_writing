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
  - When incrementing version, markdown file is renamed (with no other changes) prior to exporting the docx version that will be transfered to the [collaborators edits](versions/) folder.
  - [reference.docx](text/reference.docx) is the template document for pandoc export and SHOULD NOT BE RENAMED. Any changes to the internal styles of this document dictate the final export version from pandoc.
- [figures](figures/)
  - Will contain folders (F1_name) where individual figure panels (panel_#.svg) are collected. Panels should be collected using the [figure_panels](scripts/figure_panels.py) script. 
  - Optionally, the figure layouts for each figure (figure_#.svg) can be created using the [figure_layouts](scripts/figure_layouts.py) script.
- [data_and_analyses](data_and_analyses/)
  - Will contain each experimental repository that will contribute analyses for the figures. Repositories are initialised into this folder using the [data_collection](scripts/data_collection.py) script.
  - Also contains [resources](data_and_analysis/resources/) folder for any databases/additional resources that pertain to the analyses are stored. Note that these analyses are not tracked via version control, however the [resources index](data_and_analysis/resources/resources.md) file is to ensure a record of the relevant resources.
- [versions](versions/)
  - contains all ```.docx``` versions of the manuscript labelled with manuscript shortname and version identifier
  - for edits from collaborators, these are appended with collaborators initials and 
  - by defaults, this folder is not tracked via git to avoid exceeding the github file size limits, however the index file is. In addition, when incrementing versions in the index file, the commit will be tagged with a version identifier. 
  - also contains [version index](versions/version_index.md) which lists all versions that have been created, and who interacts with these versions (i.e. when they are sent to and returned from collaborators) 
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

- [Pandoc](https://pandoc.org/)
- [Zotero](https://www.zotero.org/) with the [ZotFile](http://zotfile.com/) and [BetterBibTex](https://retorque.re/zotero-better-bibtex/) tools installed, and the 
- [Inkscape](https://inkscape.org/) - free vector graphics editor
- Microsoft Office (specifically Word for editing the reference document)

In addition, the general workflow underlying this repository was conceived to integrate with [VSCode](https://code.visualstudio.com/) and you may find some of the following extensions useful:

- vscode-pandoc
- Pandoc Markdown Preview
- Markdown Table Prettifier
- Excel to Markdown table
- Code Spell Checker
- [Zotero citation picker](https://marketplace.visualstudio.com/items?itemName=mblode.zotero)
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

- Once individual figure panels have been created within individual data and analyses repositories, complete the [figures_panel](scripts/figure_panels.py) script to copy and rename the relevant panels into [figures](figures/)
 directory
- Changes made to individual figure panels within this folder should only be cosmetic
- From here, either use [figure_layouts](scripts/figure_layouts.py) to generate the complete figures using ```svgutils``` or manually create compiled svg files within each folder for ```figure_1```, ..., ```figure_S1``` etc
- Again, only cosmetic changes should be made within these files
- Once complete, copy the finalised figures from figures to the [text](text/figures/) folder, and export to ```.png``` using [figure_to_text](scripts/figure_to_text.py)

### Text draft

- Complete text draft within the [shortname_v0.1.md](text/shortname_v0.1.md) document
- General markdown syntax can be used to add italicised, bold text etc and to delineate sections using heading styles
- In addition, latex can be used for symbols and inline math which will be converted to inline

- Examples include:
  - ^2^ superscript
  - ~2~ subscript
  - $\alpha$ or $\beta$ or β

#### Figure captions

- Figures should be generated within the ```figures``` folder as described above, and the ```figure_to_text.py``` script used to then copy relevant the files (and convert ```.svg``` to ```.png``` as appropriate)
- The figures and associated captions can be inserted using pandoc format and relative paths to the figures folder
- In-text references to the figure can then be included which will be converted to linked references
- For more information, see [syntax guide](https://maehr.github.io/academic-pandoc-template/markdown.html))

- Example formats of interest:
  - Figure caption: ```![**title**. details.](figures/figure_1.png){#fig:shortname}```
  - In-text figure reference: ```(Fig. {@fig:short_name}panel)```
  - Supp figure caption: ```![**title**. details.](path){#fig:shortname secno=2}```
  - Tables can be referenced similarly, replacing ```fig``` with ```tbl```

#### Referencing with Zotero and BetterBibTex

- Before inserting references, you need to generate a copy of your Zotero library (or references of interest) as a ```.json``` style bibtex file, which can be exported from Zotero using ```File``` -> ```Export library``` -> ```Better CSL JSON``` with the ```Keep updated``` option checked (this will append cite keys for newly-added documents to your library automatically)
- Citations can then be included inline in plain text using the citation picker e.g. [@cox2020]
- When converting to ```.docx```, custom filter will then generate live citation fields using the style stipulated in the header yml in the draft text (default is currently set to Cell style, additional CSL styles can be found [here](https://www.zotero.org/styles)).
- The BetterBibTEx custom pandoc filter ```zotero.lua``` is included in the text folder by default. If you need a fresh download, it can be found [here](https://retorque.re/zotero-better-bibtex/exporting/zotero.lua).

#### Continuous preview using VSCode

- As mentioned above, this workflow is designed to use VSCode, and in particular it provides the ability to preview rendered versions of the output live in the editor
- When getting started with the vscode-pandoc extensions, open the user settings and under ```Pandoc Options``` add the ```reference.docx``` to the Docx Opt String, which will render test output using the template file
- Under ```Pandoc Markdown Preview```, add the following options to the ```Extra Pandoc Arguements``` field: ```--filter pandoc-fignos --bibliography=zotero.json --lua-filter=zotero.lua```
- Now, to live-preview the markdown document inside the editor ```Ctrl+Shift+R```, or to preview the exported document  ```Ctrl+K, P``` and choose format of interest

<!--Add info on the fignos (and tablenos) filters from here <!--Add info on the fignos (and tablenos) filters from here https://github.com/tomduck/pandoc-xnos-->-->

### Export to docx and versioning

- When ready to generate a version for collaborators/submission:
    1. Add version information to pandoc code commented at the end of the ```.md``` file
    2. Complete the version index with updated version information
    3. Commit the version index and manuscript with the version tag in the commit
    4. Open new terminal and complete pandoc export using the updated command, placing the exported doc version into the [versions](versions/) folder
    5. Make any final updates to the ```.docx``` version of the manuscript in the versions folder (simple cosmetic updates are often necessary at this stage)
- Version is now ready to share with collaborators/submit as necessary

## Additional Information

- Inserting changes from collaborators who use track changes in ```.docx``` format remains a sticking point in this workflow - the reverse conversion from ```.docx``` to markdown is imperfect and the individual word-level changes given by track changes are difficult to implement. For now, the simplest solution has been to copy individual chunks of edited text into the ```.md``` version, to preserve the citation entries.
- You can find more information on tagging git commits [here](https://git-scm.com/book/en/v2/Git-Basics-Tagging).

## Disclaimer

*This template repository was designed for personal use and is provided as-is. Whilst I endeavour to keep it up-to-date and respond to issues raised here,  I can provide no guarantee of the completeness, accuracy, reliability, suitability or availability of the information, services and software contained here for your use case.*
