#!/usr/bin/env python
# coding: utf-8

# # Problem set 1 
# 
# Emma Marshall <br>
# 9/13/2022

# ## Importing packages and defining functions: 

# In[1]:


import numpy as np
import math
import pint
import datetime as dt

from pint import UnitRegistry

ureg = UnitRegistry()


# In[2]:


def sci_notation(input_quantity):
    
    return '{:.3E}'.format(input_quantity)


# In[3]:


def calc_irradiance(d, radiant_flux):

    sigma = 4*np.pi*(d**2)
    print(sci_notation(sigma))
    irradiance = radiant_flux / sigma
    
    return irradiance


# In[4]:


def calc_declination(j):
    '''takes j for day of year, returns declination angle in degrees'''
    delta = 23.45*math.cos(math.radians((360*(j-172))/365))
    
    return delta


# In[5]:


def calc_zenith(delta, beta, hour_angle):
    '''takes declination, beta and hour angle values in degrees, returns zenith angle value in degrees'''
    cos_theta  = ((math.sin(math.radians(delta)))*(math.sin(math.radians(beta)))) + \
    (math.cos(math.radians(delta))*(math.cos(math.radians(beta))) * (math.cos(math.radians(hour_angle))))
    
    theta_deg = math.degrees(math.acos(cos_theta))
    
    return theta_deg
     


# In[6]:


def calc_azimuth(delta, beta, hour_angle):
    '''takes declination, beta and hour angle values in degrees, returns azimuth angle value in degrees'''
    tan_phi = (math.cos(math.radians(delta))* math.sin(math.radians(hour_angle)))/ \
    ((math.cos(math.radians(delta)) * math.sin(math.radians(beta))* math.cos(math.radians(hour_angle))) - \
     (math.sin(math.radians(delta))*math.cos(math.radians(beta))))
    
    phi_deg = math.degrees(math.atan(tan_phi))
     
    return phi_deg
    


# In[7]:


def equation_of_time(j):
    '''takes j for DOY returns eqation of time in minuets'''
    b = 360*(j-81) /365
    
    et = (9.87 * math.sin(math.radians(2*b))) - (7.53*math.cos(math.radians(b))) - (1.5 * math.sin(math.radians(b)))
    
    return et


# ## Problem 1
# 
# **1. Convert 136 THz to wavelength in μm. What name do we give this spectral region?**
# 
# c = v * lambda
# 
# lambda = c / v
# 
# 136 THz = 136 x 10^12 Hz = 136 * 10^12 s^-1

# In[8]:


c = 3e8 *ureg.meters / ureg.seconds
v1 = 136e12 / ureg.seconds


# In[9]:


lambda_1 = c/v1
lambda_1


# 2.205 * 10^-6 m = **2.2 um SWIR region of EM spectrum**

# ## Problem 2
# 
# **2. Convert 1150 nm to frequency (in THz) and to wavenumber (in cm-1). What name do we give
# this spectral region?**
# 
# v = c / lambda

# In[10]:


lambda_2 = 1150e-9 *ureg.meters
lambda_2


# In[11]:


v_2 = c / lambda_2
sci_notation(v_2)


# 2.609 * 10^14 Hz = **261 THz SWIR region of EM spectrum**
# 
# now calculate wavenumber:
# 
# lambda = 1150 * 10^-9 m (* 100 cm/m) = 1150 * 10 ^-7 cm
# 
# **wavenumber = 1 / 1150 * 10^-7cm = 1/1.15 * 10^-4 cm**

# ## Problem 3
# 
# 3. Kopp and Lean (2011) found that the sunspot cycle minimum value for exoatmospheric solar 
# irradiance (E0) is 1361 Wm-2 at the mean Earth-sun distance of 1.496 x 1011 m. <br>
#     a. Based on this value of E0, what is the radiant flux (in Watts) of the sun? Hint: It’s a big
# number. <br>
#     b. What is exoatmospheric solar irradiance at perihelion (1.471 x 1011m)? <br>
#     c. What is exoatmospheric solar irradiance at aphelion (1.521 x 1011m)? <br>

