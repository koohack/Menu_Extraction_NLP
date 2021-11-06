# Menu_Extraction_NLP
## 1. Requirements
![Generic badge](http://img.shields.io/badge/python-3.8x-yellow.svg) ![Generic badge](http://img.shields.io/badge/konlpy-0.5.2-green.svg) ![Generic badge](http://img.shields.io/badge/nltk-3.6.3-yellowgreen.svg) ![Generic badge](http://img.shields.io/badge/numpy-1.19.x-brightgreen.svg) ![Generic badge](http://img.shields.io/badge/python-3.8x-yellow.svg) 
![Generic badge](http://img.shields.io/badge/jamo-0.4.1-green.svg) ![Generic badge](http://img.shields.io/badge/scikit_learn-1.0-yellowgreen.svg) ![Generic badge](http://img.shields.io/badge/char2vec-0.1.7-brightgreen.svg)
---
## 2. How to use
### Example of python code
```python
import menu_ex

text="빈맥세트 하나 콜라 두개 후렌치후라이 하나"
menu='''list of the menu'''

string, token, replacer=menu_ex.ExtractMenu(text, menu)

print(string)
print(token)
print(replacer)
```
### Result
```bash
A두개B하나C두개
[('A', 'replacer'), ('두', 'Determiner'), ('개', 'Noun'), ('B', 'replacer'), ('하나', 'Noun'), ('C', 'replacer'), ('두', 'Determiner'), ('개', 'Noun')]
[('A', '치킨너겟'), ('B', '슈니언 버거'), ('C', '빅맥')]
```
###### The string is a collection of tokens excluding the menu extracted from text.
###### The token is the change of the menu extracted from the existing tokenized part to replacer.
###### The replacer is to explain what the extracted menu refers to.
