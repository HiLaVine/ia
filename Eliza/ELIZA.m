% Crear la interfaz de inicio
start_f = figure('Name', 'Inicio', 'Position', [480, 250, 600, 400]);

% Imágenes
ipn_img = imread('ipn.jpg');
escom_img = imread('escom.jpg');
axes('Position', [0.001, 0.57, 0.32, 0.32]);
imshow(ipn_img);
axes('Position', [0.75, 0.6, 0.27, 0.27]);
imshow(escom_img);

% Texto
text_panel = uicontrol('Style', 'text', 'String', {'Practica No.3 "Eliza:Experta en Star Wars"';'';'Integrantes del Equipo:'; 'Hernández Hernández Jorge Gabriel'; 'Farrera Mendez Emmanuel Sinai';'';  'Grupo: 6CM2';''; 'Unidad de Aprendizaje: Inteligencia Artificial';''; 'Profesor: Rodolfo Romero Herrera'}, 'Position', [150, 200, 300, 150], 'FontSize', 10, 'FontWeight', 'bold');

% Botón para comenzar la conversación con ELIZA
start_button = uicontrol('Style', 'pushbutton', 'String', 'Comienza el Viaje por el mundo de Star Wars', 'Position', [160, 50, 280, 100], 'Callback', {@startEliza, start_f}, 'FontSize', 9,'FontWeight', 'bold','ForegroundColor', 'white', 'BackgroundColor', 'red');

% Función para iniciar ELIZA
function startEliza(~, ~, start_f)
    % Cerrar la ventana de inicio
    close(start_f);
    
    % Iniciar la conversación de ELIZA
    flagGo = true;

    % Inicializar la conversación
    conversation = {'Eliza: Bienvenido a ELIZA';
                    'Eliza: La Fuerza te ha guiado hasta aquí';
                    'Eliza: Eliza es una experta en el mundo de Star Wars';
                    'Eliza: El programa original fue descrito por Joseph Weizenbaum en 1966.';
                    'Eliza: Sentimos la Fuerza fluyendo a través de ti, y esperamos que tus conocimientos del universo Star Wars sean tan vastos como las arenas de Tatooine.';
                    'Eliza: Introduzca ''fuerza'' cuando desees terminar la sesión.'
                    ''
                    };
    conversationStr = strjoin(conversation, '\n');

    % Iniciar la interfaz gráfica
f = figure('Name', 'Eliza', 'Position', [150, 60, 1210, 750]);

% Crear un contenedor para la conversación con scroll
scroll_handle = uicontrol('Style', 'edit', 'String', '', 'Position', [20, 20, 1180, 750], ...
                          'HorizontalAlignment', 'left', 'BackgroundColor', [0.1, 0.1, 0.1], ...
                          'ForegroundColor', [1, 1, 0], 'FontWeight', 'bold', ...
                          'Max', inf, 'Enable', 'inactive');

% Botón de ayuda
help_button = uicontrol('Style', 'pushbutton', 'String', 'Ayuda', 'Position', [1104, 725, 80, 30], 'Callback', @showHelp);

edit_handle = uicontrol('Style', 'edit', 'String', '', 'Position', [20, -10, 1100, 30], 'Callback', @submitResponse);

submit_button = uicontrol('Style', 'pushbutton', 'String', 'Enviar', 'Position', [1100, -10, 80, 30], 'Callback', @submitResponse);

% Dentro del bucle while
while (flagGo)
    % Esperar hasta que el usuario ingrese una respuesta
    uiwait(f);

    % Obtener la respuesta del usuario del cuadro de texto
    patientSays = lower(edit_handle.String);

    % Limpiar el cuadro de texto
    edit_handle.String = '';

    % Procesar la respuesta y actualizar la conversación
    if ~isempty(patientSays)
        conversation{end+1} = ['TU: ', patientSays];
        conversationStr = strjoin(conversation, '\n');
        set(scroll_handle, 'String', conversationStr);
    end

    % Obtener la respuesta de Eliza y actualizar la conversación
    if flagGo
        [prompt] = getTriggeredReply(patientSays);
        if isempty(prompt)
            [prompt] = getQuestionForQuestion(patientSays);
        end
        if isempty(prompt)
            [prompt] = fillDeadAirtime();
        end

        conversation{end+1} = ['Eliza: ', prompt];
        conversationStr = strjoin(conversation, '\n');
        set(scroll_handle, 'String', conversationStr);
    end

    % Verificar si el usuario quiere terminar la sesión
    if contains(patientSays, 'fuerza')
        % Mostrar mensaje de despedida en la conversación
        conversation{end+1} = 'Eliza: ¡Que la Fuerza te acompañe!';
        conversationStr = strjoin(conversation, '\n');
        set(scroll_handle, 'String', conversationStr);

        pause(2);
        flagGo = false;
        close(f); % Cerrar la ventana del chat
    end
end

 end

% Función para procesar la respuesta del usuario
function submitResponse(src, ~)
    uiresume(src.Parent);
end

% Función para mostrar la ayuda
function showHelp(~, ~)
    msg = {'¡Bienvenido a ELIZA! Esta aplicación te permite tener una conversación en el mundo de Star Wars.';
           'Aquí tienes algunos consejos:';
           '- Introduce tus respuestas en el cuadro de diálogo etiquetado como TU>.';
           '- Para finalizar la sesión, simplemente escribe "fuerza" en minúsculas y sin comillas.';
           '- Que la Fuerza esté contigo.'};
    msgbox(msg, 'Ayuda - ELIZA', 'help', 'modal');
end
