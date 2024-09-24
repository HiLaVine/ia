import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Label, Canvas, Entry, Button, END
from PIL import Image, ImageTk

# Define la función "test" que realiza el análisis difuso
def test(dirt_type_value, cloth_dirtiness_value, cloth_mass_value, cloth_sensitivity_value, water_hardness_value):
    # clean data
    cloth_mass_value = cloth_mass_value / 10
    cloth_sensitivity_value = cloth_sensitivity_value / 10

    # Define los rangos de las variables de entrada
    dirt_type = np.arange(0, 101, 1)
    cloth_dirtiness = np.arange(0, 101, 1)
    cloth_mass = np.arange(0, 11, 1)
    cloth_sensitivity = np.arange(0, 11, 1)
    water_hardness = np.arange(0, 101, 1)

    # Define los rangos de las variables de salida
    wash_time = np.arange(0, 61, 1)
    wash_speed = np.arange(0, 1401, 1)
    water_amount = np.arange(0, 101, 1)
    detergent_amount = np.arange(0, 101, 1)
    water_temperature = np.arange(0, 81, 1)

    # Lista para almacenar los resultados de las variables de salida
    output_list = [wash_time, wash_speed, water_amount, detergent_amount, water_temperature]
    output_name = ['Duración del Lavado', 'Velocidad de Lavado', 'Cantidad de Agua', 'Cantidad de Detergente', 'Temperatura del Agua']
    output_unit = ['Minutos', 'rpm', 'Litros', 'Mililitros', '°C']

    # Define las funciones de pertenencia para las variables de entrada
    dirt_type_NotGreasy = fuzz.trimf(dirt_type, [0, 0, 50])
    dirt_type_LessGreasy = fuzz.trimf(dirt_type, [20, 50, 80])
    dirt_type_Greasy = fuzz.trimf(dirt_type, [50, 100, 100])

    cloth_dirtiness_Small = fuzz.trimf(cloth_dirtiness, [0, 0, 50])
    cloth_dirtiness_Medium = fuzz.trimf(cloth_dirtiness, [20, 50, 80])
    cloth_dirtiness_Large = fuzz.trimf(cloth_dirtiness, [50, 100, 100])

    cloth_mass_Light = fuzz.trimf(cloth_mass, [0, 0, 5])
    cloth_mass_Medium = fuzz.trimf(cloth_mass, [2, 5, 8])
    cloth_mass_Heavy = fuzz.trimf(cloth_mass, [5, 10, 10])

    cloth_sensitivity_NotSensitive = fuzz.trimf(cloth_sensitivity, [0, 0, 5])
    cloth_sensitivity_LessSensitive = fuzz.trimf(cloth_sensitivity, [2, 5, 8])
    cloth_sensitivity_MoreSensitive = fuzz.trimf(cloth_sensitivity, [5, 10, 10])

    water_hardness_Soft = fuzz.trimf(water_hardness, [0, 0, 50])
    water_hardness_Moderate = fuzz.trimf(water_hardness, [20, 50, 80])
    water_hardness_Hard = fuzz.trimf(water_hardness, [50, 100, 100])

    # Define las funciones de pertenencia para las variables de salida
    wash_time_VeryShort = fuzz.trimf(wash_time, [0, 0, 13])
    wash_time_Short = fuzz.trimf(wash_time, [0, 13, 25])
    wash_time_Medium = fuzz.trimf(wash_time, [15, 25, 35])
    wash_time_Long = fuzz.trimf(wash_time, [25, 35, 45])
    wash_time_VeryLong = fuzz.trimf(wash_time, [40, 60, 60])

    wash_speed_VerySlow = fuzz.trimf(wash_speed, [0, 0, 200])
    wash_speed_Slow = fuzz.trimf(wash_speed, [120, 300, 500])
    wash_speed_Medium = fuzz.trimf(wash_speed, [340, 540, 740])
    wash_speed_Fast = fuzz.trimf(wash_speed, [700, 1000, 1200])
    wash_speed_VeryFast = fuzz.trimf(wash_speed, [1000, 1400, 1400])

    water_amount_Less = fuzz.trimf(water_amount, [0, 0, 70])
    water_amount_Normal = fuzz.trimf(water_amount, [50, 65, 80])
    water_amount_More = fuzz.trimf(water_amount, [80, 100, 100])

    detergent_amount_Less = fuzz.trimf(detergent_amount, [0, 0, 30])
    detergent_amount_Normal = fuzz.trimf(detergent_amount, [30, 65, 80])
    detergent_amount_More = fuzz.trimf(detergent_amount, [80, 100, 100])

    water_temperature_Low = fuzz.trimf(water_temperature, [0, 0, 40])
    water_temperature_Medium = fuzz.trimf(water_temperature, [20, 40, 60])
    water_temperature_High = fuzz.trimf(water_temperature, [40, 80, 80])

    #---------------------------Reglas Difusas-------------------------
    # Regla 1
    rule1_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_Greasy, dirt_type_value)
    rule1_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Large, cloth_dirtiness_value)
    rule1_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Heavy, cloth_mass_value)
    rule1_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_MoreSensitive,
                                                     cloth_sensitivity_value)
    rule1_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Hard, water_hardness_value)
    rule_1_antecedent = max(rule1_dirt_type, rule1_cloth_dirtiness, rule1_cloth_mass, rule1_cloth_sensitivity,
                            rule1_water_hardness)

    rule_1_clip = []
    rule_1_clip.append(np.fmin(rule_1_antecedent, wash_time_Long))
    rule_1_clip.append(np.fmin(rule_1_antecedent, wash_speed_Medium))
    rule_1_clip.append(np.fmin(rule_1_antecedent, water_amount_Normal))
    rule_1_clip.append(np.fmin(rule_1_antecedent, detergent_amount_Normal))
    rule_1_clip.append(np.fmin(rule_1_antecedent, water_temperature_Medium))

    ## Regla 2
    rule2_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule2_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule2_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule2_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_NotSensitive,
                                                     cloth_sensitivity_value)
    rule2_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Soft, water_hardness_value)
    rule_2_antecedent = min(rule2_dirt_type, rule2_cloth_dirtiness, rule2_cloth_mass, rule2_cloth_sensitivity,
                            rule2_water_hardness)

    rule_2_clip = []
    rule_2_clip.append(np.fmin(rule_2_antecedent, wash_time_VeryShort))
    rule_2_clip.append(np.fmin(rule_2_antecedent, wash_speed_VerySlow))
    rule_2_clip.append(np.fmin(rule_2_antecedent, water_amount_Less))
    rule_2_clip.append(np.fmin(rule_2_antecedent, detergent_amount_Less))
    rule_2_clip.append(np.fmin(rule_2_antecedent, water_temperature_Low))

    # Regla 3
    rule3_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_LessGreasy, dirt_type_value)
    rule3_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Medium, cloth_dirtiness_value)
    rule3_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Medium, cloth_mass_value)
    rule3_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                     cloth_sensitivity_value)
    rule3_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Moderate, water_hardness_value)
    rule_3_antecedent = min(rule3_dirt_type, rule3_cloth_dirtiness, rule3_cloth_mass, rule3_cloth_sensitivity,
                            rule3_water_hardness)

    rule_3_clip = []
    rule_3_clip.append(np.fmin(rule_3_antecedent, wash_time_Medium))
    rule_3_clip.append(np.fmin(rule_3_antecedent, wash_speed_Medium))
    rule_3_clip.append(np.fmin(rule_3_antecedent, water_amount_Normal))
    rule_3_clip.append(np.fmin(rule_3_antecedent, detergent_amount_Normal))
    rule_3_clip.append(np.fmin(rule_3_antecedent, water_temperature_Medium))

    # Regla 4
    rule4_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule4_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule4_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule4_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_NotSensitive,
                                                     cloth_sensitivity_value)
    rule4_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Soft, water_hardness_value)
    rule_4_antecedent = max(rule4_dirt_type, rule4_cloth_dirtiness, rule4_cloth_mass, rule4_cloth_sensitivity,
                            rule4_water_hardness)

    rule_4_clip = []
    rule_4_clip.append(np.fmin(rule_4_antecedent, wash_time_Short))
    rule_4_clip.append(np.fmin(rule_4_antecedent, wash_speed_Medium))
    rule_4_clip.append(np.fmin(rule_4_antecedent, water_amount_Normal))
    rule_4_clip.append(np.fmin(rule_4_antecedent, detergent_amount_Normal))
    rule_4_clip.append(np.fmin(rule_4_antecedent, water_temperature_Low))

    # Regla 5
    rule5_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_Greasy, dirt_type_value)
    rule5_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Large, cloth_dirtiness_value)
    rule5_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Heavy, cloth_mass_value)
    rule5_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_MoreSensitive,
                                                     cloth_sensitivity_value)
    rule5_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Hard, water_hardness_value)
    rule_5_antecedent = min(rule5_dirt_type, rule5_cloth_dirtiness, rule5_cloth_mass, rule5_cloth_sensitivity,
                            rule5_water_hardness)

    rule_5_clip = []
    rule_5_clip.append(np.fmin(rule_5_antecedent, wash_time_VeryLong))
    rule_5_clip.append(np.fmin(rule_5_antecedent, wash_speed_VeryFast))
    rule_5_clip.append(np.fmin(rule_5_antecedent, water_amount_More))
    rule_5_clip.append(np.fmin(rule_5_antecedent, detergent_amount_More))
    rule_5_clip.append(np.fmin(rule_5_antecedent, water_temperature_High))

    # Regla 6
    rule6_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule6_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule6_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule6_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_NotSensitive,
                                                     cloth_sensitivity_value)
    rule6_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Moderate, water_hardness_value)
    rule_6_antecedent = min(rule6_dirt_type, rule6_cloth_dirtiness, rule6_cloth_mass, rule6_cloth_sensitivity,
                            rule6_water_hardness)

    rule_6_clip = []
    rule_6_clip.append(np.fmin(rule_6_antecedent, wash_time_VeryShort))
    rule_6_clip.append(np.fmin(rule_6_antecedent, wash_speed_VerySlow))
    rule_6_clip.append(np.fmin(rule_6_antecedent, water_amount_Less))
    rule_6_clip.append(np.fmin(rule_6_antecedent, detergent_amount_Less))
    rule_6_clip.append(np.fmin(rule_6_antecedent, water_temperature_Low))

    # Regla 7
    rule7_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule7_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule7_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule7_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_NotSensitive,
                                                     cloth_sensitivity_value)
    rule7_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Hard, water_hardness_value)
    rule_7_antecedent = min(rule7_dirt_type, rule7_cloth_dirtiness, rule7_cloth_mass, rule7_cloth_sensitivity,
                            rule7_water_hardness)

    rule_7_clip = []
    rule_7_clip.append(np.fmin(rule_7_antecedent, wash_time_VeryShort))
    rule_7_clip.append(np.fmin(rule_7_antecedent, wash_speed_Slow))
    rule_7_clip.append(np.fmin(rule_7_antecedent, water_amount_Less))
    rule_7_clip.append(np.fmin(rule_7_antecedent, detergent_amount_Less))
    rule_7_clip.append(np.fmin(rule_7_antecedent, water_temperature_Low))

    # Regla 8
    rule8_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule8_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule8_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule8_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                     cloth_sensitivity_value)
    rule8_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Soft, water_hardness_value)
    rule_8_antecedent = min(rule8_dirt_type, rule8_cloth_dirtiness, rule8_cloth_mass, rule8_cloth_sensitivity,
                            rule8_water_hardness)

    rule_8_clip = []
    rule_8_clip.append(np.fmin(rule_8_antecedent, wash_time_VeryShort))
    rule_8_clip.append(np.fmin(rule_8_antecedent, wash_speed_VerySlow))
    rule_8_clip.append(np.fmin(rule_8_antecedent, water_amount_Less))
    rule_8_clip.append(np.fmin(rule_8_antecedent, detergent_amount_Less))
    rule_8_clip.append(np.fmin(rule_8_antecedent, water_temperature_Low))

    #Regla 9
    rule9_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule9_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule9_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule9_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                     cloth_sensitivity_value)
    rule9_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Moderate, water_hardness_value)
    rule_9_antecedent = min(rule9_dirt_type, rule9_cloth_dirtiness, rule9_cloth_mass, rule9_cloth_sensitivity,
                            rule9_water_hardness)

    rule_9_clip = []
    rule_9_clip.append(np.fmin(rule_9_antecedent, wash_time_VeryShort))
    rule_9_clip.append(np.fmin(rule_9_antecedent, wash_speed_VerySlow))
    rule_9_clip.append(np.fmin(rule_9_antecedent, water_amount_Less))
    rule_9_clip.append(np.fmin(rule_9_antecedent, detergent_amount_Less))
    rule_9_clip.append(np.fmin(rule_9_antecedent, water_temperature_Low))

    #Regla 10
    rule10_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule10_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule10_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule10_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                      cloth_sensitivity_value)
    rule10_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Hard, water_hardness_value)
    rule_10_antecedent = min(rule10_dirt_type, rule10_cloth_dirtiness, rule10_cloth_mass, rule10_cloth_sensitivity,
                             rule10_water_hardness)

    rule_10_clip = []
    rule_10_clip.append(np.fmin(rule_10_antecedent, wash_time_Short))
    rule_10_clip.append(np.fmin(rule_10_antecedent, wash_speed_Slow))
    rule_10_clip.append(np.fmin(rule_10_antecedent, water_amount_Less))
    rule_10_clip.append(np.fmin(rule_10_antecedent, detergent_amount_Less))
    rule_10_clip.append(np.fmin(rule_10_antecedent, water_temperature_Low))

    #Regla 11
    rule11_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule11_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule11_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule11_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_MoreSensitive,
                                                      cloth_sensitivity_value)
    rule11_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Soft, water_hardness_value)
    rule_11_antecedent = min(rule11_dirt_type, rule11_cloth_dirtiness, rule11_cloth_mass, rule11_cloth_sensitivity,
                             rule11_water_hardness)

    rule_11_clip = []
    rule_11_clip.append(np.fmin(rule_11_antecedent, wash_time_VeryShort))
    rule_11_clip.append(np.fmin(rule_11_antecedent, wash_speed_VerySlow))
    rule_11_clip.append(np.fmin(rule_11_antecedent, water_amount_Less))
    rule_11_clip.append(np.fmin(rule_11_antecedent, detergent_amount_Less))
    rule_11_clip.append(np.fmin(rule_11_antecedent, water_temperature_Low))

    #Regla 12
    rule12_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule12_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule12_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule12_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_MoreSensitive,
                                                      cloth_sensitivity_value)
    rule12_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Moderate, water_hardness_value)
    rule_12_antecedent = min(rule12_dirt_type, rule12_cloth_dirtiness, rule12_cloth_mass, rule12_cloth_sensitivity,
                             rule12_water_hardness)

    rule_12_clip = []
    rule_12_clip.append(np.fmin(rule_12_antecedent, wash_time_Short))
    rule_12_clip.append(np.fmin(rule_12_antecedent, wash_speed_Slow))
    rule_12_clip.append(np.fmin(rule_12_antecedent, water_amount_Less))
    rule_12_clip.append(np.fmin(rule_12_antecedent, detergent_amount_Less))
    rule_12_clip.append(np.fmin(rule_12_antecedent, water_temperature_Low))

    #Regla 13
    rule13_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule13_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule13_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule13_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_MoreSensitive,
                                                      cloth_sensitivity_value)
    rule13_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Hard, water_hardness_value)
    rule_13_antecedent = min(rule13_dirt_type, rule13_cloth_dirtiness, rule13_cloth_mass, rule13_cloth_sensitivity,
                             rule13_water_hardness)

    rule_13_clip = []
    rule_13_clip.append(np.fmin(rule_13_antecedent, wash_time_Short))
    rule_13_clip.append(np.fmin(rule_13_antecedent, wash_speed_Medium))
    rule_13_clip.append(np.fmin(rule_13_antecedent, water_amount_Less))
    rule_13_clip.append(np.fmin(rule_13_antecedent, detergent_amount_Normal))
    rule_13_clip.append(np.fmin(rule_13_antecedent, water_temperature_Medium))

    #Regla 14
    rule14_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule14_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule14_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Medium, cloth_mass_value)
    rule14_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                      cloth_sensitivity_value)
    rule14_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Soft, water_hardness_value)
    rule_14_antecedent = min(rule14_dirt_type, rule14_cloth_dirtiness, rule14_cloth_mass, rule14_cloth_sensitivity,
                             rule14_water_hardness)

    rule_14_clip = []
    rule_14_clip.append(np.fmin(rule_14_antecedent, wash_time_Short))
    rule_14_clip.append(np.fmin(rule_14_antecedent, wash_speed_Medium))
    rule_14_clip.append(np.fmin(rule_14_antecedent, water_amount_Less))
    rule_14_clip.append(np.fmin(rule_14_antecedent, detergent_amount_Normal))
    rule_14_clip.append(np.fmin(rule_14_antecedent, water_temperature_Medium))

    #Regla 15
    rule15_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_NotGreasy, dirt_type_value)
    rule15_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Medium, cloth_dirtiness_value)
    rule15_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Medium, cloth_mass_value)
    rule15_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                      cloth_sensitivity_value)
    rule15_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Moderate, water_hardness_value)
    rule_15_antecedent = min(rule15_dirt_type, rule15_cloth_dirtiness, rule15_cloth_mass, rule15_cloth_sensitivity,
                             rule15_water_hardness)

    rule_15_clip = []
    rule_15_clip.append(np.fmin(rule_15_antecedent, wash_time_Medium))
    rule_15_clip.append(np.fmin(rule_15_antecedent, wash_speed_Fast))
    rule_15_clip.append(np.fmin(rule_15_antecedent, water_amount_Normal))
    rule_15_clip.append(np.fmin(rule_15_antecedent, detergent_amount_Normal))
    rule_15_clip.append(np.fmin(rule_15_antecedent, water_temperature_Medium))

    #Regla 16
    rule16_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_LessGreasy, dirt_type_value)
    rule16_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Medium, cloth_dirtiness_value)
    rule16_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Medium, cloth_mass_value)
    rule16_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                      cloth_sensitivity_value)
    rule16_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Moderate, water_hardness_value)
    rule_16_antecedent = min(rule16_dirt_type, rule16_cloth_dirtiness, rule16_cloth_mass, rule16_cloth_sensitivity,
                             rule16_water_hardness)

    rule_16_clip = []
    rule_16_clip.append(np.fmin(rule_16_antecedent, wash_time_Medium))
    rule_16_clip.append(np.fmin(rule_16_antecedent, wash_speed_Fast))
    rule_16_clip.append(np.fmin(rule_16_antecedent, water_amount_Normal))
    rule_16_clip.append(np.fmin(rule_16_antecedent, detergent_amount_Normal))
    rule_16_clip.append(np.fmin(rule_16_antecedent, water_temperature_Medium))

    #Regla 17
    rule17_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_LessGreasy, dirt_type_value)
    rule17_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Medium, cloth_dirtiness_value)
    rule17_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Heavy, cloth_mass_value)
    rule17_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                      cloth_sensitivity_value)
    rule17_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Moderate, water_hardness_value)
    rule_17_antecedent = min(rule17_dirt_type, rule17_cloth_dirtiness, rule17_cloth_mass, rule17_cloth_sensitivity,
                             rule17_water_hardness)

    rule_17_clip = []
    rule_17_clip.append(np.fmin(rule_17_antecedent, wash_time_Long))
    rule_17_clip.append(np.fmin(rule_17_antecedent, wash_speed_Fast))
    rule_17_clip.append(np.fmin(rule_17_antecedent, water_amount_More))
    rule_17_clip.append(np.fmin(rule_17_antecedent, detergent_amount_More))
    rule_17_clip.append(np.fmin(rule_17_antecedent, water_temperature_High))

    #Regla 18
    rule18_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_Greasy, dirt_type_value)
    rule18_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Medium, cloth_dirtiness_value)
    rule18_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Medium, cloth_mass_value)
    rule18_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_MoreSensitive,
                                                      cloth_sensitivity_value)
    rule18_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Hard, water_hardness_value)
    rule_18_antecedent = min(rule18_dirt_type, rule18_cloth_dirtiness, rule18_cloth_mass, rule18_cloth_sensitivity,
                             rule18_water_hardness)

    rule_18_clip = []
    rule_18_clip.append(np.fmin(rule_18_antecedent, wash_time_Long))
    rule_18_clip.append(np.fmin(rule_18_antecedent, wash_speed_Fast))
    rule_18_clip.append(np.fmin(rule_18_antecedent, water_amount_More))
    rule_18_clip.append(np.fmin(rule_18_antecedent, detergent_amount_More))
    rule_18_clip.append(np.fmin(rule_18_antecedent, water_temperature_High))

    #Regla 19
    rule19_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_Greasy, dirt_type_value)
    rule19_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Medium, cloth_dirtiness_value)
    rule19_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Heavy, cloth_mass_value)
    rule19_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_MoreSensitive,
                                                      cloth_sensitivity_value)
    rule19_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Hard, water_hardness_value)
    rule_19_antecedent = min(rule19_dirt_type, rule19_cloth_dirtiness, rule19_cloth_mass, rule19_cloth_sensitivity,
                             rule19_water_hardness)

    rule_19_clip = []
    rule_19_clip.append(np.fmin(rule_19_antecedent, wash_time_VeryLong))
    rule_19_clip.append(np.fmin(rule_19_antecedent, wash_speed_Fast))
    rule_19_clip.append(np.fmin(rule_19_antecedent, water_amount_More))
    rule_19_clip.append(np.fmin(rule_19_antecedent, detergent_amount_More))
    rule_19_clip.append(np.fmin(rule_19_antecedent, water_temperature_High))

    #Regla 20
    rule20_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_Greasy, dirt_type_value)
    rule20_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Large, cloth_dirtiness_value)
    rule20_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Medium, cloth_mass_value)
    rule20_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_MoreSensitive,
                                                      cloth_sensitivity_value)
    rule20_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Hard, water_hardness_value)
    rule_20_antecedent = min(rule20_dirt_type, rule20_cloth_dirtiness, rule20_cloth_mass, rule20_cloth_sensitivity,
                             rule20_water_hardness)

    rule_20_clip = []
    rule_20_clip.append(np.fmin(rule_20_antecedent, wash_time_VeryLong))
    rule_20_clip.append(np.fmin(rule_20_antecedent, wash_speed_VeryFast))
    rule_20_clip.append(np.fmin(rule_20_antecedent, water_amount_More))
    rule_20_clip.append(np.fmin(rule_20_antecedent, detergent_amount_More))
    rule_20_clip.append(np.fmin(rule_20_antecedent, water_temperature_High))

    #Regla 21
    rule21_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_LessGreasy, dirt_type_value)
    rule21_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Large, cloth_dirtiness_value)
    rule21_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Medium, cloth_mass_value)
    rule21_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                      cloth_sensitivity_value)
    rule21_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Moderate, water_hardness_value)
    rule_21_antecedent = min(rule21_dirt_type, rule21_cloth_dirtiness, rule21_cloth_mass, rule21_cloth_sensitivity,
                             rule21_water_hardness)

    rule_21_clip = []
    rule_21_clip.append(np.fmin(rule_21_antecedent, wash_time_Long))
    rule_21_clip.append(np.fmin(rule_21_antecedent, wash_speed_Fast))
    rule_21_clip.append(np.fmin(rule_21_antecedent, water_amount_More))
    rule_21_clip.append(np.fmin(rule_21_antecedent, detergent_amount_More))
    rule_21_clip.append(np.fmin(rule_21_antecedent, water_temperature_High))

    #Regla 22
    rule22_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_Greasy, dirt_type_value)
    rule22_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule22_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Heavy, cloth_mass_value)
    rule22_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                      cloth_sensitivity_value)
    rule22_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Hard, water_hardness_value)
    rule_22_antecedent = min(rule22_dirt_type, rule22_cloth_dirtiness, rule22_cloth_mass, rule22_cloth_sensitivity,
                             rule22_water_hardness)

    rule_22_clip = []
    rule_22_clip.append(np.fmin(rule_22_antecedent, wash_time_Long))
    rule_22_clip.append(np.fmin(rule_22_antecedent, wash_speed_Fast))
    rule_22_clip.append(np.fmin(rule_22_antecedent, water_amount_More))
    rule_22_clip.append(np.fmin(rule_22_antecedent, detergent_amount_More))
    rule_22_clip.append(np.fmin(rule_22_antecedent, water_temperature_High))

    #Regla 23
    rule23_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_Greasy, dirt_type_value)
    rule23_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Large, cloth_dirtiness_value)
    rule23_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule23_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                      cloth_sensitivity_value)
    rule23_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Hard, water_hardness_value)
    rule_23_antecedent = min(rule23_dirt_type, rule23_cloth_dirtiness, rule23_cloth_mass, rule23_cloth_sensitivity,
                             rule23_water_hardness)

    rule_23_clip = []
    rule_23_clip.append(np.fmin(rule_23_antecedent, wash_time_Long))
    rule_23_clip.append(np.fmin(rule_23_antecedent, wash_speed_Fast))
    rule_23_clip.append(np.fmin(rule_23_antecedent, water_amount_Normal))
    rule_23_clip.append(np.fmin(rule_23_antecedent, detergent_amount_More))
    rule_23_clip.append(np.fmin(rule_23_antecedent, water_temperature_High))

    #Regla 24
    rule24_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_Greasy, dirt_type_value)
    rule24_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Large, cloth_dirtiness_value)
    rule24_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Heavy, cloth_mass_value)
    rule24_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                      cloth_sensitivity_value)
    rule24_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Soft, water_hardness_value)
    rule_24_antecedent = min(rule24_dirt_type, rule24_cloth_dirtiness, rule24_cloth_mass, rule24_cloth_sensitivity,
                             rule24_water_hardness)

    rule_24_clip = []
    rule_24_clip.append(np.fmin(rule_24_antecedent, wash_time_Long))
    rule_24_clip.append(np.fmin(rule_24_antecedent, wash_speed_Fast))
    rule_24_clip.append(np.fmin(rule_24_antecedent, water_amount_Normal))
    rule_24_clip.append(np.fmin(rule_24_antecedent, detergent_amount_More))
    rule_24_clip.append(np.fmin(rule_24_antecedent, water_temperature_High))

    #Regla 25
    rule25_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_LessGreasy, dirt_type_value)
    rule25_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule25_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Light, cloth_mass_value)
    rule25_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_NotSensitive,
                                                      cloth_sensitivity_value)
    rule25_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Moderate, water_hardness_value)
    rule_25_antecedent = min(rule25_dirt_type, rule25_cloth_dirtiness, rule25_cloth_mass, rule25_cloth_sensitivity,
                             rule25_water_hardness)

    rule_25_clip = []
    rule_25_clip.append(np.fmin(rule_25_antecedent, wash_time_VeryShort))
    rule_25_clip.append(np.fmin(rule_25_antecedent, wash_speed_VerySlow))
    rule_25_clip.append(np.fmin(rule_25_antecedent, water_amount_Less))
    rule_25_clip.append(np.fmin(rule_25_antecedent, detergent_amount_Less))
    rule_25_clip.append(np.fmin(rule_25_antecedent, water_temperature_Low))

    #Regla 26
    rule26_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_LessGreasy, dirt_type_value)
    rule26_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule26_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Medium, cloth_mass_value)
    rule26_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                      cloth_sensitivity_value)
    rule26_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Moderate, water_hardness_value)
    rule_26_antecedent = min(rule26_dirt_type, rule26_cloth_dirtiness, rule26_cloth_mass, rule26_cloth_sensitivity,
                             rule26_water_hardness)

    rule_26_clip = []
    rule_26_clip.append(np.fmin(rule_26_antecedent, wash_time_Short))
    rule_26_clip.append(np.fmin(rule_26_antecedent, wash_speed_Medium))
    rule_26_clip.append(np.fmin(rule_26_antecedent, water_amount_Normal))
    rule_26_clip.append(np.fmin(rule_26_antecedent, detergent_amount_Normal))
    rule_26_clip.append(np.fmin(rule_26_antecedent, water_temperature_Low))

    #Regla 27
    rule27_dirt_type = fuzz.interp_membership(dirt_type, dirt_type_LessGreasy, dirt_type_value)
    rule27_cloth_dirtiness = fuzz.interp_membership(cloth_dirtiness, cloth_dirtiness_Small, cloth_dirtiness_value)
    rule27_cloth_mass = fuzz.interp_membership(cloth_mass, cloth_mass_Heavy, cloth_mass_value)
    rule27_cloth_sensitivity = fuzz.interp_membership(cloth_sensitivity, cloth_sensitivity_LessSensitive,
                                                      cloth_sensitivity_value)
    rule27_water_hardness = fuzz.interp_membership(water_hardness, water_hardness_Moderate, water_hardness_value)
    rule_27_antecedent = min(rule27_dirt_type, rule27_cloth_dirtiness, rule27_cloth_mass, rule27_cloth_sensitivity,
                             rule27_water_hardness)

    rule_27_clip = []
    rule_27_clip.append(np.fmin(rule_27_antecedent, wash_time_Medium))
    rule_27_clip.append(np.fmin(rule_27_antecedent, wash_speed_Fast))
    rule_27_clip.append(np.fmin(rule_27_antecedent, water_amount_Normal))
    rule_27_clip.append(np.fmin(rule_27_antecedent, detergent_amount_Normal))
    rule_27_clip.append(np.fmin(rule_27_antecedent, water_temperature_Medium))

    # Combina todas las reglas en una lista
    rule_list = [rule_1_clip, rule_2_clip, rule_3_clip, rule_4_clip, rule_5_clip,
                 rule_6_clip, rule_7_clip, rule_8_clip,rule_9_clip,rule_10_clip,
                 rule_11_clip, rule_12_clip, rule_13_clip, rule_14_clip, rule_15_clip,
                 rule_16_clip,rule_17_clip, rule_18_clip,rule_19_clip, rule_20_clip,
                 rule_21_clip, rule_22_clip, rule_23_clip, rule_24_clip, rule_25_clip,
                 rule_26_clip, rule_27_clip]

    # Lista para almacenar los resultados
    ans_list = []
    # Itera sobre cada salida en la lista de salidas
    for output_idx, output in enumerate(output_list):
        # Inicializa con la primera regla
        x = rule_list[0]
        # Itera sobre todas las reglas en la lista
        for rule_idx in range(1, len(rule_list)):
            # Toma la siguiente regla
            if rule_idx == 1:
                x = x[output_idx]
            y = rule_list[rule_idx]
            x = np.fmax(x, y[output_idx])
            # Calcula el resultado final para la salida actual usando el centroide y redondearlo a 2 decimales
        ans = round(fuzz.defuzz(output, x, 'centroid'), 2)
        # Agrega el resultado a la lista de resultados
        ans_list.append(ans)
        #Devuelve la lista de resultados
    return ans_list


