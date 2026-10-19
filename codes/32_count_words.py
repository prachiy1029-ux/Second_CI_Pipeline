def  count_words(sentence):
    sentence = sentence.strip()

    if not sentence:
        return 0

    return len(sentence.split())
