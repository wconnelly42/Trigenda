def whatToPack(city, genda):
    if city == "NewYorkCity":
        if genda == "Men": 
            return{"desc": "4 t-shirts, 1 polo/button up shirt, 1 pair of pants, 2 shorts, 1 light-weight sweater and 1 rain jacket", "img" : "http://res.cloudinary.com/simpleview/image/upload/v1518214102/clients/newyorkcity/_EmpireStateBuilding_JulienneSchaer_Manhattan_NYC_055_2a0b62e3-1f5e-4330-9ac3-8f4c7163d09a.jpg"}
        elif genda == "Women":
            return{"desc": "4 t-shirts, 2 blouses, 1 pair of pants, 2 shorts, 2 dresses, 1 light-weight sweater, 1 rain jacket, sandals and sneakers.", "img" : "http://res.cloudinary.com/simpleview/image/upload/v1518214102/clients/newyorkcity/_EmpireStateBuilding_JulienneSchaer_Manhattan_NYC_055_2a0b62e3-1f5e-4330-9ac3-8f4c7163d09a.jpg"}
        elif genda == "Other":
            return{"desc":"4 t-shirts, 1 pair of pants, 2 shorts, 1 light-weight sweater, 1 rain jacket, sandals and sneakers.", "img" : "http://res.cloudinary.com/simpleview/image/upload/v1518214102/clients/newyorkcity/_EmpireStateBuilding_JulienneSchaer_Manhattan_NYC_055_2a0b62e3-1f5e-4330-9ac3-8f4c7163d09a.jpg"}
    elif city == "HongKong":
        if genda == "Men":
            return{"desc": "1-2 pairs of pants, 2 polos/button up shirts, 1 light-weight sweater, 4 t-shirt/tank top, sneakers and socks. TEEN CHOICE ADDITION: Decorative dust mask.", "img" : "https://besthqwallpapers.com/img/original/10671/hong-kong-china-skyscrapers-city-lights-night.jpg"}
        elif genda == "Women":
            return{"desc": "1-2 pairs of pants, 2 blouses, 1 light-weight sweater, 2 t-shirt/tank tops, 2 dresses, sneakers and socks. TEEN CHOICE ADDITION: Decorative dust mask.", "img" : "https://besthqwallpapers.com/img/original/10671/hong-kong-china-skyscrapers-city-lights-night.jpg"}
        elif genda == "Other":
            return{"desc":"1-2 pairs of pants, 1 light-weight sweater, 2 t-shirts, sneakers and socks. TEEN CHOICE ADDITION: Decorative dust mask.", "img" : "https://besthqwallpapers.com/img/original/10671/hong-kong-china-skyscrapers-city-lights-night.jpg"}
    elif city == "Chicago":
        if genda == "Men":
            return{"desc": "sneakers, 3 t-shirts, 1 polo/button up shirt, sandals, 2 shorts, 1 light-weight sweater, 1 swimsuit", "img" : "https://media.timeout.com/images/101468999/image.jpg"}
        elif genda == "Women":
            return{"desc": "sneakers, 3 t-shirts, 1 blouse, 2 dresses, sandals, 2 shorts, 1 light-weight sweater, 1 swimsuit", "img" : "https://media.timeout.com/images/101468999/image.jpg"}
        elif genda == "Other":
            return{"desc":"sneakers, 3 t-shirts ,sandals, 2 shorts, 1 light-weight sweater, 1 swimsuit", "img" : "https://media.timeout.com/images/101468999/image.jpg"}
    elif city == "Madrid":
        if genda == "Men":
            return{"desc":"4 tank-tops, 2 t-shirts, 1 swimsuit (optional), 3 shorts/skirts, 1 pair of sunglasses.", "img" : "https://www.parisvatry.com/wp-content/uploads/2018/12/madrid-light.jpeg"}
        elif genda == "Women":
            return{"desc":"4 tank-tops, 2 t-shirts, 1 dress, 1 swimsuit(optional), 3 shorts/skirts, 1 pair of sunglasses.", "img" : "https://www.parisvatry.com/wp-content/uploads/2018/12/madrid-light.jpeg"}
        elif genda == "Other":
            return{"desc":"4 tank-tops, 2 t-shirts, 1 swimsuit(optional), 3 shorts, 1 pair of sunglasses.", "img" : "https://www.parisvatry.com/wp-content/uploads/2018/12/madrid-light.jpeg"}
    elif city == "Paris":
        if genda == "Men":
            return{"desc":"2 tank-tops/t-shirts, 1 polo shirt/button-up shirt, 3 shorts, 1 pair of sunglasses, pair of sneakers, sandals & 1 swimsuit(optional) ","img": "https://i2.wp.com/frenchmoments.eu/wp-content/uploads/2013/07/Panoramic-View-from-Montparnasse-%C2%A9-French-Moments-Paris-79.jpg?fit=2048%2C1371&ssl=1"}
        elif genda == "Women":
            return{"desc":"2 tank-tops/t-shirts, 2 blouses, 1 sundress, 2 pairs of shorts, pair of sneakers, sandals, 1 swimsuit(optional)", "img": "https://i2.wp.com/frenchmoments.eu/wp-content/uploads/2013/07/Panoramic-View-from-Montparnasse-%C2%A9-French-Moments-Paris-79.jpg?fit=2048%2C1371&ssl=1"}
        elif genda == "Other":
            return{"desc": "3 tank-tops/t-shirts, 3 shorts, 1 pair of sunglasses, pair of sneakers, sandals & 1 swimsuit(optional)", "img":"https://i2.wp.com/frenchmoments.eu/wp-content/uploads/2013/07/Panoramic-View-from-Montparnasse-%C2%A9-French-Moments-Paris-79.jpg?fit=2048%2C1371&ssl=1"}
    elif city == "Rome":
        if genda == "Men":
            return{"desc":"2 polo shirts/button-up shirts, 2 t-shirts, 3 shorts, 1 pair of pants, pair of sneakers, pair of sandals, 1 pair of sunglasses. ", "img":"http://top10hub.com/wp-content/uploads/2019/01/rome.jpg"}
        elif genda == "Women":
            return{"desc":"2 blouses/t-shirts, 2 sundresses, 2 shorts, pair of sneakers", "img":"http://top10hub.com/wp-content/uploads/2019/01/rome.jpg"}
        elif genda == "Other":
            return{"desc":"4 t-shirts, 3 shorts, 1 pair of pants, pair of sneakers, pair of sandals, 1 pair of sunglasses.", "img":"http://top10hub.com/wp-content/uploads/2019/01/rome.jpg"}
    elif city == "London":
        if genda == "Men":
            return{"desc":"1 light-weight sweater, 3 t-shirts, 2 tank-tops, pair of sandals, 1 rain jacket, 1 umbrella,  1 pair of sunglasses, 2 polo/button-up shirts, 2 pairs of pants, 2 pairs of shorts", "img": "https://www.theviewfromtheshard.com/content/uploads/2018/06/5_Shard_View_2017_D2-364_300dpi_RGB-1920x950.jpg"}
        elif genda == "Women":
            return{"desc":"1 light-weight sweater, 1 long sleeve shirt, 2 tank-tops/t-shirts, 1 rain jacket, 1 pair of sunglasses, 2 blouses, 1 dress, 2 pairs of pants, 1 pair of shorts", "img":"https://www.theviewfromtheshard.com/content/uploads/2018/06/5_Shard_View_2017_D2-364_300dpi_RGB-1920x950.jpg"}
        elif genda == "Other":
            return{"desc":"1 light-weight sweater, 5 t-shirts, 2 tank-tops, pair of sandals, 1 rain jacket, 1 umbrella,  1 pair of sunglasses, 2 pairs of pants, 2 pairs of shorts", "img":"https://www.theviewfromtheshard.com/content/uploads/2018/06/5_Shard_View_2017_D2-364_300dpi_RGB-1920x950.jpg"}
    elif city == "Sydney":
        if genda == "Men":
            return{"desc":"3 tank-tops, 2 swimsuits, sunscreen, pair of sandals, 1 pair of sunglasses, 1 polo/button up shirt, 3 shorts, 1 pair of pants", "img":"https://content.api.news/v3/images/bin/c3832cd4ad0b2f05aba13b523365d235?width=1280"}
        elif genda == "Women":
            return{"desc":"3 tanks-tops, 2 swimsuits, sunscreen, pair of sandals, 1 pair of sunglasses 2 blouses, 2 pairs of shorts/pants", "img":"https://content.api.news/v3/images/bin/c3832cd4ad0b2f05aba13b523365d235?width=1280"}
        elif genda == "Other":
            return{"desc":"4 tank-tops, 2 swimsuits, sunscreen, pair of sandals, 1 pair of sunglasses, 3 shorts, 1 pair of pants", "img":"https://content.api.news/v3/images/bin/c3832cd4ad0b2f05aba13b523365d235?width=1280"}
    elif city == "Casablanca":
        if genda == "Men":
            return{"desc":"2 pairs of pants(perferably linen), 2 pairs of shorts, 1 pair of sunglasses, 3 t-shirts(perferably with sleeves), 1 polo shirt, 1 pair of sneakers, 1 pair of sandals, 1 swimsuit", "img":"https://i.pinimg.com/originals/19/40/53/194053048e9dc596c6e0e50c8b41f6b7.jpg"}
        elif genda == "Women":
            return{"desc":"**This country has a very conservative culture regarding women's clothing.** 2 pairs of shorts (perferably at knee length), 2 dresses, 2 pairs of pants(perferably loose/flowy), 3 shirts/blouses, 1 pair of sunglasses, 1 pair of sandals, 1 pair of sneakers, 1 swimsuit & suncreen", "img":"https://i.pinimg.com/originals/19/40/53/194053048e9dc596c6e0e50c8b41f6b7.jpg"}
        elif genda == "Other":
            return{"desc":"2 pairs of pants(perferably linen), 2 pairs of shorts, 1 pair of sunglasses, 3 t-shirts(perferably with sleeves), 1 pair of sneakers, 1 pair of sandals, 1 swimsuit", "img":"https://i.pinimg.com/originals/19/40/53/194053048e9dc596c6e0e50c8b41f6b7.jpg"}
    elif city == "SantoDomingo":
        if genda == "Men":
            return{"desc":"2 swimsuits, 3 pairs of shorts, 1 pair of sunglasses, 3 t-shirts/tank-tops, 1 pair of pants & sunscreen, 1 pair of sneakers, 1 pair of sandals", "img":"https://images.unsplash.com/photo-1524778880162-1b5dccfbdb0b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80"}
        elif genda == "Women":
            return{"desc":"3 swimsuits, 1 pair of sunglasses, 3 tank-tops, 1 pair of pants, 2 pairs of shorts, 2 sundresses, sunscreen & 1 pair of sandals. optional: floppy sunhat", "img":"https://images.unsplash.com/photo-1524778880162-1b5dccfbdb0b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80"}
        elif genda == "Other":
            return{"desc":"2 swimsuits, 3 pairs of shorts, 1 pair of sunglasses, 3 t-shirts/tank-tops, 1 pair of pants & sunscreen, 1 pair of shoes.", "img":"https://images.unsplash.com/photo-1524778880162-1b5dccfbdb0b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80"}
    