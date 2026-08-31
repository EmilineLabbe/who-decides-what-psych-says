/* Contents rail */

(function () {
  'use strict';

  /* h2 does two things: section headings and chart titles; only the section headings belong in the rail. */
  var SELECTOR = 'article h2:not(.chart-title), article h3';

  /* how far down the viewport a heading counts as "the section you are in" */
  var CROSS_LINE = 120;

  function slugify(text) {
    return text.toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
  }

  /* prefer a short data-toc label over the full heading text, which is often a
     whole sentence and would wrap to five lines in a 190px column */
  function labelFor(heading) {
    return heading.getAttribute('data-toc') || heading.textContent.trim();
  }

  function build(nav, headings) {
    var list = document.createElement('ul');
    var used = {};

    var items = headings.map(function (heading) {
      var label = labelFor(heading);

      if (!heading.id) {
        var base = slugify(label) || 'section';
        var slug = base;
        var n = 2;
        while (used[slug] || document.getElementById(slug)) {
          slug = base + '-' + n;
          n += 1;
        }
        heading.id = slug;
      }
      used[heading.id] = true;

      var link = document.createElement('a');
      link.href = '#' + heading.id;
      /* the ::before ghost that reserves the bold width reads this attribute */
      link.setAttribute('data-label', label);
      var span = document.createElement('span');
      span.textContent = label;
      link.appendChild(span);

      var item = document.createElement('li');
      if (heading.tagName === 'H3') item.classList.add('toc--sub');
      item.appendChild(link);
      list.appendChild(item);

      return item;
    });

    nav.appendChild(list);
    return items;
  }

  /* active entry is the last heading whose top has passed CROSS_LINE */
  function activeIndex(headings) {
    var atBottom = window.innerHeight + window.scrollY >=
                   document.body.scrollHeight - 2;
    if (atBottom) return headings.length - 1;

    var index = -1;
    for (var i = 0; i < headings.length; i++) {
      if (headings[i].getBoundingClientRect().top > CROSS_LINE) break;
      index = i;
    }
    return index;
  }

  function start() {
    var nav = document.querySelector('.toc');
    if (!nav) return;

    var headings = Array.prototype.slice.call(document.querySelectorAll(SELECTOR));
    if (!headings.length) return;

    var items = build(nav, headings);
    var current = null;

    function paint() {
      var index = activeIndex(headings);
      if (index === current) return;
      if (current !== null && items[current]) items[current].classList.remove('is-active');
      if (index >= 0) items[index].classList.add('is-active');
      current = index;
    }

    var queued = false;
    function onScroll() {
      if (queued) return;
      queued = true;
      window.requestAnimationFrame(function () {
        queued = false;
        paint();
      });
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    paint();
  }

  start();
})();
