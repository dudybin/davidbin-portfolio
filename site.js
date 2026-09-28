(function () {
  var burger = document.getElementById('burger');
  var menu = document.getElementById('menu');

  if (burger && menu) {
    var closeBtn = document.getElementById('menu-close');
    var setOpen = function (open) {
      menu.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
    };
    burger.addEventListener('click', function () {
      setOpen(!menu.classList.contains('open'));
    });
    if (closeBtn) closeBtn.addEventListener('click', function () { setOpen(false); });
    menu.addEventListener('click', function (e) {
      if (e.target === menu || e.target.tagName === 'A') setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) setOpen(false);
    });

    // mark the current page the way the original highlights it
    var here = (location.pathname.split('/').pop() || 'index.html');
    [].forEach.call(menu.querySelectorAll('.menu__list a'), function (a) {
      if (a.getAttribute('href') === here) a.setAttribute('aria-current', 'page');
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
