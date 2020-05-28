# Example commands for interconversion using pandoc

- To get reference.docx file (to then update templates)

```pandoc --print-default-data-file reference.docx > reference.docx```

- to convert word to md

```pandoc -s Text_drafts/Draft_1 _manuscript.md -o Text_drafts/draft_1_manuscript.docx```

- to convert using updating reference template

```pandoc -f markdown -t docx --reference-doc reference.docx -o text/200425_Draft_v1.1.md text/200425_Draft_v1.2.docx```

- convert word to markdown

```pandoc -f docx -t markdown -o text/200425_Draft 1 Urea Manuscript.md text/200425_Draft 1 Urea Manuscript.docx```