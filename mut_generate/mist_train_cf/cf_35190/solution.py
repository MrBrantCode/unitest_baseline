"""
QUESTION:
The function `process_seismic_observations` receives a list of seismic observations `st_obs`, an event `event`, and a boolean `noise`. The function must replace the channel name of the third observation in `st_obs` by replacing any occurrence of "X" with "H", trim the start and end times of the third observation to be from the event's origin time to 800 seconds after the origin time, and return the updated `st_obs` list. If `noise` is True, the function must also return a list of three file names representing noise data for the BHE, BHN, and BHZ channels.
"""

def entrance(st_obs, event, noise):
    # Replace the channel name of the third seismic observation
    st_obs[2].stats.channel = st_obs[2].stats.channel.replace("X", "H")

    # Trim the start and end times of the third seismic observation
    st_obs[2].trim(starttime=event.origin_time, endtime=event.origin_time + 800.0)

    if noise:
        # Set the Path variable for noise data
        Path = "/home/nienke/Documents/Research/Data/Noise/"
        
        # Populate the File_names list with noise data file names
        File_names = [
            "XB.02.ELYSE.BHE-2019.274T0809-2019.274T0920",
            "XB.02.ELYSE.BHN-2019.274T0809-2019.274T0920",
            "XB.02.ELYSE.BHZ-2019.274T0809-2019.274T0920",
        ]
        
        return st_obs, File_names
    else:
        return st_obs