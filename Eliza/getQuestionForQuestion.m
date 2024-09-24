function [strQuestionBack] = getQuestionForQuestion(patientSays)

strQuestionBack = [];
% Check for 'Can I' keyword
if ((strfind(patientSays, 'can i')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'.') || contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(6:end));
    else
        strTempReply = [lower(strTempReply(6:end)) '?'];
    end
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = ['Do you want to be able to' strTempReply];
        case 2
            strQuestionBack = ['Perhaps you really don''t want to' strTempReply];
        case 3
            strQuestionBack = ['What would it mean if you could' strTempReply];
        otherwise
            strQuestionBack = ['Why do you ask if you can' strTempReply];
    end
    return
end

% Check for 'Can you' keyword
if ((strfind(patientSays, 'can you')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'.') || contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(8:end));
    else
        strTempReply = [lower(strTempReply(8:end)) '?'];
    end
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = ['Don''t you believe that I can' strTempReply];
        case 2
            strQuestionBack = ['Perhaps you would like me to be able to' strTempReply];
        case 3
            strQuestionBack = ['You want me to be able to' strTempReply];
        otherwise
            strQuestionBack = ['Why do you want me to' strTempReply];
    end
    return
end

% Check for 'Don't you' keyword
if ((strfind(patientSays, 'don''t you')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'.') || contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(9:end));
    else
        strTempReply = [lower(strTempReply(9:end)) '?'];
    end
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = ['Do you really believe that I don''t' strTempReply];
        case 2
            strQuestionBack = ['Do you want me to' strTempReply];
        case 3
            strQuestionBack = ['Why do you care if I' strTempReply];
        otherwise
            strQuestionBack = ['Is it important to you that I' strTempReply];
    end
    return
end

% Check for 'Don't you' keyword
if ((strfind(patientSays, 'do you')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'.') || contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(7:end));
    else
        strTempReply = [lower(strTempReply(7:end)) '?'];
    end
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = ['Do you really believe that I ' strTempReply];
        case 2
            strQuestionBack = ['Do you want me to' strTempReply];
        case 3
            strQuestionBack = ['Why do you care if I' strTempReply];
        otherwise
            strQuestionBack = ['Is it important to you that I' strTempReply];
    end
    return
end

% Check for 'Are you' keyword
if ((strfind(patientSays, 'are you')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'.') || contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(8:end));
    else
        strTempReply = [lower(strTempReply(8:end)) '?'];
    end
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = ['Would you prefer if I were not' strTempReply];
        case 2
            strQuestionBack = ['Perhaps you are imagining that I am' strTempReply];
        case 3
            strQuestionBack = ['Do you really care if I am' strTempReply];
        otherwise
            strQuestionBack = ['Why should you care if I am' strTempReply];
    end
    return
end

