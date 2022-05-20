# importing Flask and other modules
from flask import Flask, request, render_template ,redirect, url_for
from typing import  List


# Flask constructor
app = Flask(__name__)

def format_param(value, param) -> List:
    """
        Returns all query and filter parameters as a list
        """
    result = param[0].split(",")
    return result


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET"])
def flask_test():
    query = request.args.getlist("query")
    if query:
        query = format_param("query" , query)
        if (len(query)>1):
            query_file = query[0]
            filter = query[1][7:].strip("[").strip("]").split("to")
            print("cccccc",filter)
            return render_template(query_file,n = [10,20])
        else:
            query_file = query[0]
            return render_template(query_file)
    return render_template("file1.html")


if __name__ == '__main__':
    app.run()

#http://127.0.0.1:5000/?query=file1.html,filter=[1to10]

