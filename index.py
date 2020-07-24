from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from markupsafe import escape
import random

list_of_numbers_to_highlighte_at_the_end = []
list_of_nums = []
list_of_nums_to_highlight_rn = []


def start():
    global list_of_numbers_to_highlighte_at_the_end
    global list_of_nums
    global list_of_nums_to_highlight_rn

    list_of_numbers_to_highlighte_at_the_end = []
    list_of_nums = []
    list_of_nums_to_highlight_rn = []

    # list_of_nums = []
    for i in range(1, 91):
        list_of_nums.append(i)
    # print(list_of_nums)
    # list_of_numbers_to_highlighte_at_the_end = []

    while len(list_of_nums) != 0:
        number_selected = random.choice(list_of_nums)
        list_of_nums.remove(number_selected)
        list_of_numbers_to_highlighte_at_the_end.append(number_selected)
    print(list_of_numbers_to_highlighte_at_the_end)


start()
app = Flask(__name__)


@app.route('/index')
def index():
    try:
        list_of_nums_to_highlight_rn.append(
            list_of_numbers_to_highlighte_at_the_end[0])
        list_of_numbers_to_highlighte_at_the_end.pop(0)
        return render_template('board.html', list=list_of_nums_to_highlight_rn)
    except:
        list2 = list_of_nums_to_highlight_rn
        start()
        return render_template('board.html', list=["ALL DONE!!"], list2=list2)

# @app.route('/',methods=['POST','GET'])
# def get_input():
#     pp = request.form['Next']
#     print(pp)


@app.route("/housie", methods=["POST", "GET"])
def Num1():
    if request.method == "POST":
        # next = request.form("Next")
        print("::::::::::::::::::::::::::::::::::::::::::::::::")
        return redirect('/index')
        # return render_template("board.html",Num1=Num1())
    else:
        print("NOt CAlledß")
    # c = list_of_numbers_to_highlighte_at_the_end[0]
    # list_of_numbers_to_highlighte_at_the_end.pop(0)
    # return c
