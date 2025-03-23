clear all

close all

clc

%% Problem Preparation

% Create the graph

[graph] = createGraph();


% Draw the Graph
figure
subplot(1,3,1) % 1 row, 3 columns, 1 is the graph itself
drawGraph(graph);

%% ACO algorithm

%% Initial parameters of the ACO

maxIter = 100;

%%

% Main Loop

for t = 1: maxIter

  % Create Ants

  % Calculate the fitness values of all ants

  % Find the best ant (queen)

  % Update pheromone matrix

  % Evaporation

  % Display the results

end
