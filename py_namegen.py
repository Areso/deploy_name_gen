import random
import argparse

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
        "giddy","fussy","bold","agile","wise",
        "daring","magic","honest"]
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


def genname(max_obj_len=8,digits=2,separator="-")->str:
    """
    Generates a random name in the format:
    adjective-noun-XX, XX is two digits number

    Parameters:
        digits (int): Number of digits to use for the suffix, def is 2
        max_obj_len (int): Max len of adj-noun combination (exc. separator), def is 8
        separator (str): Separator between Adj,noun and digits, def is "-" 
    """
    while True:
        the_adj  = random.choice(adjs)
        the_noun = random.choice(nouns)
        if len(the_adj + the_noun) <= max_obj_len:
            break
    max_number = 10**digits-1
    idx    = str(random.randint(1,max_number))
    if len(idx)<digits:
        idx  = "0"+idx
    fullname = f"{the_adj}{separator}{the_noun}{separator}{idx}"
    print(fullname)
    return fullname


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l","--max_obj_len", 
                        help="max object len except for separator",
                        default=8, type=int)
    parser.add_argument("-d","--digits", help="len of digits in suffix",
                        default=2, type=int)
    parser.add_argument("-s","--separator", 
                        help="separator to divide words and digital suffix",
                        default="-",type=str)
    args = parser.parse_args()
    genname(max_obj_len=args.max_obj_len,
            digits=args.digits,
            separator=args.separator)
