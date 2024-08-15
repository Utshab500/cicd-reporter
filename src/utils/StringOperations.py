import re

class StringOperations:
    def __init__(self):
        pass

    def makeBoldHero(self, heroList):
        for i in range(0, len(heroList)):
            heroList[i] = re.sub(r"\*\*(?=\w)", "<b>", heroList[i])
            heroList[i] = re.sub(r"\*\*(?!\w)", "</b>", heroList[i])
        return heroList

    def findLineHero(self, msg):
        # regexPattern = r"\*\*.+\*\*(?=\s*\w)"
        regexPattern = r"\*\*.+\*\*(?=[ \t\f]*\w)"
        matches = re.findall(regexPattern, msg)
        return matches

    def replaceInMessage(self, msg, originalList, replaceableList):
        for i in range(0, len(originalList)):
            regexPattern = re.escape(originalList[i])
            msg = re.sub(regexPattern, replaceableList[i], msg)
        return(msg)

    # def addLineBreaks(self, msg):
    #     # regexPattern = r"(\* \*{2}|\*{2})(\w+[ \t\f\/\+\(/)\:\*\`\',\.\-\"]*)*"
    #     regexPattern = r"^(((\* \*{2}|\*{2})(([\(\']\w+|\w+|\w+[\),\'\.\+]|[\(\']\w+[\)\'])[ \t\f\/\:\-])*\*{2}[ \t\f]{1,2})|(\*[ \t\f]))(([\(\']\w+|(\w+|\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z)|(\w+|\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z)[\),\'\.\+][,\.]?|[\(\'\`\*\"][\*]?\w+[\*]?[\)\'\`\*\"]\.?|[\'\`]?\w+[\'\-\/]\w+[\'\`]?|\'?\d+-\d+-\d+\'?)[ \t\f\n])+"
    #     regexPattern = re.compile(regexPattern, re.MULTILINE)
    #     matches = re.finditer(regexPattern, msg)
    #     match = [x.group() for x in matches]
    #     matchWithLineBreak = [x+"<br />" for x in match]
    #     msg = self.replaceInMessage(msg, match, matchWithLineBreak)
    #     return msg