# Quality assessment — private-book edition

## Sources inspected

- Learnova, 809 pages, text and embedded diagrams in original source PDF.
- M. R. Islam, 638 pages, image-only scanned PDF with 800 claimed solved problems.
- NCEES FE Reference Handbook, 506 pages, edition 10.6.

## Source navigation and metadata

- 1,052 Learnova main-section questions indexed to original PDF pages.
- 1,051 solution page anchors detected automatically; question 277 was mapped manually to PDF page 516 after visual inspection of its malformed heading. All 1,052 indexed questions now have a source solution-page reference.
- 1,050 publisher answer-letter matches automatically extracted. Question 277 was inspected manually and its correct result corresponds to option A, though the publisher printed B. Question 218 has no unambiguous answer letter and remains ungraded.
- 14 Learnova source subject classifications.
- M. R. Islam entire 638-page scan available, but its individual questions cannot be reliably extracted without a separate detailed indexing and validation process.

## Verified by engineering and editorial review?

**No.** The answer keys, diagrams, equations, handbook references and mathematical solutions have not been independently solved and validated one by one. Formatting, indexed headings and publisher answer extraction are not equivalent to engineering verification. Do not promise 100% correctness or NCEES-equivalent difficulty.

## How content is delivered

The user's PDFs are stored under `books/` and loaded automatically from a private local HTTP server. Unlike a public GitHub Pages package, this personal ZIP contains the full protected source PDFs. It is **not** licensed for public redistribution by this project.

## Functional tests

The build process checks indexed question IDs, source page ranges, file hashes, JavaScript syntax, static resource availability and dashboard navigation. Browser PDF plugin rendering can depend on browser and operating system. Consult the accompanying README for limitations.

## Two independently checked, known publisher errors

- **Learnova #276** (question PDF p. 112, solution pp. 515–516): As written, the axis passes through the thin rod's **center**. The applicable mass moment of inertia is `I = mL²/12` (option B). The publisher's printed solution answers A (`mL²/3`) for an axis through the **end**, contrary to the question statement. The private website grades B and displays this discrepancy.
- **Learnova #277** (question PDF p. 113, solution PDF p. 516): For the central axis of a solid cylinder, `k = R/√2`, which is **option A** on the question page. The publisher's solution gives this formula but incorrectly labels it B. The private website grades A and displays this discrepancy.

Only these particular entries received targeted calculation/statement review. The other entries have not been independently recalculated.
