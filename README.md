# Chinatimes news analysis about Ukraine-Russia war with NLP(TF-IDF)
## Problem
The Ukrainian-Russian war has been going on for more than a month now, and both sides have achieved mutual success. According to foreign reports, Ukraine successfully received online speeches by President Zelensky, and received strong funding and weapons from the European Union and the United States. NATO and European countries have imposed economic sanctions on Russia. At the same time when Western countries are in full swing, wondering how Taiwan views this incident.

This project will use web scraping to crawl the relevant news of ChinaTimes in the first week (20220224 ~ 20220302) and the fifth week (20220324 ~ 20220330) after the start of the Ukrainian-Russian war, and use Natural Language Processing (NLP) for keyword analysis.

## Authors
[@IsaacLee0904](https://github.com/IsaacLee0904)

## Data Source
Web Scraping news on [Chinatimes](https://www.chinatimes.com/?chdtv) using Scrapy Frame.

## Methods
* Exploratory data analysis
* Text Mining
* Natural Language Processing / NLP
* TF-IDF

## Tech Stack
* Python
* Scrapy
* Ckiptagger

## Set up Ckiptagger
1. Install ckiptagger
2. Downloading model file (require 2GB disk space)
* Follow https://github.com/ckiplab/ckiptagger
* python>=3.6
* tensorflow>=1.13.1,<2 / tensorflow-gpu>=1.13.1,<2 (one of them)

## Set up Scrapy
### Install
```
$ conda install -c conda-forge scrapy
```
### Set up environment
```
# create project file
$ cd Deskop/
$ mkdir scrapy

# create basic scrapy object
$ cd scrapy/
$ startproject tutorial
```
### Run Scrapy
```
$ scrapy crawl spider
```
## Quick glance at the results
First week top ten category.

![Week1](https://github.com/IsaacLee0904/Chinatimes-Ukraine-Russia-NLP/blob/main/assets/week1.png)

Fifth week top ten category.

![Week5](https://github.com/IsaacLee0904/Chinatimes-Ukraine-Russia-NLP/blob/main/assets/week5.png)

 
