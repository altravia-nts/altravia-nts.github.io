// Scrolls to the selected menu item on the page
$(function() {
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname) {

      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});

// Change navbar style on scroll
$(document).ready(function() {
  var mainNav = $("#mainNav");
  var collapseElement = document.getElementById('bs-example-navbar-collapse-1');

  // Function to add/remove class
  var navbarCollapse = function() {
    if (mainNav.offset().top > 250) {
      mainNav.addClass("bg-dark");
    } else {
      // Only remove bg-dark if the navbar is not collapsed
      if (!$(collapseElement).hasClass('show')) {
        mainNav.removeClass("bg-dark");
      }
    }
  };
  // Collapse now if page is not at top
  navbarCollapse();
  // Collapse the navbar when page is scrolled
  $(window).scroll(navbarCollapse);

  // Add dark background when navbar is expanded on mobile
  $(collapseElement).on('show.bs.collapse', function () { mainNav.addClass('bg-dark'); });
  // Remove dark background when navbar is collapsed (if not scrolled)
  $(collapseElement).on('hide.bs.collapse', function () { if (mainNav.offset().top <= 250) { mainNav.removeClass('bg-dark'); } });
});