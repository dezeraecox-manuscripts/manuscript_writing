
- To get reference.docx file (to then update templates)
  
    ```pandoc --print-default-data-file reference.docx > reference.docx```

- To convert markdown to word
  - Using standard citeproc with ```.bib``` library:
  
    ```pandoc -f markdown -t docx --reference-doc reference.docx -o shortname_v##.docx shortname_v##.md --filter pandoc-fignos --bibliography=zotero_library.bib```

  - Using custom ```.json``` with lua filter:

    ```pandoc -f markdown -t docx --reference-doc reference.docx -o shortname_v##.docx shortname_v##.md --filter pandoc-fignos --bibliography=zotero.json --lua-filter=zotero.lua```

- To convert word to md
  
    ```pandoc -t markdown -f docx --reference-doc reference.docx -o draft.md draft.docx --filter pandoc-fignos --bibliography=zotero_library.bib --filter pandoc-citeproc --track-changes=accept --extract-media=figures --wrap=none```