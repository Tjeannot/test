#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 19:16:27 2025

@author: danielle
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def fuel_flow_model(vitesse_data, altitude_data, fuel_flow_data, altitude):
    #Initialisation
    # fuel_speed_list=[]
    fuel_flow_list=[]
    vitesse_list=[]
    for j in range(Nb_col):
        #Initialisation des listes pour les valeurs de vitesse et altitudes à 8000 pieds
        valid_speeds=[]
        valid_flows=[]
        found_altitude_data = False
        for i in range (len(altitude_data[j])):
            if altitude_data[j][i] == altitude:
                found_altitude_data=True
                if fuel_flow_data[j][i] >= 1:
                    continue
                #Construction pour chaque vol, des vitesses et fuel flows à 8000 pieds
                valid_speeds.append(vitesse_data[j][i])
                valid_flows.append(fuel_flow_data[j][i])
                
                
        if found_altitude_data:
            
            # Construction de la liste de données vitesse et fuel_flows à 8000 pieds
            # fuel_speed_list.append(np.array([valid_speeds,valid_flows]))
            fuel_flow_list.append(valid_flows)
            vitesse_list.append(valid_speeds)
    return vitesse_list, fuel_flow_list
    



def IndexPlotFueLFlow_VS_Speed(fuel_flow, var, index):
    """
    Crée un graphique de dispersion du flux de carburant en fonction de la vitesse.

    :param df: DataFrame contenant les données avec les colonnes 'speed' et 'fuel_flow'.
    """
    fuel_flow = np.asarray(fuel_flow[index]) # Ensures data is in array form
    var= np.asarray(var[index])

    
    plt.subplot()
    plt.scatter(var, fuel_flow, color='b', alpha=0.7)
    plt.title('Fuel Flow en Fonction de la Vitesse (à 8000 pieds)')
    plt.xlabel('Vitesse (km/h)')
    plt.ylabel('Fuel Flow (pound/s)')
    plt.grid(True)
    # plt.show()
    
    
    
def PlotFueLFlow_VS_Speed(fuel,speed):

    fig, ax = plt.subplots(figsize=(10, 6))
    
    for i in range (len(fuel)):
        IndexPlotFueLFlow_VS_Speed(fuel, speed, i)
    # Plot all data on a single set of axes
    speed_array = np.concatenate(speed)
    fuel_array = np.concatenate(fuel)
    ax.scatter(speed_array, fuel_array, color='b', alpha=0.7)
    
    ax.set_title('Fuel Flow en Fonction de la Vitesse (à 8000 pieds)')
    ax.set_xlabel('Vitesse (km/h)')
    ax.set_ylabel('Fuel Flow (pound/s)')
    ax.grid(True)
    
    plt.show()

    
speed, fuel = fuel_flow_model(output_speed, output_altitude, output_fuel_flow, 8000.0)

print(len(speed))
# print(fuel)
PlotFueLFlow_VS_Speed(fuel, speed)



