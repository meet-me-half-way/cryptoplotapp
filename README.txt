The app uses an SSE to obtain data from the api "https://www.cryptingup.com/api/markets"
and display on a chart.js plot. 

The app displays the BTC-USD exchange rate for the last 100s by default but it also allows 
for the user to enter the curreny for which they want to see the exhange rate and how many 
points they want to see at once. This data is enetered using a form on HTML passed to the
SSE using the request URL. This is then used to modify the data displayed accordingly. 
       