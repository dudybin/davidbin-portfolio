(function () {
  var burger = document.getElementById('burger');
  var menu = document.getElementById('menu');
  var bar = document.querySelector('.topbar');

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

  if (bar) {
    var solid = function () { bar.classList.toggle('solid', window.scrollY > 40); };
    solid();
    window.addEventListener('scroll', solid, { passive: true });
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

  // Home page only: dot nav + parallax
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

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) return;

  var ticking = false;
  function parallax() {
    panels.forEach(function (p) {
      var bg = p.querySelector('.panel__bg');
      if (!bg) return;
      var r = p.getBoundingClientRect();
      if (r.bottom < -200 || r.top > window.innerHeight + 200) return;
      var progress = (r.top + r.height / 2 - window.innerHeight / 2) / window.innerHeight;
      bg.style.transform = 'translate3d(0,' + (progress * -9).toFixed(2) + '%,0) scale(1.12)';
    });
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(parallax); }
  }, { passive: true });
  window.addEventListener('resize', parallax);
  parallax();
})();
