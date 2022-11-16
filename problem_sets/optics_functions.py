#functions for optics 
import numpy as np
import math
import pint
import datetime as dt

def calc_irradiance(d, radiant_flux):
    '''calculate irradiance given a distance, d and radiant flux'''

    sigma = 4*np.pi*(d**2)
    print(sci_notation(sigma))
    irradiance = radiant_flux / sigma
    
    return irradiance

def calc_declination(j):
    '''takes j for day of year, returns declination angle in degrees'''
    delta = 23.45*math.cos(math.radians((360*(j-172))/365))
    
    return delta

def calc_zenith(delta, beta, hour_angle):
    '''takes declination, beta and hour angle values in degrees, returns zenith angle value in degrees'''
    cos_theta  = ((math.sin(math.radians(delta)))*(math.sin(math.radians(beta)))) + \
    (math.cos(math.radians(delta))*(math.cos(math.radians(beta))) * (math.cos(math.radians(hour_angle))))
    
    theta_deg = math.degrees(math.acos(cos_theta))
    
    return theta_deg
     
def calc_azimuth(delta, beta, hour_angle):
    '''takes declination, beta and hour angle values in degrees, returns azimuth angle value in degrees'''
    tan_phi = (math.cos(math.radians(delta))* math.sin(math.radians(hour_angle)))/ \
    ((math.cos(math.radians(delta)) * math.sin(math.radians(beta))* math.cos(math.radians(hour_angle))) - \
     (math.sin(math.radians(delta))*math.cos(math.radians(beta))))
    
    phi_deg = math.degrees(math.atan(tan_phi))
     
    return phi_deg
    
def equation_of_time(j):
    '''takes j for DOY returns eqation of time in minuets'''
    b = 360*(j-81) /365
    
    et = (9.87 * math.sin(math.radians(2*b))) - (7.53*math.cos(math.radians(b))) - (1.5 * math.sin(math.radians(b)))
    
    return et

def calc_theta2(n1, n2, theta1):
    '''snel's law - return theta2'''
    
    theta2 = math.degrees(math.asin(1 * math.sin(math.radians(theta1))/n2))
    return theta2

def fresnels3(theta1, theta2):
    '''fresnel's equation'''
    
    dif1 = theta1 - theta2
    sum1 = theta1 + theta2 
    
    ref_par = (math.tan(math.radians(theta1 - theta2)) / math.tan(math.radians(theta1 + theta2)))**2
    ref_perp = (math.sin(math.radians(theta1 - theta2)) / math.sin(math.radians(theta1 + theta2)))**2
    ref_tot = (ref_par + ref_perp)/2
    
    return ref_tot

def calc_alpha(k, l):
    '''return absorption coefficient given k and lambda'''
    return (4*np.pi*k) / l

def calc_transmittance(alpha, d):
    '''calculate transmittance thru a medium given a certain path length distance and absorption coefficient'''
    return math.exp(-alpha*d)

def beerlambert_oz(E_nought, tau_nought, theta):
    '''Beer Lambert's Law taking into account optical depth and zenith angle'''
    x = (-tau_n / math.cos(math.radians(theta)))
    
    E_theta = E_n * math.exp(x)
    
    return E_theta