# ###     a. Based on this value of E0, what is the radiant flux (in Watts) of the sun? Hint: It’s a big number. 

# In[12]:


e_S_mean = 1.496e11 * ureg.meters
print(sci_notation(e_S_mean))

toa_E = 1361 *ureg.watts / (ureg.meters**2)
print(toa_E)


# In[13]:


sigma = 4*np.pi * (e_S_mean**2)
sigma


# In[14]:


radiant_flux = toa_E * sigma
print('Radiant flux of the sun is: ', radiant_flux)


# ###     b. What is exoatmospheric solar irradiance at perihelion (1.471 x 1011m)? <br>
# 
# E = radiant flux / sigma
# 
# Have radiant flux, want to calculate E for sigma when d = d_perihelion
# 

# In[15]:


perihelion_d = 1.471e11 * ureg.meters

sci_notation(perihelion_d)

sigma_perihelion = 4*np.pi*(perihelion_d**2)

print('exoatmospheric solar irradiance at perihelion is: ', radiant_flux / sigma_perihelion)


# ###     c. What is exoatmospheric solar irradiance at aphelion (1.521 x 1011m)? <br>
# 
# E = radiant_flux/sigma
# 
# calculate E for sigma when d = d_aphelion

# In[16]:


aphelion_d = 1.521e11 * ureg.meters

sigma_aphelion = 4*np.pi*(aphelion_d**2)

print('exoatmospheric solar irradiance at aphelion is: ', radiant_flux / sigma_aphelion)


# ## Problem 4
# 
# ```{note} 
# I've been playing around with a python package that handles units but don't have it quite figured out yet - the units on some of the quantities with `ureg.XXXX` aren't always correct! The units on paper should be
# ```

# 1. Convert wavelength to m

# 0.8 um = 0.8 * 10^-6 m

# In[17]:


wavelength = 0.8e-6 * ureg.meters
wavelength


# 2. convert radiance from W cm-2 sr-1 nm-1 to W m-2 sr-1 m-1

# In[18]:


L_lambda = 2.1e3 *ureg.watts / (ureg.centimeters**2) / ureg.nanometers / ureg.steradian
L_lambda / 0.0001 *ureg.meters**2 / 1e-9 *ureg.meter


# L_lambda = 2.1 * 10^16 W m^-2 sr^-1 m^-1

# 3. Use eqn 1.7:
# 
# L_v = (L_lambda * (lambda^2) )/c

# In[19]:


L_v = L_lambda * (wavelength**2) / c
L_v


# ^^ Units in the above quantity (`L_v`) incorrect <br>
# answer should be: **L_v  = 4.48 * 10^-5 W m^-2 sr^-1 s**

# In[20]:


sci_notation(2.1e3 / (0.01**2) / 1e-9)


# In[21]:


sci_notation((0.8e-6)**2)


# In[22]:


2.1*6.4/3


# ## Problem 5
# 
# 39 deg N, 110.15 deg W <br>
# 10/7/2022

# ### a. solar zenith and azimuth angles at solar noon

# In[23]:


beta_gr = 39
lambda_gr = -110.15
j_oct7 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 +30 + 7


# In[24]:


delta_oct7 = calc_declination(j_oct7)
delta_oct7


# In[25]:


theta_oct7_solar_noon = calc_zenith(delta_oct7, beta_gr, 0)
theta_oct7_solar_noon


# In[26]:


phi_oct7_solar_noon = calc_azimuth(delta_oct7, beta_gr, 0)
phi_oct7_solar_noon


# ### b. solar zentih and azimuth angles at 6:30 pm

# use equation of time, DST, position within time zone to find time of solar noon, find difference btw solar noon time and 6:30 pm to find hour angle, solve for zenith, azimuth:

# In[27]:


et_oct7 = equation_of_time(j_oct7)
et_oct7


# In[28]:


noon = dt.time(hour=12)
noon 
et_time = dt.timedelta(minutes = et_oct7)
et_time


