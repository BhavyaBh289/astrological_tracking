import numpy as np
from datetime import datetime

def RaDec2AzEl(Ra, Dec, lat, lon):
    current_time = datetime.utcnow()

    # Convert time to Julian Date
    JD = (current_time - datetime(2000, 1, 1)).days + (current_time - datetime(2000, 1, 1)).seconds / 86400.0 + 2451545.0

    # Calculate T_UT1 (Julian centuries since J2000.0)
    T_UT1 = (JD - 2451545.0) / 36525.0

    # Calculate ThetaGMST (Greenwich Mean Sidereal Time)
    ThetaGMST = 67310.54841 + (876600 * 3600 + 8640184.812866) * T_UT1 \
                + 0.093104 * (T_UT1 ** 2) - 6.2e-6 * (T_UT1 ** 3)
    ThetaGMST = ((ThetaGMST % 86400.0) * (ThetaGMST / abs(ThetaGMST))) / 240.0 % 360.0

    # Calculate ThetaLST (Local Sidereal Time)
    ThetaLST = ThetaGMST + lon

    # Calculate Local Hour Angle (LHA)
    LHA = (ThetaLST - Ra) % 360.0

    # Calculate Elevation (El)
    El = np.degrees(np.arcsin(np.sin(np.radians(lat)) * np.sin(np.radians(Dec)) +
                np.cos(np.radians(lat)) * np.cos(np.radians(Dec)) * np.cos(np.radians(LHA))))

    # Calculate Azimuth (Az)
    Az = (np.degrees(np.arctan2(-np.sin(np.radians(LHA)), np.cos(np.radians(LHA)) * np.sin(np.radians(lat)) -
         np.tan(np.radians(Dec)) * np.cos(np.radians(lat))))) % 360.0

    return Az, El

# Example usage:
Ra = 18.628944
Dec = 38.809389
lat =  18.5204
lon = 73.8567
Az, El = RaDec2AzEl(Ra, Dec, lat, lon)
print(f"Azimuth (Az): {Az} degrees")
print(f"Elevation (El): {El} degrees")
