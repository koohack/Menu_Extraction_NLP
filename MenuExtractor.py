# MenuExtractor Class

from pororo import Pororo
from anytree import Node, RenderTree, PreOrderIter, LevelOrderIter

import menu_ex_pororo

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
quantity_dict={
    "하나" : 1,
    "한개" : 1,
    "1" : 1,
    "둘" : 2,
    "두개" : 2,
    "2" : 2,
    "셋" : 3,
    "세개" : 3,
    "3":3,
    "넷" : 4,
    "네개" : 4,
    "4" : 4,
    "다섯" : 5,
    "5" : 5,
    "여섯" : 6,
    "6" : 6,
    "일곱" : 7,
    "7" : 7,
    "여덟" : 8,
    "8" : 8,
    "아홉" : 9,
    "9" : 9,
    "열개" : 10,
    "10" : 10,
    


}

def get_tree(dlist):
    node_list=[]
    node_list.append(Node("dummy"))
    root = None
    for d in dlist:
        cur_node = d[0]
        parent_node = d[2]
        if parent_node == -1:
            root = cur_node
        value = d[1]
        node_list.append(Node(value))

    for d in dlist:
#        print(d[2])
        cur_node = d[0]
        parent_node = d[2]
        if parent_node != -1:
            node_list[cur_node].parent = node_list[parent_node]
    return node_list[root]

def get_all_children(node,child_list):

    for c in node.children:
        child_list.append(c.name)
        get_all_children(c,child_list)
    return child_list


class MenuExtractor():
    def __init__(self):
        self.dp = Pororo(task="dep_parse", lang="ko")
        self.pos = Pororo(task="pos", lang="ko")
        self.quant = ["하나","두개","세개","네개","다섯개","여섯개","일곱개","여덟개","아홉개","열개"]
        
    def delexicalize_text(self,text,replacer_del):
        text_split = text.split(" ")
        no_space = []
        for tok in text_split:
            for rep in replacer_del:
                tok=tok.replace(rep[1],rep[0])
            no_space.append(tok)
        for i,tok in enumerate(no_space):
            toks = "".join(no_space[i:i+2])
            for rep in replacer_del:
                if rep[1] in toks:
                    toks=toks.replace(rep[1],rep[0])
                    no_space[i]=toks
                    try:
                        no_space[i+1]=""
                    except:
                        pass
                    
        for i,tok in enumerate(no_space):
            toks = "".join(no_space[i:i+3])
            for rep in replacer_del:
                if rep[1] in toks:
                    toks=toks.replace(rep[1],rep[0])
                    no_space[i]=toks
                    try:
                        no_space[i+1]=""
                    except:
                        pass
                    try:
                        no_space[i+2]=""
                    except:
                        pass
                    
        for i,tok in enumerate(no_space):
            for q in self.quant:
                if q in tok:
                    no_space[i]=no_space[i].replace(q+" ",q+", ")

        no_space[-1] = no_space[-1].replace(",","")
                    
        return " ".join(no_space).replace("  "," ").replace(",,",",")
            
    def get_menu_dict(self,node):
        ret_dict={}
        for c in node.children:
            subtree_list=[]
            subtree_list=get_all_children(c,subtree_list)
            subtree_list.append(c.name)
            alps = []
            quantities=[]
            options=[]
            for word in subtree_list:
                flag = False
                for alp in alphabet_list:
                    if alp in word:
                        alps.append(alp)
                        flag=True
                for key in quantity_dict.keys():
                    if key in word:
                        quantities.append(quantity_dict[key])
                        flag=True
                if not flag:
                    pos_list = self.pos(word)
                    nouns=[]
                    for p in pos_list:
                        print(p[1][0])
                        if p[1][0]=="N":
                            nouns.append(p[0])
                    options="".join(nouns)
            for alp in alps:
                ret_dict[alp]={}
                if quantities:
                    ret_dict[alp]["quantity"]=quantities[0] # 일단은 겹치면 첫 숫자를 씀.
                else:
                    ret_dict[alp]["quantity"]=1
                if options:
                    ret_dict[alp]["options"]=options
        return ret_dict
                
        
    def extract(self,text,menu):
        string, token, replacer, replacer_del =menu_ex_pororo.ExtractMenu(text, menu)
        delex_text=self.delexicalize_text(text,replacer_del)
#         print(string, token, replacer, replacer_del)
#         print(delex_text)
        dlist=self.dp(delex_text)
        root=get_tree(dlist)
        ret_dict = self.get_menu_dict(root)
        for key in ret_dict.keys():
            for r in replacer:
                if r[0]==key:
                    ret_dict[key]["menu_name"]=r[1]
#         print(ret_dict)
        
#         for pre, fill, node in RenderTree(root):
#             print("%s%s" % (pre, node.name))

#         for d in dlist:
#             print(d)
        
        return ret_dict
        
        
        
if __name__=="__main__":
    me = MenuExtractor()
    menu=["빅맥세트","맥플러리","슈니언 버거","치킨너겟", "후렌치후라이","콜라"]
    text="빈맥세트 하나 라지세트로, 콜라, 후렌치 후라이 라지로 두개씩, 그리고 맥플라리 초코맛 추가"
    me.extract(text,menu)

        
        
        
        
        
        
        