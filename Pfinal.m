% Paso 1: Preparar el Conjunto de Datos
imageFolder = 'C:\Users\sinna\Downloads\all-images';  % Cambia esto a la ruta donde descomprimiste el conjunto de datos

% Crear un conjunto de datos de imágenes 
imds = imageDatastore(imageFolder, ...
    'IncludeSubfolders', true, ...
    'LabelSource', 'foldernames'); 

% Dividir en conjuntos de entrenamiento y validación 
[imdsTrain, imdsValidation] = splitEachLabel(imds, 0.8, 'randomized');

% Paso 2: Cargar un Modelo Preentrenado y Ajustar las Capas
net = resnet50;
inputSize = net.Layers(1).InputSize;
lgraph = layerGraph(net);

% Reemplazar las últimas capas de la red
newLearnableLayer = fullyConnectedLayer(numel(categories(imdsTrain.Labels)), ...
    'Name', 'new_fc', ...
    'WeightLearnRateFactor', 10, ...
    'BiasLearnRateFactor', 10);
lgraph = replaceLayer(lgraph, 'fc1000', newLearnableLayer);

newSoftmaxLayer = softmaxLayer('Name', 'new_softmax');
lgraph = replaceLayer(lgraph, 'fc1000_softmax', newSoftmaxLayer);

newClassLayer = classificationLayer('Name', 'new_classoutput');
lgraph = replaceLayer(lgraph, 'ClassificationLayer_fc1000', newClassLayer);

% Paso 3: Ajustar el tamaño de las imágenes al tamaño de entrada de la red (224x224 para ResNet-50) 
augimdsTrain = augmentedImageDatastore(inputSize(1:2), imdsTrain); 
augimdsValidation = augmentedImageDatastore(inputSize(1:2), imdsValidation);

% Paso 4: Configurar las Opciones de Entrenamiento
options = trainingOptions('sgdm', ...
    'MiniBatchSize', 32, ...
    'MaxEpochs', 6, ...
    'InitialLearnRate', 1e-4, ...
    'Shuffle', 'every-epoch', ...
    'ValidationData', augimdsValidation, ...
    'ValidationFrequency', 30, ...
    'Verbose', false, ...
    'Plots', 'training-progress', ...
    'OutputFcn', @(info) trainingMonitor(info));

% Paso 5: Entrenar la Red
netTransfer = trainNetwork(augimdsTrain, lgraph, options);

% Paso 6: Evaluar el Modelo
[YPred, scores] = classify(netTransfer, augimdsValidation); 
accuracy = mean(YPred == imdsValidation.Labels); 
fprintf('Precisión en el conjunto de validación: %.2f%%\n', accuracy * 100);

% Función para monitorear el entrenamiento
function stop = trainingMonitor(info)
    stop = false;
    if info.State == "iteration"
        if isfield(info, 'TrainingLoss') && ~isempty(info.TrainingLoss)
            fprintf('Época %d, Iteración %d, Pérdida de Entrenamiento: %.4f\n', ...
                info.Epoch, info.Iteration, info.TrainingLoss);
        end
    end
    if info.State == "done"
        fprintf('Entrenamiento completado en %d iteraciones.\n', info.Iteration);
    end
    updateTrainingProgressPlot();
end

% Función para actualizar la gráfica de progreso del entrenamiento
function updateTrainingProgressPlot()
    h = findall(groot, 'Type', 'Figure', 'Name', 'Training Progress');
    if ~isempty(h)
        % Cambiar etiquetas
        ax1 = h.CurrentAxes(1);
        ax2 = h.CurrentAxes(2);
        ax1.YLabel.String = 'Precisión (%)';
        ax2.YLabel.String = 'Pérdida';
        ax1.Title.String = 'Progreso del Entrenamiento';
        ax2.Title.String = 'Progreso del Entrenamiento';
        ax1.Legend.String{1} = 'Entrenamiento (suavizado)';
        ax1.Legend.String{2} = 'Entrenamiento';
        ax1.Legend.String{3} = 'Validación';
        ax2.Legend.String{1} = 'Pérdida (suavizada)';
        ax2.Legend.String{2} = 'Pérdida';

        % Cambiar colores de las líneas
        ax1.Children(1).Color = [0 0.4470 0.7410]; % Suavizado (azul)
        ax1.Children(2).Color = [0.8500 0.3250 0.0980]; % Entrenamiento (rojo)
        ax1.Children(3).Color = [0.9290 0.6940 0.1250]; % Validación (amarillo)
        ax2.Children(1).Color = [0.4940 0.1840 0.5560]; % Pérdida suavizada (púrpura)
        ax2.Children(2).Color = [0.4660 0.6740 0.1880]; % Pérdida (verde)
    end
end