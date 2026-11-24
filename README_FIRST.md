# FE Civil Prep — Private Book Edition

This is a **personal-use, offline study website** designed to resemble the previous FE Civil Prep dark dashboard. The source PDFs you provided are **already bundled** in the `books` directory. **You do not have to upload or select them in the browser.**

## Open the website on Mac

1. Download and fully extract the ZIP archive to a folder (do not preview files inside the ZIP).
2. Double-click `START_MAC.command`. If macOS prevents it from opening, open Terminal, navigate to the extracted folder, and run `python3 start.py` instead.
3. Your browser will open `http://127.0.0.1:8765/`. If it does not, copy that address into Chrome, Safari, Edge, or Firefox.
4. Keep the Terminal window running while studying. Close it with Ctrl+C when finished.

If `python3` is unavailable, a Python 3 installation is required for the private local server. You can try opening `index.html` directly, but embedded PDF page-jumping can fail on `file://` URLs; the local server is recommended.

## Open the website on Windows

1. Download and fully extract the ZIP.
2. Double-click `START_WINDOWS.bat` (Python 3 is required).
3. Browse `http://127.0.0.1:8765/` if it did not open automatically.

## Included source materials

- `books/learnova.pdf` — the uploaded 2025 Learnova FE Civil Prep book, **809 pages**.
- `books/islam.pdf` — the uploaded M. R. Islam *FE Civil Review with 800 Solved Problems* scan, **638 pages**.
- `books/handbook.pdf` — the uploaded NCEES FE Reference Handbook edition 10.6, **506 pages**.

Original figures, question wording, diagrams, and publisher solutions are displayed from these PDFs. The Learnova question browser indexes 1,052 consecutively numbered problems and maps 1,052 publisher solution page locations (one manually recovered from a malformed heading). M. R. Islam's image-only scan is fully viewable but its 800 problems are **not individually indexed or machine graded**.

## Included features

- Dark dashboard, 14 FE Civil subjects, question library, bookmarks, personal notes, and issue reports.
- Random practice sets with a 20-question / 60-minute default or a 110-question customizable timed set.
- Answer selection (A–D), comparison against the publisher's extracted key when unambiguous, and a source solution PDF viewer.
- Local progress saved in your browser, plus exportable JSON backups and issue reports.

No user accounts, cloud synchronization, or public hosting is provided. The website can be used on your computer even without an internet connection, as long as the included files and a local Python server are available.

## Limitations and accuracy

- **Publisher keys are not independently verified.** The source heading for question 277 was manually located on PDF page 516, and its answer is corrected to A because the publisher incorrectly labels the correct value as B. Question 276 is corrected to B because the publisher answers for the wrong rotational axis. Question 218 has no unambiguous option letter and remains ungraded. Do not treat automatically generated performance scores as a validated pass prediction.
- A few questions and their answer choices span more than one page. The original PDF viewer lets you scroll onward.
- The book by M. R. Islam refers to reference handbook 9.5; the included FE Handbook is 10.6, so some equation/page locations may differ.
- This version preserves original publisher pages, rather than individually recreating every question as editable HTML.
- Some browser PDF viewers ignore `#page=` navigation; open the source PDF in a new tab and use the toolbar's page field when needed.

## Copyright / sharing

These source books and handbook are copyrighted. **The complete ZIP includes full copyrighted works and is for your private study only. Do not commit the `books/` folder to a public GitHub repository, publish this ZIP, or send it to friends without the rights holders' permission to redistribute those works.** Your permission to this assistant to work on uploaded copies does not by itself confer republication rights.

If you need a publicly shareable website, retain the web interface and provide a licensing-compliant way for visitors to access their *own* copies of the books, or secure explicit publisher licenses to distribute the material.
