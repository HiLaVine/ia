% Generar datos sintéticos
rng(1); % Para reproducibilidad
n = 100; % Número de muestras por clase
X = [randn(n, 2) + 1; randn(n, 2) - 1]; % Características
y = [ones(n, 1); zeros(n, 1)]; % Etiquetas: 1 y 0

% Visualizar los datos
figure;
gscatter(X(:,1), X(:,2), y, 'rb', '*o');
xlabel('Característica 1');
ylabel('Característica 2');
title('Datos Sintéticos para Naive Bayes');

% Entrenar el modelo Naive Bayes
naiveBayesModel = fitcnb(X, y);
% Mostrar el modelo entrenado
disp(naiveBayesModel);

% Predecir las etiquetas
predicciones = predict(naiveBayesModel, X);
% Evaluar la precisión del modelo
precision = mean(predicciones == y);
fprintf('Precisión del Modelo: %.2f%%\n', precision * 100);

% Visualizar las predicciones
d = 0.1; % Aumentar la densidad de la malla
[x1Grid, x2Grid] = meshgrid(min(X(:,1)):d:max(X(:,1)), min(X(:,2)):d:max(X(:,2)));
xGrid = [x1Grid(:), x2Grid(:)];
prediccionesGrid = predict(naiveBayesModel, xGrid);

figure;
gscatter(X(:,1), X(:,2), y, 'rb', '*o');
hold on;

% Convertir prediccionesGrid a valores binarios para gscatter
prediccionesGridBin = double(prediccionesGrid);
prediccionesGridBin(prediccionesGridBin == 0) = 2; % Convertir 0 a 2 para gscatter

% Visualizar la frontera de decisión
gscatter(xGrid(:,1), xGrid(:,2), prediccionesGridBin, 'yg', '.', [], 'off');
xlabel('Característica 1');
ylabel('Característica 2');
title('Naive Bayes con Frontera de Decisión');
legend('Clase 1', 'Clase 0', 'Ubicaciones Predichas');
hold off;
