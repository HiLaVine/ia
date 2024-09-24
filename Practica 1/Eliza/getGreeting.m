function [strGreeting] = getGreeting(icase)

if (~exist('icase','var'))
    icase = floor(3*rand(1,1)+1);
end

switch icase
    case 1
        strGreeting = 'Hola fanatico, ¿Pregunta lo que quieras';
    case 2
        strGreeting = 'Bienvenido, ¿que te gustaria saber de la NBA?';
    otherwise
        strGreeting = '¿Te gusta la NBA?';
end
  
end

