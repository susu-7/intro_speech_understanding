import bs4
from gtts import gTTS

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.
    
    @params: 
    text (string): the text of a webpage
    
    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    soup = bs4.BeautifulSoup(text, 'html.parser')
    articles = soup.find_all('article')
    stories = []
    
    for article in articles:
        title_tag = article.find('h3', class_='title')
        teaser_tag = article.find('p', class_='teaser')
        title = title_tag.get_text(strip=True) if title_tag else ''
        teaser = teaser_tag.get_text(strip=True) if teaser_tag else ''
        stories.append((title, teaser))
    
    return stories

def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.
    
    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
    if n < 0 or n >= len(stories):
        raise IndexError("Story index out of range")
    
    title, teaser = stories[n]
    text = f"Title: {title}\nTeaser: {teaser}"
    
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
