info = """
disclaimer: I am not resposible for illegal use of this product.
this program is ment for educational purpouses only.
what you do with this program is solely your responsibility.
version: 0.0.4
welcome to the key direct text encryption system
"""
print(info)

#main class
class crypt_translator:
    #class init method
    def __init__(self, key="12345678abc"):
        #import the key to the class and parse it
        self.key = key
        self.col = [self.key[0], self.key[1], self.key[2], self.key[3], self.key[4], self.key[5], self.key[6], self.key[7]]
        self.tables = [self.key[8], self.key[9], self.key[10]]
        #translation dict variable
        self.translation = {
            "a":"{}{}1".format(self.tables[0],self.col[0]),
            "e":"{}{}1".format(self.tables[0],self.col[1]),
            "i":"{}{}1".format(self.tables[0],self.col[2]),
            "o":"{}{}2".format(self.tables[0],self.col[0]),
            "u":"{}{}2".format(self.tables[0],self.col[1]),
            "y":"{}{}2".format(self.tables[0],self.col[2]),
            "b":"{}{}1".format(self.tables[1],self.col[0]),
            "c":"{}{}1".format(self.tables[1],self.col[1]),
            "d":"{}{}1".format(self.tables[1],self.col[2]),
            "f":"{}{}1".format(self.tables[1],self.col[3]),
            "g":"{}{}1".format(self.tables[1],self.col[4]),
            "h":"{}{}2".format(self.tables[1],self.col[0]),
            "j":"{}{}2".format(self.tables[1],self.col[1]),
            "k":"{}{}2".format(self.tables[1],self.col[2]),
            "l":"{}{}2".format(self.tables[1],self.col[3]),
            "m":"{}{}2".format(self.tables[1],self.col[4]),
            "n":"{}{}3".format(self.tables[1],self.col[0]),
            "p":"{}{}3".format(self.tables[1],self.col[1]),
            "q":"{}{}3".format(self.tables[1],self.col[2]),
            "r":"{}{}3".format(self.tables[1],self.col[3]),
            "s":"{}{}3".format(self.tables[1],self.col[4]),
            "t":"{}{}4".format(self.tables[1],self.col[0]),
            "v":"{}{}4".format(self.tables[1],self.col[1]),
            "w":"{}{}4".format(self.tables[1],self.col[2]),
            "x":"{}{}4".format(self.tables[1],self.col[3]),
            "z":"{}{}4".format(self.tables[1],self.col[4]),
            "~":"{}{}1".format(self.tables[2],self.col[0]),
            "1":"{}{}1".format(self.tables[2],self.col[1]),
            "2":"{}{}1".format(self.tables[2],self.col[2]),
            "3":"{}{}1".format(self.tables[2],self.col[3]),
            "4":"{}{}1".format(self.tables[2],self.col[4]),
            "5":"{}{}1".format(self.tables[2],self.col[5]),
            "6":"{}{}1".format(self.tables[2],self.col[6]),
            "7":"{}{}1".format(self.tables[2],self.col[7]),
            "8":"{}{}2".format(self.tables[2],self.col[0]),
            "9":"{}{}2".format(self.tables[2],self.col[1]),
            "0":"{}{}2".format(self.tables[2],self.col[2]),
            "-":"{}{}2".format(self.tables[2],self.col[3]),
            "_":"{}{}2".format(self.tables[2],self.col[4]),
            "=":"{}{}2".format(self.tables[2],self.col[5]),
            "+":"{}{}2".format(self.tables[2],self.col[6]),
            "[":"{}{}2".format(self.tables[2],self.col[7]),
            "]":"{}{}3".format(self.tables[2],self.col[0]),
            "{":"{}{}3".format(self.tables[2],self.col[1]),
            "}":"{}{}3".format(self.tables[2],self.col[2]),
            "\\":"{}{}3".format(self.tables[2],self.col[3]),
            "|":"{}{}3".format(self.tables[2],self.col[4]),
            ";":"{}{}3".format(self.tables[2],self.col[5]),
            ":":"{}{}3".format(self.tables[2],self.col[6]),
            "\"":"{}{}3".format(self.tables[2],self.col[7]),
            "'":"{}{}4".format(self.tables[2],self.col[0]),
            ",":"{}{}4".format(self.tables[2],self.col[1]),
            ".":"{}{}4".format(self.tables[2],self.col[2]),
            "<":"{}{}4".format(self.tables[2],self.col[3]),
            ">":"{}{}4".format(self.tables[2],self.col[4]),
            "/":"{}{}4".format(self.tables[2],self.col[5]),
            "?":"{}{}4".format(self.tables[2],self.col[6]),
            "`":"{}{}4".format(self.tables[2],self.col[7]),
            "!":"{}{}4".format(self.tables[2],self.col[0]),
            "@":"{}{}5".format(self.tables[2],self.col[1]),
            "#":"{}{}5".format(self.tables[2],self.col[2]),
            "$":"{}{}5".format(self.tables[2],self.col[3]),
            "%":"{}{}5".format(self.tables[2],self.col[4]),
            "^":"{}{}5".format(self.tables[2],self.col[5]),
            "&":"{}{}5".format(self.tables[2],self.col[6]),
            "*":"{}{}5".format(self.tables[2],self.col[7]),
            "(":"{}{}6".format(self.tables[2],self.col[0]),
            ")":"{}{}6".format(self.tables[2],self.col[1]),
            " ":"{}{}6".format(self.tables[2],self.col[2]),
            "°":"{}{}6".format(self.tables[2],self.col[3]),
            "±":"{}{}6".format(self.tables[2],self.col[4]),
            "©":"{}{}6".format(self.tables[2],self.col[5]),
            "®":"{}{}6".format(self.tables[2],self.col[6]),
            "¢":"{}{}6".format(self.tables[2],self.col[7]),
        }
    #encryption method
    def encrypt(self, text="hello world"):
        #set the text o a readable lower case format
        text = text.lower()
        #predefine the output as empty string
        newText = ""
        #parse throughthe old text and using translation var translate it to the new text
        for i in text:
            newText = newText + "{}".format(self.translation[i])
        #return the new text
        return newText
    #decryption method
    def decrypt(self, text="b12a21b42b42a12c36b34a12b43b42b31"):
        #sets text to lowercase
        text = text.lower()
        #predefines the necessary vars
        textCode = []#result predefinition
        tempText = ""#temperary string
        count = 0#counter from 0 - 2 to keep track of where we are
        #parses text and seperates into 3 chars per string sets
        #and adding it to a var textCode that was prdefined
        for i in text:
            if count == 0:
                tempText = i
                count = count +1
            elif count == 1:
                tempText = tempText + i
                count = count +1
            elif count == 2:
                tempText = tempText + i
                textCode.append(tempText)
                count = 0
        #predefines output as empty string
        newText = ""
        #translates each 3 char string into the output
        for i in textCode:
            for k, v in self.translation.items():
                if v == i:
                    newText = newText + k
                    break
        #returns the output
        return newText


class init:
    
    def __init__(self, k):
        self.key = k
        valid = self.testKeyValidity()
        if valid:
            self.c = crypt_translator(self.key)
            self.suc = True
        else:
            self.suc = False
            
    def getSuccess(self):
        return self.suc
    
    def getCryptInstance(self):
        return self.c
    
    def encrypt(self, text):
        return self.c.encrypt(text)
    
    def decrypt(self, text):
        return self.c.decrypt(text)
        
    def testKeyValidity(self):
        ko = ""
        for i in self.key:
            if i not in ko:
                ko = "{}{}".format(ko, i)
        self.key = ko
        ko = None
        l = len(self.key)
        if l == 11:
            l = None
            return True
        else:
            l = None
            return False
