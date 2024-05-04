%{ This file contains the codes of my blog: "Evaluating Drought Characteristics Using MATLAB." 
Feel free to use it and apply to your reseach. 
Created by: Kumar Puran Tripathy
%}
%% PDSI TIME SERIES
df = readmatrix('PDSI_DATA_1901_2017.xlsx');
pdsi = df(:,2);
dates = num2str(df(:,1));
years = str2num(dates(:,1:4));
months = str2num(dates(:,5:6));

dates = datenum(years, months, 1);

% Plotting the sc-PDSI data
figure;
plot(dates, df(:,2), 'LineWidth', 2); % Plot with a thicker line for better visibility
hold on;

% Add a horizontal dashed line at the threshold
yline(-1, '--r', 'LineWidth', 1.5);
text(datenum(years(end), 6, 1), -1, '  Threshold -1', 'VerticalAlignment', 'bottom', 'Color', 'red');


xlabel('Year');
ylabel('sc-PDSI');
title('sc-PDSI Time Series Analysis');
datetick('x','yyyy'); 
axis tight; 
grid on; 
set(gcf, 'Color', 'w');

%% Calling the function
drought_table = Evaluate_Drought_Characteristics(pdsi, -1, 2, 1);
writetable(drought_table, 'drought_characteristics.xlsx')
