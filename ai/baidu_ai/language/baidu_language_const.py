# coding=utf-8
from common.constant_base import ConstantBase


# 百度自然语言处理词性常量
class PosTagConstant(object):
    # Ag    形语素	g	语素	    ns	地名	    u	助词
    # a     形容词	h	前接成分	nt	机构团体	vg	动语素
    # ad	副形词	i	成语	    nz	其他专名	v	动词
    # an	名形词	j	简称略语	o	拟声词	    vd	副动词
    # b	    区别词	k	后接成分	p	介词	    vn	名动词
    # c	    连词	l	习用语	    q	量词	    w	标点符号
    # dg	副语素	m	数词	    r	代词	    x	非语素字
    # d	    副词	Ng	名语素	    s	处所词	    y	语气词
    # e	    叹词	n	名词	    tg	时语素	    z	状态词
    # f	    方位词	nr	人名	    t	时间词	    un	未知词
    post = "Ag,g,ns,u,a,h,nt,vg,ad,i," \
           "nz,v,an,j,o,vd,b,k,p,vn,c,l,q,w,dg,m,r,x,d,Ng,s,y,e,n,tg,z,f,nr,t,un"
    __const = ConstantBase(post)

    # 暴露的常量
    vars = locals()
    for key in __const.__dict__:
        vars[key] = __const.__dict__[key]


