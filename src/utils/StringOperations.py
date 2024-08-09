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
        regexPattern = r"\*\*.+\*\*(?=\s*\w)"
        matches = re.findall(regexPattern, msg)
        return matches

    def replaceInMessage(self, msg, originalList, replaceableList):
        for i in range(0, len(originalList)):
            regexPattern = re.escape(originalList[i])
            msg = re.sub(regexPattern, replaceableList[i], msg)
        return(msg)

    def addLineBreaks(self, msg):
        regexPattern = r"\*\*.+\*\*((\s+\d+-\d+-\d+)|(\s+[\(\`\']{0,1}((\d+-\d+-\d+)|\w+\'\w+|\w+)[\)\`\']{0,1}[.,!?]*)+)"
        matches = re.finditer(regexPattern, msg)
        match = [x.group() for x in matches]
        matchWithLineBreak = [x+"<br />" for x in match]
        msg = self.replaceInMessage(msg, match, matchWithLineBreak)
        return msg