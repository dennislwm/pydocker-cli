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
* In **main.yml**, set both *steps.with.entrypoint* and *steps.with.args* values in combination with *steps.uses*
  * These overwrite ENTRYPOINT and CMD in your Dockerfile respectively
  * For example, set *steps.with.entrypoint* and *steps.with.args* to "python3" and "udemyenrol/app.py" respectively
  * Why? In **Dockerfile**, GitHub Actions (GA) sets its source folder to GITHUB_WORKSPACE, ie. **root** folder, when using commands COPY or ADD
  * We tried THREE (3) workarounds that failed:
    * In **main.yml**, *steps.working-directory* does not work in combination with *steps.uses*
    * In **actions.yml**, *run.steps.working-directory* does not work in combination with *runs.using*: docker
    * In  **Dockerfile**, Github Actions ignores WORKDIR command
  * For example, when using "COPY . .", the source folder is the parent of current folder (see structure below).
```
     GITHUB_WORKSPACE/                            <-- Root of your project
       +- udemyenrol/                             <-- Current folder for Dockerfile
          |- Dockerfile                           <-- In Dockerfile, "COPY . ." copies from GITHUB_WORKSPACE instead of current folder
```

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
- [Dockerfile support for GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions/creating-actions/dockerfile-support-for-github-actions#entrypoint)

---
## Contributing

Please read the [contributing guide](https://github.com/dennislwm/pydocker-cli/blob/master/CONTRIBUTING.md) on how you can actively participate in the development of this repository.

---
### Reach Out!

Please consider giving this repository a star on GitHub.