% Check for 'I don't' keyword
if ((strfind(patientSays, 'i don''t')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(8:end));
    else
        strTempReply = [lower(strTempReply(8:end)) '?'];
    end
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = ['Don''t you really' strTempReply];
        case 2
            strQuestionBack = ['Why don''t you' strTempReply];
        case 3
            strQuestionBack = ['Do you wish to be able to' strTempReply];
        otherwise
            strQuestionBack = ['So you really don''t' strTempReply];
    end
    return
end

% Check for 'I feel' keyword
if ((strfind(patientSays, 'i feel')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(7:end));
    else
        strTempReply = [lower(strTempReply(7:end)) '?'];
    end
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = ['Do you often feel' strTempReply];
        case 2
            strQuestionBack = ['Do you enjoy feeling' strTempReply];
        case 3
            strQuestionBack = ['How often do you feel' strTempReply];
        otherwise
            strQuestionBack = ['What do you think about when you feel' strTempReply];
    end
    return
end

% Check for 'I want' keyword
if ((strfind(patientSays, 'i want')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(7:end));
    else
        strTempReply = [lower(strTempReply(7:end)) '?'];
    end
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = ['What would it mean if you got' strTempReply];
        case 2
            strQuestionBack = ['Why do you want' strTempReply];
        case 3
            strQuestionBack = ['What would happen if you got' strTempReply];
        otherwise
            strQuestionBack = ['What if you never got' strTempReply];
    end
    return
end

% Check for 'I am' keyword
if ((strfind(patientSays, 'i am')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(5:end));
    else
        strTempReply = [lower(strTempReply(5:end)) '?'];
    end
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = ['Did you come to me because you are' strTempReply];
        case 2
            strQuestionBack = ['How long have you been' strTempReply];
        case 3
            strQuestionBack = ['Do you believe it is normal to be' strTempReply];
        otherwise
            strQuestionBack = ['Why are you' strTempReply];
    end
    return
end

% Check for 'I'm' keyword
if ((strfind(patientSays, 'i''m')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(4:end));
    else
        strTempReply = [lower(strTempReply(4:end)) '?'];
    end
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = ['Did you come to me because you are' strTempReply];
        case 2
            strQuestionBack = ['How long have you been' strTempReply];
        case 3
            strQuestionBack = ['Do you believe it is normal to be' strTempReply];
        otherwise
            strQuestionBack = ['Why are you' strTempReply];
    end
    return
end

% Check for 'I can't' keyword
if ((strfind(patientSays, 'i can''t')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(8:end));
    else
        strTempReply = [lower(strTempReply(8:end)) '?'];
    end
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = ['How do you know you can''t' strTempReply];
        case 2
            strQuestionBack = ['Perhaps now you can' strTempReply];
        case 3
            strQuestionBack = ['Why don''t you try to' strTempReply];
        otherwise
            strQuestionBack = ['How would you feel if you could' strTempReply];
    end
    return
end

% Check for 'You're' keyword
if ((strfind(patientSays, 'you''re')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(7:end));
    else
        strTempReply = [lower(strTempReply(7:end)) '?'];
    end
    switch floor(1+5*rand(1,1))
        case 1
            strQuestionBack = ['Does it please you to believe that I am' strTempReply];
        case 2
            strQuestionBack = ['Perhaps you would like to be' strTempReply];
        case 3
            strQuestionBack = ['Do you sometimes wish you were' strTempReply];
        case 4
            strQuestionBack = ['What makes you think I am' strTempReply];
        otherwise
            strQuestionBack = ['Why do you care that I might be' strTempReply];
    end
    return
end

% Check for 'You aren't' keyword
if ((strfind(patientSays, 'you aren''t')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(11:end));
    else
        strTempReply = [lower(strTempReply(11:end)) '?'];
    end
    switch floor(1+5*rand(1,1))
        case 1
            strQuestionBack = ['Why do you think that I am not' strTempReply];
        case 2
            strQuestionBack = ['Is it important that you think I am not' strTempReply];
        case 3
            strQuestionBack = ['Why does it matter that I may not be' strTempReply];
        case 4
            strQuestionBack = ['Why do you think I am not' strTempReply];
        otherwise
            strQuestionBack = ['Why do you care that I might not be' strTempReply];
    end
    return
end

% Check for 'You are' keyword
if ((strfind(patientSays, 'you are')) == 1)
    % Convert You to Me
    [strTempReply] = You2Me(patientSays);
    if (contains(strTempReply(end),'?'))
        strTempReply = lower(strTempReply(8:end));
    else
        strTempReply = [lower(strTempReply(8:end)) '?'];
    end
    switch floor(1+5*rand(1,1))
        case 1
            strQuestionBack = ['Does it please you to believe that I am' strTempReply];
        case 2
            strQuestionBack = ['Perhaps you would like to be' strTempReply];
        case 3
            strQuestionBack = ['Do you sometimes wish that you were' strTempReply];
        case 4
            strQuestionBack = ['What makes you think that I am' strTempReply];
        otherwise
            strQuestionBack = ['Why do you care that I might be' strTempReply];
    end
    return
end


end

