from flask import Flask, render_template, request, redirect

from bot import *

app = Flask(__name__)


def func():
    bot.run(token)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/apply", methods=["GET", "POST"])
def apply():
    if request.method == "POST":
        req = request.form
        nickname = req["nickname"]
        contact = req["contact"]
        select = req["select"]
        osebe = req["osebe"]
        print(nickname, contact, select, osebe)
        data = "Ник: " + nickname + "\nКонтакт: " + contact + "\nИздание: " + select + "\nО себе: \n" + osebe

        with open("json/data.json", "w") as write:
            json.dump(data, write)
        with open("json/nicknames.json", "w") as write:
            json.dump(nickname, write)

        Process(target=func).start()

        return redirect(request.url)
    return render_template("apply.html")


if __name__ == '__main__':
    app.run(debug=True)
