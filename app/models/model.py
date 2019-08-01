
# def whatToPackMen(city) :  
#     whatToPackMen= {
#     "NewYorkCity": "4 t-shirts, 1 polo/button up shirt, 1 pair of pants, 2 shorts, 1 light-weight sweater, 1 rain jacket, sandals and sneakers."
#     "HongKong": "1-2 pairs of pants, 2 polos/button up shirts, 1 light-weight sweater, 4 t-shirt/tank top, socks, sneakers and socks. TEEN CHOICE ADDITION: Decorative dusk mask.",
#     "Madrid": "4 tanks, 2 t-shirts, 1 bikini(optional), 3 shorts/skirts, 1 pair of sunglasses.",
#     "Chicago":"sneakers, 3 t-shirt, 1 polo/button up shirt, sandals, 2 shorts, 1 light-weight sweater,1 swimsuit",
# }

        
def whatToPack(city, genda):
    if city == "NewYorkCity":
        if genda == "Men": 
            return{"desc": "4 t-shirts, 1 polo/button up shirt, 1 pair of pants, 2 shorts, 1 light-weight sweater and 1 rain jacket"}
        elif genda == "Women":
            return{"desc": "4 t-shirts, 2 blouses, 1 pair of pants, 2 shorts, 2 dresses, 1 light-weight sweater, 1 rain jacket, sandals and sneakers."}
        elif genda == "Other":
            return{"desc":"4 t-shirts, 1 pair of pants, 2 shorts, 1 light-weight sweater, 1 rain jacket, sandals and sneakers."}
    elif city == "HongKong":
        if genda == "Men":
            return{"desc": "1-2 pairs of pants, 2 polos/button up shirts, 1 light-weight sweater, 4 t-shirt/tank top, socks, sneakers and socks. TEEN CHOICE ADDITION: Decorative dusk mask."}
        elif genda == "Women":
            return{"desc": "1-2 pairs of pants, 2 blouses, 1 light-weight sweater, 2 t-shirt/tank tops, 2 dresses, socks, sneakers and socks. TEEN CHOICE ADDITION: Decorative dusk mask.",}
        elif genda == "Other":
            return{"desc":"1-2 pairs of pants, 1 light-weight sweater, 2 t-shirts, socks, sneakers and socks. TEEN CHOICE ADDITION: Decorative dusk mask."}
    elif city == "Chicago":
        if genda == "Men":
            return{"desc": "sneakers, 3 t-shirt, 1 polo/button up shirt, sandals, 2 shorts, 1 light-weight sweater,1 swimsuit"}
        elif genda == "Women":
            return{"desc": "sneakers, 3 t-shirt, 1 blouse, 2 dresses, sandals, 2 shorts, 1 light-weight sweater, 1 swimsuit"}
        elif genda == "Other":
            return{"desc":"sneakers, 3 t-shirt,sandals, 2 shorts, 1 light-weight sweater, 1 swimsuit"}
    elif city == "Madrid":
        if genda == "Men":
            return{"desc":"4 tank-tops, 2 t-shirts, 1 swimsuit (optional), 3 shorts/skirts, 1 pair of sunglasses."}
        elif genda == "Women":
            return{"desc":"4 tank-tops, 2 t-shirts, 1 dress, 1 swimsuit(optional), 3 shorts/skirts, 1 pair of sunglasses."}
        elif genda == "Other":
            return{"desc":"4 tank-tops, 2 t-shirts, 1 swimsuit(optional), 3 shorts, 1 pair of sunglasses."}