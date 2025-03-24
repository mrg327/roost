from flask import Flask, render_template

app = Flask(__name__)

TITLE = "Roost App"

TEST_TASK_ITEMS = {
    "task1": {
        "sub1": "",
        "sub2": "",
        "sub3": "",
    },
    "task2": {
        "sub1": "",
        "sub2": "",
    },
    "task3": {
        "sub1": "",
    },
    "task4": {
        "sub1": "",
    },
    "task5": {
        "sub1": "",
    },
}


@app.route("/")
def index():
    return render_template("index.html", title=TITLE, task_items=TEST_TASK_ITEMS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
