function [NewReply] = fillDeadAirtime()

% No keywords found
switch floor(1+7*rand(1,1))
    case 1
        NewReply = 'Disfruta de la NBA';
    case 2
        NewReply = 'No te entiendo';
    case 3
        NewReply = 'El goat es Michael jordan';
    case 4
        NewReply = 'El goat es lebron james';
    case 5
        NewReply = 'Curry es mejor que Magic';
    case 6
        NewReply = 'KD sin curry no es nada';
    otherwise
        NewReply = 'Jimmy Buttler es el supuesto hijo de Michale Jordan';
end

end

