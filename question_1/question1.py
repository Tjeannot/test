#%% Imports des librairies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# %% Tests de verif

# print ("speed : " , output_speed[8])
# print ("altitude", output_altitude[8])
# # print("wind", output_wind[4])
# print("fuel_flow", output_fuel_flow[8])



# %% Chargement des données depuis les fichiers pickle

output_altitude = pd.read_pickle("signals_altitude.pkl")
output_speed = pd.read_pickle("signals_vitesse.pkl")
output_wind = pd.read_pickle("signals_wind.pkl")
output_fuel_flow = pd.read_pickle("signals_fuel_flow.pkl")




# %% Fonctions pour l'étude de la consomation de carburant en fonction de la vitesse

Nb_col = output_altitude.shape[1]

fuel_speed_list=[]

def fuel_flow_model_1(vitesse_data, altitude_data, fuel_flow_data, altitude):
    #Initialisation
    fuel_flow_list=[]
    vitesse_list=[]
    
    for j in range(Nb_col):
        
        #Initialisation des listes pour les valeurs de vitesse et altitudes à 8000 pieds
        valid_speeds=[]
        valid_flows=[]
        
        for i in range (len(altitude_data[j])):
            
            if altitude_data[j][i] == altitude and fuel_flow_data[j][i] >= 1 :
                #Construction pour chaque vol, des vitesses et fuel flows à 8000 pieds
                valid_speeds.append(vitesse_data[j][i])
                valid_flows.append(fuel_flow_data[j][i])
                
        fuel_flow_list.append(valid_flows)
        vitesse_list.append(valid_speeds)
    return vitesse_list, fuel_flow_list
    


def IndexPlotFueLFlow_VS_Speed(fuel_flow, var, index):
    """
    Crée un graphique de dispersion du flux de carburant en fonction de la vitesse.
    """
    fuel_flow = np.asarray(fuel_flow[index])
    var= np.asarray(var[index])

    plt.subplot()
    plt.scatter(var, fuel_flow, color='b', alpha=0.7)
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
    
    ax.grid(True)
    
    plt.show()

# %%

def fuel_flow_model_2(vitesse_data, altitude_data, fuel_flow_data, vitesse):
    #Initialisation
    # fuel_speed_list=[]
    fuel_flow_list=[]
    altitude_list=[]
    for j in range(Nb_col):
        #Initialisation des listes pour les valeurs de vitesse et altitudes à 8000 pieds
        valid_altitudes=[]
        valid_flows=[]

        for i in range (len(altitude_data[j])):
            if vitesse_data[j][i] == vitesse and fuel_flow_data[j][i] < 1 and 0 <= altitude_data[j][i] <= 15000:
                #Construction pour chaque vol, des vitesses et fuel flows à 8000 pieds
                valid_altitudes.append(altitude_data[j][i])
                valid_flows.append(fuel_flow_data[j][i])

        fuel_flow_list.append(valid_flows)
        altitude_list.append(valid_altitudes)
    return altitude_list, fuel_flow_list


def IndexPlotFuelFlow_VS_altitude( fuel_flow, var, index):
    """
    Crée un graphique de dispersion du flux de carburant en fonction de 
    l'altitude à une vitesse de 665km/h.
    """  
    fuel_flow = np.asarray(fuel_flow[index])
    var= np.asarray(var[index])

    
    plt.subplot()
    plt.scatter(var, fuel_flow, color='b', alpha=0.7)
    plt.grid(True)

def PlotFueLFlow_VS_Altitude(fuel, altitude):

    fig, ax = plt.subplots(figsize=(10, 6))
    
    for i in range (len(fuel)):
        IndexPlotFuelFlow_VS_altitude(fuel, altitude, i)


    altitude_array = np.concatenate(altitude)
    fuel_array = np.concatenate(fuel)
    
    # Plot all data on a single set of axes
    ax.scatter(altitude_array, fuel_array, color='b', alpha=0.7)
    ax.set_title("Fuel Flow en fonction de l'altitude (à 665 km/h)")
    ax.set_xlabel('Valtitude(fts)')
    ax.set_ylabel('Fuel Flow (pound/s)')
    ax.grid(True)
    
    plt.show()


# %% Etude de la consomation de carburant en fonction de la vitesse pour une altitude de 8000 pieds

speed, fuel_v = fuel_flow_model_1(output_speed, output_altitude, output_fuel_flow, 8000.0)
PlotFueLFlow_VS_Speed(fuel_v, speed)

# %% Etude de la consomation de carburant en fonction de l'altitude pour une vitesse de 665km/h

altitude, fuel_a = fuel_flow_model_2(output_speed, output_altitude, output_fuel_flow, 665.0)
PlotFueLFlow_VS_Altitude(fuel_a, altitude)



