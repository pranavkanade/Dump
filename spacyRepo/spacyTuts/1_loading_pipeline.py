#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:07:36 2017

@author: farzicoder
"""
import spacy
nlp = spacy.load('en') 
doc = nlp(u'Hello, Spacy')