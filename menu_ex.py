from jamo import h2j, j2hcj
import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt

def DicKor2En():
    ### Preprocessing korean to english
    ja_kor=['ㄱ', 'ㄲ', 'ㅋ', 'ㄷ', 'ㄸ', 'ㅌ', 'ㅂ', 'ㅃ', 'ㅍ', 'ㅈ',
            'ㅉ', 'ㅊ', 'ㅅ', 'ㅆ', 'ㅎ', 'ㅁ', 'ㄴ', 'ㅇ', 'ㄹ',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    mo_kor=['ㅏ', 'ㅓ', 'ㅗ', 'ㅜ', 'ㅡ', 'ㅣ', 'ㅐ', 'ㅔ', 'ㅚ', 'ㅑ',
            'ㅕ', 'ㅛ', 'ㅠ', 'ㅒ', 'ㅖ', 'ㅘ', 'ㅙ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ']
    under_kor=['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅎ',
               'ㄲ', 'ㅆ', 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ']
    ja_en=['g', 'gg', 'k', 'd', 'dd', 't', 'b', 'bb', 'p', 'j', 'jj',
           'ch', 's', 'ss', 'h', 'm', 'n', 'ng', 'r',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    mo_en=['a', 'eo', 'o', 'u', 'eu', 'i', 'ae', 'e', 'oe', 'ya', 'yeo',
           'yo', 'yu', 'yae', 'ye', 'wa', 'wae', 'wo', 'we', 'wi', 'ui']
    under_en=['g', 'n', 'd', 'r', 'm', 'b', 's', 'ng', 'j', 'ch', 'k', 't', 'h',
              'gg', 'ss', 'gs', 'nj', 'nh', 'rg', 'nh', 'rg', 'rm', 'rs', 'rt', 'rp', 'rh', 'bs']
    #####################################


    ### Store JaKor2En, MoKor2En, UnderKor2En
    total=[]
    #########################################

    ### Make dictionary (JaKor2En, MoKor2En, UnderKor2En)
    JaKor2En=[]
    for i, item in enumerate(ja_kor):
        temp=[]
        temp.append(item)
        temp.append(ja_en[i])
        JaKor2En.append(temp)
    JaKor2En=dict(JaKor2En)
    total.append(JaKor2En)

    MoKor2En=[]
    for i, item in enumerate(mo_kor):
        temp=[]
        temp.append(item)
        temp.append(mo_en[i])
        MoKor2En.append(temp)
    MoKor2En=dict(MoKor2En)
    total.append(MoKor2En)

    UnderKor2En=[]
    for i, item in enumerate(under_kor):
        temp=[]
        temp.append(item)
        temp.append(under_en[i])
        UnderKor2En.append(temp)
    UnderKor2En=dict(UnderKor2En)
    total.append(UnderKor2En)
    ###########################################

    return total

def SepKor(wordlist):
    ### seperate the word in to 자음 and 모음
    out=[]
    for word in wordlist:
        if word==' ':
            continue
        temp=list(j2hcj(h2j(word)))
        out.append(temp)
    ##########################################

    return out


def Ko2En(word):
    dickor2en=DicKor2En()

    ### change korean word to english
    st=''
    for ch in word:
        length=len(ch)
        for i in range(length):
            st+=dickor2en[i][ch[i]]
        #st+=","
    ##################################
    return st

def Ko2En_List(wordlist):
    out = []
    for i in wordlist:
        sepword = SepKor(i)
        ko2en = Ko2En(sepword)
        out.append(ko2en)
    return out

def Ko2En_Word(word):
    sepword=SepKor(word)
    ko2en=Ko2En(sepword)
    return ko2en

def embedding(words, label):
    ### embedding the word into 2d graph
    c2v_model = chars2vec.load_model('eng_50')
    word_embeddings = c2v_model.vectorize_words(words)
    projection_2d = sklearn.decomposition.PCA(n_components=2).fit_transform(word_embeddings)

    for j in range(len(projection_2d)):
        plt.scatter(projection_2d[j, 0], projection_2d[j, 1],
                    marker=('$' + words[j] + '$'),
                    s=500 * len(words[j]), label=j,
                    facecolors='green' if words[j]
                                          in ['binmaegseteu', 'bigmaegseteu', 'chikinneoges', 'chikinneo'] else 'black')
    #plt.show()
    return word_embeddings
    #return projection_2d

    #######################################

def GetMenu(file):
    words=[]
    line=1
    while True:
        line=file.readline()
        if not line:
            break
        words.append(line[:-1])

    return words
