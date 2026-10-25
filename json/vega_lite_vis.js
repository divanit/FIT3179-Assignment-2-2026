// Defining chart file paths 
var specVis1 = "json/choropleth_map.vg.json";
var specVis2 = "json/bump_chart.vg.json";
var specVis3 = "json/butterfly_chart.vg.json";
var specVis4 = "json/propotional_symbol_map.vg.json";
var specVis5 = "json/graduated_symbol_map.vg.json";
var specVis6 = "json/connected_dot_plot(yield_per_region).vg.json";
var specVis7 = "json/heatmap_price.vg.json";
var specVis8 = "json/heatmap_revenue.vg.json";
var specVis9 = "json/flowmap.vg.json";
var specVis10 = "json/parallel_coordinate.vg.json";
var specVis11 = "json/horizontal_stacked_bar_chart.vg.json";

// Embedding visualisations - connects the HTML container to the JSON file
vegaEmbed('#vis1', specVis1, { "actions": false }).catch(console.error);
vegaEmbed('#vis2', specVis2, { "actions": false }).catch(console.error);
vegaEmbed('#vis3', specVis3, { "actions": false }).catch(console.error);
vegaEmbed('#vis4', specVis4, { "actions": false }).catch(console.error);
vegaEmbed('#vis5', specVis5, { "actions": false }).catch(console.error);
vegaEmbed('#vis6', specVis6, { "actions": false }).catch(console.error);
vegaEmbed('#vis7', specVis7, { "actions": false }).catch(console.error);
vegaEmbed('#vis8', specVis8, { "actions": false }).catch(console.error);
vegaEmbed('#vis9', specVis9, { "actions": false }).catch(console.error);
vegaEmbed('#vis10', specVis10, { "actions": false }).catch(console.error);
vegaEmbed('#vis11', specVis11, { "actions": false }).catch(console.error);