# WORK IN PROGRESS...

Notebooks from the Seminar:

# Human Machine Readable < WS21/22

### Introduction into programming

Georg Trogemann, Christian Heck, Mattis Kuhn, Ting Chun Liu

Basic Seminar Material/Sculpture/Code

Compact seminar 11 - 4 pm | 31.01.2022 until 11.02.2022 

Online @ BigBlueButton

[Experimental Informatics](https://en.khm.de/exMedia_experimentelle_informatik/)

Academy of Media Arts Cologne

Email: g.trogemann@khm.de, c.heck@khm.de, m.kuhn@khm.de

### Description

The generation of text by means of deep neural nets (NLG) has spread rapidly. Among other things, text-based dialog systems such as chatbots, assistance systems (Alexa/Siri) or robot journalism are increasingly used in news portals, e-commerce and social media; wherever context-based, natural language or reader-friendly texts are to be generated from structured data. Deep writing techniques have also found their way into the arts and literature with the help of models such as ELMo (Embeddings from Language Models), BERT (Bidirectional Encoder Representations from Transformers) or GPT-2/3 (Generative Pre-Training Transformer).

The goal of the seminar is that at the end each student has produced (a) text based on one of the neural language models mentioned above. No matter if poem, prose, novella, essay, manifesto, shopping list or social bot.

The course is intended as a general introduction to programming. It will not only teach skills to generate texts, but also the basics of Python, a universal programming language that can be used to program images, PDFs or web applications. Furthermore, Python is the most widely used language in programming Artificial Intelligences, especially Deep Neural Nets.

We ask for registration at [ground-zero@khm.de](mailto:ground-zero@khm.de) until 20.09.2021. No prior knowledge of programming is required to participate in the basic seminar.

# Course

## Week 1 (31.1. - 4.2.)

### Hands on Python

[First book](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/books_1.ipynb)

[Python: Variables](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_variables.ipynb)

[Python: Loops & Lists](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_loops_lists.ipynb)

[Programmed books 2](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/books_2.ipynb)

[Python: Booleans, If - Else, While-loop](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_booleans_conditionals.ipynb)

[Python: Strings, Files, Try & Except](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_strings_files_try.ipynb)

[Programmed books 3](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/books_3.ipynb)

[Python: Functions](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_functions.ipynb)

[Python: Modules](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_modules_pypi.ipynb)

[Programmed books 4](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/books_4.ipynb)

[Python: Tuples, Dictionaries, Set](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_tuples_dictionaries_set.ipynb)

[Python: Class / OOP](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_class.ipynb)

---

## Week 2 (7.2. - 11.2.)

### Monday

#### Hands on Text as Data

[0-order text generation]() < random word generation, wiederholung von Char, String and List 

[Data cleaning and Parsing]() < python method for parsing text as data

[Text analysing]() < how computer understanding text, basic priciple of NLP

[1-order text generation and Probability]() < probability calculation

### Tuesday 

#### Hands on Markov Chain

[Markov Chain - Background and knowledge]() < basic knowledge of Markov chain

[Character based Markov Chain]() < Character based Markov chain, second order text generation.

[N-Order text generation]() < N-Order text generation.

[Markov Chain - OOP]() < Markov Chain based on object oriented programming.

[extented knowledge - word based Markov chain]()

### Wednesday 

#### morning < Artificial Neural Networks presentation

* a basic introduction in ANN's (the most simple with only one hidden layer)
  * [ANN-in-Keras.ipynb]() + little presentation-slide o.ä. 
* going step by step over it with Copilot (just as a presentation...)
  * [Keras-ANN-with-Copilot.py]()
* after that - short what is an RNN in comparsion to ANN...

#### afternoon < Hands on Pytorch, (maybe Huggingface) & GPT-2/3, bzw. Transformers

* general presentation about gpt, AI Dungeon, Transformers, Pytorch etc.
* preparing your dataset for gpt-2
* setting up environment for next day

#### alternativ< Hands on RNN/LSTM's??

* [Text generation with LSTM]() < notebook

### Thursday

#### Hands on GPT-2/3

* [aitextgen]() ??
* [gpt-2 with huggingface]() ??

### Friday

* finetuning 
* überarbeitung der eigenen generierten texte 
* rendern eines eigenen buches...



---

### General Info 

**Executing the Notebooks:**

- *You can run, execute and work on the following Notebooks here:* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/experimental-informatics/how-to-make-human-machine-readable/HEAD)

**Folder in KHM-Cloud:**

- *[??Here??](https://wolke.khm.de/LINK?) you can find some material for the seminar*

---

#### Anaconda & Jupyter Notebooks

##### Hands on Jupyter Notebooks

* [little-helpers-in-jupyter-notebooks.ipynb](https://github.com/experimental-informatics/hands-on-python/blob/master/little-helpers-in-jupyter-notebooks.ipynb) < Introduction to Jupyter Notebooks (general info, Installation & Help-Functions)

##### Hands on **Markdown**

* Jupyter-Notebook: [Markdown-basics.ipynb](https://github.com/experimental-informatics/hands-on-python/blob/master/Markdown-basics.ipynb)

---

#### Datasets

* [scraper_wikipedia.ipynb](https://github.com/experimental-informatics/hands-on-text-generators/blob/master/scraper_wikipedia.ipynb) < extract text of specific wikipedia articles
* [scrape-load_textcorpora.ipynb](https://github.com/experimental-informatics/hands-on-text-generators/blob/master/scrape-load_textcorpora.ipynb) < some basic examples and code-snippets to srape, load and walk through datasets
* [dataset-list.md](https://github.com/experimental-informatics/hands-on-text-generators/blob/master/dataset-list.md) < just some resources of datasets & archives

---
#### Cheat Sheets

| Title                       | URL                                                          |
| --------------------------- | ------------------------------------------------------------ |
| Python Beginner Cheat Sheet | https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf |
| Markdown Syntax             | https://help.github.com/articles/basic-writing-and-formatting-syntax/ |
| Jupyter Notebook            | https://cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/pdf_bw/ |
| Conda                       | https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf |

---

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/experimental-informatics/how-to-make-human-machine-readable/HEAD)