# In[29]:


'12:{}'.format(np.round(60*float(str(et_oct7)[2:]))) #this is the amount of minutes ahead of noon at which solar noon occurs


# So before taking into account DST, position within time zone, solar noon occurs at 11:47:02
# 
# After DST: 12:47:02

# taking into account position within time zone:

# In[30]:


central_meridian = 105


# In[31]:


longitude_offset = np.abs(lambda_gr) - central_meridian

longitude_adjustment = np.round(longitude_offset * 4) *ureg.minutes
longitude_adjustment


# Solar noon in Green River on October 7: 12:47:02 + 21 minutes = 1:08:02 pm

# Time difference between solar noon, target time (6:30 pm):
# 
# 6 hr 21 min 58 sec <br>
# as a decimal: 

# In[32]:


5+(22/60)


# Now calculate hour angle: 

# In[33]:


hour_angle_time = (5 + (22/60)) * ureg.hours

hour_angle = - (hour_angle_time * 15 * ureg.degrees / ureg.hours)
hour_angle # negative because pm


# In[34]:


gr_zenith_6pm = calc_zenith(delta_oct7, beta_gr, -80.5)


# In[35]:


gr_zenith_6pm


# In[36]:


gr_azimuth_6pm = calc_azimuth(delta_oct7, beta_gr, -80.5)


# In[37]:


gr_azimuth_6pm


# ### c. ratio of irradiance at 6:30 pm to irradiance at solar noon
# 
# Use lambert's cosine law
# 
# E_theta = E_nought(cos_theta)

# In[38]:


math.cos(math.radians(gr_zenith_6pm))


# ## Problem 6
# 
# Assuming same date, loc as prob 5. E_10am = 395 Wm2 <br>
# Find E_2pm on 20 deg S-facing slope

# In[39]:


E_10am = 395 *ureg.watts / ureg.meters**2
E_10am


# 1. Use Lambert's cosine law to find irradiance at solar noon (first need to find theta_10am)
# 
# Time difference btw 10 am, 1:08:02 pm = 3:08:02
# 
# as a decimal:

# In[40]:


time_diff_10a = 3 + (8/60)


# In[41]:


time_diff_10a


# In[42]:


hour_angle_10a = time_diff_10a * 15 * ureg.degrees


# In[43]:


hour_angle_10a


# Now can calculate zenith angle at 10 am:

# In[44]:


gr_theta_10a = calc_zenith(delta_oct7, beta_gr, 47) * ureg.degrees
gr_theta_10a


# Irradiance at solar noon:

# In[45]:


E_solar_noon = E_10am / math.cos(math.radians(63.041))
E_solar_noon


# Will use the equation for cos(theta) of a sloped surface to solve for irradiance at the sloped surface at 2pm. First need zenith and azimuth at 2pm
# 
# time difference btw 2pm, solar noon = 51 mins 58 sec. as a decimal: 

# In[46]:


time_diff_2p = (52/60)
hour_angle_2p = time_diff_2p * 15 *ureg.degrees
hour_angle_2p #negative because afternoon


# In[47]:


theta_2pm = calc_zenith(-6.68, 39, -13)
theta_2pm


# In[48]:


phi_2pm = calc_azimuth(-6.68, 39, -13)
phi_2pm


# In[49]:


slope = 20
exposure = 0


# Now, use equation for cos(theta) on a sloped surface to solve for cos_theta

# In[50]:


def calc_zenith_slope(theta, slope, phi, exposure):
    
    cos_theta_slope = math.cos(math.radians(theta)) * math.cos(math.radians(slope))  + math.sin(math.radians(theta))*math.sin(math.radians(slope))*math.cos(math.radians(phi - exposure))
    
    return cos_theta_slope


# In[51]:


cos_theta_slope = calc_zenith_slope(theta_2pm, slope, phi_2pm, exposure)
cos_theta_slope


# In[52]:


E_2pm_slope = E_solar_noon * cos_theta_slope
E_2pm_slope


# In[ ]:




