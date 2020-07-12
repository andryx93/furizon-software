from flask import Flask
from flask import render_template
app = Flask(__name__)


"""
   SUMMARY
      1. ERROR PAGES
         - 404
         - 500
         - 503
      2. MAIN ENTRY POINTS (index, login)
         - / (index)


"""


"""
   1. ERROR PAGES
"""
@app.errorhandler(404)
def error404(e):
   return render_template("404.html"),404

@app.errorhandler(500)
def error500(e):
   return render_template("500.html"),500

@app.errorhandler(503)
def error503(e):
   return render_template("503.html"),503
"""
   --- END ---
"""


"""
   2. MAIN ENTRY POINTS
"""
@app.route('/')
def index():
   name = "Kyrill"
   return render_template("index.html", name=name)


"""
   --- END ---
"""