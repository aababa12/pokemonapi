import requests,json,random

def request():
    file = requests.get('https://pokeapi.co/api/v2/pokemon/')
    data=file.json()["results"]
    return data

def make_list(data):
    pokemon_list=[]
    for i in range(len(data)):
        pokemon_list.append(data[i]["name"])
    return pokemon_list

#add the first pokemon in the JSON file
def first_init(data):
    first_value=True
    if first_value:
        url = data[0]["url"]
        new = requests.get(data[0]["url"])
        data2 = new.json()
        first_pokemon = {data[0]["name"]: [data2["abilities"][0]["ability"]["name"], data2["height"], data2["weight"]]}
        with open('/home/ec2-user/GHRepository/Pockjson.json', 'w') as file:
            json.dump(first_pokemon, file, indent=4)
        first_value=False

#open Pockjson.json for read  :
def load_to_json():
    with open('/home/ec2-user/GHRepository/Pockjson.json', 'r') as json_file:
        imported_data = json.load(json_file)
    return imported_data

def main(imported_data,pokemon_list,data):
    valid = True
    while valid:
        try:
            draw=input("Hello would like to draw a Pokémon y/n?")
            if draw=="y":
                # choose pokemon randomly
                random_pokemon  = random.choice(pokemon_list)
                ##cheak if the random pokemon is in the JSON if yes present details:

                if random_pokemon in imported_data:
                    ability = imported_data[random.choice][0]
                    height = imported_data[random.choice][1]
                    weight = imported_data[random.choice][2]
                    print(f"Name : {random.choice} Ability : {ability} Height : {height} Weight : {weight}")
                        # random pokemon is not in Pockjson.json, we add it and present details:
                else:
                    for pokemon in data:
                        if pokemon['name'] == random_pokemon:
                            url = pokemon['url']
                    new = requests.get(url)
                    data2 = new.json()
                    ability = data2["abilities"][0]["ability"]["name"]
                    height = data2["height"]
                    weight = data2["weight"]
                    print(f"Name : {random_pokemon} Ability : {ability} Height : {height} Weight : {weight}")
                    new_pokemon = {random_pokemon: [data2["abilities"][0]["ability"]["name"], data2["height"], data2["weight"]]}
                    # print(new_pokemon)
                    imported_data.update(new_pokemon)
                    with open('/home/ec2-user/GHRepository/Pockjson.json', 'w') as json1_file:
                        json.dump(imported_data, json1_file, indent=4)
            else:
                if draw=="n":
                    print("Goodbye")
                    valid=False
        except:
            print("Try Again (y/n")

if __name__ == '__main__':
    data=request()
    pokemon_list=make_list(data)
    first_init(data)
    imported_data =load_to_json()
    main(imported_data, pokemon_list, data)
