"""
Counts the number of individual words in a string. 
For added complexity read these strings in from a text file and generate a summary.
"""

def words_count(path):
    file = open(path)
    filecontent = file.read()
    content_list = []
    
    [content_list.append(word) for word in filecontent.split(' ') if word not in content_list]
    file.close()
    return(content_list)