class DepRelConstant(object):
    # 1.定中关系ATT
    # 定中关系就是定语和中心词之间的关系，定语对中心词起修饰或限制作用。
    # 如：工人/n师傅/n（工人/n ← 师傅/n）。
    #
    # 2. 数量关系QUN（quantity）
    # 数量关系是指量词或名词同前面的数词之间的关系，该关系中，数词作修饰成分，依存于量词或名词。
    # 如：三/m天/q（三/m ← 天/q）。
    #
    # 3.并列关系COO（coordinate）
    # 并列关系是指两个相同类型的词并列在一起。
    # 如：奔腾/v咆哮/v的怒江激流（奔腾/v → 咆哮/v）。
    #
    # 4.同位关系APP（appositive）
    # 同位语是指所指相同、句法功能也相同的两个并列的词或词组。
    # 如：我们大家 （我们 → 大家）。
    #
    # 5.附加关系ADJ（adjunct）
    # 附加关系是一些附属词语对名词等成分的一种补充说明，使意思更加完整，有时候去掉也不影响意思。
    # 如：约/d 二十/m 多/m 米/q 远/a 处/n （二十/m → 多/m，米/q → 远/a）。
    #
    # 6.动宾关系VOB（verb-object）
    # 对于动词和宾语之间的关系我们定义了两个层次，一是句子的谓语动词及其宾语之间的关系，我们定为OBJ，在下面的单句依存关系中说明；二是非谓语动词及其宾语的关系，即VOB。这两种关系在结构上没有区别，只是在语法功能上，OBJ中的两个词充当句子的谓语动词和宾语，VOB中的两个词构成动宾短语，作为句子的其他修饰成分。
    # 如：历时/v 三/m 天/q 三/m夜/q（历时/v → 天/q）。
    #
    # 7.介宾关系POB（preposition-object）
    # 介词和宾语之间的关系，介词的属性同动词相似。
    # 如：距/p球门/n（距/p → 球门/n）。
    #
    # 8.主谓关系SBV（subject-verb）
    # 主谓关系是指名词和动作之间的关系。
    # 如：父亲/n 逝世/v １０/m 周年/q 之际/nd（父亲/n ← 逝世/v）。
    #
    # 9.比拟关系SIM（similarity）
    # 比拟关系是汉语中用于表达比喻的一种修辞结构。
    # 如：炮筒/n 似的/u 望远镜/n（炮筒/n ← 似的/u）。
    #
    # 10.时间关系TMP（temporal）
    # 时间关系定义的是时间状语和其所修饰的中心动词之间的关系。
    # 如：十点以前到公司（以前 ← 到）。
    #
    # 11.处所关系LOC（locative）
    # 处所关系定义的是处所状语和其所修饰的中心动词之间的关系，如：在公园里玩耍（在 ← 玩耍）。
    #
    # 12.“的”字结构DE
    # “的”字结构是指结构助词“的”和其前面的修饰语以及后面的中心词之间的关系。
    # 如：上海/ns 的/u 工人/n（上海/ns ← 的/u，的/u ← 工人/n）。
    #
    # 13.“地”字结构DI
    # “地”字结构在构成上同DE类似，只是在功能上不同，DI通常作状语修饰动词。
    # 如： 方便/a 地/u 告诉/v 计算机/n（方便/a ← 地/u，地/u ← 告诉/v）。
    #
    # 14.“得”字结构DEI
    # 助词“得”同其后的形容词或动词短语等构成“得”字结构，对前面的动词进行补充说明。
    # 如：讲/v 得/u 很/d 对/a（讲/v → 得/u，得/u → 对/a）。
    #
    # 15.“所”字结构SUO
    # “所”字为一结构助词，后接一宾语悬空的动词做“的”字结构的修饰语，“的”字经常被省略，使结构更加简洁。
    # 如：机电/b 产品/n 所/u 占/v 比重/n 稳步/d 上升/v（所/u ← 占/v）。
    #
    # 16.“把”字结构BA
    # 把字句是主谓句的一种，句中谓语一般都是及物动词。
    # 如：我们把豹子打死了（把/p → 豹子/n）。
    #
    # 17.“被”字结构BEI
    # 被字句是被动句，是主语接受动作的句子。
    # 如：豹子被我们打死了（豹子/n ← 被/p）。
    #
    # 18.状中结构ADV（adverbial）
    # 状中结构是谓词性的中心词和其前面的修饰语之间的关系，中心词做谓语时，前面的修饰成分即为句子的状语，中心词多为动词、形容词，修饰语多为副词，介词短语等。
    # 如：连夜/d 安排/v 就位/v（连夜/d ← 安排/v）。
    #
    # 19.动补结构CMP（complement）
    # 补语用于对核心动词的补充说明。
    # 如：做完了作业（做/v → 完）。
    #
    # 20.兼语结构DBL（double）
    # 兼语句一般有两个动词，第二个动词是第一个动作所要表达的目的或产生的结果。
    # 如：[7]曾经/d [8]使/v [9]多少/r [10]旅游/n [11]人/n [12]隔/v [13]岸/n [14]惊叹/v [15]！/wp（使 → 人/n ，/v使/v → 惊叹/v）。
    #
    # 21.关联词CNJ（conjunction）
    # 关联词语是复句的有机部分。
    # 如：只要他请客，我就来。（只要 ← 请 ，就 ← 来）。
    #
    # 22.关联结构 CS(conjunctive structure)
    # 当句子中存在关联结构时，关联词所在的两个句子（或者两个部分）之间通过各部分的核心词发生依存关系CS。
    # 如：只要他请客，我就来。（请 ← 来）。
    #
    # 23.语态结构MT（mood-tense）
    # 汉语中，经常用一些助词表达句子的时态和语气，这些助词分语气助词，如：吧，啊，呢等；还有时态助词，如：着，了，过。
    # 如： [12]答应/v [13]孩子/n [14]们/k [15]的/u [16]要求/n [17]吧/u [18]，/wp [19]他们/r [20]这/r [21]是/v [22]干/v [23]事业/n [24]啊/u [25]！/wp（[12]答应/v ← [17]吧/u，[21]是/v ← [24]啊/u）。
    #
    # 24.连谓结构VV（verb-verb）
    # 连谓结构是同多项谓词性成分连用、这些成分间没有语音停顿、书面标点，也没有关联词语，没有分句间的逻辑关系，且共用一个主语。
    # 如：美国总统来华访问。（来华/v → 访问/v）。
    #
    # 25.核心HED（head）
    # 该核心是指整个句子的核心，一般是句子的核心词和虚拟词（<EOS>或ROOT）的依存关系。
    # 如：这/r 就是/v恩施/ns最/d]便宜/a的/u出租车/n，/wp相当于/v北京/ns的/u “/wp 面的/n ”/wp 。/wp <EOS>/<EOS>（就是/v ← <EOS>/<EOS>）
    #
    # 26.前置宾语FOB（fronting object）
    # 在汉语中，有时将句子的宾语前置，或移置句首，或移置主语和谓语之间，以起强调作用，我认识这个人 ← 这个人我认识。
    # 如：他什么书都读（书/n ← 读/v）。
    #
    # 27.双宾语DOB（double object）
    # 动词后出现两个宾语的句子叫双宾语句，分别是直接宾语和间接宾语。
    # 如：我送她一束花。（送/v → 她/r，送/v → 花/n）。
    #
    # 28.主题TOP（topic）
    # 在表达中，我们经常会先提出一个主题性的内容，然后对其进行阐述说明；而主题部分与后面的说明部分并没有直接的语法关系，主题部分依存于后面的核心成分，且依存关系为TOP。
    # 如：西直门，怎么走？（西直门 ← 走）。
    #
    # 29.独立结构IS（independent structure）
    # 独立成分在句子中不与其他成分产生结构关系，但意义上又是全句所必需的，具有相对独立性的一种成分。
    # 如：事情明摆着，我们能不管吗？
    #
    # 30.独立分句IC（independent clause）
    # 两个单句在结构上彼此独立，都有各自的主语和谓语。
    # 如：我是中国人，我们爱自己的祖国。（是 → 爱）
    #
    # 31.依存分句DC（dependent clause）
    # 两个单句在结构上不是各自独立的，后一个分句的主语在形式上被省略，但不是前一个分句的主语，而是存在于前一个分句的其他成分中，如宾语、主题等成分。规定后一个分句的核心词依存于前一个分句的核心词。该关系同连谓结构的区别是两个谓词是否为同一主语，如为同一主语，则为VV，否则为DC。
    # 如：大家/r叫/v 它/r “/wp 麻木/a 车/n ”/wp ，/wp 听/v起来/v 怪怪的/a 。/wp（叫/v → 听/v）。
    #
    # 32.叠词关系VNV （verb-no-verb or verb-one-verb)
    # 如果叠词被分开了，如“是 不 是”、“看一看”，那么这几个词先合并在一起，然后预存到其他词上，叠词的内部关系定义为：(是1→不；不→是2） 。
    #
    # 33.一个词YGC
    # 当专名或者联绵词等切散后，他们之间本身没有语法关系，应该合起来才是一个词。如：百 度。
    #
    # 34.标点 WP
    # 大部分标点依存于其前面句子的核心词上，依存关系WP。

    """
    #1.定中关系ATT
    #2. 数量关系QUN（quantity）
    #3.并列关系COO（coordinate）
    #4.同位关系APP（appositive）
    #5.附加关系ADJ（adjunct）
    #6.动宾关系VOB（verb-object）
    #7.介宾关系POB（preposition-object）
    #8.主谓关系SBV（subject-verb）
    #9.比拟关系SIM（similarity）
    #10.时间关系TMP（temporal）
    #11.处所关系LOC（locative）
    #12.“的”字结构DE
    #13.“地”字结构DI
    #14.“得”字结构DEI
    #15.“所”字结构SUO
    #16.“把”字结构BA
    #17.“被”字结构BEI
    #18.状中结构ADV（adverbial）
    #19.动补结构CMP（complement）
    #20.兼语结构DBL（double）
    #21.关联词CNJ（conjunction）
    #22.关联结构 CS(conjunctive structure)
    #23.语态结构MT（mood-tense）
    #24.连谓结构VV（verb-verb）
    #25.核心HED（head）
    #26.前置宾语FOB（fronting object）
    #27.双宾语DOB（double object）
    #28.主题TOP（topic）
    #29.独立结构IS（independent structure）
    #30.独立分句IC（independent clause）
    #31.依存分句DC（dependent clause）
    #32.叠词关系VNV （verb-no-verb or verb-one-verb)
    #33.一个词YGC
    #34.标点 WP
    """
    dep_rel = "ATT,QUN,COO,APP,ADJ,VOB,POB,SBV,SIM,TMP,LOC,DE,DI,DEI,SUO," \
              "BA,BEI,ADV,CMP,DBL,CNJ,CS,MT,VV,HED,FOB,DOB,TOP,IS,IC,DC,VNV,YGC,WP"
    __const = ConstantBase(dep_rel)

    # 暴露的常量
    vars = locals()
    for key in __const.__dict__:
        vars[key] = __const.__dict__[key]