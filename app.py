from flask import Flask, render_template, request
import utils.moviedb as db

# To my knowledge, when we import moviedb we will be running the connection calls

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def root():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        year = request.form["year"]
        genre = request.form["genre"]
        titleList = []
        for movie in db.by_year_genre( year, genre ):
            titleList.append( movie["title"] )
        return render_template( "index.html", titles = titleList )


if __name__=="__main__":
    app.debug=True
    app.run()
