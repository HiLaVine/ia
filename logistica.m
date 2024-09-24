% Generar datos sintéticos
rng(0); % Para reproducibilidad
n = 100; % Número de muestras por clase
X = [randn(n, 2) + 1; randn(n, 2) - 1]; % Características
y = [ones(n, 1); zeros(n, 1)]; % Etiquetas

% Visualizar los datos
figure;
gscatter(X(:,1), X(:,2), y, 'rg', '*+');
xlabel('Característica 1');
ylabel('Característica 2');
title('Datos Sintéticos para Regresión Logística');
legend({'Clase 1', 'Clase 0'}, 'Location', 'best');

% Convertir los datos a una tabla
data = array2table(X, 'VariableNames', {'Caracteristica1', 'Caracteristica2'});
data.Respuesta = y;

% Ajustar el modelo de regresión logística
modelo = fitglm(data, 'Respuesta ~ Caracteristica1 + Caracteristica2', 'Distribution', 'binomial');

% Mostrar el resumen del modelo
disp(modelo);

% Predecir las probabilidades
probabilidades = predict(modelo, data);

% Convertir probabilidades a etiquetas (0 o 1) con un umbral de 0.5
predicciones = round(probabilidades);

% Evaluar la precisión del modelo
precision = mean(predicciones == y);
fprintf('Precisión del Modelo: %.2f%%\n', precision * 100);

% Visualizar las predicciones
figure;
gscatter(X(:,1), X(:,2), predicciones, 'rg', '*+');
xlabel('Característica 1');
ylabel('Característica 2');
title('Predicciones del Modelo de Regresión Logística');
legend({'Predicción Clase 1', 'Predicción Clase 0'}, 'Location', 'best');