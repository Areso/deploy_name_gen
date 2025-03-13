import random

adjs = ["red","orange","yellow",
        "green","blue","violet",
        "black","gold","white",
        "silver","purple","pink",
        "brown","grey","teal",
        "amber","cyan","azure",
        "coral","dark","lazy","fast",
        "slow","bald","fancy","plain",
        "plump","skinny","brave",
        "calm","eager","gentle","happy",
        "jolly","kind","lively","nice",
        "polite","proud","silly","witty",
        "angry","clumsy","fierce",
        "itchy","scary","big","great",
        "huge","large","little","puny",
        "short","small","tiny","wicked",
        "rich","poor","new","old","strange",
        "rocky","grumpy","devoted","smart",
        "safe","unsafe","sleepy","tardy",
        "hungry","royal","round","mild",
        "rude","thin","thick","oval",
        "hot","modern","petite","weary",
        "lucky","sad","quick","swift",
        "tough","dizzy","bumpy","sober",
        "zany","brisk","quiet","rough",
        "sharp","dull","neat","snug","sly",
        "loyal","canny","chic","icy","wry",
        "giddy","fussy","bold","agile"]
nouns= ["fox","wolf","hare","mouse",
        "llama","planet","sun","dog",
        "cat","eagle","hawk",
        "lizard","wombat","sheep",
        "sloth","racoon","lynx",
        "lemur","whale","cow",
        "tiger","turtle","frog",
        "jackal","goose","cobra",
        "deer","koala","bison","owl",
        "mule","rat","lion","bear",
        "crow","emu","crab","dodo",
        "zebra","bull","duck",
        "vulture","elk","snake",
        "horse","panther","monkey",
        "camel","possum","otter",
        "boar","goat","gecko",
        "eel","carp","pike","shark",
        "tuna","salmon","dove","stork"]

def genname():
    theadj = random.choices(adjs)[0]
    thenoun= random.choices(nouns)[0]
    if len(theadj+thenoun)>8:
        return genname()
    idx    = str(random.randint(1,99))
    if len(idx)==1:
        idx  = "0"+idx
    fullname = f"{theadj}-{thenoun}-{idx}"
    print(fullname)
    return fullname

if __name__ == "__main__":
    genname()
