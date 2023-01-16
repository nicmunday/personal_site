// Open the Modal
function openDefaultModal() {
  $("#defaultModal").css("display", "block")
}

// Close the Modal
function closeDefaultModal() {
  $("#defaultModal").css("display", "none")
}

var defaultSlideIndex = 1;
showDefaultSlides(defaultSlideIndex);

// Next/previous controls
function plusDefaultSlides(n) {
  showDefaultSlides(defaultSlideIndex += n);
}

// Thumbnail image controls
function currentDefaultSlide(n) {
  showDefaultSlides(defaultSlideIndex = n);
}

function showDefaultSlides(n) {
  var i;
  var slides = $(".defaultSlides");
  if (n > slides.length) {defaultSlideIndex = 1}
  if (n < 1) {defaultSlideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
   }
  $(slides[defaultSlideIndex-1]).css("display", "block");
  $("#defaultCaption").text($(".defaultImage").eq([defaultSlideIndex-1]).attr("alt"));
  $("html").css("overflow-x", "hidden")
  $(document).keydown(function(event){
    if(event.which === 27){
      closeDefaultModal();
    }
   });

}
