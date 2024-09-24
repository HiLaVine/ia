%Tener "Transmitir a MatLab"
%m = mobiledev
%m.Logging = 1

load('C:\Users\sinna\MATLAB Drive\MobileSensorData\sensorlog_20240315_073100.mat')
figure
geoplot(Position.latitude, Position.longitude, 'LineWidth', 10)

% Definir la ubicación objetivo
objLat = 19.402372;
objLon = -99.188564;

% Crear una figura para el mapa
figure
hold on

% Definir la función haversine como función anónima
haversine = @(lat1, lon1, lat2, lon2) ...
    6371 * 2 * asin(sqrt(...
    sin(deg2rad(lat2 - lat1) / 2)^2 + ...
    cos(deg2rad(lat1)) * cos(deg2rad(lat2)) * ...
    sin(deg2rad(lon2 - lon1) / 2)^2));

while true
    % Obtener la ubicación actual
    iniLat = m.latitude;
    iniLon = m.longitude;

    % Limpiar la figura antes de trazar nuevamente
    clf

    % Trazar una línea entre la ubicación actual y el objetivo
    geoplot([iniLat objLat],[iniLon objLon],'-*')

    % Calcular los límites del mapa basados en la ubicación actual y el objetivo
    latlim = [min(iniLat, objLat), max(iniLat, objLat)];
    lonlim = [min(iniLon, objLon), max(iniLon, objLon)];
    geolimits(latlim, lonlim);

    % Cambiar el mapa base
    geobasemap streets;
    
    % Calcular la distancia entre los dos puntos utilizando la fórmula haversine
    distance_km = haversine(iniLat, iniLon, objLat, objLon);
    disp(['Distancia entre los dos puntos: ' num2str(distance_km) ' km'])
    
    % Pausa de 10 segundos antes de la próxima actualización
    pause(100);

    
end

% ctrl + c
% m.Logging = 0
% clear m