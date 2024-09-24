function [NewReply] = fillDeadAirtime()

% No keywords found
switch floor(1+8*rand(1,1))
    case 1
        NewReply = 'Qué bueno que te interese el mundo de Star Wars! Es un universo complejo y lleno de detalles.';
    case 2
        NewReply = 'Comparto tu entusiasmo por Star Wars! Es un universo fascinante lleno de aventuras, personajes memorables y una rica historia.';
    case 3
        NewReply = '¡Hola! Me alegra saber que te apasiona la ciencia ficción y el universo de Star Wars.';
    case 4
        NewReply = 'Me encanta la ciencia ficcion y este mundo de Star Wars.';
    case 5
        NewReply = 'Este mundo de Star Wars en estan interesante';
    case 6
        NewReply = ['Que bueno que te gustaria saber sobre este mundo de Star Wars'];
    otherwise
        NewReply = 'Hola yo te puedo ayudar sobre el mundo de Star Wars!!';
end

end

