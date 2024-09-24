% Mean Shift Clustering

% Generación de Datos Aleatorios
rng(1); % Fijar la semilla para reproducibilidad
data = [randn(100,2)*0.75 + ones(100,2);   % Datos del Clúster 1 (centrado en [1, 1])
        randn(100,2)*0.5 - ones(100,2)];  % Datos del Clúster 2 (centrado en [-1, -1])

% Visualización de Datos (ANTES del Clustering)
figure;
scatter(data(:,1), data(:,2));  
title('Conjunto de Datos Aleatorios');
xlabel('Dimensión 1');
ylabel('Dimensión 2');

% Aplicación de Mean Shift
bandwidth = 1.0;  % Parámetro de ancho de banda (radio de búsqueda)
[cluster_centers, assignments] = MeanShiftCluster(data, bandwidth);

% Visualización de Resultados (DESPUÉS del Clustering)
figure;
gscatter(data(:,1), data(:,2), assignments);  % Colorea los puntos según su clúster
hold on;
plot(cluster_centers(:,1), cluster_centers(:,2), 'kx', 'MarkerSize', 15, 'LineWidth', 3); % Marca los centroides
title('Resultados de Mean Shift Clustering');
xlabel('Dimensión 1');
ylabel('Dimensión 2');
legend({'Cluster 1', 'Cluster 2', 'Centroides'}); % Leyenda para los elementos del gráfico
hold off;

% Función MeanShiftCluster
function [cluster_centers, assignments] = MeanShiftCluster(data, bandwidth)
    [n, ~] = size(data);
    cluster_centers = [];  % Inicialmente vacío
    assignments = zeros(n, 1);
    
    for i = 1:n
        x = data(i, :);    % Punto actual a analizar
        while true
            distances = sqrt(sum((data - x).^2, 2));  % Distancias a todos los puntos
            within_bandwidth = distances <= bandwidth; % Puntos dentro del radio
            new_center = mean(data(within_bandwidth, :), 1); % Nueva media
            
            % Condición de parada: el centro ya no se mueve significativamente
            if norm(new_center - x) < 1e-5
                break; 
            end
            x = new_center;  % Actualizar el centro
        end
        
        % Asignar el punto al clúster correspondiente
        if isempty(cluster_centers) || ~ismember(x, cluster_centers, 'rows')
            cluster_centers = [cluster_centers; x]; % Agregar nuevo centro
        end
        [~, cluster_index] = ismember(x, cluster_centers, 'rows');
        assignments(i) = cluster_index;
    end
end