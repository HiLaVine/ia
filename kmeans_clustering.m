% K-means Clustering

% Generar datos aleatorios (dos grupos gaussianos)
rng(1); % Para reproducibilidad
data = [randn(100,2)*0.75 + ones(100,2);  % Grupo 1
        randn(100,2)*0.5 - ones(100,2)]; % Grupo 2

% Visualización de los datos originales
figure;
scatter(data(:,1), data(:,2), 'o');
title('Datos originales');
xlabel('Característica 1');
ylabel('Característica 2');

% Aplicar K-means
k = 2; % Número de clusters
[idx, centroids] = kmeans(data, k);

% Resultados
fprintf('Centroides encontrados:\n');
disp(centroids);

figure;
gscatter(data(:,1), data(:,2), idx, 'br', 'o'); % 'br' para colores azul y rojo
hold on;
plot(centroids(:,1), centroids(:,2), 'kx', 'MarkerSize', 15, 'LineWidth', 3); 
title('Resultados de K-means');
xlabel('Característica 1');
ylabel('Característica 2');
legend('Cluster 1', 'Cluster 2', 'Centroides');
hold off;