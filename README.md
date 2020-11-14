# pydocker-cli

pydocker-cli starter project.

---
## Table of Contents
- [pydocker-cli](#pydocker-cli)
  - [Table of Contents](#table-of-contents)
  - [Hypothesis](#hypothesis)
  - [Project Structure](#project-structure)
  - [Methodology](#methodology)
    - [Non-existant viable feature](#non-existant-viable-feature)
    - [Existing viable feature](#existing-viable-feature)
  - [Complexity](#complexity)
    - [Non-existant bloat](#non-existant-bloat)
    - [Existing bloat](#existing-bloat)
    - [References](#references)
  - [Contributing](#contributing)
    - [Reach Out!](#reach-out)

---
## Hypothesis
**pydocker-cli** was a personal project to:
* make lots of half-baked tiny python command line apps

---
## Project Structure
     pydocker-cli/                                <-- Root of your project
       |- .gitignore                              <-- Git ignore file
       |- README.md                               <-- This README markdown file
       +- htmltopdf/                              <-- Source files for Html link to PDF conversion
       +- udemyenrol/                             <-- Source files for Udemy free course
          |- .dockerignore                        <-- Docker ignore file
          |- actions.yml                          <-- GitHub actions file for app
          |- app.py                               <-- Tiny Python app
          |- Dockerfile                           <-- Dockerfile for app
          |- requirements.txt                     <-- Tiny Python app dependencies

---
## Methodology

This is the minimum viable product (MVP) to test the above hypothesis.

### Non-existant viable feature
* make lots of half-baked tiny python command line apps
* Moved from **main.yml** 'steps.working-directory' to **actions.yml** 'run.steps.working-directory' as it does not work in combination with **main.yml** 'steps.uses'

### Existing viable feature

* send email from Gmail using smtplib (Rade2020)
* continuous deployment of tiny python apps using GitHub Actions (Mezz2020)

---
## Complexity

Count the cost of complexity, i.e. incremental reward and risk reduction, before evolving MVP.

### Non-existant bloat
* Nil

### Existing bloat 
* Nil

---
### References
- (Rade2020) Dano Radecic, 2-Nov-2020, [How to Send Beautiful Emails With Python — The Essential Guide](https://towardsdatascience.com/how-to-send-beautiful-emails-with-python-the-essential-guide-a01d00c80cd0)
- (Mezz2020) David Mezzetti, 14-Nov-2020, [GitHub Actions For the Win](https://towardsdatascience.com/github-actions-for-the-win-8a215d390c1b)

---
## Contributing

Please read the [contributing guide](https://github.com/dennislwm/pydocker-cli/blob/master/CONTRIBUTING.md) on how you can actively participate in the development of this repository.

---
### Reach Out!

Please consider giving this repository a star on GitHub.
