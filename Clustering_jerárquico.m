% Clustering Jerárquico
% Generar datos aleatorios
rng(1); % Fijar la semilla para reproducibilidad
data = [randn(20,2)*0.75+ones(20,2);
        randn(20,2)*0.5-ones(20,2)];

% Calcular la matriz de enlace usando el método de enlace completo (complete linkage)
Z = linkage(data, 'complete');

% Visualizar el dendrograma
figure;
dendrogram(Z);
title('Dendrograma del Clustering Jerárquico');
xlabel('Índices de los datos');
ylabel('Distancia');

% Definir el número de clusters
k = 2;

% Obtener los índices de los clusters
idx = cluster(Z, 'maxclust', k);

% Visualizar los datos agrupados por los clusters obtenidos
figure;
gscatter(data(:,1), data(:,2), idx, 'rb', 'ox');
title('Datos Agrupados por Clustering Jerárquico');
xlabel('Eje X');
ylabel('Eje Y');
legend('Cluster 1', 'Cluster 2');