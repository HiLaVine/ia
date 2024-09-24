function [strTriggered] = getTriggeredReply(patientSays)

persistent triggers 
persistent response
persistent maxResponses
persistent numTriggers 
persistent maxSynonyms
persistent usedResponses
persistent lukeCount
persistent anakinCount
persistent personajeCount
persistent sidiusCount
persistent mandaCount
persistent rebeCount
persistent impeCount
persistent ahsokaCount
persistent yodaCount
persistent bobaCount
persistent recomendacionCount
persistent infoCount
persistent datoCount
persistent graciasCount


if isempty(response)
    response = readtable('ChatData.xlsx','Sheet','ElizaResponse');
    response = table2array(response);
end
if isempty(maxResponses)
    maxResponses = size(response,1) - 1; % sub one for headers
end
if isempty(triggers)
    triggers = readtable('ChatData.xlsx','Sheet','TriggerWord');
end
if isempty(numTriggers)
    numTriggers = size(triggers,2);
end
if isempty(maxSynonyms)
    maxSynonyms = size(triggers,1);
end
if isempty(usedResponses)
    usedResponses = uint8(zeros(size(response)));
end
if isempty(lukeCount)
    lukeCount = 0;
end

if isempty(anakinCount)
    anakinCount = 0;
end

if isempty(personajeCount)
    personajeCount = 0;
end

if isempty(sidiusCount)
    sidiusCount = 0;
end

if isempty(mandaCount)
    mandaCount = 0;
end

if isempty(rebeCount)
    rebeCount = 0;
end

if isempty(impeCount)
    impeCount = 0;
end

if isempty(ahsokaCount)
    ahsokaCount = 0;
end

if isempty(yodaCount)
    yodaCount = 0;
end

if isempty(bobaCount)
    yodaCount = 0;
end

if isempty(recomendacionCount)
    recomendacionCount = 0;
end

if isempty(infoCount)
    infoCount = 0;
end

if isempty(datoCount)
    datoCount = 0;
end

if isempty(graciasCount)
    graciasCount = 0;
end

strTriggered = [];
patientSays = lower(patientSays);

flagTriggered = false;
idxTrigger = nan;
for itrigger = 1:numTriggers
    k = 1;
    while(k <= maxSynonyms && ~flagTriggered)
        if (contains(patientSays,triggers{k,itrigger}))
            flagTriggered = true;
            idxTrigger = itrigger;
            break;
        else
            k = k + 1;
        end
    end
end

