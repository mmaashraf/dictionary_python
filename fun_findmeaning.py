r"""extract data  from file into an onject"""
"""
we need to import json lib to extract data stored in .json file
load method is used to load the data into an object
"""
import json
from difflib import SequenceMatcher
from difflib import get_close_matches
file=open("data.json")
data=json.load(file)

"""
sequence matching
"""

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


"""fuction to find the meaning of a word"""
def find_word(key):
    key=key.lower()
    try:
         print(data[key])
    except:
        """
        we try to find the best possible match
        """
        data_keys=data.keys()
        lis=get_close_matches(key,data_keys,3,0.8)
        print(lis)
        match=[]
        for j in lis:
            match.append(similar(j,key))
#if max result is empty then no matching key exits
        try:
            choice=input("is    "+lis[match.index(max(match))]+"  this the word .\nenter y for yes and n for no\n")
            if choice.lower()=='y':
                print(data[lis[match.index(max(match))]])
        except:
            print("word does not exist")
#end of function
find_word(input("enter a word\n"))
