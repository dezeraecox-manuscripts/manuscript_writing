
- To get reference.docx file (to then update templates)
pandoc --print-default-data-file reference.docx > reference.docx

- to convert word to md
pandoc -t markdown -f docx --reference-doc reference.docx -o draft.md draft.docx --filter pandoc-fignos --bibliography=zotero_library.bib --filter pandoc-citeproc --track-changes=accept --extract-media=figures
