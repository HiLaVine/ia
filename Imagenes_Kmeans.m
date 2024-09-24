%Imagenes K-means
% Leer la imagen
img = imread('curry.jpg');

% Convertir la imagen a una matriz de doble precisión
img_double = im2double(img);

% Obtener las dimensiones de la imagen
[rows, cols, channels] = size(img_double);

% Convertir la imagen a una matriz de píxeles (cada fila representa un píxel)
pixels = reshape(img_double, rows * cols, channels);

% Definir el número de clusters
num_clusters = 5;

% Aplicar K-means a los píxeles de la imagen
[cluster_indices, centroids] = kmeans(pixels, num_clusters, 'MaxIter', 1000, 'Display', 'final');

% Asignar a cada píxel el color del centroide más cercano
pixels_reconstructed = centroids(cluster_indices, :);

% Restaurar la estructura de la imagen
img_reconstructed = reshape(pixels_reconstructed, rows, cols, channels);

% Convertir la imagen reconstruida a uint8
img_reconstructed = im2uint8(img_reconstructed);

% Mostrar la imagen original y la imagen procesada
figure;
subplot(1, 2, 1);
imshow(img);
title('Imagen Original');
subplot(1, 2, 2);
imshow(img_reconstructed);
title('Imagen Procesada con K-means');