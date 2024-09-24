% Modelo de Mezcla Gaussiana Mejorado

% Generar datos aleatorios con mayor control y variedad
rng(1); % Fijar la semilla para reproducibilidad

% Parámetros para mayor flexibilidad
num_clusters = 2; % Número de clusters (grupos) a modelar
num_samples_per_cluster = 100; % Muestras por cluster
cluster_means = [1 1; -1 -1]; % Medias de los clusters (personalizable)
cluster_covariances = cat(3, [0.75 0; 0 0.75], [0.5 0; 0 0.5]); % Covarianzas (forma de los clusters)

% Generar datos agrupados
data = [];
for i = 1:num_clusters
    data = [data; mvnrnd(cluster_means(i,:), cluster_covariances(:,:,i), num_samples_per_cluster)];
end

% Visualizar los datos originales
figure;
scatter(data(:,1), data(:,2), [], 'filled'); % Marcadores rellenos para mejor visualización
title('Conjunto de Datos Aleatorios Agrupados');
xlabel('Dimensión 1'); ylabel('Dimensión 2');

% Ajustar el modelo GMM con opciones adicionales
options = statset('Display','final'); % Mostrar información del ajuste
gmm_model = fitgmdist(data, num_clusters, 'Options', options, 'RegularizationValue', 0.01); % Regularización para evitar singularidades

% Visualizar los datos generados y los resultados del modelo
figure;
scatter(data(:,1), data(:,2), [], 'filled'); % Datos originales
hold on;

% Generar y visualizar muestras del modelo
generated_data = random(gmm_model, num_samples_per_cluster * num_clusters); % Mismo número total de muestras
scatter(generated_data(:,1), generated_data(:,2), [], 'filled'); % Datos generados

% Visualizar elipses de confianza de los clusters (opcional)
colors = lines(num_clusters); % Colores para cada cluster
for i = 1:num_clusters
    ezcontour(@(x,y)pdf(gmm_model,[x y]), xlim(), ylim()); % Contornos de densidad
end

% Visualizar centroides de los clusters
plot(gmm_model.mu(:,1), gmm_model.mu(:,2), 'kx', 'MarkerSize', 15, 'LineWidth', 3); 

title('Datos Originales, Datos Generados y Modelo de Mezcla Gaussiana');
legend('Datos Originales', 'Datos Generados', 'Elipses de Confianza', 'Centroides');
hold off;