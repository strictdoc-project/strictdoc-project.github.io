document.addEventListener("DOMContentLoaded", function () {
  var heroVideo = document.querySelector(".hero-video video");
  if (!heroVideo) return;

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          heroVideo.play();
        } else {
          heroVideo.pause();
        }
      });
    },
    { threshold: 0.5 }
  );

  observer.observe(heroVideo);
});
