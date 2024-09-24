function [strReply] = You2Me(patientSays)

strReply = [];
flagReplyFinished = false;

idxCricket = strfind(patientSays, 'you are ');
if (idxCricket > 1)
    strLeft = patientSays(1:idxCricket - 1);
    strRight = patientSays(idxCricket+7:end);
    strReply = [strLeft 'I am ' strRight];
end

idxCricket = strfind(patientSays, 'you aren''t');
if (idxCricket > 1)
    strLeft = patientSays(1:idxCricket - 1);
    strRight = patientSays(idxCricket+7:end);
    strReply = [strLeft 'I am not' strRight];
end

idxCricket = strfind(patientSays, 'i''m');
if (idxCricket > 1)
    strLeft = patientSays(1: idxCricket - 1);
    strRight = patientSays(idxCricket+4:end);
    strReply = [strLeft 'you''re' strRight];
    flagReplyFinished = true;
end

idxCricket = strfind(patientSays, 'you''re');
if ((idxCricket > 4) & ~flagReplyFinished)
    strLeft = patientSays(1: idxCricket - 1);
    strRight = patientSays(idxCricket+6:end);
    strReply = [strLeft 'I am' strRight];
end
flagReplyFinished = false;

idxCricket = strfind(patientSays, ' you ');
if (idxCricket > 1)
    strLeft = patientSays(1: idxCricket - 1);
    strRight = patientSays(idxCricket+3:end);
    strReply = [strLeft ' me ' strRight];
    flagReplyFinished = true;
end

idxCricket = strfind(patientSays, ' me ');
if ((idxCricket > 3) & ~flagReplyFinished)
    strLeft = patientSays(1: idxCricket - 1);
    strRight = patientSays(idxCricket+2:end);
    strReply = [strLeft ' you ' strRight];
end

idxCricket = strfind(patientSays, ' my ');
if (idxCricket > 3)
    strLeft = patientSays(1: idxCricket - 1);
    strRight = patientSays(idxCricket+2:end);
    strReply = [strLeft ' your ' strRight];
end

if (isempty(strReply))
    strReply= patientSays;
end

end
