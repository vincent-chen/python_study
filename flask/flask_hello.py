from  flask import Flask
app=Flask(__name__)

@app.route('/')
def home_page():
  return "data of home page"

@app.route('/books')
def books():
  return "all books list"

@app.route('/book/<string:book_id>')
def book(book_id):
  return "return data of  a book:{}".format(book_id)

if __name__=="__main__":
  app.run(host='172.27.0.4')

