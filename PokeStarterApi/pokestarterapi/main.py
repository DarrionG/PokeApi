
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

#returns the whole starter pokemon dataframe
def read_file():
    pokeFile = (pd.read_csv("http://storageguest13.blob.core.windows.net/starterpokemon/PokemonStarterDB.csv").set_index('Pokedex_Number'))
    return pokeFile.to_dict()

#takes an int as an input returns Pokemon
@app.route('/dexnumber', methods=['GET'])
def pokemon_by_dexnumber():

    dex_num = int(request.args.get('dex_num'))
    
    poke_db = read_file()
    poke_dict = {}

    if not type (dex_num) is int:
        raise TypeError("Please enter an integer")
    elif (dex_num < 1 or dex_num > 818):
        raise IndexError("Please enter a number between 1 and 818")
    else:
        for pokenum in poke_db["Name"]:
            if (pokenum == dex_num):
                poke_dict[pokenum] = poke_db["Name"][pokenum], poke_db["Main_Type"][pokenum], poke_db["Secondary_Type"][pokenum]
            
    return jsonify(poke_dict)


#takes a string as an input returns Pokemon
@app.route('/maintype', methods=['GET'])
def pokemon_by_maintype():

    main_type = request.args.get('main_type')

    poke_db = read_file()
    poke_dict = {}

    if not type (main_type) is str:
        raise TypeError("Please enter a string")
    else:
        for pokenum in poke_db["Main_Type"]:
            if (poke_db["Main_Type"][pokenum] == main_type):
                poke_dict[pokenum] = poke_db["Name"][pokenum], poke_db["Main_Type"][pokenum], poke_db["Secondary_Type"][pokenum]
                
    return jsonify(poke_dict)
    
#takes a string as an input returns Pokemon
@app.route('/secondtype', methods=['GET'])
def pokemon_by_secondarytype():

    secnd_type = request.args.get('secnd_type')

    poke_db = read_file()
    poke_dict = {}

    if not type (secnd_type) is str:
        raise TypeError("Please enter a string")
    else:
        for pokenum in poke_db["Secondary_Type"]:
            if (poke_db["Secondary_Type"][pokenum] == secnd_type):
                poke_dict[pokenum] = poke_db["Name"][pokenum], poke_db["Main_Type"][pokenum], poke_db["Secondary_Type"][pokenum]

    return jsonify(poke_dict)


#takes a string as an input returns Pokemon
@app.route('/name')
def pokemon_by_name():

    name = request.args.get('name')

    poke_db = read_file()
    poke_dict = {}

    if not type (name) is str:
        raise TypeError("Please enter a string")
    else:
        for pokenum in poke_db["Name"]:
            if (poke_db["Name"][pokenum] == name):
                poke_dict[pokenum] = poke_db["Name"][pokenum], poke_db["Main_Type"][pokenum], poke_db["Secondary_Type"][pokenum]

    return jsonify(poke_dict)


if __name__ == "__main__":
    app.run(debug=True)