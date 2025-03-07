#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 19:16:27 2025

@author: danielle
"""
import pandas as pd
import numpy as np

output_altitude = pd.read_pickle("signals_altitude.pkl")
output_speed = pd.read_pickle("signals_vitesse.pkl")
output_wind = pd.read_pickle("signals_wind.pkl")
output_fuel_flow = pd.read_pickle("signals_fuel_flow.pkl")



# print ("speed : " , output_speed[8])
# print ("altitude", output_altitude[8])
# print("wind", output_wind[4])
# print("fuel_flow", output_fuel_flow[8])



# Chargement des données depuis un fichier pickle
output_altitude = pd.read_pickle("signals_altitude.pkl")
output_speed = pd.read_pickle("signals_vitesse.pkl")
output_fuel_flow = pd.read_pickle("signals_fuel_flow.pkl")

# Nombre de vols
Nb_col = output_altitude.shape[1]

fuel_speed_list=[]

for j in range(Nb_col):
    #Initialisation des listes pour les valeurs de vitesse et altitudes à 8000 pieds
    valid_speeds=[]
    valid_flows=[]
    
    for i in range (len(output_altitude[j])):
        if output_altitude[j][i] == 8000.0:
            #Construction pour chaque vol, des vitesses et fuel flows à 8000 pieds
            valid_speeds.append(output_speed[j][i])
            valid_flows.append(output_fuel_flow[j][i])
    print("trois : ", valid_speeds)
    print("quatre : " ,valid_flows )
    
    # Construction de la liste de données vitesse et fuel_flows à 8000 pieds
    fuel_speed_list.append(np.array([valid_speeds,valid_flows]))
        
#print(fuel_speed_list[1][1])


# Je te prie de ne pas insulter ma mère, mon cerveau est resté endormi trop longtemps en ces temps de chômage
# Et je ne suis pas un génie comme toi Boss

