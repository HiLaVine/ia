function [strTriggered] = getTriggeredReply(patientSays)

persistent triggers 
persistent response
persistent maxResponses
persistent numTriggers 
persistent maxSynonyms
persistent usedResponses

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

