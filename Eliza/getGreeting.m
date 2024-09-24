function [strGreeting] = getGreeting(icase)

if (~exist('icase','var'))
    icase = floor(6*rand(1,1)+1);
end

switch icase
    case 1
        strGreeting = 'Saludos, ¡Que la Fuerza te acompañe!';
    case 2
        strGreeting = '¡Saludos, joven Jedi!';
    case 3
        strGreeting = 'Holaa ¡Que el poder del Lado Oscuro no te corrompa!';
    case 4
        strGreeting = '¡Que la Fuerza este contigo!';
    case 5
        strGreeting = '¡Saludos, Maestro Jedi!';
    otherwise
        strGreeting = '¡Saludos, Lord Sith!';
end
  
end

