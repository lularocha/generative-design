# Generative Design — Personal Sketchbook

A personal study repo working through the exercises in [Generative Design](http://www.generative-gestaltung.de) by Hartmut Bohnacker, Benedikt Groß, Julia Laub, and Claudius Lazzeroni.

All original Processing source code lives in the official repo:
**[generative-design/Code-Package-Processing-1.5.1](https://github.com/generative-design/Code-Package-Processing-1.5.1)**

---

## What's in this repo

- **`implemented/`** — sketches I've worked through, with source (`.pde`) and output images
- **`tool/`** — a local gallery and sketch viewer I built to browse all sketches and run the implemented ones
- **`svg-exports/`** — SVG outputs from select sketches

The source sketch folders (`01_P`, `02_M`, `03_A`) are not committed here — they're in the original repo above. The gallery tool loads their thumbnails directly from there.

---

## Gallery tool

A lightweight local server that shows all sketches as a browsable grid with thumbnails, and lets you open the implemented ones as interactive web sketches.

```bash
python3 tool/server.py
# → http://localhost:8080
```

---

## Original repo

> Hi. This GitHub repository completes the book [Generative Design](http://www.generative-gestaltung.de). It offers direct access to all [Processing](http://processing.org/) source code for the software described in the book.
>
> **Authors**
>
> - Hartmut Bohnacker
> - [Benedikt Groß](http://benedikt-gross.de)
> - [Julia Laub](http://www.onformative.com/)
> - [Claudius Lazzeroni](http://www.lazzeroni.de/), editor
>
> All of the book's source code is licensed under the [Apache License Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
