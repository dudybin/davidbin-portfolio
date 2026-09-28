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

  // Contact: show the original's confirmation after a successful send
  var thanks = document.getElementById('thanks');
  if (thanks && /[?&]sent=1/.test(location.search)) {
    thanks.hidden = false;
    var form = document.querySelector('.contact');
    if (form) form.reset();
  }

  // Serve the phone-sized still on narrow screens
  if (window.matchMedia('(max-width: 900px)').matches) {
    [].forEach.call(document.querySelectorAll('.shots img[data-m]'), function (img) {
      img.src = img.getAttribute('data-m');
    });
  }

  // Gallery tiles: open the video in a lightbox, as the original does
  var lightbox = document.getElementById('lightbox');
  if (lightbox) {
    var frame = lightbox.querySelector('.lightbox__frame');
    var shut = function () {
      lightbox.classList.remove('open');
      lightbox.setAttribute('aria-hidden', 'true');
      frame.innerHTML = '';
      document.body.style.overflow = '';
    };
    [].forEach.call(document.querySelectorAll('.tile__open'), function (btn) {
      btn.addEventListener('click', function () {
        var label = btn.getAttribute('aria-label') || 'Video';
        var vimeo = btn.getAttribute('data-vimeo');
        var yt = btn.getAttribute('data-youtube');
        var media = btn.getAttribute('data-media');
        var html;
        if (vimeo) {
          html = '<iframe src="https://player.vimeo.com/video/' + vimeo +
            '?title=0&byline=0&portrait=0&autoplay=1" allow="autoplay; fullscreen; ' +
            'picture-in-picture" allowfullscreen title="' + label + '"></iframe>';
        } else if (yt) {
          html = '<iframe src="https://www.youtube.com/embed/' + yt +
            '?autoplay=1&rel=0&modestbranding=1" allow="autoplay; fullscreen; ' +
            'picture-in-picture" allowfullscreen title="' + label + '"></iframe>';
        } else if (media && /\.mp4$/.test(media)) {
          html = '<video src="' + media + '" controls autoplay loop playsinline></video>';
        } else if (media) {
          html = '<img src="' + media + '" alt="' + label + '">';
        }
        if (!html) return;
        frame.innerHTML = html;
        lightbox.classList.add('open');
        lightbox.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      });
    });
    lightbox.querySelector('.lightbox__close').addEventListener('click', shut);
    lightbox.addEventListener('click', function (e) { if (e.target === lightbox) shut(); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && lightbox.classList.contains('open')) shut();
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
