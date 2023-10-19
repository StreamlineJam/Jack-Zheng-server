import requests as req

question = input("what would you like to see?\n>>")

if question == "cappuccino":
    cappuccino = input("what would you like to know about cappuccino?\n>>")

    if cappuccino == "stock":
        url_string= f"http://10.6.20.239:8000/coffee_stock/cappuccino?api_key=071113"

        response = req.get(url=url_string)

        json_data = response.json()

        if "msg" in json_data:
            print(json_data['msg'])
        else:
            print(f"Heres your data {json_data['type']}  {json_data['stock']}")

    if cappuccino == "ranking":
        #his coffee stock link somehow has all the information and the ranking link refuses to work
        #goes the same for everything else
        url_string= f"http://10.6.20.239:8000/coffee_stock/cappuccino?api_key=071113"

        response = req.get(url=url_string)

        json_data = response.json()

        if "msg" in json_data:
            print(json_data['msg'])
        else:
            print(f"Heres your data {json_data['ranking']}")

    if question == "black":
        black = input("what would you like to know about black coffee?\n>>")

        if black == "stock":
            url_string = f"http://10.6.20.239:8000/coffee_stock/black?api_key=071113"

            response = req.get(url=url_string)

            json_data = response.json()

            if "msg" in json_data:
                print(json_data['msg'])
            else:
                print(f"Heres your data {json_data['type']}  {json_data['stock']}")

        if black == "ranking":
            # his coffee stock link somehow has all the information and the ranking link refuses to work
            # goes the same for everything else
            url_string = f"http://10.6.20.239:8000/coffee_stock/black?api_key=071113"

            response = req.get(url=url_string)

            json_data = response.json()

            if "msg" in json_data:
                print(json_data['msg'])
            else:
                print(f"Heres your data {json_data['ranking']}")









