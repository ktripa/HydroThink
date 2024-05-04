function droughtTable = Evaluate_Drought_Characteristics(pdsi, threshold, minDuration, mergeDuration)
    % Evaluate Drought Characteristics from PDSI Time Series
    %
    % pdsi        : Array of PDSI values
    % threshold   : Threshold value to define a drought (e.g., -1)
    % minDuration : Minimum duration of a drought (in months)
    % mergeDuration: Maximum separation between consecutive droughts to merge (in months)
    %
    % Output
    % droughtTable : Table containing drought number, onset, departure, duration, severity, intensity
    
    % Identify drought condition
    isDrought = pdsi < threshold;
    
    % Find starts and ends of droughts
    droughtStart = find(diff([0; isDrought]) == 1);
    droughtEnd = find(diff([isDrought; 0]) == -1);
    
    % Merge close droughts
    i = 1;
    while i < length(droughtStart)
        if droughtStart(i+1) - droughtEnd(i) <= mergeDuration
            droughtEnd(i) = droughtEnd(i+1);
            droughtStart(i+1) = [];
            droughtEnd(i+1) = [];
        else
            i = i + 1;
        end
    end
    
    % Calculate characteristics for each drought
    droughtNumber = (1:length(droughtStart))';
    duration = droughtEnd - droughtStart + 1;
    severity = arrayfun(@(s, e) sum(pdsi(s:e)), droughtStart, droughtEnd);
    intensity = severity ./ duration;
    
    % Filter out short droughts
    validDroughts = duration >= minDuration;
    droughtTable = table(droughtNumber(validDroughts), ...
                         droughtStart(validDroughts), ...
                         droughtEnd(validDroughts), ...
                         duration(validDroughts), ...
                         severity(validDroughts), ...
                         intensity(validDroughts), ...
                         'VariableNames', {'DroughtNumber', 'Onset', 'Departure', 'Duration', 'Severity', 'Intensity'});
end
