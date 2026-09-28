(function () {
  var burger = document.getElementById('burger');
  var menu = document.getElementById('menu');

  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      burger.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        menu.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) burger.click();
    });
  }

  // Click-to-load Vimeo: keeps the page light and means a blocked embed
  // degrades to the "Watch on Vimeo" link rather than a dead grey box.
  var facade = document.querySelector('.facade');
  if (facade) {
    facade.addEventListener('click', function () {
      var id = facade.getAttribute('data-vimeo');
      var frame = document.createElement('iframe');
      frame.src = 'https://player.vimeo.com/video/' + id +
        '?title=0&byline=0&portrait=0&autoplay=1';
      frame.setAttribute('allow', 'autoplay; fullscreen; picture-in-picture');
      frame.setAttribute('allowfullscreen', '');
      frame.setAttribute('title', facade.getAttribute('aria-label') || 'Video');
      facade.replaceWith(frame);
    });
  }

  // Home page only: section dot navigation
  var panels = [].slice.call(document.querySelectorAll('.panel'));
  if (!panels.length) return;

  var dots = [].slice.call(document.querySelectorAll('.dots a'));
  if (dots.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var id = en.target.id;
        dots.forEach(function (d) {
          d.classList.toggle('active', d.getAttribute('href') === '#' + id);
        });
      });
    }, { threshold: 0.55 });
    panels.forEach(function (p) { io.observe(p); });
  }

})();
