clearvars
close all
clc

load('C:\Users\sinna\MATLAB Drive\MobileSensorData\sensorlog_20240314_211402.mat')

figure
geoplot(Position.latitude, Position.longitude, 'LineWidth', 10)