if (~isnan(idxTrigger))
    if strcmpi(triggers{1,idxTrigger},'luke')
        lukeCount = lukeCount + 1;
        if lukeCount >= 4
            strTriggered = 'Parece que vuelves a preguntar sobre Luke debe ser alguno de tus personajes favoritos, te dare mas informacion sobre el Luke nació en el planeta Tatooine y fue criado por sus tíos Owen y Beru Lars como un granjero de humedad. ';
            lukeCount = 0; % Reset the count
        elseif lukeCount >= 3
            strTriggered = 'Claro te dare mas informacion sobre luke...Al principio, Luke es un joven granjero con grandes sueños, pero su vida cambia radicalmente cuando conoce a Obi-Wan Kenobi y descubre su destino como un Jedi.';
        end
    end

    if strcmpi(triggers{1,idxTrigger},'anakin')
        anakinCount = anakinCount + 1;
        if anakinCount >= 4
            strTriggered = 'Entiendo por que vuelves a preguntar sobre Anakin es un gran personaje, te dare mas informacion Anakin nació en el planeta Tatooine y fue esclavo en la tienda de chatarra de Watto antes de ser liberado por Qui-Gon Jinn y entrenado como Jedi.';
            anakinCount = 0; % Reset the count
        elseif anakinCount >= 3
            strTriggered = 'Ya que me has preguntado varias veces sobre el, aqui tienes mas informacion sobre Anakin es considerado el "Elegido por la Fuerza", destinado a traer equilibrio a la Fuerza. Sin embargo, su destino es profundamente afectado por el miedo, la ira y el deseo de poder.';
        end
    end

    if strcmpi(triggers{1,idxTrigger},'personaje')
        personajeCount = personajeCount + 1;
        if personajeCount >= 4
            strTriggered = 'Ya has preguntado mucho sobre tus personajes favoritos de la saga...Shin Hati hizo su primera aparición fue en la serie "Ahsoka".';
            personajeCount = 0; % Reset the count
        elseif personajeCount >= 3
            strTriggered = 'Veo que te interesa saber mucho sobre este mundo ya que has preguntado varias veces sobre los personajes, por ejemplo: Sabine Wren es una mandaloriana experta en armas y artista talentosa que se une a Ahsoka en su búsqueda. Sabine es conocida por su espíritu rebelde y su feroz lealtad a sus amigos.';
        end
    end

    if strcmpi(triggers{1,idxTrigger},'darth sidius')
        sidiusCount = sidiusCount + 1;
        if sidiusCount >= 4
            strTriggered = 'A mi tambien me gusta este personaje por todo su desarrolllo que ya te mencione anteriormente, A lo largo de las precuelas, orquestó eventos desde las sombras, manipulando tanto a la República como a los Separatistas para su propio beneficio.';
            sidiusCount = 0; % Reset the count
        elseif sidiusCount >= 3
            strTriggered = 'Darth Sidius es uno de los personajes mas importantes de la saga, veo por que el interes que tienes en el, por todos lo que me has preguntado...Ejecutó la Orden 66, una orden que hizo que los soldados clones se volvieran contra los Jedi, casi eliminando a toda la Orden.';
            
        end

    end

    if strcmpi(triggers{1,idxTrigger},'mandalorian')
        mandaCount = mandaCount + 1;
        if mandaCount >= 4
            strTriggered = 'A mi tambien me gusta este personaje..A lo largo de la serie, Din Djarin y Grogu viajan por la galaxia buscando un enclave mandaloriano para que Grogu pueda entrenar como mandaloriano.';
            mandaCount = 0; % Reset the count
        elseif mandaCount >= 3
            strTriggered = 'Acaso estas viendo la serie "The Mandalorian o por que preguntas tanto sobre el..El Mandaloriano se ha convertido en uno de los personajes más populares del universo Star Wars gracias a su estoicismo, sus habilidades de combate y su relación paternal con Grogu."';
        end
    end

    if strcmpi(triggers{1,idxTrigger},'rebelion')
        rebeCount = rebeCount + 1;
        if rebeCount >= 4
            strTriggered = 'Te dare mas informacion como lo pides...La Rebelión está formada por una amplia gama de individuos de diversas especies y orígenes.';
            rebeCount = 0; % Reset the count
        elseif rebeCount >= 3
            strTriggered = 'Claro, acabas de ver alguna de la trilogia original?,..........La Rebelión surgió durante los últimos años de la República Galáctica, cuando el Canciller Supremo Sheev Palpatine se declaró a sí mismo Emperador y estableció un régimen dictatorial. La creciente opresión del Imperio y la eliminación de las libertades civiles impulsaron a muchos a unirse a la causa rebelde.';
        end
    end

    if strcmpi(triggers{1,idxTrigger},'imperio')
        impeCount = impeCount + 1;
        if impeCount >= 4
            strTriggered = '';
            impeCount = 0; % Reset the count
        elseif impeCount >= 3
            strTriggered = 'Veo que tienes una Fascinación por la historia de universo de Star Wars: El Imperio Galáctico sigue siendo uno de los antagonistas más icónicos de la ciencia ficción. Su historia sirve como una advertencia sobre los peligros del totalitarismo y la importancia de la lucha por la libertad y la democracia.';
        end
    end

    if strcmpi(triggers{1,idxTrigger},'ahsoka')
        ahsokaCount = ahsokaCount + 1;
        if ahsokaCount >= 4
            strTriggered = 'Si claro de dare mas infromacion sobre ella. Ashoka es una Togruta, una especie alienígena humanoides con características similares a las de los humanos, pero con distintivas marcas y cuernos en la cabeza.';
            ahsokaCount = 0; % Reset the count
        elseif ahsokaCount >= 3
            strTriggered = 'Recientemente viste la Serie de Ahsoka o por que tanto interes...Apareció por primera vez en la película animada "Star Wars: The Clone Wars" (2008) y ha sido un personaje importante en varias series de televisión, cómics y novelas del universo expandido de Star Wars.'
        end
    end

    if strcmpi(triggers{1,idxTrigger},'yoda')
        yodaCount = yodaCount + 1;
        if yodaCount >= 4
            strTriggered = 'A mi tambien me encanta Yoda. Es uno de los personajes más emblemáticos de la franquicia y ha dejado una marca indeleble en la cultura popular. Su estilo de hablar peculiar y sus consejos sabios lo han convertido en un favorito de los fanáticos de todas las edades.';
            yodaCount = 0; % Reset the count
        elseif yodaCount >= 3
            strTriggered = 'El Maestro Yoda es uno de los personajes mas importantes veo por que quieres tanto aprender sobre el. Yoda es conocido por su sabiduría, paciencia y habilidad en la Fuerza. A pesar de su pequeño tamaño y apariencia frágil, es uno de los Jedi más poderosos que jamás haya existido.'
        end
    end

    if strcmpi(triggers{1,idxTrigger},'boba fett')
        bobaCount = bobaCount + 1;
        if bobaCount >= 4
            strTriggered = 'Tambien quieres ser un cazarrecompesas o por que quieres saber sobre el..Es un maestro en el uso de una variedad de armas, incluidos blásters, lanzacohetes y un jetpack que le permite volar. Su silenciosa presencia y habilidades letales lo convierten en uno de los cazarrecompensas más temidos de la galaxia.';
            bobaCount = 0; % Reset the count
        elseif bobaCount >= 3
            strTriggered = 'Recientemente viste la serie del libro de Boba Fett o por que tanto interes..Hizo su primera aparición en la película "Star Wars: Episode V - The Empire Strikes Back" (1980), donde fue contratado por Darth Vader para capturar a Han Solo y llevarlo ante Jabba the Hutt.'
        end
    end

    if strcmpi(triggers{1,idxTrigger},'recomendacion')
        bobaCount = bobaCount + 1;
        if bobaCount >= 4
            strTriggered = 'Te gustaria que te recomiende mas por lo que veo. "Mass Effect" (videojuego): Esta franquicia de videojuegos combina ciencia ficción con elementos de acción, exploración y toma de decisiones morales.';
            bobaCount = 0; % Reset the count
        elseif bobaCount >= 3
            strTriggered = 'Te deben gustar mucho las peliculas de ciencia ficcion para que me preguntes por tantas recomendaciones. "Battlestar Galactica": Esta serie de televisión ofrece una mezcla de ciencia ficción y drama político mientras sigue a la humanidad en su lucha por sobrevivir después de un ataque devastador de una raza de robots llamados Cylons. '
        end
    end

    if strcmpi(triggers{1,idxTrigger},'informacion')
        infoCount = infoCount + 1;
        if infoCount >= 4
            strTriggered = 'Aun quieres saber informacion sobre los persoanjes de Star Wars. La Princesa Padmé Amida que es la Reina y luego senadora de Naboo. Es la madre de Luke Skywalker y Leia Organa. Es una figura política importante en la galaxia y una aliada clave en la lucha contra el Imperio.';
            infoCount = 0; % Reset the count
        elseif infoCount >= 3
            strTriggered = 'Quieres conocer este universo muy bien por lo que veo. Leia Organa la Hermana gemela de Luke Skywalker y líder de la Rebelión. Es una figura clave en la lucha contra el Imperio y más tarde se convierte en una líder importante en la Nueva República.'
        end
    end

    if strcmpi(triggers{1,idxTrigger},'dato')
        datoCount = datoCount + 1;
        if datoCount >= 4
            strTriggered = 'Veo que te quieres convertir en todo un experto en este universo. La saga de Star Wars ha ganado numerosos premios, incluyendo 10 premios Óscar. La primera película ganó el Óscar a los Mejores Efectos Visuales en 1978.';
            datoCount = 0; % Reset the count
        elseif datoCount >= 3
            strTriggered = 'Con que quieres saber mas datos curiosos de esta Saga. Disney adquiere Lucasfilm en 2012, The Walt Disney Company adquirió Lucasfilm por más de 4 mil millones de dólares, lo que llevó a una nueva era de producciones de Star Wars, incluyendo nuevas películas, series de televisión y parques temáticos.'
        end
    end
    
    if strcmpi(triggers{1,idxTrigger},'gracias')
        graciasCount = graciasCount + 1;
        if graciasCount >= 3
            strTriggered = 'Veo que te quieres muy amable joven Jedi';
            graciasCount = 0; % Reset the count
        end
    end
    
    if isempty(strTriggered)
        idxResponse = floor(2+maxResponses*rand(1,1));
        while (usedResponses(idxResponse,idxTrigger) > 0)
            idxResponse = floor(2+maxResponses*rand(1,1));
        end
        strTriggered = response{idxResponse,idxTrigger};
        usedResponses(idxResponse,idxTrigger) = 1;
        if (sum(usedResponses(:,idxTrigger)) == maxResponses)
            usedResponses(:,idxTrigger) = 0;
        end
    end
    
end

end
