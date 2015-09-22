__author__ = 'riley'

import datetime
import pykemon

# https://imgur.com/Gl8omZb

def getPokemon(m, d, name_len):
    pokeNum = d*m*name_len
    while(pokeNum>649):
        pokeNum /= 2

    return pokeNum

if __name__=="__main__":
    pokeNumSet = set()
    start_date = datetime.date(2000,1,1) #Use a leap year
    end_date = datetime.date(2001,1,1)
    delta_t = datetime.timedelta(days=1)
    cur_date = start_date
    while(cur_date<end_date):
        max_name_len = 30
        for name_len in range(1,max_name_len):
            m = cur_date.month
            d = cur_date.day
            pokeNumSet.add(getPokemon(m, d, name_len))
        cur_date += delta_t

    #pokeNumSet contains all possible results
    allPokeNums = set()
    for i in range(1,650):
        allPokeNums.add(i)

    impossiblePokeNums = allPokeNums.difference(pokeNumSet)
    for pokeNum in impossiblePokeNums:
        pokemon = pykemon.get(pokemon_id=pokeNum)
        print pokemon.name+",",

