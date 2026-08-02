/* Chart behavior */ 

(function () {
  'use strict';

  var PLOT_CONFIG = { displayModeBar: false, responsive: true };
  var NARROW = '(max-width: 559px)';

  function renderCharts(specs) {
    specs.forEach(function (spec) {
      if (document.getElementById(spec.id)) {
        Plotly.newPlot(spec.id, spec.data, spec.layout, PLOT_CONFIG);
      }
    });
  }

  /* Rank-shift hover label. */
  function wrapHoverLabelsWhenNarrow(id) {
    var gd = document.getElementById(id);
    if (!gd || !gd.data) return;

    var wide = gd.data.map(function (trace) { return trace.hovertemplate; });
    var narrow = wide.map(function (template) {
      return template.replace('share of national science output',
                              'share of<br>national science output');
    });

    var query = window.matchMedia(NARROW);
    function apply() {
      Plotly.restyle(gd, 'hovertemplate', query.matches ? narrow : wide);
    }

    if (query.matches) apply();
    query.addEventListener('change', apply);
  }

  renderCharts(window.CHART_SPECS || []);
  wrapHoverLabelsWhenNarrow('c2');
})();
