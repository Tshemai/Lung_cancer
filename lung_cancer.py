import json
from matplotlib import pyplot as plt
from matplotlib.patches import Patch

# Load the data into a list.
filename = 'dataset.json'
with open(filename) as f:
    pop_data = json.load(f)

"""List of demographics """
f_with_lc, m_with_lc, m_witho, f_witho = [ ], [ ], [ ], [ ],
fsm_wlc, msm_wlc, o50ms_wlc, o50fs_wlc = [ ], [ ], [ ], [ ]
u50ms_wlc, u50fs_wlc = [ ], [ ]
for pop_dict in pop_data:
     if pop_dict["LUNG_CANCER"] == "YES":
        if pop_dict["GENDER"] == "F":
           f_with_lc.append(pop_dict["GENDER"])
           """female smokers with lung cancer"""
           if pop_dict["SMOKING"] == 1:
                fsm_wlc.append(pop_dict["SMOKING"])
                """over and under 50 female smokers with lung cancer"""
                if pop_dict["AGE"]>50:
                      o50fs_wlc.append(pop_dict["AGE"])
                else:
                      u50fs_wlc.append(pop_dict["AGE"])
           else:
                  msm_wlc.append(pop_dict["SMOKING"])
                 
                
        else:
            m_with_lc.append(pop_dict["GENDER"])
            """male smokers with lung cancer"""
            if pop_dict["SMOKING"] == "1":
                msm_wlc.append(pop_dict["SMOKING"])
                """over and under 50 male smokers with lung cancer"""
                if pop_dict["AGE"] > 50:
                    o50ms_wlc.append(pop_dict["AGE"])
                else:
                    u50ms_wlc.append(pop_dict["AGE"])

     else:
        if pop_dict["GENDER"] == "F":
            f_witho.append(pop_dict["GENDER"])
        else:
            m_witho.append(pop_dict["GENDER"])

#number of the demographic
nbr_fwlc = len(f_with_lc)
nbr_mwlc = len(m_with_lc)
nbr_mwtho =len(m_witho)
nbr_fwtho = len(f_witho)
nbr_fswlc= len(fsm_wlc)
nbr_mswlc = len(msm_wlc)
nbr_o50fswlc = len(o50fs_wlc)
nbr_u50fswlc = len(u50fs_wlc)
nbr_o50mswlc = len(o50ms_wlc)
nbr_u50mswlc = len(u50ms_wlc)

# total count of people
total_people = nbr_fwlc + nbr_mwlc + nbr_mwtho + nbr_fwtho
# dictionary to store the data
data = {
      'female_nolc' : nbr_fwtho,
      'male_nolc' : nbr_mwtho,
      'female_lc' : nbr_fwlc,
      'male_lc' : nbr_mwlc,
      'female_skwlc' : nbr_fswlc,
      'male_skwlc' : nbr_mswlc,
      'U50female_skwlc' : nbr_u50fswlc,
      'U50male_skwlc' : nbr_mswlc,
      'O50female_skwlc' : nbr_o50fswlc,
      'O50male_skwlc' : nbr_o50mswlc
      }

catagories = list(data.keys())
count = list(data.values())
      
# making a color map
color_map = {
    'MALE' : '#0000ff',
    'FEMALE' : '#ff69b4'
    }
# making a list of colors
colors = [ color_map['FEMALE'], color_map['MALE'], color_map['FEMALE'],
               color_map['MALE'], color_map['FEMALE'], color_map['MALE'],
               color_map['FEMALE'], color_map['MALE'],color_map['FEMALE'],
           color_map['MALE']]

# plotting the bar graph
plt.bar(catagories, count, color=colors)
plt.xlabel('male and female demography')
plt.xticks(rotation=45)
plt.ylabel('count of the demographics')
plt.title('Demography of people with lung-cancer')

legend_elements = [
    Patch(facecolor = '#ff69b4', label = 'FEMALE'),
    Patch(facecolor = '#0000ff', label = 'MALE')
    ]
plt.legend( handles =legend_elements, loc = 'upper right')
plt.tight_layout()
plt.show()
