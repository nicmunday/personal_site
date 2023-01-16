// Open the Modal
function openSwanModal() {
  $("#swanModal").css("display", "block")
}

// Close the Modal
function closeSwanModal() {
  $("#swanModal").css("display", "none")
}

var swanSlideIndex = 1;
showSwanSlides(swanSlideIndex);

// Next/previous controls
function plusSwanSlides(n) {
  showSwanSlides(swanSlideIndex += n);
}

// Thumbnail image controls
function currentSwanSlide(n) {
  showSwanSlides(swanSlideIndex = n);
}

function showSwanSlides(n) {
  var i;
  var slides = $(".swanSlides");
  if (n > slides.length) {swanSlideIndex = 1}
  if (n < 1) {swanSlideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
   }
  $(slides[swanSlideIndex-1]).css("display", "block");
  $("#swanCaption").text($(".swanImage").eq([swanSlideIndex-1]).attr("alt"));
  $("html").css("overflow-x", "hidden")
  $(document).keydown(function(event){
    if(event.which === 27){
      closeSwanModal();
    }
   });

}
