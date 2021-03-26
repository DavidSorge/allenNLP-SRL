# **Semantic Role Labeling using AllenNLP**

This script takes sample sentences which can be a single or list of sentences and uses AllenNLP's per-trained model on Semantic Role Labeling to make predictions.

This version is forked from the [original](https://github.com/masrb/allenNLP-SRL). I've applied a few modifications, as noted below.

Modification Plans:

- [x] Fix Text Suite
- [x] Improve allen_srl.py to make it importable for use in other python scripts
  - [x] adjust run() method to make it easier to use a 'list of strings' instead of an input file. Turned out no adjustment was needed.
  - [x] check to make sure CLI functionality is not compromised; i.e. test suite still works.
  - [x] restructure file
  - [x] create `__init.py__` file
  - [x] create `setup.py` file
  - [x] test importability
- [ ] Combine this with code from [this gist](https://gist.github.com/chssch/f788cfd227cb94d0843235a2542026fd) to make SpaCy pipeline object
  - [ ] Download original Gist and include it in the file
  - [ ] Disassemble and reassemble using allen_srl.py

## **Description**

**Semantic Role Labeling (SRL)** recovers the latent predicate argument structure of a sentence, providing representations that answer basic questions about sentence meaning, including “who” did “what” to “whom,” etc. The AllenNLP SRL model is a reimplementation of a deep BiLSTM model (He et al, 2017).

The model used for this script is found at [https://s3-us-west-2.amazonaws.com/allennlp/models/srl-model-2018.05.25.tar.gz]

## **Install prerequisites**

Prerequisites can be installed using pip3 in a `conda` or `venv` virtual environment:

```pip3 install -r requirements.txt```

But there are other options: [https://github.com/allenai/allennlp#installation]

## **Usage**

To run script with SRL model:

on project directory or virtual enviroment

```$python3 allen_srl.py input_file.txt --output_file outputf.txt```

## **Interpreting the result**

AllenNLP uses PropBank Annotation. As a result,each verb sense has numbered arguments e.g., ARG-0, ARG-1,

etc.

ARG-0 is usually PROTO-AGENT

ARG-1 is usually PROTO-PATIENT

ARG-2 is usually benefactive, instrument, attribute

ARG-3 is usually start point, benefactive, instrument, attribute

ARG-4 is usually end point (e.g., for move or push style verbs)

## **License**

AllenNLP is licensed under Apache 2.0
