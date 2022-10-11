# pydocker-cli

pydocker-cli starter project.

---
## Table of Contents
- [pydocker-cli](#pydocker-cli)
  - [Table of Contents](#table-of-contents)
  - [Famed Contributors](#famed-contributors)
  - [Hypothesis](#hypothesis)
  - [Project Structure](#project-structure)
  - [Methodology](#methodology)
    - [Non-existant viable feature](#non-existant-viable-feature)
    - [Existing viable feature](#existing-viable-feature)
  - [Complexity](#complexity)
    - [Non-existant bloat](#non-existant-bloat)
    - [Existing bloat](#existing-bloat)
  - [1. etfdata](#1-etfdata)
    - [1.1 Usage](#11-usage)
    - [1.2 Configuration](#12-configuration)
    - [1.3 References](#13-references)
  - [2. htmltopdf](#2-htmltopdf)
  - [3. udemyenrol](#3-udemyenrol)
    - [3.1 Nothing to do](#31-nothing-to-do)
    - [3.2 Fork this repository if you want to receive email](#32-fork-this-repository-if-you-want-to-receive-email)
    - [3.3 Configuration (only if you are Contributing)](#33-configuration-only-if-you-are-contributing)
    - [3.4 References](#34-references)
  - [4. textscore](#4-textscore)
    - [4.1 Usage](#41-usage)
    - [4.2 References](#42-references)
  - [5. biblia](#5-biblia)
    - [5.1 Usage](#51-usage)
    - [5.1 References](#51-references)
  - [BeautifulSoup4](https://thecodingpie.com/post/lets-do-web-scraping-with-python-beautifulsoup4)](#beautifulsoup4httpsthecodingpiecompostlets-do-web-scraping-with-python-beautifulsoup4)
  - [Common](#common)
    - [Issue #4](#issue-4)
  - [Contributing](#contributing)
    - [Reach Out!](#reach-out)

--- 
## Famed Contributors
| [![](https://github.com/dennislwm.png?size=50)](https://github.com/dennislwm) 
| ----------------------------------------------------------------------------- 
| [@dennislwm](https://github.com/dennislwm)                                    


---
## Hypothesis
**pydocker-cli** was a personal project to:
* make lots of half-baked tiny python command line apps

---
## Project Structure
     pydocker-cli/                                <-- Root of your project
       |- .gitignore                              <-- Git ignore file
       |- CONTRIBUTING.md                         <-- Contributing guide
       |- README.md                               <-- This README markdown file
       +- .github/                                <-- Root of GitHub templates, workflows, actions
          +- workflows/                           <-- Source files for GitHub workflows
       +- biblia/                                 <-- Source files for bible data
       +- etfdata/                                <-- Source files for ETF and stock data
       +- htmltopdf/                              <-- Source files for Html link to PDF conversion
       +- textscore/                              <-- Source files for text readability score
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

* The cost of Click is quite high, ~150 lines of code in **etfdata**, for a shell file that has EMPTY functions (exclude tests).

### Non-existant bloat
* Nil

### Existing bloat 
* use Click to to create and test a Python CLI app (Bowm2020), (Ppro2020)

---
## 1. etfdata

This tiny app prints etf and stock data.

### 1.1 Usage

```
$ python3 etfdata.py
Usage: etfdata.py [OPTIONS] COMMAND [ARGS]...

  This script prints etf and stock data

Options:
  -o, --out [csv|json|markdown|text]
                                  Output type, default=text
  -h, --help                      Show this message and exit.

Commands:
  cal    Economic calendar
  etf    ETF fundamentals
  list   List of symbols
  news   Latest market news
  stock  Stock fundamentals of SYMBOLS where SYMBOLS is one or more...
```

### 1.2 Configuration

**etfdata** requires a *config.json* to run correctly. This file contains sensitive information, hence it is not checked into repo.

Create a new file *config.json* in the same folder as *etfdata.py* and copy and paste below.
```
{
  "FINNHUB_API_KEY": "asdfasdfasdfasfasdfasdf",
  "FINNHUB_API_KEY_SANDBOX": "sandbox_asdfasdfasdfsadfasfdsaf"
}
```
Go to [Finnhub Stock API](https://finnhub.io) to create a free account. Then copy and paste both of the above api keys.

### 1.3 References
- (Bowm2020) Jonathan Bowman, 7-Aug-2020, [Build and Test a Command Line Interface with Python, Poetry, Click, and pytest](https://dev.to/bowmanjd/build-a-command-line-interface-with-python-poetry-and-click-1f5k)
- (Ppro2020) Pallet Projects, accessed 16-Nov-2020, [Welcome to Click — Click Documentation (7.x)](https://click.palletsprojects.com/en/7.x)
- (Finn2020) Finnhub.io, accessed 16-Nov-2020, [Finnhub API Documentation](https://finnhub.io/docs/api)

---
## 2. htmltopdf

This tiny app does what its name suggests.

---
## 3. udemyenrol

This tiny app is invoked by GitHub Actions daily.

### 3.1 Nothing to do 

The action file runs this Python app that updates this page at UTC 0:01 daily. You can bookmark this page to save thousands of dollars for Udemy courses every year (legally).

> [Daily Free Udemy Courses](https://github.com/dennislwm/pydocker-cli/blob/master/udemyenrol/udemyenrol.md)

### 3.2 Fork this repository if you want to receive email

If you want to receive this page in your email, fork this repository. In your forked repository, add these to the GitHub secrets:

```
  GMAIL: user@gmail.com
  GMAIL_APP_PASSWORD: generatedpassword
```

The app uses GMAIL to send both from (sender) and to (recepient). Go to [Gmail account](https://myaccount.google.com/apppasswords) to create GMAIL_APP_PASSWORD.

Warning: Do not use your Gmail password for the app password, which is a special password that is used to bypass two-factor authentication.

### 3.3 Configuration (only if you are Contributing)

**Udemyenrol** requires a *settings.yaml* to run in your local development. This file contains sensitive information, hence it is not checked into repo.

Create a new file *settings.yaml* in the same folder as *app.py* and copy and paste below.

```
udemy:
  email: "name@example.com" 
  password: "password123" 
  gmail: "name@gmail.com"
  gmail_app_password: "generatedpassword"
```
This is an explanation of the above settings file.

* email - Enter your Udemy registered email here (You do not need to change this as it is Disabled)
* password - Enter your Udemy password here (You do not need to change this as it is Disabled)
* gmail - Gmail address that is used by app to send daily free courses from and to
* gmail_app_password - Gmail app password (Go to https://myaccount.google.com/apppasswords to generate one)

### 3.4 References
- (Patr2020) Antariksh Patre, accessed 14-Oct-2020, [Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE](https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE)
- (Rade2020) Dano Radecic, 2-Nov-2020, [How to Send Beautiful Emails With Python — The Essential Guide](https://towardsdatascience.com/how-to-send-beautiful-emails-with-python-the-essential-guide-a01d00c80cd0)
- (Mezz2020) David Mezzetti, 14-Nov-2020, [GitHub Actions For the Win](https://towardsdatascience.com/github-actions-for-the-win-8a215d390c1b)
- (Gdoc2020) GitHub Docs, accessed 14-Nov-2020, [Dockerfile support for GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions/creating-actions/dockerfile-support-for-github-actions#entrypoint)
- (Glab2020) GitHub Lab, accessed 14-Nov-2020, [GitHub Actions: Write Docker container actions](https://lab.github.com/githubtraining/github-actions:-write-docker-container-actions)

---
## 4. textscore

This tiny app generates a readability score from a file.

### 4.1 Usage

```
$ python3 textscore.py --help
Usage: textscore.py [OPTIONS] TEXTFILE

  This script scores the readability of a TEXTFILE

  TEXTFILE may include wildcards, e.g. *.txt

Options:
  -o, --out [csv|json|markdown|text]
                                  Output type, default=text
  -h, --help                      Show this message and exit.
```

### 4.2 References

- (Moye2020) Dawn Moyer, 9-Nov-2020, [Using Data Science Skills Now: Text Readability Analysis](https://towardsdatascience.com/using-data-science-skills-now-text-readability-analysis-c4c4641f5875)

---
## 5. biblia

This tiny app prints bible data from Biblia.

### 5.1 Usage

```
$ python3 biblia.py --help
Usage: biblia.py [OPTIONS] COMMAND [ARGS]...

  This script prints bible data

Options:
  -o, --out [csv|json|markdown|text]
                                  Output type, default=text
  -h, --help                      Show this message and exit.

Commands:
  content  Returns the content of a bible
  search   Searches the text of a bible
  toc      Returns the table of contents of a bible
  votd     Returns a carefully chosen verse each day
```

### 5.1 References

- (Bibl2020) Biblia API, accessed 26-Nov-2020, [Biblia API](https://api.biblia.com/v1/RegisteredApplications)
- (Post2020) Postman Documentation, accessed 26-Nov-2020, [Postman Biblia](https://documenter.getpostman.com/view/8994004/TVmFizQo)
- (Votd2020) Biblia Verse of the Day, accessed 26-Nov-2020, [Biblia Verse of the Day plugin](https://biblia.com/plugins/VerseOfTheDay)
- (Arav2020) Aravind, accessed 26-Nov-2020, [Let's Build a Web Scraper with Python &
BeautifulSoup4](https://thecodingpie.com/post/lets-do-web-scraping-with-python-beautifulsoup4)
---
## Local Workstation

### Requirements
* `git`
* `pipenv`

### Making code changes locally

1. Clone the repository to your local workstation with `git clone`.

2. Change directory to the cloned repo and project, e.g. `cd pydocker-cli/udemyenrol`.

3. Create a Python virtual environment with `pipenv shell`.

4. Install the Python dependencies with `pipenv install`.

5. Start coding!

---
## Common

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
