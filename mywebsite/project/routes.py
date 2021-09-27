from flask import Blueprint, render_template
from mywebsite import data
from mywebsite.project.forms import WordForm
from difflib import get_close_matches
app2 = Blueprint("app2", __name__)


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    # if user entered "nebraska" this will check for "Nebraska" as well.
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:  # in case user enters words like USA or NATO
        return data[word.upper()]
    # elif len(get_close_matches(word, data.keys())) > 0:
    #     yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
    #                get_close_matches(word, data.keys())[0])
    #     if yn == "Y":
    #         return data[get_close_matches(word, data.keys())[0]]
    # elif yn == "N":
    #     return "The word does not exist. Please double Check it."
    else:
        return "We did not understand your entry. "


@app2.route('/', methods=['POST', 'GET'])
def home():
    form = WordForm()
    output = ''
    lst = 'string'
    if form.validate_on_submit():
        output = translate(form.word.data)
    if type(output) == list:
        lst = 'list'

    return render_template('home.html', form=form, output=output, lst=lst)


@app2.route('/about')
def about():
    return render_template('about.html')
