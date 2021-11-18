import json
import time
from datetime import datetime
from flask import Flask, Response, request, render_template
import urllib.request

application = Flask(__name__)


@application.route('/',methods = ["GET","POST"])
def index():
    print(str(request.headers))
    if request.method == "POST":
        currencypair = request.form.get("currencypair")
        hist_values = request.form.get("hist_values")
        return render_template('EG.html',currencypair = currencypair, hist_values = hist_values)
    else:
        return render_template('EG.html',currencypair = "BTC-USD", hist_values = 20)

@application.route('/chart-data')
def chart_data():    
    currencypair = request.args.get('currency') 
    def generate_random_data(currencypair):
        
        while True:
             
            url = "https://www.cryptingup.com/api/markets"
            response = urllib.request.urlopen(url)
            data = response.read()  
            btc_dict = json.loads(data)
            btc_dict = btc_dict["markets"]
            val = [x for x in btc_dict if x["symbol"]==currencypair]
            curr_price = val[0]["price"]
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': curr_price})
            yield f"data:{json_data}\n\n"
            time.sleep(5)

    return Response(generate_random_data(currencypair), mimetype='text/event-stream')

    

if __name__ == '__main__':
    application.run(debug=False)
