from transformers import pipeline
import multiprocessing

classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")


def grader_keyword(keyword, text):
    """

    :param keyword: Keyword
    :param text: piece of text for content grading
    :return: Bart score for keyword w.r.t text
    """
    dict_ = classifier(text, [keyword])
    return dict_['scores'][0]


def content_grader(keywords, text):
    """

    :param keywords: List of keywords
    :param text: Piece of text
    :return: Dict of bart scores for each keyword
    """
    results = {}
    for keyword in keywords:
        results[keyword] = grader_keyword(keyword, text)

    return results


def grader(dict_, threshold):
    """

    :param dict_: Dict of scores for each keyword
    :param threshold: Threshold value for grading
    :return: kwds matching with content and grades
    """
    gradings = ['E', 'E+', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A+']
    count = 0
    keywords = []
    for key in dict_:
        if (dict_[key] > threshold):
            count += 1
            keywords.append(key)

    return gradings[int(count / 3)], keywords

