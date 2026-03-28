from flask import Flask, request, render_template #this request gets data from the input - sent as post
import requests #sends request to our outlined api link

app = Flask(__name__)

def restaurant_list(postcode): 
    api_link =  f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    
    #without this 403 cloudflare error
    headers = {"User-Agent": "Mozilla/5.0"}

    get_api = requests.get(api_link, headers=headers, timeout=10) #dont wait forever for server

    #if unable to get api data - cause an error and stop the program
    get_api.raise_for_status()
    final_data = get_api.json() #raw data into json

    restaurants = []
    #loop logic to store all information we need to show
    for restaurant in final_data.get("restaurants")[:10]: #only the first 10 restaurant keys        
        cuisines = ""
        for cuisine in restaurant["cuisines"]:
            cuisines+= cuisine.get("name") + ", "
        restaurants.append({
            "name": restaurant["name"],
            "cuisines": cuisines,
            "rating": f'{restaurant["rating"]["starRating"]}({restaurant["rating"]["count"]})',
            "address": f'{restaurant["address"]["firstLine"]}, {restaurant["address"]["postalCode"]}',
            "logo": restaurant["logoUrl"]
        })
    
    return restaurants

@app.route("/", methods=["GET", "POST"])
def home():
    restaurants = []
    error = None
    if request.method == "POST":
        postcode = request.form.get("postcode").strip().replace(" ", "") #if something like abcd 123 it becomes abcd123
        
        #if user tries to enter without typing anything
        if not postcode:
            error = "Please enter a postcode!"
        else:
            try:
                #calling the function above to fill our array
                restaurants = restaurant_list(postcode)
                if not restaurants:
                    error= "No restaurants found for this postcode"

            #anything other than above goes wrong    
            except requests.exceptions.RequestException:
                error="Something went wrong"                

    # bridge between backend and frontend. 
    # first parram =  template file to render.
    # subsequent variables = python variables to Jinja names, 
    return render_template("index.html", restaurants=restaurants, error=error, postcode=postcode)
    
if __name__ == "__main__":
    app.run(debug=True) 