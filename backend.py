from flask import Flask, request, render_template #this request gets data from the input - sent as post
import requests #sends request to our outlined api link
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    restaurants = []
    error = None
    if request.method == "POST":
        postcode = request.form.get("postcode").strip().replace(" ", "") #if something like abcd 123 it becomes abcd123

        if not postcode:
            error = "Please enter a postcode!"
        
        else:
            #our api link
            api_link = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
            #without this - 403 cloudflare error
            headers = {"User-Agent": "Mozilla/5.0"}

            try:
                #raw data from api stored here
                get_api = requests.get(api_link, headers=headers)
                finalData = get_api.json() #turn into json format
                unfiltered_restaurant = finalData.get("restaurants", [])[:10]
                
                #if there are no restaurants found in the list[]
                if not unfiltered_restaurant:
                    error = "No restaurants found for that postcode!"
                else:

                    #loop through the list, and append what i need to restaurants[]
                    for restaurant in unfiltered_restaurant:
                        cuisines = ", ".join(cuisine["name"] for cuisine in restaurant["cuisines"])
                        restaurants.append({
                            "name":restaurant["name"],
                            
                            "cuisines": cuisines,

                            "address": f'{restaurant["address"]["firstLine"]}, {restaurant["address"]["postalCode"]}',

                            "rating": f'{restaurant["rating"]["starRating"]}({restaurant["rating"]["count"]})',

                            "logo": restaurant["logoUrl"]
                        })
            
            #anything other than above goes wrong    
            except:
                error = "Something went wrong!"
        
    return render_template("index.html", restaurants=restaurants, error=error)
    
if __name__ == "__main__":
    app.run(debug=True) 