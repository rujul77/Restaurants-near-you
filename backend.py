from flask import Flask, request, render_template #this request gets data from the input - sent as post
import requests #sends request to our outlined api link
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    restaurants = []
    if request.method == "POST":
        postcode = request.form.get("postcode").strip().replace(" ", "") #if something like abcd 123 it becomes abcd123

        #our api link
        api_link = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"

        #without this - 403 cloudflare error
        headers = {"User-Agent": "Mozilla/5.0"}
    
        #raw data from api stored here
        get_api = requests.get(api_link, headers=headers)
        finalData = get_api.json() #turn into json format

        #get resturant keys from json data, if not found, return empty list. get the first 10
        restaurants = finalData.get("restaurants", [])[:10]

    return render_template("index.html", restaurants=restaurants)
    
if __name__ == "__main__":
    app.run(debug=True) 