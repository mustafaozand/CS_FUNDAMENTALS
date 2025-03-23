function [] = drawGraph(graph)

  hold on

  for i = 1: graph.n -1
    for j = i + 1: graph.n

      x1 = graph.node(i).x;
      y1 = graph.node(i).y;

      x2 = graph.node(j).x;
      y2 = graph.node(j).y;

      X = [x1, x2];

      Y = [y1, y2];

      plot(X, Y, '-k');


    endfor
  endfor

  X = [graph.node(:).x]; % Collects all x-coordinates of nodes into an array
  Y = [graph.node(:).y]; % Collects all y-coordinates of nodes into an array

  plot(X,Y, 'ok', 'MarkerSize', 10, 'MarkerEdgeColor', 'r', 'MarkerFaceColor', [1,0.6,0.6]);


  title('All nodes and edges')
  % box('on')

  endfunction