class MyWindow:
    def __init__(self, win):
        self.win = win
        self.canvas = Canvas(win, width=1000, height=600)
        self.canvas.pack()

        # Establecer colores para el gradiente de fondo
        start_color = (173, 216, 230)  # Azul claro: '#ADD8E6'
        end_color = (255, 255, 255)  # Blanco: '#FFFFFF'

        # Dibujar el gradiente en el canvas
        for i in range(600):
            # Calcular el color para esta fila de píxeles
            r = int(start_color[0] + (end_color[0] - start_color[0]) * i / 600)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * i / 600)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * i / 600)
            color = '#{:02x}{:02x}{:02x}'.format(r, g, b)

            self.canvas.create_line(0, i, 1000, i, fill=color)

        self.image_ipn = Image.open("ipn.jpg")
        self.photo_ipn = ImageTk.PhotoImage(self.image_ipn)

        # Crear un label para la imagen ipn.jpg
        self.img_label_ipn = Label(win, image=self.photo_ipn)
        self.img_label_ipn.place(x=215, y=1)

        self.image_escom = Image.open("escom.png")
        self.photo_escom = ImageTk.PhotoImage(self.image_escom)
        self.img_label_escom = Label(win, image=self.photo_escom)
        self.img_label_escom.place(x=700, y=1)

        self.title_part1 = Label(win, text="Instituto Politécnico Nacional", font='Helvetica 11 bold', fg='maroon')
        self.title_part1.place(x=400, y=10)

        self.title_part2 = Label(win, text="Escuela Superior de Cómputo", font='Helvetica 10 bold', fg='#000080')
        self.title_part2.place(x=405, y=30)

        self.subtitle = Label(win, text="Práctica No. 4 'Lavadora con Lógica Difusa'", font='Helvetica 12 bold', fg='magenta')
        self.subtitle.place(x=330, y=63)

        self.subtitle = Label(win, text="Inteligencia Artificial", font='Helvetica 10 bold', fg="purple")
        self.subtitle.place(x=430, y=83)

        self.intro = Label(win, text="Datos de Entrada", font='Helvetica 10 bold', fg="red").place(x=125, y=125)
        self.intro = Label(win, text="Información", font='Helvetica 10 bold', fg="red").place(x=350, y=125)

        self.lbl1 = Label(win, text='Tipo de Suciedad').place(x=50, y=165)
        self.lbl2 = Label(win, text='Nivel de Suciedad').place(x=50, y=200)
        self.lbl3 = Label(win, text='Masa de tela').place(x=50, y=235)
        self.lbl4 = Label(win, text='Delicadez de la Ropa').place(x=50, y=270)
        self.lbl5 = Label(win, text='Dureza del Agua').place(x=50, y=305)
        self.lblA1 = Label(win, text='Duración del Lavado').place(x=32, y=400)
        self.lblA2 = Label(win, text='Velocidad de Lavado').place(x=32, y=435)
        self.lblA3 = Label(win, text='Cantidad de Agua').place(x=32, y=470)
        self.lblA4 = Label(win, text='Cantidad de Detergente').place(x=32, y=505)
        self.lblA5 = Label(win, text='Temperatura del Agua').place(x=32, y=540)

        # Crea los campos de entrada
        self.t1 = Entry(bd=5)
        self.t2 = Entry(bd=5)
        self.t3 = Entry(bd=5)
        self.t4 = Entry(bd=5)
        self.t5 = Entry(bd=5)

        self.tA1 = Entry(bd=5)
        self.tA2 = Entry(bd=5)
        self.tA3 = Entry(bd=5)
        self.tA4 = Entry(bd=5)
        self.tA5 = Entry(bd=5)

        self.t1.place(x=160, y=165)
        self.t2.place(x=160, y=200)
        self.t3.place(x=160, y=235)
        self.t4.place(x=160, y=270)
        self.t5.place(x=160, y=305)
        self.tA1.place(x=160, y=400)
        self.tA2.place(x=160, y=435)
        self.tA3.place(x=160, y=470)
        self.tA4.place(x=160, y=505)
        self.tA5.place(x=160, y=540)

        self.info1 = Label(win, text='No grasiento (0)........Grasiento (100)').place(x=300, y=165)
        self.info1 = Label(win, text='Limpio (0).................Sucio (100)').place(x=300, y=200)
        self.info1 = Label(win, text='Ligero (0)................Pesado (100)').place(x=300, y=235)
        self.info1 = Label(win, text='No sensible (0).........Sensible (100)').place(x=300, y=270)
        self.info1 = Label(win, text='Suave (0)...................Duro (100)').place(x=300, y=305)

        self.info1 = Label(win, text='Minutos (mins)').place(x=300, y=400)
        self.info1 = Label(win, text='Revoluciones por Minuto (rpm)').place(x=300, y=435)
        self.info1 = Label(win, text='Litros (l)').place(x=300, y=470)
        self.info1 = Label(win, text='Mililitros (ml)').place(x=300, y=505)
        self.info1 = Label(win, text='Grados Celsius (°C)').place(x=300, y=540)

        # Botón de ayuda
        self.btn_help = Button(win, text='Ayuda', command=self.show_help, height=1, width=8, bg='orange', fg='white')
        self.btn_help.place(x=930, y=10)

        #Boton Lavado
        self.btn1 = Button(win, text='Predict')
        self.b1 = Button(win, text='COMENZAR LAVADO', command=self.predict, height=1, width=20, bg='red', fg='white')
        self.b1.place(x=325, y=340)

        self.image = Image.open("lavadora.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.img_label = Label(win, image=self.photo)
        self.img_label.place(x=570, y=150)

    def show_help(self):
        # Función para mostrar la ventana de ayuda
        help_text = "Instrucciones de uso:\n\n1. Ingrese los datos solicitados en los campos de entrada.\n2. Haga clic en 'COMENZAR LAVADO' para predecir los resultados.\n3. Los resultados se mostrarán en los campos de salida."
        messagebox.showinfo("Ayuda", help_text)

    def predict(self):
        # Limpia los campos de salida
        self.tA1.delete(0, END)
        self.tA2.delete(0, END)
        self.tA3.delete(0, END)
        self.tA4.delete(0, END)
        self.tA5.delete(0, END)
        # Obtiene los resultados de la función
        try:
            results = test(float(self.t1.get()),
                           float(self.t2.get()),
                           float(self.t3.get()),
                           float(self.t4.get()),
                           float(self.t5.get()))

            # Inserta los resultados en los campos de salida
            self.tA1.insert(END, str(results[0]))
            self.tA2.insert(END, str(results[1]))
            self.tA3.insert(END, str(results[2]))
            self.tA4.insert(END, str(results[3]))
            self.tA5.insert(END, str(results[4]))
        except Exception as e:
            # Muestra un mensaje de error si ocurre una excepción
            messagebox.showerror("Ocurrió un Error",
                                 "¡Inténtelo de Nuevo!\nSugerencia:Ccompruebe que TODOS los espacios de entrada estén llenos de NÚMEROS")



class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio")
        self.root.geometry("600x450")

        self.label_instituto = Label(self.root, text="\n\nInstituto Politécnico Nacional", fg="maroon",
                                     font=("Arial", 11, "bold"))
        self.label_instituto.pack()

        self.label_escuela = Label(self.root, text="Escuela Superior de Cómputo\n", fg="blue",font=("Arial", 10, "bold"))
        self.label_escuela.pack()

        self.label_practica = Label(self.root, text="Práctica No.4 'Lavadora con Lógica Difusa'\n", fg="purple",
                                     font=("Arial", 13, "bold"))
        self.label_practica.pack()

        self.label_integrantes = Label(self.root, text="Integrantes del Equipo:\n"
                                                       "Hernández Hernández Jorge Gabriel\n"
                                                       "Farrera Méndez Emmanuel Sinai\n", font=("Arial", 10, "bold"))
        self.label_integrantes.pack()

        self.label_grupo = Label(self.root, text="Grupo: 6CM2\n",font=("Arial", 10, "bold"))
        self.label_grupo.pack()

        self.label_unidad = Label(self.root, text="Unidad de Aprendizaje: Inteligencia Artificial\n", font=("Arial", 10, "bold"))
        self.label_unidad.pack()

        self.label_profesor = Label(self.root, text="Profesor: Rodolfo Romero Herrera\n", font=("Arial", 10, "bold"))
        self.label_profesor.pack()

        self.btn_start = Button(self.root, text="Comenzar", command=self.open_main_window,font=("Arial", 13, "bold"))
        self.btn_start.pack(pady=35)

    def open_main_window(self):
        self.root.destroy()  # Cerrar la ventana de inicio
        main_window = Tk()
        my_window = MyWindow(main_window)
        main_window.title('Sistema de Control de Lavado')
        main_window.geometry("1000x600")
        main_window.mainloop()

if __name__ == "__main__":
    window = Tk()
    main_window = MainWindow(window)
    window.mainloop()


