from monkeylearn import MonkeyLearn

api_key = open("api_key.txt", "r+")
ml = MonkeyLearn(api_key.read())

data = ['There\'s no mention on how to fix Error 1009 on the internet. How do I fix error 1009 and what is it\'s exact meaning?!!. The device is a Samsung A520W on Oreao and it was rooted but then I unrooted it and I still get the error. Google play is set to Canada. I have been to the community forums and even they don\'t know what is causing the 1009 error. With all due respect you are the developer of this app obviously you must know what causes error 1009. Is it a time out error? A mismatch error ?', 'This product has made my life so much easier!']


def sentiment(data):
    response = ml.classifiers.classify('cl_TWmMTdgQ', data)
    print(response.body)


def insights(data):
    response = ml.extractors.extract('ex_EjosnyKK', data)
    all_insights = response.body[0]['extractions']

    keywords = []
    relevances = []
    context = []

    for i in range(len(all_insights)):
        keywords.append(all_insights[i]['extractions'][0]['parsed_value'])
        relevances.append(all_insights[i]['extractions'][0]['relevance'])
        context.append(all_insights[i]['extractions'][1]['parsed_value'])

        print(keywords[i], relevances[i], context[i])


insights(data)
