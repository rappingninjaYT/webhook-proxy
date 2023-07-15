import requests
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='template_files', static_folder='static_files')

@app.route('/')
def home():
  #return 'no lurking tit sucking big black cock having niggers allowed here!!'
  return render_template('index.html')

@app.route('/api/webhooks/<data1>/<data2>', methods=['GET', 'POST'])
def index(data1, data2):
  if request.method == 'POST':
    if request.get_json() is None:
      return 'Error, no json data found'
    else:
        webhook = 'https://discord.com/api/webhooks/'+data1+'/'+data2
        print(request.get_json())
        data = request.get_json()
        return requests.post(webhook, json=data)
  return 'Error, get methods cannot be used here'

'''if __name__ == '__main__':
  app.run()'''