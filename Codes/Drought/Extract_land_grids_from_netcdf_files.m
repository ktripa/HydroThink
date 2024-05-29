load coastlines; % our goal is to extract the grids which belong inside the land areas 

% caost line ahas coast lat and coast lon: describe what are they.

% Load the NetCDF file
filepath= 'E:\Datasets\SPEI\'
filename = [filepath, 'spei06.nc'];
%%% The data is monthly time series from 1900-january to 2018-December

% Display information about the contents of the file
ncdisp(filename);

% Read variables from the file
lat = ncread(filename, 'lat');  % Read latitude data
lon = ncread(filename, 'lon');  % Read longitude data
time = ncread(filename, 'time');  % Read time data
spei = ncread(filename, 'spei');  % Replace 'spei' with the actual variable name


% Convert time to a recognizable format, if necessary: describe properly in
% the blog. 
% Assuming time is in days since a certain date, e.g., 'days since 1900-01-01'
% You will need to adjust the datenum reference date according to your data
time_vec = datenum('1900-01-01') + double(time);

% Convert serial date number to date string or datetime object for plotting
time_datetime = datetime(time_vec, 'ConvertFrom', 'datenum');
[y,m,~] =ymd(time_datetime);
date_array = [y,m];

[LAT, LON] =meshgrid(lat,lon); %make corrdinates for each grid as a (lat, lon) combination)
% so the total number of grids will be: 
all_latlon = [reshape(LAT,[],1), reshape(LON,[],1)]; % includes all land and ocean grids at 0.5 resolutioon
% lets find the grids wchi belong to only inside land grids. 
%% inpolygon method:
index = inpolygon(all_latlon(:,1), all_latlon(:,2), coastlat,coastlon); %  logical array
disp(sum(index)); % it displays all the grids inside the land areas
latlon = all_latlon(index,:); %
% plot scatter 
scatter(latlon(:,2), latlon(:,1))
xlabel('Longitude');
ylabel('Latitude');
title('Scatter Plot of Land Grids');

% if you have any onther shape file also, you can extract the latlon inside
% that shape file using : describe how to. 



[y,m,~] =ymd(time_datetime);
date_array = [y,m];

spei_out=[];
for itim = 1:10 %length(time)
    dat = spei(:,:,itim);
    flatten_data = reshape(dat,[],1); % flatten to 1-D series which hgas a length of length(lat)* length(lon).
    extracted_land_spei_data = flatten_data(index,:)';
    spei_out = [spei_out; extracted_land_spei_data]; 
end
final_spei_ts = [date_array, spei_out]; %concatenate the date time series with the extracted SPEI time series
% this final_spei_ts has a shape of (1416, 78018). where 1416 represent the total montly time series of the dATA FROM 1900- jan to 2018-0dec
% . and 78018 represnts there are 78016 number of land grids and the first
% 2 columns are the year and month columns. Explain this proeprly to the
% readers.
%the data is basically stored in this format where each row represrtnt a particular month and column represnt a grid across the globe. except the first 2 columns.
 writematrix(final_spei_ts, 'spei6.txt', 'Delimiter','\t')
 % also save the latlon array whi9ch stores the latlon of the 78016 grids, 
 writematrix(latlon, 'latlon.txt','Delimiter','\t')

