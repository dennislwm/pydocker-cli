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
    - [Issue #4](#issue-4)
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
       +- .github/                                <-- Root of GitHub templates, workflows, actions
          +- workflows/                           <-- Source files for GitHub workflows
       +- htmltopdf/                              <-- Source files for Html link to PDF conversion
       +- udemyenrol/                             <-- Source files for Udemy free course
          |- .dockerignore                        <-- Docker ignore file
          |- actions.yml                          <-- GitHub actions file
          |- app.py                               <-- Tiny Python app
          |- Dockerfile                           <-- Dockerfile for app
          |- requirements.txt                     <-- Tiny Python app dependencies
          |- udemyenrol.md                        <-- Daily Free Udemy Courses published by GitHub Actions

---
## Methodology

This is the minimum viable product (MVP) to test the above hypothesis.

### Non-existant viable feature
* make lots of half-baked tiny python command line apps
* enable Dockerfile WORKDIR support for GitHub Actions (see [Issue #4](#issue-4))

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
- (Patr2020) Antariksh Patre, accessed 14-Oct-2020, [Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE](https://github.com/dennislwm/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE)
- (Rade2020) Dano Radecic, 2-Nov-2020, [How to Send Beautiful Emails With Python — The Essential Guide](https://towardsdatascience.com/how-to-send-beautiful-emails-with-python-the-essential-guide-a01d00c80cd0)
- (Mezz2020) David Mezzetti, 14-Nov-2020, [GitHub Actions For the Win](https://towardsdatascience.com/github-actions-for-the-win-8a215d390c1b)
- (Gdoc2020) GitHub Docs, accessed 14-Nov-2020, [Dockerfile support for GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions/creating-actions/dockerfile-support-for-github-actions#entrypoint)
- (Glab2020) GitHub Lab, accessed 14-Nov-2020, [GitHub Actions: Write Docker container actions](https://lab.github.com/githubtraining/github-actions:-write-docker-container-actions)

---
### Issue #4
* This is a solution to enable Dockerfile WORKDIR support for GitHub Actions:
  * In **main.yml**, set both *steps.with.entrypoint* and *steps.with.args* values in combination with *steps.uses*, to overwrite ENTRYPOINT and CMD in your Dockerfile respectively
    * For example, set *steps.with.entrypoint* and *steps.with.args* to "python3" and "udemyenrol/app.py" respectively
  * Why? In **Dockerfile**, GitHub Actions (GA) sets its source folder to GITHUB_WORKSPACE, ie. **root** folder.
    * For example, when using commands COPY or ADD, it copies or adds from GITHUB_WORKSPACE instead of current folder (see structure below)
```
     GITHUB_WORKSPACE/                            <-- Root of your repository
       +- udemyenrol/                             <-- Current folder for Dockerfile
          |- Dockerfile                           <-- In Dockerfile, "COPY . ." copies from GITHUB_WORKSPACE instead of current folder
```
  * We tried THREE (3) workarounds that failed:
    * In  **Dockerfile**, Github Actions ignores WORKDIR command
    * In **main.yml**, *steps.working-directory* does not work in combination with *steps.uses*
    * In **actions.yml**, *run.steps.working-directory* does not work in combination with *runs.using*: docker
  * Avoid using two separate Dockerfiles, one for GitHub Actions and one for local development.

---
## Contributing

Please read the [contributing guide](https://github.com/dennislwm/pydocker-cli/blob/master/CONTRIBUTING.md) on how you can actively participate in the development of this repository.

---
### Reach Out!

Please consider giving this repository a star on GitHub.
