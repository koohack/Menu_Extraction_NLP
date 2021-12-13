# Menu_Extraction_NLP
## 1. Requirements
![Generic badge](http://img.shields.io/badge/python-3.8x-yellow.svg) ![Generic badge](http://img.shields.io/badge/konlpy-0.5.2-green.svg) ![Generic badge](http://img.shields.io/badge/nltk-3.6.3-yellowgreen.svg) ![Generic badge](http://img.shields.io/badge/numpy-1.19.x-brightgreen.svg) ![Generic badge](http://img.shields.io/badge/python-3.8x-yellow.svg) 
![Generic badge](http://img.shields.io/badge/jamo-0.4.1-green.svg) ![Generic badge](http://img.shields.io/badge/scikit_learn-1.0-yellowgreen.svg) ![Generic badge](http://img.shields.io/badge/char2vec-0.1.7-brightgreen.svg) ![Generic badge](http://img.shields.io/badge/selenium-4.0.0-yellow.svg)
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
A하나B두개C하나
[('A', 'replacer'), ('하나', 'Noun'), ('B', 'replacer'), ('두', 'Determiner'), ('개', 'Noun'), ('C', 'replacer'), ('하나', 'Noun')]
[('A', '빅맥세트'), ('B', '콜라'), ('C', '후렌치후라이')]
```
###### The string is a collection of tokens excluding the menu extracted from text.
###### The token is the change of the menu extracted from the existing tokenized part to replacer.
###### The replacer is to explain what the extracted menu refers to.

## 3. Menu Extractor Class
### Example of python code
```python
from MenuExtractor import MenuExtractor
me = MenuExtractor()
menu=["빅맥세트","맥플러리","슈니언 버거","치킨너겟", "후렌치후라이","콜라"]
text="빈맥세트 하나 라지세트로, 콜라, 후렌치 후라이 라지로 두개씩, 그리고 맥플라리 초코맛 추가"
result = me.extract(text,menu)
print(result)
```
### Result
```bash
{'A': {'quantity': 1, 'options': '라지세트', 'menu_name': '빅맥세트'}, 'C': {'quantity': 2, 'menu_name': '후렌치후라이'}, 'B': {'quantity': 2, 'menu_name': '콜라'}, 'D': {'options': '초코맛', 'menu_name': '맥플러리'}}
```
## 4. getYogiyo Class
### Example of python code
###### !! before run this code, you need "menu_ex" code !!
###### +You must use chormedriver that fit your chrome browser
```python
import getYogiyoMenu
import time

url="url of yogiyo, extract menus in this page"
yogiyo=getYogiyoMenu.getYogiyo()
menus, menusBlock=yogiyo.getInfo(url)

str="로스까스정식 하나 새우볶음밥 두개"
position=yogiyo.findMenus(str)

yogiyo.clickMenu(position, [1,2])
time.sleep(3)
yogiyo.closeDriver() ### must enter this code
```
## 5. Installing Requirements
#### install the requirements.txt 
pip install -r requirements may not work. In the case, install line by line

#### In case of tensorflow error
```bash
pip install --upgrade tensorflow
```
